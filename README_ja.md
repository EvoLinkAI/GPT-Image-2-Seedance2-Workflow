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

GPT Image 2 × Seedance 2.0 ワークフロー集へようこそ。🤗

**このリポジトリでは、GPT Image 2 と Seedance 2.0 を組み合わせて高品質な AI 動画を制作するための、実証済みワークフロー、プロンプトテンプレート、実際のクリエイター事例をまとめています。**

GPT Image 2 は「何を描くか」とビジュアルの一貫性を担当し、Seedance 2.0 は「どう動かすか」を担当して画像を動画へとアニメーション化します。両者を組み合わせることで、現在もっとも強力な AI 動画パイプラインのひとつを構成できます。

このリポジトリの事例の多くは、X/Twitter 上のクリエイター、コミュニティ実験、実運用ワークフローからキュレーションしたものです。

Evolink ですぐ試せます: [GPT Image 2 + Seedance 2.0](https://evolink.ai?utm_source=github&utm_medium=readme&utm_campaign=gptimage2-x-seedance2)

役に立ったら、スターを付けてもらえると助かります。⭐



## 📰 ニュース

- **2026年5月1日:** Case 13–27 を追加（ダンスシーケンスグリッド、コミックページアニメーション、ラグジュアリーCM、シネマティック料理動画、ゲームインターフェースパイプライン、シングルエージェントワークフロー、絵コンテ先行コスト管理、Claude ショットリスト MV、キャスティンググリッド、3Dスカルプトパイプライン、IP サイバーパンクリメイク、GTA シティコンセプト、K-Pop 振付、プロダクト動画広告、キャラクター登場アニメーション）
- **2026年4月25日:** Case 10–12（マルチフレーム絵コンテ、日本語MV工具チェーン、Claude Code × キャラクターシート）を追加。Case 9 に ARPG シミュレーションの変形例を追加。ギャラリーにコミュニティ事例を追加
- **2026年4月23日:** 9件の厳選ワークフロー事例とともにリポジトリ公開

## 📑 メニュー

- [🎬 はじめに](#-はじめに)
- [📰 ニュース](#-ニュース)
- [📑 メニュー](#-メニュー)
- [🎥 ストーリーボード・ワークフロー](#-ストーリーボードワークフロー)
  - [Case 1: 標準ストーリーボード → 動画 (by @kiyoshi_shin)](#case-1-標準ストーリーボード--動画-by-kiyoshi_shin)
  - [Case 2: 3×3グリッド型ストーリーボード手法 (by @servasyy_ai)](#case-2-33グリッド型ストーリーボード手法-by-servasyy_ai)
  - [Case 10: マルチフレーム参照 → 高速カット動画 (by @heygentlewhale)](#case-10-マルチフレーム参照--高速カット動画-by-heygentlewhale)
  - [Case 14: コミックページ → アニメーション動画 (by @nimentrix)](#case-14-コミックページ--アニメーション動画-by-nimentrix)
  - [Case 19: 絵コンテ先行のコスト管理 (by @0xbisc)](#case-19-絵コンテ先行のコスト管理-by-0xbisc)
- [🎨 キャラクター＆アニメーション](#-キャラクターアニメーション)
  - [Case 3: キャラクター設定シート → アニメーション (by @YaReYaRu30Life)](#case-3-キャラクター設定シート--アニメーション-by-yareyaru30life)
  - [Case 4: アニメOP風動画 (by @Toshi_nyaruo_AI)](#case-4-アニメop風動画-by-toshi_nyaruo_ai)
  - [Case 12: Claude Code × キャラクターシート → アニメーション (by @old_pgmrs_will)](#case-12-claude-code--キャラクターシート--アニメーション-by-old_pgmrs_will)
  - [Case 13: ダンスシーケンスグリッド → ダンス動画 (by @Ciri_ai)](#case-13-ダンスシーケンスグリッド--ダンス動画-by-ciri_ai)
  - [Case 25: K-Pop 振付 — 精密コントロール (by @Kashberg_0)](#case-25-k-pop-振付--精密コントロール-by-kashberg_0)
  - [Case 27: キャラクター登場アニメーション (by @0xbisc)](#case-27-キャラクター登場アニメーション-by-0xbisc)
- [📱 アプリ＆プロダクトデモ](#-アプリプロダクトデモ)
  - [Case 5: アプリMVPデモ動画 (by @Shin_Engineer)](#case-5-アプリmvpデモ動画-by-shin_engineer)
  - [Case 6: 15秒CM (by @ai_mitosan)](#case-6-15秒cm-by-ai_mitosan)
  - [Case 15: ラグジュアリーCM — 絵コンテから映像へ (by @insmind_com)](#case-15-ラグジュアリーcm--絵コンテから映像へ-by-insmind_com)
  - [Case 26: 商品画像 → ショート動画広告 (by @insmind_com)](#case-26-商品画像--ショート動画広告-by-insmind_com)
- [🎵 クリエイティブ・コンビネーション](#-クリエイティブコンビネーション)
  - [Case 7: Suno を使ったミュージックビデオ (by @fukaborichannel)](#case-7-suno-を使ったミュージックビデオ-by-fukaborichannel)
  - [Case 8: サイバーパンク風短編映像 (by @ponyodong)](#case-8-サイバーパンク風短編映像-by-ponyodong)
  - [Case 9: ゲーム＆インタラクティブコンテンツ (by @AbleGPT)](#case-9-ゲームインタラクティブコンテンツ-by-ablegpt)
  - [Case 11: 日本語MV — 全AIツールチェーン (by @Tz_2022)](#case-11-日本語mv--全aiツールチェーン-by-tz_2022)
  - [Case 16: シネマティック料理動画 (by @kingofdairyque)](#case-16-シネマティック料理動画-by-kingofdairyque)
  - [Case 17: ゲームインターフェースアニメーション — フルパイプライン (by @0xInk_)](#case-17-ゲームインターフェースアニメーション--フルパイプライン-by-0xink_)
  - [Case 18: シングルエージェント自動化ワークフロー (by @venturetwins)](#case-18-シングルエージェント自動化ワークフロー-by-venturetwins)
  - [Case 20: Claude ショットリスト → ミュージックビデオ (by @CoffeeVectors)](#case-20-claude-ショットリスト--ミュージックビデオ-by-coffeevectors)
  - [Case 21: キャスティンググリッド — 俳優オーディション (by @8fstudioz)](#case-21-キャスティンググリッド--俳優オーディション-by-8fstudioz)
  - [Case 22: 3Dスカルプト → AIレンダー → アニメーション (by @_DAntunes_)](#case-22-3dスカルプト--aiレンダー--アニメーション-by-_dantunes_)
  - [Case 23: IP サイバーパンクリメイク — コンセプトフィルム (by @AYi_AInotes)](#case-23-ip-サイバーパンクリメイク--コンセプトフィルム-by-ayi_ainotes)
  - [Case 24: GTA風シティゲームコンセプト (by @markgadala)](#case-24-gta風シティゲームコンセプト-by-markgadala)
- [💡 ヒント＆テクニック](#-ヒントテクニック)
  - [一貫性ガイド](#一貫性ガイド)
  - [プロンプトテンプレート](#プロンプトテンプレート)
  - [トラブルシューティング](#トラブルシューティング)
- [🚀 Evolink で試す](#-evolink-で試す)
- [🙏 クレジット](#-クレジット)

## 🎥 ストーリーボード・ワークフロー

<!-- Case 1: Standard Storyboard → Video (by @kiyoshi_shin) -->
### Case 1: [標準ストーリーボード → 動画](https://x.com/kiyoshi_shin/status/2047133524403400847) (by [@kiyoshi_shin](https://x.com/kiyoshi_shin))

もっとも一般的なワークフローです。GPT Image 2 でストーリーボードのコマを生成し、それを Seedance 2.0 で動画化します。プロモーション動画、短編ドラマ、アニメの OP などに向いています。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/storyboard_case1/output.jpg" width="400" alt="Storyboard output panel"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/ac25fc3d-b6cb-4149-a8ba-e7e10c5b1faa" width="400" controls></video></td>
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
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/storyboard_case2/output.jpg" width="400" alt="3×3 grid storyboard output"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/00f32388-a17b-4b9c-8da3-1956436ce91b" width="400" controls></video></td>
</tr></table>



**手順:**

1. GPT Image 2 に、すべてのコマを 1 枚の 3×3 グリッド画像として出力させる
2. そのグリッド全体を 1 枚の画像として Seedance 2.0 に読み込む
3. Seedance がグリッドを動きの連続として解釈し、連続した動画を生成する

**GPT Image 2 プロンプト:**

```
Generate a single 3×3 storyboard grid image (9 panels total) showing the following continuous action:
[describe your scene here]
Requirements: each panel is clean and self-contained, character positions are consistent across panels, background is consistent, no text labels or annotations.
Output as a single image with all 9 panels arranged in a grid.
```

**Seedance 2.0 プロンプト:**

```
[Describe the motion and style. Example: Japanese full-color animation, fast cuts, high frame count, 24fps, dark fantasy anime OP style, intense battle scenes.]
```

> [!NOTE]
> **使用前に角括弧内を置き換えてください。** この方法が有効なのは、Seedance が 1 枚の画像から動きの意図を解析するためです。グリッドは進行方向の参照になり、別々の画像を渡すよりも一貫した動きを生成しやすくなります。

<!-- Case 10: Multi-Frame Reference Storyboard (by @heygentlewhale + @ai_gezgini) -->
### Case 10: [マルチフレーム参照 → 高速カット動画](https://x.com/heygentlewhale/status/2047969137969004946) (by [@heygentlewhale](https://x.com/heygentlewhale))

複数の参考フレームを含む絵コンテ画像を Seedance 2.0 に渡し、シーンの順序に従うよう指示します。モデルはフレームの位置をシーン指示として解釈し、手動での組み合わせなしに、一貫した高速カット編集を出力します。

<table><tr>
<td align="center"><video src="https://github.com/user-attachments/assets/4d7af334-4e49-4de4-899e-803f72116c21" width="400" controls></video></td>
<td align="center"><video src="https://github.com/user-attachments/assets/5def7e00-6fc6-4a4e-8075-5f37cb24b84c" width="400" controls></video></td>
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
> このプロンプトはジャンルを問わず使えます。スタイルの説明をSF、ホラー、ドキュメンタリーなど任意のものに入れ替えてください。キーフレーズは `follow the storyboard sequence of the [N] reference frames` で、フレームの位置を単一の構図ではなくタイムラインとして扱うよう Seedance に指示します。

<!-- Case 14: Comic Page → Animated Video (by @nimentrix) -->
### Case 14: [コミックページ → アニメーション動画](https://x.com/nimentrix/status/2049560412979708334) (by [@nimentrix](https://x.com/nimentrix))

GPT Image 2 で斜めレイアウト・吹き出し・シネマティックな演出を含むマルチパネルのコミックページを作成し、そのページ全体を Seedance 2.0 で動画化します。モデルはコミックのコマをナラティブシーケンスとして読み取り、連続したアニメーションショートを生成します。330 いいね / 2.1万 再生 / 360 ブックマーク。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/comic_case14/output.jpg" width="400" alt="Comic page animated video output"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/0b5038e2-dfca-4c65-b5d7-a719a74408b0" width="400" controls></video></td>
</tr></table>

**手順:**

1. GPT Image 2 でキャラクターデザインシート（正面・側面・背面）を作成し、キャラクターの外見を固定する
2. そのキャラクターを参照してマルチパネルのコミックページを生成する
3. コミックページを Seedance 2.0 に読み込んでアニメーション化する

**GPT Image 2 プロンプト — キャラクターシート:**

```
Create a character design style sheet for [describe your character]:
front view, side view, back view on white background.
Make the aspect ratio 4:3.
```

**GPT Image 2 プロンプト — コミックページ:**

```
[Character description] and [companion], american comic multi-panel illustration,
diagonal layout, six panels, cinematic storytelling, clear reading flow, with speech bubbles.
[Describe the story sequence across panels.]
```

**Seedance 2.0 プロンプト:**

```
Animate this comic page as a cinematic sequence. Follow the panel order from top-left to bottom-right.
Smooth transitions between panels, maintain character consistency, cinematic camera movement.
```

> [!NOTE]
> 斜めレイアウトと吹き出しは、Seedance にコマの境界と読み順を明確に伝える視覚的手がかりになります。各コマのアクションはシンプルかつ明確にするのが効果的です。このワークフローは Suno と組み合わせて最終動画にサウンドトラックを付けるのにも向いています。

<!-- Case 19: Storyboard-First Cost Control (by @0xbisc) -->
### Case 19: [絵コンテ先行のコスト管理](https://x.com/0xbisc/status/2049100073481716076) (by [@0xbisc](https://x.com/0xbisc))

制作コストを意識したアプローチです。まず GPT Image 2 で絵コンテを繰り返し調整し（安い）、構図が確定してから動画を生成します（高い）。動画の試行錯誤は画像の 10〜50 倍のクレジットを消費するため、大幅な節約になります。298 いいね / 1.3万 再生 / 291 ブックマーク。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/storyboard_case19/output.jpg" width="400" alt="Storyboard-first workflow output"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/09e04d80-c0d1-4a8c-9b74-2efe474acfcd" width="400" controls></video></td>
</tr></table>

**手順:**

1. GPT Image 2 で 8 コマの絵コンテグリッドを生成する
2. 各コマを確認し、満足するまで個別に再生成・編集する
3. 絵コンテ全体が確定してから、Seedance 2.0 に読み込む
4. 確定した絵コンテから一発で動画を生成する

**GPT Image 2 プロンプト:**

```
Create a single cinematic storyboard image containing 8 panels,
arranged in a 4-column horizontal grid layout across the canvas.
Panels are evenly distributed in 4 columns, forming a balanced multi-row composition.
Use generous spacing between panels for visual clarity.
[Describe each panel's content, camera angle, and action.]
Character: [fixed appearance description across all panels].
Style: [art style], cinematic lighting, high detail.
```

**Seedance 2.0 プロンプト:**

```
Follow the storyboard sequence. Cinematic [genre] style,
smooth transitions between shots, maintain character consistency,
[describe pacing and mood]. 24fps.
```

> [!NOTE]
> **絵コンテ先行がコスト面で有利な理由:** 動画の試行錯誤はクレジットを急速に消費します。絵コンテなら、カットごとに微調整して問題を早期に発見できます。動画ステップは最終レンダリング 1 回で済み、高コストな試行錯誤ループを避けられます。長尺シーケンスにおいて最もコスト効率の良いワークフローだとコミュニティでも確認されています。

## 🎨 キャラクター＆アニメーション

<!-- Case 3: Character Sheet → Animation (by @YaReYaRu30Life) -->
### Case 3: [キャラクター設定シート → アニメーション](https://x.com/YaReYaRu30Life/status/2047203375314571501) (by [@YaReYaRu30Life](https://x.com/YaReYaRu30Life))

GPT Image 2 で三面図（正面・側面・背面）のキャラクターシートを作成し、それを Seedance 2.0 でアニメーションの基準として使います。アニメキャラ、ゲームキャラ、フィギュア演出に最適です。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/character_case3/input0.jpg" width="260" alt="Character sheet front"></a></td>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/character_case3/input1.jpg" width="260" alt="Character sheet side"></a></td>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/character_case3/input2.jpg" width="260" alt="Equipment sheet"></a></td>
</tr></table>

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/character_case3/output.jpg" width="400" alt="Combined character sheet with equipment"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/92a0aa56-441f-40db-b9c9-13410254cb3f" width="400" controls></video></td>
</tr></table>

**手順:**

1. GPT Image 2 でキャラクターの三面図（正面 / 側面 / 背面）を生成する
2. 必要なら装備シートを別途生成し、完全装備の三面図にまとめる
3. その三面図を参照としてストーリーボードの各フレームを作る
4. ストーリーボードを Seedance 2.0 に読み込んで動画化する

**GPT Image 2 プロンプト:**

```
Create a character three-view sheet (front, side, back views) for the following character:
[character name], [hair color], [eye color], [outfit description], [body type].
Style: Japanese anime illustration, clean linework, flat color, white background.
All three views must maintain consistent proportions and design details.
```

**Seedance 2.0 プロンプト — 待機モーション:**

```
Japanese full-color anime style, character in natural idle breathing animation, subtle hair movement, 24fps, seamless loop.
```

**Seedance 2.0 プロンプト — 戦闘モーション:**

```
Japanese full-color anime style, high-speed cuts, high frame count, 24fps, dark fantasy anime OP style. Protagonist faces a giant creature — a sequence of high-impact combat scenes.
```

<!-- Case 4: Anime OP Style Video (by @Toshi_nyaruo_AI) -->
### Case 4: [アニメOP風動画](https://x.com/Toshi_nyaruo_AI/status/2047216971184546231) (by [@Toshi_nyaruo_AI](https://x.com/Toshi_nyaruo_AI))

GPT Image 2 でシーン設定画像を作り、Seedance 2.0 に自由に動かさせる方法です。制御を強めた出力（ストーリーボード主導）と自由度の高い出力（プロンプト主導）を比較すると、カットごとに最適なアプローチを選びやすくなります。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/character_case4/output0.jpg" width="280" alt="Anime OP output 1"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/f08a2fee-89a7-4c7c-a58a-f1306f87419a" width="280" controls></video></td>
<td align="center"><video src="https://github.com/user-attachments/assets/09d81a41-b5c5-47f3-8c67-442b7a93b019" width="280" controls></video></td>
</tr></table>

**手順:**

1. GPT Image 2 でディテールの多いシーン設定画像を生成する
2. 最小限の動きプロンプトで Seedance 2.0 に読み込む
3. 必要に応じて比較する: 1 つは厳密なストーリーボード制御、もう 1 つは Seedance に自由に動かさせる

**GPT Image 2 プロンプト:**

```
Create a scene setting illustration for a dark fantasy anime:
Location: [describe location], Time: [day/night], Atmosphere: [mood].
Style: Japanese anime production art, high detail, cinematic composition.
Character: [character name and appearance]. Fix this visual design across all panels.
```

**Seedance 2.0 プロンプト:**

```
Japanese full-color anime, fast cuts, high frame count, 24fps. Dark fantasy anime OP style. Epic battle between protagonist and massive supernatural creatures. High-impact sequence of scenes. Only [character name] appears.
```

> [!NOTE]
> ストーリーボード参照なしで Seedance に自由に動かさせると、よりダイナミックな結果になりやすい一方、元画像との一致度は下がります。主要キャラクターの重要カットはストーリーボード制御、アクションシーンは自由アニメーションという使い分けが有効です。

<!-- Case 12: Claude Code + Character Sheet → Animation (by @old_pgmrs_will) -->
### Case 12: [Claude Code × キャラクターシート → アニメーション](https://x.com/old_pgmrs_will/status/2045091769180914019) (by [@old_pgmrs_will](https://x.com/old_pgmrs_will))

Claude Code で世界観とキャラクター設定を書き、その構造化した記述を GPT Image 2 に渡してキャラクターのキービジュアルを生成し、最後に Seedance 2.0 でアニメーション化します。開発者向けのオリジナル IP 制作ワークフローです。191 いいね / 7K 再生。

<table><tr>
<td align="center"><a href="https://evolink.ai/seedance2?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/character_case12/output.jpg" width="400" alt="Claude Code + GPT Image 2 キャラクターキービジュアル"></a></td>
</tr></table>

**手順:**

1. Claude Code で世界観メモと構造化されたキャラクター仕様（名前・外見・性格・設定）を作成する
2. そのキャラクター仕様をそのまま GPT Image 2 に渡し、キービジュアルやキャラクターシートを生成する
3. そのキービジュアルを Seedance 2.0 の参考画像として使ってアニメーション化する

**Claude Code → GPT Image 2 引き渡しプロンプト:**

```
Based on the following character spec, generate a key visual for [character name]:
[Paste Claude Code output here — name, appearance, outfit, world setting, mood]
Style: [anime / cinematic illustration / game art], [color palette].
Fix this character design — it will be used as a reference across all subsequent images.
```

**Seedance 2.0 プロンプト:**

```
Japanese full-color anime style, character in natural idle breathing animation,
subtle hair and clothing movement, 24fps, seamless loop.
[Or: high-speed cuts, 24fps, dark fantasy anime OP style — protagonist in opening sequence.]
```

> [!NOTE]
> Claude Code が出力する構造化テキスト（キャラクター仕様、シーン説明、セリフ概要など）は、GPT Image 2 の詳細プロンプトとして非常に相性が良いです。オリジナルストーリー IP に特に有効なパイプラインです：世界観をコードで構築し、GPT Image 2 で可視化し、Seedance でアニメーション化する。

<!-- Case 13: Dance Sequence Grid → Dance Video (by @Ciri_ai) -->
### Case 13: [ダンスシーケンスグリッド → ダンス動画](https://x.com/Ciri_ai/status/2049034340160704643) (by [@Ciri_ai](https://x.com/Ciri_ai))

GPT Image 2 で 4×4 のダンスポーズグリッドを生成し、それを Seedance 2.0 にモーションリファレンスとして渡します。モデルはグリッドを振付シーケンスとして読み取り、連続したダンス動画を出力します。上級テクニック: 複数のキャラクターリファレンスをアップロードして、ビートに合わせた衣装チェンジも可能。161 いいね / 9K 再生。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/dance_case13/output.jpg" width="400" alt="Dance sequence grid output"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/39376245-e7c7-4812-b770-9e81acf4eca2" width="400" controls></video></td>
</tr></table>

**手順:**

1. GPT Image 2 で連続したダンスポーズを示す 4×4 グリッド画像を生成する
2. そのグリッドを Seedance 2.0 にリファレンス画像としてアップロードする
3. リファレンス画像のダンスシーケンスに従うよう Seedance にプロンプトを書く
4. （上級）衣装 A のキャラクター、衣装 B のキャラクター、ダンスグリッドの 3 枚をリファレンスとしてアップロードし、ダンス中の衣装チェンジを実現する

**GPT Image 2 プロンプト:**

```
Create a 4x4 image grid showing [character description] in various dance moves, in a logical sequence.
Style: [anime / realistic / stylized], consistent character design across all 16 panels.
```

**Seedance 2.0 プロンプト:**

```
The character dances according to the sequence in the reference image@image1. No text.
```

**上級 — ビート同期の衣装チェンジ:**

```
Character from Image 1 performs the dance based on the breakdown in Image 3.
Midway through the performance, they switch outfits on beat into the character from Image 2.
Then, the character from Image 2 continues and completes the remaining dance steps from Image 3.
Emphasize precise beat synchronization with the music.
```

> [!NOTE]
> このテクニックはダンスに限らず、格闘技、スポーツなど、あらゆる動きのシーケンスに応用できます。4×4 グリッドは Seedance に 16 フレームの補間参照を与えるため、少ないパネルよりも滑らかな動きが得られます。
>
> **コミュニティの変形例:** [@airina_xyz](https://x.com/airina_xyz/status/2049830199236190326) がストリートダンサーで基本ワークフローを実演。[@Kashberg_0](https://x.com/Kashberg_0/status/2049697925262102689) がキャラクターボード + モーションリファレンスフレームで K-Pop 振付を実現（52 いいね / 2K 再生）。

<!-- Case 25: K-Pop Choreography with Detailed Control (by @Kashberg_0) -->
### Case 25: [K-Pop 振付 — 精密コントロール](https://x.com/Kashberg_0/status/2049839091899088948) (by [@Kashberg_0](https://x.com/Kashberg_0))

ダンスアニメーションの最大限のコントロール: 16 ステップの振付ブレイクダウンを詳細な動き記述付きで書き、GPT Image 2 でリファレンスグリッドを生成し、Seedance 2.0 でアニメーション化します。各ステップ 2〜3 秒で、35〜50 秒の連続ダンス動画が本格的な K-Pop のクオリティで仕上がります。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/kpop_case25/input.jpg" width="400" alt="K-Pop choreography reference grid"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/1c088b5e-6305-4bf6-9377-97784d5f8fac" width="400" controls></video></td>
</tr></table>

**手順:**

1. 詳細な振付シーケンスを書く（16 ステップ、具体的なダンスムーブ付き）
2. GPT Image 2 で各ステップを示すリファレンスグリッドを生成する
3. グリッド + 振付の全記述を Seedance 2.0 に渡す
4. モデルがステップシーケンスに従い、滑らかなトランジションで動画を生成する

**GPT Image 2 プロンプト:**

```
Create a 4x4 grid (16 panels) showing a [character description] performing K-pop choreography:
Step 1: Starting Pose
Step 2: Step Touch Right
Step 3: Step Touch Left
[... list all 16 steps ...]
Step 16: Final Pose (hold)
Style: photorealistic, consistent character, clean background, full-body framing.
```

**Seedance 2.0 プロンプト:**

```
K-pop dance video, [character description], performing the exact 16-step choreography
from the reference grid in order. Each step 2-3 seconds.
Movement style: mix of sharp hits and smooth transitions, clean isolations,
controlled spins, balanced footwork. No jitter.
Full-body framing, smooth tracking camera, continuous flow.
Tempo: 100-115 BPM feel. Final pose held 2-3 seconds.
```

> [!NOTE]
> ステップの記述が具体的であるほど、Seedance は振付に忠実に従います。曖昧な表現ではなく、実際のダンスムーブ名（ボディロール、ヘアフリップ、チェストポップなど）を使いましょう。このテクニックは格闘技の型、ヨガフロー、その他の連続動作にも応用できます。

<!-- Case 27: Character Intro Animation (by @0xbisc) -->
### Case 27: [キャラクター登場アニメーション](https://x.com/0xbisc/status/2049496584283656690) (by [@0xbisc](https://x.com/0xbisc))

サイバーパンク AAA ゲーム風のキャラクター登場アニメーションを作成します。任意のキャラクター画像を GPT Image 2 でゲームキャラクターにリデザインし、シネマティックなイントロ画面を生成してから、Seedance 2.0 で登場演出をアニメーション化します。どんなキャラクターでも差し替え可能な汎用ワークフローです。55 いいね / 3K 再生。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/intro_case27/output.jpg" width="400" alt="Character intro animation output"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/e52eaa0b-b2fa-4c35-b790-a92af05d0c82" width="400" controls></video></td>
</tr></table>

**手順:**

1. キャラクター画像を用意する（自作イラスト、写真、AI 生成画像など）
2. GPT Image 2 でサイバーパンク AAA ゲームキャラクターにリデザインする — 顔の特徴は維持しつつスタイルをアップグレード
3. そのキャラクターでシネマティックなイントロ画面を生成する（暗い背景、ドラマチックな照明、タイトルカードレイアウト）
4. Seedance 2.0 でイントロの登場演出をアニメーション化する

**GPT Image 2 プロンプト — キャラクターリデザイン:**

```
Based on the provided image, redesign as a cyberpunk AAA game character.
Keep face identity, keep original outfit.
Hyper-realistic game character, near-photoreal but still game-rendered.
Cinematic lighting, dark moody atmosphere, neon accent colors.
```

**GPT Image 2 プロンプト — イントロ画面:**

```
Cinematic game character introduction screen.
Character: [redesigned character] standing in [dramatic pose].
Background: dark, atmospheric, [genre-appropriate environment].
Layout: character centered, space for title text above, dramatic rim lighting.
Style: AAA game quality, Unreal Engine 5 look.
```

**Seedance 2.0 プロンプト:**

```
Cinematic character reveal animation. Camera slowly pushes in on the character,
dramatic lighting builds, subtle particle effects, atmospheric fog,
character shifts weight slightly, eyes lock to camera.
AAA game intro quality, 24fps, 5 seconds.
```

> [!NOTE]
> このワークフローはキャラクターを選びません。アニメ、リアル、スタイライズなど、どんなキャラクターでもパイプラインが適応します。ポイントは GPT Image 2 の 2 段階プロセス: まずキャラクターをターゲットスタイルにリデザインし、次にイントロ画面のレイアウトを構成することです。

## 📱 アプリ＆プロダクトデモ

<!-- Case 5: App MVP Demo Video (by @Shin_Engineer) -->
### Case 5: [アプリMVPデモ動画](https://x.com/Shin_Engineer/status/2047182050323812381) (by [@Shin_Engineer](https://x.com/Shin_Engineer))

まだ存在しないアプリでも、GPT Image 2 で完成したように見える UI スクリーンショットを作り、それを Seedance 2.0 で動画化すればプロダクトデモになります。TikTok などに投稿し、開発前に市場反応を検証できます。

| Output |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/app_case5/output0.jpg" width="400" alt="GPT Image 2 generated app UI screenshot 1"></a> |

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/app_case5/output1.jpg" width="220" alt="App UI screenshot 2"></a></td>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/app_case5/output2.jpg" width="220" alt="App UI screenshot 3"></a></td>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/app_case5/output3.jpg" width="220" alt="App UI screenshot 4"></a></td>
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

2 段階のワークフローです。まず GPT Image 2 でキービジュアルと対応するストーリーボードを生成し、その後 Seedance 2.0 で各カットをアニメーション化します。最後に字幕と音楽を加えれば、15 秒の完成 CM になります。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/commercial_case6/output.jpg" width="400" alt="Commercial output image"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/09ae3c57-b8fb-4323-ba76-7777541fe4a3" width="400" controls></video></td>
</tr></table>

**手順:**

1. GPT Image 2 でヒーロービジュアル（商品 / キャラクター / シーン）を生成する
2. そのビジュアルをもとに 4〜5 コマのストーリーボードを作る
3. 各コマを Seedance 2.0 で 3〜4 秒程度のクリップにする
4. クリップをつなぎ、字幕と音楽を追加する

**ストーリーボード枚数の目安:**

| 動画尺 | コマ数 | 1クリップあたりの長さ |
| :---: | :---: | :---: |
| 15秒 | 4〜5 | 3〜4秒 |
| 30秒 | 8〜10 | 3秒 |
| 60秒 | 15〜18 | 3〜4秒 |

**GPT Image 2 プロンプト:**

```
Create a 5-panel storyboard for a 15-second commercial for [product/brand]:
Panel 1: [opening shot]
Panel 2: [product feature]
Panel 3: [emotional moment]
Panel 4: [call to action]
Panel 5: [closing brand shot]
Style: [brand aesthetic], 16:9 widescreen, cinematic.
```

**Seedance 2.0 プロンプト:**

```
Cinematic commercial quality, [brand tone: premium / energetic / warm], [product name] centered in frame, slow camera push-in, [lighting direction] lighting highlights the product, clean background, no people, 3 seconds.
```

<!-- Case 15: Luxury Commercial — Storyboard to Film (by @insmind_com) -->
### Case 15: [ラグジュアリーCM — 絵コンテから映像へ](https://x.com/insmind_com/status/2049481439285223785) (by [@insmind_com](https://x.com/insmind_com))

GPT Image 2 でラグジュアリーフレグランス広告用の 3×4 絵コンテグリッド（12 フレーム）を生成し、Seedance 2.0 でシネマティックなブランドレベルの映像にアニメーション化します。イントロ → 儀式 → 変容 → 解決 → ブランドクロージングという構造化されたフローが、1 回の生成で完全なナラティブアークを生み出します。371 いいね / 8.4万 再生 / 255 ブックマーク。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/luxury_case15/output.jpg" width="400" alt="Luxury commercial storyboard"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/281fef1e-f42d-442c-b06e-44d7cff221ec" width="400" controls></video></td>
</tr></table>

**手順:**

1. GPT Image 2 で 12 フレームの絵コンテグリッド（3×4）を生成する。エディトリアルレイアウトとラグジュアリーブランドの美学を使用
2. 絵コンテグリッドを 1 枚のリファレンス画像として Seedance 2.0 に読み込む
3. シネマティックなラグジュアリー CM としてシーケンスをアニメーション化するよう Seedance にプロンプトを書く
4. 編集ソフトで音楽と最終カラーグレーディングを追加する

**GPT Image 2 プロンプト:**

```
Create a high-end 9:16 luxury fragrance pitch deck storyboard in 3x4 grid (12 frames),
editorial layout, Aesop/Byredo style, beige + lavender palette.
Structured flow: intro → ritual → transformation → resolution → brand closure.
Each frame split: top = visual direction, bottom = scene.
Minimal text, elegant typography, soft lighting, product-centered compositions.
```

**Seedance 2.0 プロンプト:**

```
Follow the storyboard sequence. Cinematic luxury fragrance commercial,
soft natural lighting, slow deliberate movements, shallow depth of field,
editorial pacing, premium brand aesthetic, smooth transitions between scenes.
```

> [!NOTE]
> エディトリアルなピッチデックレイアウト（各フレームにビジュアルディレクションのメモ付き）は、プレーンなグリッドよりも Seedance に強いナラティブの手がかりを与えます。このワークフローはスキンケア、時計、ファッションなど、あらゆるラグジュアリー商品カテゴリーに応用可能です。パレットと商品リファレンスを入れ替えるだけで対応できます。

<!-- Case 26: Product Image → Short Video Ad (by @insmind_com) -->
### Case 26: [商品画像 → ショート動画広告](https://x.com/insmind_com/status/2049843814337306974) (by [@insmind_com](https://x.com/insmind_com))

静止画の商品写真を、スクロールを止めるソーシャルメディア動画に変換します。既存の商品写真を GPT Image 2 にリファレンスとしてアップロードし、シーン構成を生成してから、Seedance 2.0 でアニメーション化します。EC やソーシャルメディアマーケティング向けに設計されており、手持ちの商品写真から TikTok/Reels 対応のコンテンツを制作できます。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/product_case26/output.jpg" width="400" alt="Product video ad output"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/880c0019-e45a-4eb9-be6f-638ff71a0e0f" width="400" controls></video></td>
</tr></table>

**手順:**

1. 既存の商品画像を GPT Image 2 にリファレンスとして入力する
2. 商品をコンテキスト内で見せるシーン構成を生成する
3. 構成されたシーンを Seedance 2.0 に読み込む
4. 自然な商品インタラクションモーションでアニメーション化する

**GPT Image 2 プロンプト:**

```
Product A (ref image 1), Product B (ref image 2).
Fixed camera shot. [Describe the scene context — e.g., a phone playing a video,
hands interacting with products, lifestyle setting].
Style: commercial photography, soft lighting, clean composition.
9:16 vertical format for social media.
```

**Seedance 2.0 プロンプト:**

```
Smooth product showcase animation, natural hand interaction,
subtle camera movement, soft lighting transitions,
commercial quality, clean and modern feel, 3-5 seconds.
```

> [!NOTE]
> Case 15（ラグジュアリー CM）との違いは、すべてをゼロから生成するのではなく、既存の商品写真からスタートする点です。すでに商品画像を持っている EC セラーが、それを素早く動画広告に変換したい場合に最適です。

## 🎵 クリエイティブ・コンビネーション

<!-- Case 7: Music Video with Suno (by @fukaborichannel) -->
### Case 7: [Suno を使ったミュージックビデオ](https://x.com/fukaborichannel/status/2047206670020055317) (by [@fukaborichannel](https://x.com/fukaborichannel))

3 つのツールを組み合わせるワークフローです。ビジュアルは GPT Image 2、動きは Seedance 2.0、音楽は Suno が担当します。先に楽曲を作ってテンポと構成を確定し、そのビートに合わせてストーリーボードを設計します。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/music_case7/input.jpg" width="280" alt="GPT Image 2 generated storyboard for MV"></a></td>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/music_case7/output.jpg" width="280" alt="Music video output frame"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/fd4be5c7-cd02-4a77-ae07-6b80efeff201" width="280" controls></video></td>
</tr></table>

**手順:**

1. Suno で狙った雰囲気の楽曲を生成し、構成（イントロ / Aメロ / サビ）を確定する
2. 各パートに対応するストーリーボードを GPT Image 2 で作る
3. Seedance 2.0 で各パネルをアニメーション化し、尺をビートに合わせる
4. 編集ソフト上で映像を音楽に同期させる

**GPT Image 2 プロンプト:**

```
Create a [N]-panel storyboard for a music video in [style] style:
Intro: [visual concept]
Verse: [visual concept]
Chorus: [visual concept]
Style: [art style], [color palette], [mood].
```

**Seedance 2.0 プロンプト — City Pop 風:**

```
Japanese city pop anime style, soft summer afternoon light, character walking lightly, Tokyo street background, blue sky, film grain texture, 24fps.
```

> [!NOTE]
> 先に音楽を作るのが重要です。テンポと曲尺を把握してからストーリーボードを設計すると、各カットの長さをビートに正確に合わせられます。

<!-- Case 8: Cyberpunk Style Short Film (by @ponyodong) -->
### Case 8: [サイバーパンク風短編映像](https://x.com/ponyodong/status/2047210987263230133) (by [@ponyodong](https://x.com/ponyodong))

GPT Image 2 でサイバーパンク、ネオン、提灯、フェミニンな雰囲気などのビジュアルルールを固定し、その画像を Seedance 2.0 で動かして、壁紙・ポスター・物語の導入の中間にあるようなスタイライズ短編を作ります。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/cyberpunk_case8/input.jpg" width="280" alt="GPT Image 2 generated cyberpunk illustration"></a></td>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/cyberpunk_case8/output.jpg" width="280" alt="Cyberpunk output frame"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/db6ebb63-90dc-47c5-96c5-ab2fa53ed56d" width="280" controls></video></td>
</tr></table>

**手順:**

1. GPT Image 2 で色、照明、キャラクターデザインを固定したビジュアルルールを定義する
2. 同じムードを持つ画像を 4〜6 枚生成する
3. Seedance 2.0 で、ゆっくりした雰囲気重視のモーションプロンプトを使って各画像を動かす
4. クリップを並べて短い映像ナラティブにする

**GPT Image 2 プロンプト:**

```
Generate a [style] illustration:
Visual elements: [neon lights / lanterns / rain / specific props].
Character: [appearance description]. Keep this character design fixed across all images.
Color palette: [dominant colors].
Mood: [atmospheric, cinematic, etc.].
```

**Seedance 2.0 プロンプト:**

```
Slow atmospheric camera drift, neon reflections on wet pavement, soft particle effects, cinematic color grade, 24fps, 4 seconds.
```

<!-- Case 9: Game & Interactive Content (by @AbleGPT) -->
### Case 9: [ゲーム＆インタラクティブコンテンツ](https://x.com/AbleGPT/status/2047149644778746020) (by [@AbleGPT](https://x.com/AbleGPT))

HUD、スキルバー、選択肢オーバーレイ付きのゲーム風 UI 画像を GPT Image 2 で作り、それを Seedance 2.0 で動かして、インタラクティブなゲームシーケンスを再現します。リアルな人物映像よりも、ゲーム・イラスト・アニメ系のスタイルは Seedance 上で制限が少なく、表現の幅も広いです。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/game_case9/output.jpg" width="400" alt="Game UI output image"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/fa3b3fed-21eb-417a-a6a6-7f98990368ce" width="400" controls></video></td>
</tr></table>

**手順:**

1. HUD を含む ARPG / ゲーム UI 風の画像を GPT Image 2 で生成する
2. Seedance 2.0 に読み込み、操作や戦闘の流れを記述する
3. パーティクルやグローなどの後処理を加えて完成度を上げる

**GPT Image 2 プロンプト:**

```
Generate a game UI screenshot in [Black Myth / ARPG / JRPG] style:
Theme: [Chinese mythology / fantasy / sci-fi].
UI elements: health bar, skill icons, choice panel with options A/B/C.
Art style: [realistic / painterly / anime], high detail rendering.
```

**Seedance 2.0 プロンプト:**

```
Click option A, normal UI transition animation, then a reasonable combat sequence begins.
[Style: Black Myth style, Chinese mythological martial arts, realistic rendering, dynamic camera work.]
```

**バリエーション — ARPG ゲームシミュレーション (by [@0xbisc](https://x.com/0xbisc/status/2047315350862352715)):**

ワンピース、ストレンジャー・シングス、どの IP でも OK。存在しないゲームのスクリーンショットを GPT Image 2 で生成し、Seedance 2.0 でリアルなゲームプレイに拡張します。934 いいね / 12.5万 再生。

<table><tr>
<td align="center"><video src="https://github.com/user-attachments/assets/983b433a-88ea-4843-9047-fc01396752fe" width="400" controls></video></td>
</tr></table>

**GPT Image 2 プロンプト:**

```
Generate an ARPG dialogue game screenshot inspired by [film/series name]
```

**Seedance 2.0:** Image-to-Video モードを使います。プロンプト不要 — Seedance が HUD レイアウトを読み取り、自動的にゲームプレイシーケンスに拡張します。

> [!NOTE]
> Seedance 2.0 はリアルな人物コンテンツに制限があります。ゲーム、アニメ、イラスト系のスタイルなら、こうした制約の多くを回避でき、より広い表現が可能です。
>
> **ARPG のヒント (via [@peter6759](https://x.com/peter6759/status/2047130834180903166)):** インタラクティブムービーゲーム風にするには、2つのステップを1回に統合します。GPT Image 2 プロンプト: `Interactive movie game, Black Myth style, Water Margin` → Seedance 2.0 プロンプト: `Click option A, normal UI shift, then reasonable combat happens`。GPT Image 2 に中国語プロンプト、Seedance に英語という二言語アプローチが文化的再現度を高めることが多いです。
>
> **コミュニティ紹介:** [@markgadala](https://x.com/markgadala/status/2047825115631518115) はこのワークフローを使って存在しないゲームの完全なトレーラーを生成しました。[@0xInk_](https://x.com/0xInk_/status/2048809000121360649) はビデオゲームインターフェースアニメーションの完全な 4 ステップワークフローを共有しました — Midjourney キャラクターシート → GPT Image 2 で 3D 変換と UI デザイン → Seedance 2.0 でアニメーション化（2280 いいね / 20.8万 再生 / 2793 ブックマーク）。[@0xbisc](https://x.com/0xbisc/status/2049496584283656690) はサイバーパンクキャラクター登場アニメーションのワークフローを実演（55 いいね / 3K 再生）。

<!-- Case 11: Japanese MV Full Toolchain (by @Tz_2022) -->
### Case 11: [日本語MV — 全AIツールチェーン](https://x.com/Tz_2022/status/2047684399404056609) (by [@Tz_2022](https://x.com/Tz_2022))

4ツールのパイプラインで完全な日本語スタイルのミュージックビデオを制作: GPT Image 2 でビジュアル → Seedance 2.0 でモーション → Suno 5.5 で音楽 → CapCut で最終編集。742 いいね / 10.7万 再生。

<table><tr>
<td align="center"><video src="https://github.com/user-attachments/assets/e5ce621c-7fa3-47b5-99a7-00df7741a651" width="400" controls></video></td>
</tr></table>

**手順:**

1. まず Suno 5.5 で音楽を生成する — 曲の長さ、テンポ、ムードを確定する
2. 曲のセクションに合わせて GPT Image 2 で絵コンテパネルを設計する
3. Seedance 2.0 で各パネルをアニメーション化し、クリップの長さをビートに合わせる
4. 動画クリップと Suno トラックを CapCut にインポートし、同期してエクスポートする

**GPT Image 2 プロンプト:**

```
Create a [N]-panel storyboard for a Japanese-style music video:
Intro: [visual concept]
Verse: [visual concept]
Chorus: [visual concept]
Style: [anime illustration / painterly / film still], [color palette], [mood].
Character: [name and appearance]. Keep this character design fixed across all panels.
```

**Seedance 2.0 プロンプト:**

```
Japanese anime style, [season] atmosphere, [lighting description], soft film grain, 24fps.
[Character name] [action description], [background description].
```

> [!NOTE]
> 先に音楽を作りましょう。絵コンテを設計する前にビート構造を把握しておくと、パネルのタイミングを曲のカットに正確に合わせられます。これは Case 7（シティポップ MV）の発展形で、Suno をループに追加し、パイプライン全体を後付け組み立てではなく同期したプロダクションとして扱います。

<!-- Case 16: Cinematic Food Video (by @kingofdairyque) -->
### Case 16: [シネマティック料理動画](https://x.com/kingofdairyque/status/2049812014596599834) (by [@kingofdairyque](https://x.com/kingofdairyque))

GPT Image 2 + Seedance 2.0 で、タイムスタンプ付きショット記述による超リアルな料理動画を作成します。各タイムスタンプセグメント（0〜2秒、2〜4秒など）が特定のカメラアングルとアクションを定義し、Seedance に 15 秒のシーケンスを精密にコントロールさせます。55 いいね / 1K 再生。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/food_case16/input.jpg" width="400" alt="Food video storyboard input"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/30a20e57-8384-4117-adf7-4f92faebeb33" width="400" controls></video></td>
</tr></table>

**手順:**

1. 各 2 秒セグメントを記述した詳細なタイムスタンプ付きショットリストを書く
2. そのショットリストに基づいて GPT Image 2 で絵コンテ画像を生成する
3. 画像 + タイムスタンプ付きプロンプト全文を Seedance 2.0 に渡す
4. モデルがタイムスタンプ構造に従い、一貫した調理シーケンスを生成する

**GPT Image 2 プロンプト:**

```
Ultra-realistic cinematic food photography storyboard, dark rustic wooden table,
soft dramatic lighting, shallow depth of field, natural textures.
[Describe the dish and key preparation moments across 6-8 panels.]
Style: editorial food photography, warm tones, no text.
```

**Seedance 2.0 プロンプト:**

```
Ultra-realistic cinematic 15-second vertical video (9:16), 4K, dark rustic wooden table,
soft dramatic lighting, shallow depth of field, natural textures, no text, no subtitles, no music.
[0-2s] Top-down shot: hands gently touch a bowl of [ingredient]. Subtle ambient movement.
[2-4s] Side close shot: [preparation action] in slow motion, catching warm light.
[4-6s] Macro shot: hands [action]. Texture detail visible.
[6-8s] 45-degree angle: [ingredient] pours into [vessel]. Natural bounce and movement.
[8-10s] Top angled close-up: hands carefully [assembly action]. Precise controlled motion.
[10-12s] Side shot: oven door opens. Warm golden light spills out with gentle steam.
[12-14s] Close-up: [finishing touch]. Surface becomes glossy, light reflecting softly.
[14-15s] Final frontal shot: finished [dish] on rustic table. Hands enter frame softly.
```

> [!NOTE]
> タイムスタンプ付きプロンプトのテクニックは、Seedance にショットごとの正確なタイムラインを与えます。開封動画、クラフト制作、カクテルメイキングなど、あらゆるプロダクト・プロセス動画に応用可能です。各セグメントは 2 秒に抑え、カメラアングルとアクションの両方を記述するのが効果的です。

<!-- Case 17: Game Interface Animation Full Pipeline (by @0xInk_) -->
### Case 17: [ゲームインターフェースアニメーション — フルパイプライン](https://x.com/0xInk_/status/2048809000121360649) (by [@0xInk_](https://x.com/0xInk_))

このコレクションで最もバイラルになったワークフロー: ゼロから完全なビデオゲームインターフェースアニメーションを作成します。Midjourney で 2D キャラクターを作り、GPT Image 2 で 3D ゲーム風に変換し、フルゲーム UI（HUD、ローディング画面、メニュー）をデザインしてから、Seedance 2.0 ですべてをアニメーション化します。GPT Image 2 は UI の細部を扱い、品質劣化なしに繰り返し修正できるため、ここで真価を発揮します。2280 いいね / 20.8万 再生 / 2793 ブックマーク。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/game_case17/output.jpg" width="400" alt="Game interface animation output"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/b83da8f3-3dd6-44a3-bb27-b0d59cab381a" width="400" controls></video></td>
</tr></table>

**手順:**

1. Midjourney で 2D キャラクターシートを作成する（全身、正面、詳細な外見付き）
2. GPT Image 2 で 2D キャラクターを 3D ゲームレンダリング風に変換する
3. GPT Image 2 でゲーム UI 画面をデザインする — キャラクター選択、ローディング画面、HUD オーバーレイ
4. 各 UI 画面を Seedance 2.0 に読み込み、トランジションをアニメーション化する

**GPT Image 2 プロンプト — 3D 変換:**

```
Based on the provided image, redesign as a [genre] AAA game character.
Keep face identity, keep original outfit.
Hyper-realistic game character, near-photoreal but still game-rendered.
Cinematic lighting, Unreal Engine 5 quality.
```

**GPT Image 2 プロンプト — ゲーム UI:**

```
Create a AAA game [screen type: character select / loading / HUD] screen.
Character: [description from previous step].
UI elements: [health bar / skill icons / menu buttons / loading progress].
Style: [cyberpunk / fantasy / sci-fi], dark cinematic lighting, 16:9.
```

**Seedance 2.0 プロンプト:**

```
Game UI animation sequence. Smooth transition from [screen A] to [screen B],
cinematic camera movement, UI elements animate in with subtle glow effects,
AAA game quality, 24fps.
```

> [!NOTE]
> 重要なポイント: GPT Image 2 は品質劣化なしに画像を何度でも修正できるため、UI レイアウトの反復作業に最適です。ゲームインターフェース全体を一連の静止画面として構築し、Seedance でそれらをシームレスなアニメーションにつなげましょう。

<!-- Case 18: Single Agent Automated Workflow (by @venturetwins) -->
### Case 18: [シングルエージェント自動化ワークフロー](https://x.com/venturetwins/status/2048526911056613586) (by [@venturetwins](https://x.com/venturetwins))

手間ゼロのアプローチ: 単一の AI エージェント（Glif など）に欲しい動画を伝えるだけで、GPT Image 2 での絵コンテ生成から Seedance 2.0 でのアニメーション化まで、パイプライン全体を 1 つの会話内で処理します。手動のファイル転送もステップごとのプロンプト設計も不要です。934 いいね / 7万 再生。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/agent_case18/output.jpg" width="400" alt="Single agent automated workflow output"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/cc01849d-ee9b-47af-a7b0-d13250a001e0" width="400" controls></video></td>
</tr></table>

**手順:**

1. エージェントプラットフォーム（Glif、Flowith など）を開く
2. 欲しい動画を自然言語で説明する
3. エージェントが GPT Image 2 で絵コンテを自動生成する
4. エージェントが絵コンテを Seedance 2.0 に渡し、最終動画を返す

**エージェントへのプロンプト例:**

```
I want to create a [genre] anime short.
Scene: [describe the story in 2-3 sentences].
Style: [anime / cinematic / realistic].
Make it [duration] seconds.
```

> [!NOTE]
> このワークフローは技術的な摩擦をすべて取り除きます。プロンプトエンジニアリングの知識もツール間のファイル管理も不要です。トレードオフは個々のショットに対するコントロールが減ること。ラピッドプロトタイピングやアイデア検証に最適です。[@heyglif](https://x.com/heyglif)、[@flowith](https://x.com/flowith) などのエージェントプラットフォームで動作確認済みです。

<!-- Case 20: Claude Shotlist → MV (by @CoffeeVectors) -->
### Case 20: [Claude ショットリスト → ミュージックビデオ](https://x.com/CoffeeVectors/status/2049592150581485757) (by [@CoffeeVectors](https://x.com/CoffeeVectors))

Claude で詳細なショットリスト（異なるカメラアングルとアクションの 15 本の 1 秒クリップ）を生成し、GPT Image 2 で 1 枚のポートレートを作成してから、Seedance 2.0 で各ショットを制作します。クリップを編集して自作の Suno 音楽と合わせれば、完全な MV の完成です。AI がクリエイティブディレクションを書き、あなたは実行するだけです。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/shotlist_case20/output.jpg" width="400" alt="Claude shotlist music video output"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/d6ba86c4-65c3-4b1d-aa3c-846667f53b5e" width="400" controls></video></td>
</tr></table>

**手順:**

1. GPT Image 2 でビジュアルアンカーとなる 1 枚のキャラクターポートレートを生成する
2. Claude に 15 ショットのショットリスト（1 秒 1 ショット）を書かせる。多様なアングルとアクション付き
3. ポートレート + 各ショット記述を Seedance 2.0 に個別に渡す
4. すべてのクリップを編集し、音楽トラックに同期させる

**Claude へのショットリストプロンプト:**

```
Write a 15-second prestige-TV sequence, one shot per second.
Character: [describe the character from your GPT Image 2 portrait].
Mood: [apocalyptic / romantic / action / ethereal].
Each shot should specify: camera angle, character action, lighting, and visual effect.
Format as a numbered list, one line per shot.
```

**Seedance 2.0 プロンプト（ショットごと）:**

```
[Paste individual shot description from Claude's list.]
Reference image: the character portrait.
Style: cinematic, [mood], dramatic lighting, 24fps.
```

> [!NOTE]
> このワークフローはクリエイティブディレクション（Claude）とビジュアル実行（GPT Image 2 + Seedance）を分離します。同じキャラクターの多様なショットが必要なミュージックビデオに特に効果的です。1 枚のポートレートをアンカーにすることで、15 クリップすべてで一貫性を維持できます。

<!-- Case 21: Casting Grid Actor Audition (by @8fstudioz) -->
### Case 21: [キャスティンググリッド — 俳優オーディション](https://x.com/8fstudioz/status/2049547426198151627) (by [@8fstudioz](https://x.com/8fstudioz))

1 回の生成で 4 人の俳優をオーディションしてクレジットを節約します。GPT Image 2 で同じ役に異なる 4 人の俳優を示す 4 パネルのキャスティンググリッドを生成し、Seedance 2.0 で同じセリフを使って各俳優をテストします。フル動画にクレジットを投入する前に、どの俳優に価値があるかを見極められます。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/casting_case21/input.jpg" width="400" alt="Casting grid input"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/dcdd958f-70cd-43f6-b191-4e0715fe2472" width="400" controls></video></td>
</tr></table>

**手順:**

1. GPT Image 2 で 4 パネルのキャスティンググリッドを生成する — 同じ役、4 人の異なる俳優
2. Seedance 2.0 で同じセリフとアクションを使って各俳優を個別にテストする
3. パフォーマンスの品質（アイコンタクト、表情、動き）を比較する
4. 残りのクレジットは勝者の俳優にのみ投入する

**GPT Image 2 プロンプト:**

```
Create a 16:9 horizontal cinematic casting board showing 4 different actor candidates for the same role.
Style: [CGI AAA video game cinematic / photorealistic / anime / stylized 3D].
Role brief: [describe the character type, age, build, personality].
Each actor should look distinct but fit the role requirements.
Layout: 4 panels side by side, each showing the actor in the same pose and framing.
```

**Seedance 2.0 プロンプト（俳優ごと）:**

```
[Actor description from panel N] delivers the line: "[dialogue]".
Natural eye contact with camera, subtle facial expressions,
[emotional tone: confident / vulnerable / menacing].
Medium close-up, soft cinematic lighting, 3 seconds.
```

> [!NOTE]
> 静止画では良く見えるキャラクターでも、セリフ、アイコンタクト、演技をテストすると完全に役に合わないことがあります。このワークフローはフルシーンにクレジットを使う前に、キャスティング判断を前倒しで行えます。

<!-- Case 22: 3D Sculpt → AI Render → Animation (by @_DAntunes_) -->
### Case 22: [3Dスカルプト → AIレンダー → アニメーション](https://x.com/_DAntunes_/status/2049142166232904078) (by [@_DAntunes_](https://x.com/_DAntunes_))

従来の 3D モデリングと AI 動画を橋渡しします。Nomad Sculpt（または任意のスカルプトアプリ）でラフな 3D クレイモデルを作り、GPT Image 2 で洗練されたイラストにレンダリングしてから、ComfyUI 経由で Seedance 2.0 でアニメーション化します。テキストプロンプトだけでは実現できない、ポーズと構図の精密なコントロールが得られます。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/sculpt_case22/output.jpg" width="400" alt="3D sculpt to animation output"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/f5ecdb0c-d1ca-4291-91bc-eb88de91cd82" width="400" controls></video></td>
</tr></table>

**手順:**

1. Nomad Sculpt（または Blender、ZBrush など）でラフな 3D モデルをスカルプトする
2. 希望のカメラアングルからモデルのスクリーンショットをエクスポートする
3. GPT Image 2 で 3D モデルを洗練されたイラストまたはリアルな画像にレンダリングする
4. レンダリングされた画像を Seedance 2.0（ComfyUI 経由または直接）に読み込んでアニメーション化する

**GPT Image 2 プロンプト:**

```
Based on this 3D clay model reference, create a fully rendered [style] illustration.
Maintain the exact pose, proportions, and camera angle from the reference.
Style: [anime / realistic / painterly / game art].
Add: [lighting, textures, background, clothing details].
```

**Seedance 2.0 プロンプト:**

```
[Character description] in [action], maintaining the pose from the reference.
[Style] animation, smooth natural movement, cinematic lighting, 24fps.
```

> [!NOTE]
> 3D モデルはテキストプロンプトでは得られないものを提供します: 体のポーズ、手の位置、カメラアングルの正確なコントロールです。ラフなクレイモデルでも十分で、レンダリングとディテールの仕上げは GPT Image 2 が担当します。すでに 3D ツールを使っているクリエイターが AI アニメーションをワークフローに追加するのに理想的なパイプラインです。

<!-- Case 23: IP Cyberpunk Remake (by @AYi_AInotes) -->
### Case 23: [IP サイバーパンクリメイク — コンセプトフィルム](https://x.com/AYi_AInotes/status/2048745866538647912) (by [@AYi_AInotes](https://x.com/AYi_AInotes))

既存の映画/TV の IP を GPT Image 2 + Seedance 2.0 でまったく異なる設定にリメイクします。この例では『ゲーム・オブ・スローンズ』を 2048 年のサイバーパンクディストピアに再構築しています。鉄の玉座は金の AK-47 で鍛造され、ドラゴンはプラズマを吐くメカに、ナイトキングは光るサイバーアンデッドに。すべてのフレームが映画ポスター品質です。181 いいね / 4.3万 再生。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/remake_case23/output.jpg" width="400" alt="IP cyberpunk remake output"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/ac605d02-6871-47dc-9b58-414356872def" width="400" controls></video></td>
</tr></table>

**手順:**

1. 既存の IP を選び、リミックスコンセプトを定義する（例:「ゲーム・オブ・スローンズ in 2048 サイバーパンク」）
2. GPT Image 2 で主要キャラクターのリデザインを生成する — 各キャラクターの象徴的な特徴を新しい設定に翻訳する
3. オリジナルの象徴的なシーンを反映したシーン構成を生成する
4. Seedance 2.0 でシネマティックなモーションを付けて各シーンをアニメーション化する

**GPT Image 2 プロンプト:**

```
Reimagine [character name] from [IP] in a [new setting] aesthetic:
Original traits: [list iconic visual elements].
New interpretation: [how each trait translates to the new setting].
Style: cinematic concept art, [new setting] visual language, movie poster quality.
Lighting: [neon / holographic / dystopian glow].
```

**Seedance 2.0 プロンプト:**

```
Cinematic [new setting] sequence, epic scale, dramatic camera movement,
[character] in [iconic action reimagined for new setting],
atmospheric particles, volumetric lighting, 24fps.
```

> [!NOTE]
> このワークフローはどんな IP × 設定の組み合わせにも使えます: 封建時代の日本のスター・ウォーズ、アールデコのマーベル、サイバーパンクのハリー・ポッターなど。ポイントは各キャラクターの象徴的なビジュアル特徴を、認識可能性を保ちながら新しい美学言語に翻訳することです。

<!-- Case 24: GTA-Style City Game Concept (by @markgadala) -->
### Case 24: [GTA風シティゲームコンセプト](https://x.com/markgadala/status/2048560337960489385) (by [@markgadala](https://x.com/markgadala))

好きなバージョンの GTA を 5 分で作れます。GPT Image 2 で任意の都市（東京、ラゴス、ムンバイ）を舞台にしたゲーム UI スクリーンショットを生成し、Seedance 2.0 でゲームプレイ映像にアニメーション化します。存在しないゲームの本物のトレーラーのような仕上がりになります。99 いいね / 8.7K 再生。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/gta_case24/output.jpg" width="400" alt="GTA-style city game concept output"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/d3b0a7b9-827a-47f6-b24e-eabfacf3e892" width="400" controls></video></td>
</tr></table>

**手順:**

1. GTA のバリエーションを定義する — 都市、時代、ビジュアルスタイル
2. GPT Image 2 でゲームスクリーンショットを生成する: 三人称視点、HUD オーバーレイ、都市環境
3. Seedance 2.0 に読み込んでゲームプレイ映像としてアニメーション化する
4. クリップをトレーラーに組み立てる

**GPT Image 2 プロンプト:**

```
GTA-style open world game screenshot set in [city], [time period].
Third-person camera behind the player character.
Character: [description], walking/driving through [specific street scene].
HUD elements: minimap bottom-left, health bar, wanted stars.
Style: photorealistic AAA game, ray-traced lighting, [time of day].
16:9 widescreen, 4K quality.
```

**Seedance 2.0 プロンプト:**

```
Third-person gameplay footage, character walking through [city] streets,
natural pedestrian movement, dynamic camera following behind,
neon signs and city lights, AAA game quality, smooth 24fps.
```

> [!NOTE]
> これは Case 9 のゲームコンセプトアプローチをオープンワールドシティゲームに特化させたものです。HUD 要素（ミニマップ、体力バー、手配度の星）が「本物のゲーム」の錯覚を生み出す鍵です。どの都市でも使えます。ストリートレベルのディテールが具体的であるほど、説得力のある結果になります。

## 💡 ヒント＆テクニック

### 一貫性ガイド

GPT Image 2 の出力と、それを Seedance 2.0 で動かした後の見た目の一貫性を保つことは、最もよくある課題です。以下の方法で層ごとに対処できます。

**商品画像の一貫性**

Seedance 上で商品が崩れる根本原因は、モーション補間によって細部が再構成されることです。ロゴ、テクスチャ、表面パターンなどが変形しやすくなります。

対策:
- Seedance のプロンプトに `keep the product appearance completely unchanged, camera movement only, no rotation` を加える
- 被写体を動かすより、カメラ移動（寄り / 引き）を選ぶ — 商品は静止させてカメラを動かす
- クリップは 3 秒未満に抑える — 短いほど歪みが蓄積しにくい

**キャラクターの一貫性**

- まず三面図のキャラクターシートを生成し、後続の全ストーリーボードの基準にする
- すべてのパネルプロンプトに、髪色・衣装・体格などの簡潔なキャラ説明を含める
- 1 つのクリップ内で視点を切り替えすぎない

**シーンの一貫性**

複数のストーリーボードコマを GPT Image 2 で生成する場合、プロンプト冒頭でシーン条件を固定します:

```
Scene setting: [location], [time of day], [lighting direction], [fixed background elements].
Maintain this scene setting unchanged across all panels.
```

---

### プロンプトテンプレート

**GPT Image 2 → ストーリーボード用テンプレート**

```
Create a [N]-panel storyboard for [subject]:
- Style: [realistic / anime / illustration / cinematic]
- Aspect ratio: 16:9 widescreen
- Each panel: include shot type (wide / medium / close-up) + action description
- Character: [fixed appearance description]
- Scene tone: [color palette / lighting / mood]
Output as a single image with [N] panels separated by thin lines.
```

**GPT Image 2 → 3×3グリッド用テンプレート**

```
Output a single 3×3 grid storyboard image showing the following continuous action:
[describe the action sequence]
Requirements:
- 9 panels arranged left-to-right, top-to-bottom showing continuous motion
- Character position and scale consistent across all panels
- Background consistent throughout
- No text, labels, or content outside the panel borders
```

**Seedance 2.0 → アニメ調テンプレート**

```
Japanese full-color animation, high-speed editing, high frame count, 24fps.
[Scene description]. [Character description]. [Action description].
Strong camera work, high visual impact.
```

**Seedance 2.0 → CM向けテンプレート**

```
Cinematic commercial quality, [brand tone: premium / energetic / warm],
[product] centered in frame, slow camera push-in,
[lighting direction] highlights the product, clean background, no people.
Duration: 3 seconds.
```

**プロンプトの長さ — 短い方が勝つことが多い**

コミュニティ実験 (via [@Iancu_ai](https://x.com/Iancu_ai/status/2047882924679168083)): 1500 語の映画品質 Seedance プロンプトが、たった 1 文に負けました。同じキャラクター、同じ 15 秒。短いプロンプトの勝ちです。Seedance は網羅的な描写よりも方向性の明確さを評価します。シーンの細部すべてではなく、動きの意図を書きましょう。

---

### トラブルシューティング

**Seedance のコンテンツモデレーションに引っかかる**

原因: 画像にセンシティブと判定される要素（リアルな暴力、特定の姿勢の人物顔など）が含まれている。
対処: アニメ調またはイラスト調に切り替えるか、人物描写をプロンプトから削除する。

**出力の動きが不安定**

原因: ストーリーボードが複雑すぎて、Seedance が主要な動きの方向を判断できない。
対処: 1 コマにつき主題を 1 つ、動作を 1 つに絞る。背景要素も減らす。

**商品画像が崩れる**

上記の「一貫性ガイド → 商品画像の一貫性」を参照してください。

**プラットフォームごとの入力要件**

| プラットフォーム | 推奨入力サイズ | 対応形式 | 最大ファイルサイズ |
| :---: | :---: | :---: | :---: |
| Hailuo | 1280×720 または 720×1280 | JPG / PNG | 10 MB |
| Higgsfield | 1920×1080 | PNG | 20 MB |
| HitPaw | 任意比率 | JPG / PNG / WEBP | 15 MB |

## 🚀 Evolink で試す

Evolink なら、GPT Image 2 と Seedance 2.0 を 1 か所で実行できます。プラットフォームを切り替える必要も、ファイルを再アップロードする必要もありません。

**Evolink の利点**

- GPT Image 2 と Seedance 2.0 を 1 つの API キーで利用可能
- 同じ画面内で画像から動画へ直接受け渡し可能 — 画像生成後にダウンロードせず「Send to Video」をクリックするだけ
- バッチ処理対応 — 複数のストーリーボードパネルを順番に動画化できる

**使い方**

```
Step 1: Evolink を開く → GPT Image 2 を選ぶ → ストーリーボード画像を生成
Step 2: "Generate Video" をクリック → 画像が自動で Seedance 2.0 に渡される
Step 3: Seedance 用プロンプトを追加 → 生成
```

<a href='https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=gptimage2-x-seedance2'><img src='https://img.shields.io/badge/🚀 Get%20Started-Evolink-black' height="25"></a>


## 🙏 クレジット

このリポジトリは、優れた公開ワークフロー集と、コミュニティで共有された実験事例に着想を得ています。

作品を公開し、これらのケーススタディを可能にしてくれたクリエイターとコントリビューターに感謝します:
[@szounft](https://x.com/szounft) · [@Toshi_nyaruo_AI](https://x.com/Toshi_nyaruo_AI) · [@ponyodong](https://x.com/ponyodong) · [@servasyy_ai](https://x.com/servasyy_ai) · [@YaReYaRu30Life](https://x.com/YaReYaRu30Life) · [@fukaborichannel](https://x.com/fukaborichannel) · [@Shin_Engineer](https://x.com/Shin_Engineer) · [@ai_mitosan](https://x.com/ai_mitosan) · [@kiyoshi_shin](https://x.com/kiyoshi_shin) · [@AbleGPT](https://x.com/AbleGPT) · [@patata1216](https://x.com/patata1216) · [@peter6759](https://x.com/peter6759) · [@hibi_ai__](https://x.com/hibi_ai__) · [@heygentlewhale](https://x.com/heygentlewhale) · [@ai_gezgini](https://x.com/ai_gezgini) · [@Tz_2022](https://x.com/Tz_2022) · [@old_pgmrs_will](https://x.com/old_pgmrs_will) · [@0xbisc](https://x.com/0xbisc) · [@Iancu_ai](https://x.com/Iancu_ai) · [@Jake_Joseph](https://x.com/Jake_Joseph) · [@venturetwins](https://x.com/venturetwins) · [@0xInk_](https://x.com/0xInk_) · [@markgadala](https://x.com/markgadala) · [@Ankit_patel211](https://x.com/Ankit_patel211) · [@Ciri_ai](https://x.com/Ciri_ai) · [@nimentrix](https://x.com/nimentrix) · [@insmind_com](https://x.com/insmind_com) · [@kingofdairyque](https://x.com/kingofdairyque) · [@Kashberg_0](https://x.com/Kashberg_0) · [@airina_xyz](https://x.com/airina_xyz) · [@CoffeeVectors](https://x.com/CoffeeVectors) · [@mdmadeit](https://x.com/mdmadeit) · [@Morph_VGart](https://x.com/Morph_VGart) · [@MEnesKirca](https://x.com/MEnesKirca) · [@MrLarus](https://x.com/MrLarus) · [@AYi_AInotes](https://x.com/AYi_AInotes) · [@8fstudioz](https://x.com/8fstudioz) · [@_DAntunes_](https://x.com/_DAntunes_)

*すべての事例が原作者に正確に帰属していることを保証するものではありません。修正が必要な場合はご連絡ください。更新対応します。*

さらに興味深いワークフロー事例があれば、ぜひ共有してください。Evolink のワークフローライブラリ拡充にご協力いただけます。

[![Star History Chart](https://api.star-history.com/svg?repos=EvoLinkAI/GPT-Image-2-Seedance2-Workflow&type=Date)](https://www.star-history.com/#EvoLinkAI/GPT-Image-2-Seedance2-Workflow&Date)
