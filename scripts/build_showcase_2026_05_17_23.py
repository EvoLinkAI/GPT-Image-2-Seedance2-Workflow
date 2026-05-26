"""One-shot builder for the 2026-05-17/19/21/23 candidate batch.

Reads `data/x-search/candidate_tweets_48h_2026-05-17_19_21_23_with_media.json`,
dedups against the current README showcase + Case sections, picks the best mp4
variant, and writes:

  - data/x-search/showcase_2026_05_17_23_new.json
  - data/x-search/showcase_2026_05_17_23_section.md
  - data/x-search/showcase_2026_05_17_23_upload.csv
  - data/x-search/showcase_2026_05_17_23_links.csv

Run modes:
  python3 scripts/build_showcase_2026_05_17_23.py --dry-run
  python3 scripts/build_showcase_2026_05_17_23.py
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SRC = REPO_ROOT / "data" / "x-search" / "candidate_tweets_48h_2026-05-17_19_21_23_with_media.json"
README = REPO_ROOT / "README.md"
SHOWCASE_URLS = REPO_ROOT / "data" / "x-search" / "showcase_video_urls.json"

OUT_JSON = REPO_ROOT / "data" / "x-search" / "showcase_2026_05_17_23_new.json"
OUT_MD = REPO_ROOT / "data" / "x-search" / "showcase_2026_05_17_23_section.md"
OUT_CSV = REPO_ROOT / "data" / "x-search" / "showcase_2026_05_17_23_upload.csv"
OUT_LINKS = REPO_ROOT / "data" / "x-search" / "showcase_2026_05_17_23_links.csv"
OUT_GUIDE = REPO_ROOT / "data" / "x-search" / "showcase_2026_05_17_23_upload_guide.md"
OUT_DIR = REPO_ROOT / "images" / "showcase"

URL_RE = re.compile(r"https?://\S+")
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?。！？\n])\s+")
README_TWEET_ID_RE = re.compile(r"/status/(\d+)")
README_SHOWCASE_AUTHOR_RE = re.compile(r"<b>@([^<]+)</b>")

MAX_VIDEO_BYTES = 45 * 1024 * 1024
MIN_TEXT_LEN = 40

PROMO_KEYWORDS = (
    "GlobalGPT",
    "GlbGPT",
    "Announcing",
    "BREAKING NEWS",
    "🚨 BREAKING",
)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) "
        "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"
    ),
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
}


def readme_sections() -> tuple[str, str]:
    text = README.read_text()
    showcase_start = text.index("## 🌟 Community Showcase")
    showcase_end = text.index("## 💡 Tips & Techniques")
    showcase = text[showcase_start:showcase_end]
    non_showcase = text[:showcase_start] + text[showcase_end:]
    return showcase, non_showcase


def existing_showcase_tweet_ids_and_authors() -> tuple[set[str], set[str]]:
    showcase, _ = readme_sections()
    return set(README_TWEET_ID_RE.findall(showcase)), {
        handle.lower() for handle in README_SHOWCASE_AUTHOR_RE.findall(showcase)
    }


def existing_case_tweet_ids() -> set[str]:
    _, non_showcase = readme_sections()
    return set(README_TWEET_ID_RE.findall(non_showcase))


def next_slug_num() -> int:
    if not SHOWCASE_URLS.exists():
        return 1
    url_map = json.loads(SHOWCASE_URLS.read_text())
    if not url_map:
        return 1
    return max(int(slug) for slug in url_map) + 1


def best_video_variant(media: dict) -> dict | None:
    variants = (media.get("video_info") or {}).get("variants") or []
    mp4s = [v for v in variants if v.get("content_type") == "video/mp4" and v.get("bitrate")]
    if not mp4s:
        return None
    duration_ms = (media.get("video_info") or {}).get("duration_millis") or 0
    duration_sec = max(duration_ms / 1000.0, 0.001)

    def fits(v: dict) -> bool:
        est_bytes = (v["bitrate"] / 8.0) * duration_sec
        return est_bytes <= MAX_VIDEO_BYTES

    in_budget = [v for v in mp4s if fits(v)]
    if in_budget:
        return max(in_budget, key=lambda v: v["bitrate"])
    return min(mp4s, key=lambda v: v["bitrate"])


def first_video_media(record: dict) -> dict | None:
    raw = record.get("raw_payload") or {}
    ext = raw.get("extendedEntities") or {}
    for media in ext.get("media") or []:
        if media.get("type") == "video" and best_video_variant(media):
            return media
    return None


def short_description(text: str, limit: int = 60) -> str:
    cleaned = URL_RE.sub("", text).strip()
    if not cleaned:
        return "Created with GPT Image 2 + Seedance 2.0"
    first = SENTENCE_SPLIT_RE.split(cleaned, maxsplit=1)[0].strip()
    if len(first) < 8:
        first = cleaned
    first = first.replace("\n", " ").strip()
    if len(first) > limit:
        first = first[: limit - 1].rstrip() + "…"
    if not first or all(not c.isalnum() for c in first):
        return "Created with GPT Image 2 + Seedance 2.0"
    return first


def normalize_tweet_url(handle: str, tweet_id: str) -> str:
    return f"https://x.com/{handle}/status/{tweet_id}"


def download(url: str, dest: Path, retries: int = 2, timeout: int = 120) -> tuple[bool, str]:
    if dest.exists() and dest.stat().st_size > 0:
        return True, "exists"
    last_err = ""
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                data = resp.read()
            tmp = dest.with_suffix(dest.suffix + ".part")
            tmp.write_bytes(data)
            tmp.rename(dest)
            return True, f"downloaded {len(data):,}B"
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, ConnectionError) as exc:
            last_err = f"{type(exc).__name__}: {exc}"
            if attempt < retries:
                time.sleep(1.5 * (attempt + 1))
    return False, last_err


def render_cell(item: dict) -> str:
    src = f'{{{{VIDEO_URL:{item["slug"]}}}}}'
    desc = item["description"].replace("|", "·").replace("<", "&lt;").replace(">", "&gt;")
    return (
        f'<td align="center" valign="top" width="25%">\n'
        f'<video src="{src}" width="240" controls></video>\n'
        f'<br/><a href="{item["tweet_url"]}"><b>@{item["author"]}</b></a> · '
        f'<sub>{item["view_count"]:,} views</sub>\n'
        f'<br/><sub>{desc}</sub>\n'
        f'</td>'
    )


def render_section(items: list[dict]) -> str:
    cols = 4
    lines = [
        "### Update — May 17–23, 2026",
        "",
        (
            "Selected creator works from the May 17–23, 2026 candidate batches "
            "(one entry per author, promo-style posts excluded). Ranked by view count "
            "captured in the raw tweet payload."
        ),
        "",
    ]
    for row_start in range(0, len(items), cols):
        row = items[row_start : row_start + cols]
        lines.append("<table><tr>")
        for item in row:
            lines.append(render_cell(item))
        for _ in range(cols - len(row)):
            lines.append('<td align="center" valign="top" width="25%"></td>')
        lines.append("</tr></table>")
        lines.append("")
    return "\n".join(lines)


def render_upload_guide(items: list[dict]) -> str:
    lines = [
        "# Showcase video upload checklist",
        "",
        "**Goal:** turn each local `images/showcase/<slug>.mp4` into a GitHub `user-attachments` URL,",
        "then paste each URL back into `data/x-search/showcase_2026_05_17_23_links.csv` or your final URL map.",
        "",
        "## How to use this file",
        "",
        "1. Open <https://github.com/EvoLinkAI/seedance2-gptimage-2-together/issues/new>",
        "2. Paste this whole document into the issue body (do **not** submit yet — keep it as a draft / preview).",
        "3. For each row below, drag the matching mp4 from `images/showcase/` onto the **▼ DROP HERE ▼** line.",
        "4. GitHub will replace that line with a `https://github.com/user-attachments/assets/<uuid>` URL.",
        "5. Copy those URLs back into `data/x-search/showcase_2026_05_17_23_links.csv`.",
        "",
        "---",
        "",
    ]
    for item in items:
        lines.append(f"### #{item['rank']} — @{item['author']} ({item['view_count']:,} views)")
        lines.append("")
        lines.append(f"- File: `images/showcase/{item['video_filename']}`")
        lines.append(f"- Slug: `{item['slug']}`")
        lines.append(f"- Tweet: {item['tweet_url']}")
        lines.append("")
        lines.append("▼ DROP HERE ▼")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="plan-only, no downloads")
    parser.add_argument("--limit", type=int, default=None, help="cap selected entries (debug)")
    args = parser.parse_args()

    raw_records = json.loads(SRC.read_text())
    showcase_tweet_ids, showcase_authors = existing_showcase_tweet_ids_and_authors()
    case_tweet_ids = existing_case_tweet_ids()
    existing_tweet_ids = showcase_tweet_ids | case_tweet_ids
    next_slug = next_slug_num()

    skipped = {
        "no_media": 0,
        "short_text": 0,
        "dup_tweet": 0,
        "dup_author_existing": 0,
        "dup_author_new": 0,
        "promo": 0,
    }
    selected: list[dict] = []
    seen_authors_in_new: set[str] = set()

    for rec in raw_records:
        tweet_id = rec["tweet_id"]
        author = rec["author_handle"]
        author_l = author.lower()
        text = rec.get("full_text") or (rec.get("raw_payload") or {}).get("text") or ""
        media = first_video_media(rec)
        if not media:
            skipped["no_media"] += 1
            continue
        if len(URL_RE.sub("", text).strip()) < MIN_TEXT_LEN:
            skipped["short_text"] += 1
            continue
        if any(kw in text for kw in PROMO_KEYWORDS):
            skipped["promo"] += 1
            continue
        if tweet_id in existing_tweet_ids:
            skipped["dup_tweet"] += 1
            continue
        if author_l in showcase_authors:
            skipped["dup_author_existing"] += 1
            continue
        if author_l in seen_authors_in_new:
            skipped["dup_author_new"] += 1
            continue
        variant = best_video_variant(media)
        if not variant:
            skipped["no_media"] += 1
            continue
        seen_authors_in_new.add(author_l)
        payload = rec.get("raw_payload") or {}
        selected.append(
            {
                "tweet_id": tweet_id,
                "tweet_url": normalize_tweet_url(author, tweet_id),
                "author": author,
                "author_display_name": (payload.get("author") or {}).get("name", ""),
                "created_at": rec.get("created_at"),
                "text": text,
                "description": short_description(text),
                "video_url": variant["url"],
                "video_bitrate": variant["bitrate"],
                "thumbnail_url": media.get("media_url_https"),
                "view_count": int(payload.get("viewCount") or 0),
                "like_count": int(payload.get("likeCount") or 0),
                "lang": payload.get("lang"),
            }
        )

    selected.sort(
        key=lambda item: (
            item["view_count"],
            item["like_count"],
            item["created_at"] or "",
        ),
        reverse=True,
    )

    if args.limit:
        selected = selected[: args.limit]

    width = max(3, len(str(next_slug + len(selected) - 1)))
    for index, item in enumerate(selected):
        slug = f"{next_slug + index:0{width}d}"
        item["rank"] = index + 1
        item["slug"] = slug
        item["video_filename"] = f"{slug}.mp4"
        item["thumbnail_filename"] = f"{slug}.jpg"

    print(f"Source records:                       {len(raw_records)}")
    print(f"Existing showcase tweet ids:         {len(showcase_tweet_ids)}")
    print(f"Existing showcase authors:           {len(showcase_authors)}")
    print(f"Existing case tweet ids:             {len(case_tweet_ids)}")
    print(f"Skipped — no video media:            {skipped['no_media']}")
    print(f"Skipped — text too short:            {skipped['short_text']}")
    print(f"Skipped — duplicate tweet id:        {skipped['dup_tweet']}")
    print(f"Skipped — author already in showcase:{skipped['dup_author_existing']}")
    print(f"Skipped — duplicate author in batch: {skipped['dup_author_new']}")
    print(f"Skipped — promo/templated post:      {skipped['promo']}")
    print(f"Selected new entries:                {len(selected)}")
    if selected:
        print(f"Slug range:                          {selected[0]['slug']} .. {selected[-1]['slug']}")
    print()
    print(f"{'Slug':>4}  {'Views':>8}  {'Lang':>4}  {'Author':<24}  Description")
    print("-" * 110)
    for item in selected:
        print(
            f"{item['slug']:>4}  {item['view_count']:>8}  {item['lang'] or '?':>4}  "
            f"@{item['author']:<23}  {item['description']}"
        )

    OUT_JSON.write_text(json.dumps(selected, ensure_ascii=False, indent=2))
    print(f"\nWrote {OUT_JSON.relative_to(REPO_ROOT)}")

    OUT_MD.write_text(render_section(selected))
    print(f"Wrote {OUT_MD.relative_to(REPO_ROOT)}")

    with OUT_CSV.open("w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(
            [
                "slug",
                "rank",
                "author",
                "view_count",
                "tweet_url",
                "description",
                "video_filename",
                "thumbnail_filename",
                "video_url",
                "github_link",
            ]
        )
        for item in selected:
            writer.writerow(
                [
                    item["slug"],
                    item["rank"],
                    item["author"],
                    item["view_count"],
                    item["tweet_url"],
                    item["description"],
                    item["video_filename"],
                    item["thumbnail_filename"],
                    item["video_url"],
                    "",
                ]
            )
    print(f"Wrote {OUT_CSV.relative_to(REPO_ROOT)}")

    with OUT_LINKS.open("w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["slug", "link"])
        for item in selected:
            writer.writerow([item["slug"], ""])
    print(f"Wrote {OUT_LINKS.relative_to(REPO_ROOT)}")

    OUT_GUIDE.write_text(render_upload_guide(selected))
    print(f"Wrote {OUT_GUIDE.relative_to(REPO_ROOT)}")

    if args.dry_run:
        print("\n--dry-run set, skipping downloads.")
        return 0

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    jobs: list[tuple[str, Path, str]] = []
    for item in selected:
        jobs.append((item["video_url"], OUT_DIR / item["video_filename"], "video"))
        jobs.append((item["thumbnail_url"], OUT_DIR / item["thumbnail_filename"], "thumb"))
    print(f"\nDownloading {len(jobs)} files into {OUT_DIR.relative_to(REPO_ROOT)} ...")
    success = 0
    failures: list[tuple[str, str, str]] = []
    with ThreadPoolExecutor(max_workers=6) as ex:
        futures = {ex.submit(download, url, dest): (url, dest, kind) for url, dest, kind in jobs}
        for fut in as_completed(futures):
            url, dest, kind = futures[fut]
            try:
                ok, msg = fut.result()
            except Exception as exc:
                ok, msg = False, f"unhandled: {exc}"
            tag = "OK" if ok else "FAIL"
            print(f"  [{tag}] {kind:>5}  {dest.name:<40}  {msg}")
            if ok:
                success += 1
            else:
                failures.append((kind, dest.name, msg))
    print(f"\nDone. {success}/{len(jobs)} succeeded.")
    if failures:
        print(f"\n{len(failures)} failures:")
        for kind, name, msg in failures:
            print(f"  - {kind} {name}: {msg}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
