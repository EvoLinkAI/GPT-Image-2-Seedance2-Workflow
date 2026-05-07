"""One-shot builder for the 2026-05-06 X-search batch.

Reads `data/x-search/gpt-image2-seedance2-2026-05-06.json`, dedups against the
existing showcase + Case sections in the README, picks the best mp4 variant,
writes:

  - data/x-search/showcase_2026_05_06_new.json    (selected new entries with slug)
  - data/x-search/showcase_2026_05_06_section.md  (gallery markdown w/ placeholders)
  - data/x-search/showcase_2026_05_06_upload.csv  (slug -> empty github_link column)

Run modes:
  python3 scripts/build_showcase_2026_05_06.py --dry-run   # plan only
  python3 scripts/build_showcase_2026_05_06.py             # plan + download mp4/jpg
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
SRC = REPO_ROOT / "data" / "x-search" / "gpt-image2-seedance2-2026-05-06.json"
EXISTING_SELECTED = REPO_ROOT / "data" / "x-search" / "showcase_selected.json"
README = REPO_ROOT / "README.md"

OUT_JSON = REPO_ROOT / "data" / "x-search" / "showcase_2026_05_06_new.json"
OUT_MD = REPO_ROOT / "data" / "x-search" / "showcase_2026_05_06_section.md"
OUT_CSV = REPO_ROOT / "data" / "x-search" / "showcase_2026_05_06_upload.csv"
OUT_DIR = REPO_ROOT / "images" / "showcase"

URL_RE = re.compile(r"https?://\S+")
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?。！？\n])\s+")
README_TWEET_ID_RE = re.compile(r"/status/(\d+)")

MAX_VIDEO_BYTES = 45 * 1024 * 1024
MIN_TEXT_LEN = 40

PROMO_KEYWORDS = (
    "GlobalGPT", "GlbGPT",
    "Announcing", "BREAKING NEWS", "🚨 BREAKING",
)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
}


def existing_readme_tweet_ids() -> set[str]:
    if not README.exists():
        return set()
    text = README.read_text()
    showcase_start = text.find("## 🌟 Community Showcase")
    if showcase_start != -1:
        showcase_end = text.find("## ", showcase_start + 1)
        if showcase_end == -1:
            showcase_end = len(text)
        text = text[:showcase_start] + text[showcase_end:]
    return set(README_TWEET_ID_RE.findall(text))


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


def first_video_media(tweet: dict) -> dict | None:
    for m in tweet.get("media_items") or []:
        if m.get("type") == "video" and best_video_variant(m):
            return m
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
            with urllib.request.urlopen(req, timeout=timeout) as r:
                data = r.read()
            tmp = dest.with_suffix(dest.suffix + ".part")
            tmp.write_bytes(data)
            tmp.rename(dest)
            return True, f"downloaded {len(data):,}B"
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, ConnectionError) as e:
            last_err = f"{type(e).__name__}: {e}"
            if attempt < retries:
                time.sleep(1.5 * (attempt + 1))
    return False, last_err


def render_cell(item: dict) -> str:
    src = f'{{{{VIDEO_URL:{item["slug"]}}}}}'
    desc = item["description"].replace("|", "·").replace("<", "&lt;").replace(">", "&gt;")
    return (
        f'<td align="center" valign="top" width="25%">\n'
        f'<video src="{src}" width="240" controls></video>\n'
        f'<br/><a href="{item["tweet_url"]}"><b>@{item["author"]}</b></a>\n'
        f'<br/><sub>{desc}</sub>\n'
        f'</td>'
    )


def render_section(items: list[dict]) -> str:
    cols = 4
    lines: list[str] = []
    for row_start in range(0, len(items), cols):
        row = items[row_start : row_start + cols]
        lines.append("<table><tr>")
        for it in row:
            lines.append(render_cell(it))
        for _ in range(cols - len(row)):
            lines.append('<td align="center" valign="top" width="25%"></td>')
        lines.append("</tr></table>")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="plan-only, no downloads")
    parser.add_argument("--limit", type=int, default=None, help="cap selected entries (debug)")
    args = parser.parse_args()

    raw = json.loads(SRC.read_text())
    existing_selected = json.loads(EXISTING_SELECTED.read_text())
    existing_tweet_ids = {it["tweet_id"] for it in existing_selected}
    existing_authors = {it["author"].lower() for it in existing_selected}
    readme_ids = existing_readme_tweet_ids()
    existing_tweet_ids |= readme_ids

    next_slug_num = max((int(it["slug"]) for it in existing_selected), default=0) + 1

    skipped = {"no_media": 0, "short_text": 0, "dup_tweet": 0, "dup_author_existing": 0, "dup_author_new": 0, "promo": 0}
    selected: list[dict] = []
    seen_authors_in_new: set[str] = set()

    for tweet in raw:
        tweet_id = tweet["tweet_id"]
        author = tweet["author_handle"]
        author_l = author.lower()
        text = tweet.get("text", "") or ""
        media = first_video_media(tweet)
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
        if author_l in existing_authors:
            skipped["dup_author_existing"] += 1
            continue
        if author_l in seen_authors_in_new:
            skipped["dup_author_new"] += 1
            continue
        seen_authors_in_new.add(author_l)
        variant = best_video_variant(media)
        record = {
            "tweet_id": tweet_id,
            "tweet_url": normalize_tweet_url(author, tweet_id),
            "author": author,
            "author_display_name": tweet.get("author_name", ""),
            "created_at": tweet.get("created_at"),
            "text": text,
            "description": short_description(text),
            "video_url": variant["url"],
            "video_bitrate": variant["bitrate"],
            "thumbnail_url": media.get("media_url_https"),
        }
        selected.append(record)

    if args.limit:
        selected = selected[: args.limit]

    width = max(2, len(str(next_slug_num + len(selected) - 1)))
    for i, item in enumerate(selected):
        slug = f"{next_slug_num + i:0{width}d}"
        item["slug"] = slug
        item["video_filename"] = f"{slug}.mp4"
        item["thumbnail_filename"] = f"{slug}.jpg"

    print(f"Source entries:                     {len(raw)}")
    print(f"Existing showcase tweets:           {len(existing_selected)}")
    print(f"Existing tweet ids (showcase+cases): {len(existing_tweet_ids)}")
    print(f"Existing authors (showcase):        {len(existing_authors)}")
    print(f"Skipped — no video media:           {skipped['no_media']}")
    print(f"Skipped — text too short:           {skipped['short_text']}")
    print(f"Skipped — duplicate tweet id:       {skipped['dup_tweet']}")
    print(f"Skipped — author already in showcase: {skipped['dup_author_existing']}")
    print(f"Skipped — duplicate author in batch: {skipped['dup_author_new']}")
    print(f"Skipped — promo/templated post:     {skipped['promo']}")
    print(f"Selected new entries:               {len(selected)}")
    print(f"Slug range:                         {selected[0]['slug']} .. {selected[-1]['slug']}" if selected else "(none)")
    print()
    print(f"{'Slug':>4}  {'Author':<22}  Description")
    print("-" * 100)
    for r in selected:
        print(f"{r['slug']:>4}  @{r['author']:<21}  {r['description']}")

    OUT_JSON.write_text(json.dumps(selected, ensure_ascii=False, indent=2))
    print(f"\nWrote {OUT_JSON.relative_to(REPO_ROOT)}")

    section_md = render_section(selected)
    OUT_MD.write_text(section_md)
    print(f"Wrote {OUT_MD.relative_to(REPO_ROOT)}")

    with OUT_CSV.open("w", newline="") as fp:
        writer = csv.writer(fp)
        writer.writerow([
            "slug", "author", "tweet_url", "description",
            "video_filename", "thumbnail_filename", "video_url",
            "github_link",
        ])
        for r in selected:
            writer.writerow([
                r["slug"], r["author"], r["tweet_url"], r["description"],
                r["video_filename"], r["thumbnail_filename"], r["video_url"],
                "",
            ])
    print(f"Wrote {OUT_CSV.relative_to(REPO_ROOT)}")

    if args.dry_run:
        print("\n--dry-run set, skipping downloads.")
        return 0

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    jobs: list[tuple[str, Path, str]] = []
    for r in selected:
        jobs.append((r["video_url"], OUT_DIR / r["video_filename"], "video"))
        jobs.append((r["thumbnail_url"], OUT_DIR / r["thumbnail_filename"], "thumb"))
    print(f"\nDownloading {len(jobs)} files into {OUT_DIR.relative_to(REPO_ROOT)} ...")
    success = 0
    failures: list[tuple[str, str, str]] = []
    with ThreadPoolExecutor(max_workers=6) as ex:
        futures = {ex.submit(download, url, dest): (url, dest, kind) for url, dest, kind in jobs}
        for fut in as_completed(futures):
            url, dest, kind = futures[fut]
            try:
                ok, msg = fut.result()
            except Exception as e:
                ok, msg = False, f"unhandled: {e}"
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
