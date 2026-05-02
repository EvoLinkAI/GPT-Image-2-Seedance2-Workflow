<div align="center">

<a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=banner&utm_campaign=gptimage2-x-seedance2"><img src="images/logo.png" alt="GPT Image 2 × Seedance 2.0 Workflow Guide"></a>

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)
[![awesome-seedance-2.0-prompts](https://img.shields.io/badge/📦_awesome--seedance--2.0--prompts-181717?logo=github)](https://github.com/EvoLinkAI/awesome-seedance-2.0-prompts)
[![Seedance-2.0-Gateway-Service](https://img.shields.io/badge/📦_Seedance--2.0--Gateway--Service-181717?logo=github)](https://github.com/EvoLinkAI/Seedance-2.0-Gateway-Service)
[![awesome-seedance-2-guide](https://img.shields.io/badge/📦_awesome--seedance--2--guide-181717?logo=github)](https://github.com/EvoLinkAI/awesome-seedance-2-guide)
[![awesome-gpt-image-2-prompts](https://img.shields.io/badge/📦_awesome--gpt--image--2--prompts-181717?logo=github)](https://github.com/EvoLinkAI/awesome-gpt-image-2-prompts)


[![🇺🇸 English](https://img.shields.io/badge/🇺🇸_English-Default_Source-111111)](README.md)
[![🇪🇸 Español](https://img.shields.io/badge/🇪🇸_Español-Ver-ffb703)](README_es.md)
[![🇵🇹 Português](https://img.shields.io/badge/🇵🇹_Português-Ver-2a9d8f)](README_pt.md)
[![🇯🇵 日本語](https://img.shields.io/badge/🇯🇵_日本語-表示-52b788)](README_ja.md)
[![🇰🇷 한국어](https://img.shields.io/badge/🇰🇷_한국어-보기-4ea8de)](README_ko.md)
[![🇩🇪 Deutsch](https://img.shields.io/badge/🇩🇪_Deutsch-Ansehen-f4a261)](README_de.md)
[![🇫🇷 Français](https://img.shields.io/badge/🇫🇷_Français-Voir-e76f51)](README_fr.md)
[![🇹🇷 Türkçe](https://img.shields.io/badge/🇹🇷_Türkçe-Görüntüle-d62828)](README_tr.md)
[![🇹🇼 繁體中文](https://img.shields.io/badge/🇹🇼_繁體中文-查看-8338ec)](README_zh-TW.md)
[![🇨🇳 简体中文](https://img.shields.io/badge/🇨🇳_简体中文-查看-ef476f)](README_zh-CN.md)
[![🇷🇺 Русский](https://img.shields.io/badge/🇷🇺_Русский-Смотреть-577590)](README_ru.md)

</div>




## 🎬 はじめに

GPT Image 2 × Seedance 2.0 ワークフロー集へようこそ！🤗

**このリポジトリでは、GPT Image 2 と Seedance 2.0 を組み合わせて高品質な AI 動画を制作するための、実証済みワークフロー、プロンプトテンプレート、実際のクリエイター事例をまとめています。**

GPT Image 2 は「何を描くか」とビジュアルの一貫性を担当し、Seedance 2.0 は「どう動かすか」を担当して画像を動画へとアニメーション化します。両者を組み合わせることで、現在もっとも強力な AI 動画パイプラインのひとつを構成できます。

このリポジトリの事例の多くは、X/Twitter 上のクリエイター、コミュニティ実験、実運用ワークフローからキュレーションしたものです。

Evolink ですぐ試せます: [GPT Image 2 + Seedance 2.0](https://evolink.ai?utm_source=github&utm_medium=readme&utm_campaign=gptimage2-x-seedance2)

役に立ったら、スターを付けてもらえると助かります。⭐



## 📰 ニュース

- **2026年5月1日:** Case 13〜27 を追加（ダンスシーケンスグリッド、コミックページアニメーション、ラグジュアリーCM、シネマティック料理動画、ゲームインターフェースパイプライン、シングルエージェントワークフロー、絵コンテ先行コスト管理、Claude ショットリスト MV、キャスティンググリッド、3Dスカルプトパイプライン、IP サイバーパンクリメイク、GTA シティコンセプト、K-Pop 振付、プロダクト動画広告、キャラクター登場アニメーション）
- **2026年4月25日:** Case 10〜12（マルチフレーム絵コンテ、日本語MVツールチェーン、Claude Code × キャラクターシート）を追加。Case 9 に ARPG シミュレーションの変形例を追加。ギャラリーにコミュニティショーケースを追加
- **2026年4月23日:** 9件の厳選ワークフロー事例とともにリポジトリ公開

## 📑 メニュー

- [🎬 はじめに](#-はじめに)
- [📰 ニュース](#-ニュース)
- [📑 メニュー](#-メニュー)
- [🎥 ストーリーボード技法](#-ストーリーボード技法)
  - [Case 1: 標準ストーリーボード → 動画 (by @kiyoshi_shin)](#case-1-標準ストーリーボード--動画-by-kiyoshi_shin)
  - [Case 2: 3×3グリッド型ストーリーボード手法 (by @servasyy_ai)](#case-2-33グリッド型ストーリーボード手法-by-servasyy_ai)
  - [Case 10: マルチフレーム参照 → 高速カット動画 (by @heygentlewhale)](#case-10-マルチフレーム参照--高速カット動画-by-heygentlewhale)
  - [Case 19: 絵コンテ先行のコスト管理 (by @0xbisc)](#case-19-絵コンテ先行のコスト管理-by-0xbisc)
- [📱 CM＆プロダクト](#-cmプロダクト)
  - [Case 5: アプリMVPデモ動画 (by @Shin_Engineer)](#case-5-アプリmvpデモ動画-by-shin_engineer)
  - [Case 6: 15秒CM (by @ai_mitosan)](#case-6-15秒cm-by-ai_mitosan)
  - [Case 15: ラグジュアリーCM — 絵コンテから映像へ (by @insmind_com)](#case-15-ラグジュアリーcm--絵コンテから映像へ-by-insmind_com)
  - [Case 16: シネマティック料理動画 (by @kingofdairyque)](#case-16-シネマティック料理動画-by-kingofdairyque)
  - [Case 26: 商品画像 → ショート動画広告 (by @insmind_com)](#case-26-商品画像--ショート動画広告-by-insmind_com)
- [🎨 アニメーション＆キャラクター](#-アニメーションキャラクター)
  - [Case 3: キャラクター設定シート → アニメーション (by @YaReYaRu30Life)](#case-3-キャラクター設定シート--アニメーション-by-yareyaru30life)
  - [Case 4: アニメOP風動画 (by @Toshi_nyaruo_AI)](#case-4-アニメop風動画-by-toshi_nyaruo_ai)
  - [Case 12: Claude Code × キャラクターシート → アニメーション (by @old_pgmrs_will)](#case-12-claude-code--キャラクターシート--アニメーション-by-old_pgmrs_will)
  - [Case 13: ダンスシーケンスグリッド → ダンス動画 (by @Ciri_ai)](#case-13-ダンスシーケンスグリッド--ダンス動画-by-ciri_ai)
  - [Case 14: コミックページ → アニメーション動画 (by @nimentrix)](#case-14-コミックページ--アニメーション動画-by-nimentrix)
  - [Case 25: K-Pop 振付 — 精密コントロール (by @Kashberg_0)](#case-25-k-pop-振付--精密コントロール-by-kashberg_0)
  - [Case 27: キャラクター登場アニメーション (by @0xbisc)](#case-27-キャラクター登場アニメーション-by-0xbisc)
- [🎵 ミュージックビデオ＆短編映画](#-ミュージックビデオ短編映画)
  - [Case 7: Suno を使ったミュージックビデオ (by @fukaborichannel)](#case-7-suno-を使ったミュージックビデオ-by-fukaborichannel)
  - [Case 8: サイバーパンク風短編映像 (by @ponyodong)](#case-8-サイバーパンク風短編映像-by-ponyodong)
  - [Case 11: 日本語MV — 全AIツールチェーン (by @Tz_2022)](#case-11-日本語mv--全aiツールチェーン-by-tz_2022)
  - [Case 20: Claude ショットリスト → ミュージックビデオ (by @CoffeeVectors)](#case-20-claude-ショットリスト--ミュージックビデオ-by-coffeevectors)
- [🎮 ゲームコンセプト](#-ゲームコンセプト)
  - [Case 9: ゲーム＆インタラクティブコンテンツ (by @op7418)](#case-9-ゲームインタラクティブコンテンツ-by-op7418)
  - [Case 17: ゲームインターフェースアニメーション — フルパイプライン (by @0xInk_)](#case-17-ゲームインターフェースアニメーション--フルパイプライン-by-0xink_)
  - [Case 24: GTA風シティゲームコンセプト (by @markgadala)](#case-24-gta風シティゲームコンセプト-by-markgadala)
- [🛠 制作ツール](#-制作ツール)
  - [Case 18: シングルエージェント自動化ワークフロー (by @venturetwins)](#case-18-シングルエージェント自動化ワークフロー-by-venturetwins)
  - [Case 21: キャスティンググリッド — 俳優オーディション (by @8fstudioz)](#case-21-キャスティンググリッド--俳優オーディション-by-8fstudioz)
  - [Case 22: 3Dスカルプト → AIレンダー → アニメーション (by @_DAntunes_)](#case-22-3dスカルプト--aiレンダー--アニメーション-by-_dantunes_)
- [💡 ヒント＆テクニック](#-ヒントテクニック)
  - [一貫性ガイド](#一貫性ガイド)
  - [プロンプトテンプレート](#プロンプトテンプレート)
  - [トラブルシューティング](#トラブルシューティング)
- [🚀 Evolink で試す](#-evolink-で試す)
- [🙏 クレジット](#-クレジット)


## 🎥 ストーリーボード技法

<!-- Case 1: Standard Storyboard → Video (by @kiyoshi_shin) -->
### Case 1: [標準ストーリーボード → 動画](https://x.com/kiyoshi_shin/status/2047133524403400847) (by [@kiyoshi_shin](https://x.com/kiyoshi_shin))

もっとも一般的なワークフローです。GPT Image 2 でストーリーボードのコマを生成し、それを Seedance 2.0 で動画化します。プロモーション動画、短編ドラマ、アニメの OP などに向いています。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/storyboard_case1/input.jpg" width="280" alt="GPT Image 2 で生成した絵コンテ"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/ac25fc3d-b6cb-4149-a8ba-e7e10c5b1faa" width="280" controls></video></td>
</tr></table>

**手順:**

1. GPT Image 2 にシーンを説明して、ストーリーボード画像を生成する
2. そのストーリーボードを Seedance 2.0 の Image-to-Video モードに読み込む
3. 各クリップを書き出し、編集ソフトでつなぎ合わせる

**GPT Image 2 プロンプト:**

```
Create a 6-panel storyboard for a 15-second brand promotional video. Label each panel with a shot description.
Style: cinematic, cool color tone, widescreen 16:9.
Content: the journey of a product from factory to the customer's hands.
```

**Seedance 2.0 プロンプト:**

```
Cinematic brand advertisement, slow camera push-in, product centered in frame, warm side lighting, soft background blur, no people, 3 seconds.
```

> [!NOTE]
> Seedance の自動クロップを避けるため、ストーリーボード画像は 16:9 で出力してください。フレームレートは映画標準に合わせて 24fps に設定すると安定します。各コマはできるだけシンプルにするほど、動きの精度が上がります。


<!-- Case 2: 3×3 Grid Storyboard Method (by @servasyy_ai) -->
### Case 2: [3×3グリッド型ストーリーボード手法](https://x.com/servasyy_ai/status/2047198012750143999) (by [@servasyy_ai](https://x.com/servasyy_ai))

コミュニティから見つかった重要なテクニックです。ストーリーボードの各コマを 1 枚ずつ読み込むより、1 枚の 3×3 グリッド画像にまとめてから Seedance に渡す方が、失敗率を大きく下げられます。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/storyboard_case2/output.jpg" width="400" alt="3×3グリッド絵コンテ出力"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/00f32388-a17b-4b9c-8da3-1956436ce91b" width="400" controls></video></td>
</tr></table>



**手順:**

1️⃣ 作りたいコンテンツ + ✅ プロンプト「Create a storyboard in a 3×3 grid format」を入力する
2️⃣ 1 で生成した画像から ChatGPT でプロンプトを作成する
3️⃣ 1 の画像を seedance でリファレンスとして指定する
4️⃣ 2 で作成したプロンプトを入力する

**GPT Image 2 プロンプト:**

```
[describe your scene] and Create a storyboard in a 3×3 grid format
```

**Seedance 2.0 プロンプト:**
turn this image into video
```
[Describe the motion and style. Example: Japanese full-color animation, fast cuts, high frame count, 24fps, dark fantasy anime OP style, intense battle scenes.]
```

> [!NOTE]
> **使用前に角括弧内を置き換えてください。** この方法が有効なのは、Seedance が 1 枚の画像から動きの意図を解析するためです。グリッドは進行方向の参照になり、別々の画像を渡すよりも一貫した動きを生成しやすくなります。


<!-- Case 10: Multi-Frame Reference Storyboard (by @heygentlewhale + @ai_gezgini) -->
### Case 10: [マルチフレーム参照 → 高速カット動画](https://x.com/heygentlewhale/status/2047969137969004946) (by [@heygentlewhale](https://x.com/heygentlewhale))

複数の参考フレームを含む絵コンテ画像を Seedance 2.0 に渡し、シーンの順序に従うよう指示します。モデルはフレームの位置をシーン指示として解釈し、手動での組み合わせなしに、一貫した高速カット編集を出力します。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/storyboard_case10/input.jpg" width="280" alt="GPT Image 2 マルチフレーム絵コンテ"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/4d7af334-4e49-4de4-899e-803f72116c21" width="280" controls></video></td>
<td align="center"><video src="https://github.com/user-attachments/assets/5def7e00-6fc6-4a4e-8075-5f37cb24b84c" width="280" controls></video></td>
</tr></table>

**手順:**

1. GPT Image 2 でマルチパネルの絵コンテ画像を生成する（12フレーム、3×4 または 4×3 グリッド）
2. そのグリッドを Seedance 2.0 に参考画像としてアップロードする
3. フレーム数と編集スタイルを明記したシーケンスプロンプトを書く

**GPT Image 2 プロンプト:**

```
Create a 12-panel storyboard grid for a [N]-second [genre] film:
- 4 columns × 3 rows, left-to-right, top-to-bottom reading order
- Each panel: [shot type] + [action description]
- Location: [setting], Time: [day/night], Mood: [atmosphere]
- Consistent character design and scene across all panels
- No text labels, no panel borders
Output as a single image.
```

**Seedance 2.0 プロンプト:**

```
Follow the storyboard sequence of the 12 reference frames in image1, edited as a fast-cut memory montage.
[Describe visual style — example below:]
A nostalgic romance film set in 1990s Singapore, shot on 35mm film in Kodak Portra 800 style.
Soft grain, dreamy blur, warm highlights, and slight color shifts create a vintage cinematic atmosphere.
```

**汎用シーケンスプロンプト (via [@ai_gezgini](https://x.com/ai_gezgini/status/2047349122315805016)):**

```
Use this storyboard to generate a video, follow the scene order, keep transitions smooth,
and preserve cinematic lighting and pacing.
[Add any extra visual details you want.]
```

> [!NOTE]
> このプロンプトはジャンルを問わず使えます。スタイルの説明を SF、ホラー、ドキュメンタリーなど任意のものに入れ替えてください。キーフレーズは `follow the storyboard sequence of the [N] reference frames` で、フレームの位置を単一の構図ではなくタイムラインとして扱うよう Seedance に指示します。


<!-- Case 19: Storyboard-First Cost Control (by @0xbisc) -->
### Case 19: [絵コンテ先行のコスト管理](https://x.com/0xbisc/status/2049100073481716076) (by [@0xbisc](https://x.com/0xbisc))

制作コストを意識したアプローチです。まず GPT Image 2 で絵コンテを繰り返し調整し（安い）、構図が確定してから動画を生成します（高い）。動画の試行錯誤は画像の 10〜50 倍のクレジットを消費するため、大幅な節約になります。298 いいね / 1.3万 再生 / 291 ブックマーク。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/storyboard_case19/output.jpg" width="400" alt="絵コンテ先行ワークフロー出力"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/09e04d80-c0d1-4a8c-9b74-2efe474acfcd" width="400" controls></video></td>
</tr></table>

**手順:**

1. GPT Image 2 で 8 コマの絵コンテグリッドを生成する
2. 各コマを確認し、満足するまで個別に再生成・編集する
3. 絵コンテ全体が確定してから、Seedance 2.0 に読み込む
4. 確定した絵コンテから一発で動画を生成する

**GPT Image 2 プロンプト:**

```
Create a single cinematic storyboard image containing 8 panels, arranged in a 4-column horizontal grid layout across the canvas.
Panels are evenly distributed in 4 columns, forming a balanced multi-row composition.
Use generous white space between panels and around the entire layout, creating a calm, refined editorial presentation.
Minimalist editorial design, white background, precise alignment, consistent spacing, strong grid system.
Subtle divider lines, ultra-thin, low-contrast, neutral tone, strictly aligned to the grid.
Each panel is presented as a clean modular card with a clear hierarchy: image frame on top, minimal text block below.
Refined modern sans-serif typography, light to regular weight, tight typographic control, consistent scale rhythm.
Visual consistency across all panels: a white flying dragon and a short blond-haired young male wearing a loose flowing white robe riding on its back. A glowing spherical object remains consistent in appearance.
Style: live-action cinematic realism, human actor proportions, natural skin detail, physically accurate lighting, real-world materials, high-end film still quality, ultra high resolution, sharp focus.
Cinematic sequence:
Scene 01
Shot type
Wide shot, low-angle tracking
Narrative
Dragon skims rapidly above ground toward vast geometric ruins, rider standing steadily, bright daylight
Scene 02
Shot type
Wide shot, side view
Narrative
Dragon enters ruin airspace, stone structures begin sinking and shifting, geometry reconfigures
Scene 03
Shot type
Medium shot, tracking
Narrative
Dragon navigates through moving structures forming a spatial maze, rider leans forward, focused
Scene 04
Shot type
Push-in shot, centered composition
Narrative
Massive floating ring appears at center, glowing sphere suspended inside, focal point established
Scene 05
Shot type
Wide-angle, low-angle tracking, high speed
Narrative
Dragon dives through narrow moving gaps, massive structures pass extremely close, intense speed and compression
Scene 06
Shot type
Close-up, centered composition
Narrative
Rider reaches forward to grasp glowing sphere, golden light illuminating face and arm
Scene 07
Shot type
Wide shot, upward motion
Narrative
Dragon ascends sharply as ruins collapse below, structures sinking and closing, dust fills air
Scene 08
Shot type
Wide shot, high-angle view
Narrative
Dragon exits above collapsed ruins, open sky, clear silhouette of rider and dragon, resolution moment
```

**Seedance 2.0 プロンプト:**

```
Generate video based strictly on storyboard @ image1. Follow the storyboard exactly as shown, matching each panel's composition, framing, and action. Keep perfect visual continuity with no errors or inconsistencies.
```

> [!NOTE]
> **絵コンテ先行がコスト面で有利な理由:** 動画の試行錯誤はクレジットを急速に消費します。絵コンテなら、カットごとに微調整して問題を早期に発見できます。動画ステップは最終レンダリング 1 回で済み、高コストな試行錯誤ループを避けられます。長尺シーケンスにおいて最もコスト効率の良いワークフローだとコミュニティでも確認されています。


## 📱 CM＆プロダクト

<!-- Case 5: App MVP Demo Video (by @Shin_Engineer) -->
### Case 5: [アプリMVPデモ動画](https://x.com/Shin_Engineer/status/2047182050323812381) (by [@Shin_Engineer](https://x.com/Shin_Engineer))

まだ存在しないアプリでも、GPT Image 2 で完成したように見える UI スクリーンショットを作り、それを Seedance 2.0 で動画化すればプロダクトデモになります。TikTok やソーシャルメディアに投稿し、開発前に市場反応を検証できます。

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/app_case5/output0.jpg" width="400" alt="GPT Image 2 で生成したアプリ UI スクリーンショット 1"></a> |

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/app_case5/output1.jpg" width="220" alt="アプリ UI スクリーンショット 2"></a></td>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/app_case5/output2.jpg" width="220" alt="アプリ UI スクリーンショット 3"></a></td>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/app_case5/output3.jpg" width="220" alt="アプリ UI スクリーンショット 4"></a></td>
</tr></table>

**手順:**

1. アプリのコンセプトとデザイン言語を GPT Image 2 に説明する
2. 主要 UI 画面を 3〜5 枚生成する（ホーム、機能、プロフィールなど）
3. ユーザーフロー順に並べて Seedance 2.0 に読み込む
4. デモ動画を書き出し、投稿して市場の反応を見る

**GPT Image 2 プロンプト:**

```
Design [N] UI screenshots for a "[app concept]" app:
1. [Page 1 name and description]
2. [Page 2 name and description]
3. [Page 3 name and description]
Style: [iOS/Android] native design language, [primary color] accent, [light/dark] mode.
Output as realistic app screenshots, not wireframes or mockups.
```

**Seedance 2.0 プロンプト:**

```
Smooth app UI transition animation, screen tap interaction, natural interface motion, clean and modern feel, 3 seconds.
```

> [!NOTE]
> **使用前に角括弧のプレースホルダーを置き換えてください。** 動画キャプションでは AI 生成と明記せず、まずは通常のプロダクトデモとして投稿し、コメント欄で実際の反応を観察するのが有効です。


<!-- Case 6: 15-Second Commercial (by @ai_mitosan) -->
### Case 6: [15秒CM](https://x.com/ai_mitosan/status/2047146600422846762) (by [@ai_mitosan](https://x.com/ai_mitosan))

2 段階のワークフローです。GPT Image 2 でキービジュアルと対応するストーリーボードを生成し、Seedance 2.0 で各カットをアニメーション化します。字幕と音楽を加えれば、15 秒の完成 CM になります。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/commercial_case6/input1.jpg" width="280" alt="GPT Image 2 キービジュアル"></a></td>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/commercial_case6/input2.jpg" width="280" alt="GPT Image 2 絵コンテ"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/09ae3c57-b8fb-4323-ba76-7777541fe4a3" width="280" controls></video></td>
</tr></table>

**手順:**

1. image2 でメイン画像 + 絵コンテを生成する
2. それを Seedance2.0 に渡して動画化する

**ストーリーボード枚数の目安:**

| 動画尺 | コマ数 | 1クリップあたりの長さ |
| :---: | :---: | :---: |
| 15秒 | 4〜5 | 3〜4秒 |
| 30秒 | 8〜10 | 3秒 |
| 60秒 | 15〜18 | 3〜4秒 |

**GPT Image 2 プロンプト:**

```
夜カフェ　深夜スイーツをテーマにした15秒CMを作るので、絵コンテを作って。 
プロの映像クリエイターによる15秒、８カット、マルチショット、ライティング重視。
```

**Seedance 2.0 プロンプト:**

```
15秒、８カット、マルチショット、ライティング重視
```

<!-- PLACEHOLDER_CASE15 -->
