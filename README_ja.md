<div align="center">

<a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=banner&utm_campaign=gptimage2-x-seedance2"><img src="images/logo.png" alt="GPT Image 2 × Seedance 2.0 ワークフローガイド"></a>

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

GPT Image 2 × Seedance 2.0 ワークフローリポジトリへようこそ！ 🤗

**GPT Image 2 と Seedance 2.0 を組み合わせて高品質なAI動画を制作するための、実証済みワークフロー、プロンプトテンプレート、実際のクリエイター事例を収集しています。**

GPT Image 2 は「何を描くか」とビジュアルの一貫性を担当します。Seedance 2.0 は「どう動かすか」を担当し、画像をアニメーション動画に変換します。この2つを組み合わせることで、現在利用可能な最も高性能なAI動画パイプラインの一つが構築できます。

このリポジトリのほとんどのケースは、X/Twitterのクリエイター、コミュニティの実験、実際の制作ワークフローから厳選されています。

試してみる: [GPT Image 2 + Seedance 2.0](https://evolink.ai?utm_source=github&utm_medium=readme&utm_campaign=gptimage2-x-seedance2)

お役に立てたら、スターをお願いします。 ⭐



## 📰 ニュース

- **2026年5月1日:** ケース13〜27を追加（ダンスシーケンスグリッド、コミックページアニメーション、ラグジュアリーCM、シネマティックフード動画、ゲームインターフェースパイプライン、シングルエージェントワークフロー、ストーリーボード優先コスト管理、Claude ショットリストMV、キャスティンググリッド、3Dスカルプトパイプライン、IPサイバーパンクリメイク、GTAシティコンセプト、K-Popコレオグラフィー、商品動画広告、キャラクター紹介アニメーション）
- **2026年4月25日:** ケース10〜12を追加（マルチフレームストーリーボード、日本語MVツールチェーン、Claude Code × キャラクターシート）、ケース9にARPGシミュレーションバリアントを拡張、ギャラリーにコミュニティショーケースを追加
- **2026年4月23日:** 9つの厳選ワークフローケースでリポジトリを公開

## 📑 目次

- [🎬 はじめに](#-はじめに)
- [📰 ニュース](#-ニュース)
- [📑 目次](#-目次)
- [🎥 ストーリーボードテクニック](#-ストーリーボードテクニック)
  - [ケース1: 標準ストーリーボード → 動画 (by @kiyoshi_shin)](#ケース1-標準ストーリーボード--動画-by-kiyoshi_shin)
  - [ケース2: 3×3グリッドストーリーボード手法 (by @servasyy_ai)](#ケース2-33グリッドストーリーボード手法-by-servasyy_ai)
  - [ケース10: マルチフレーム参照 → ファストカット動画 (by @heygentlewhale)](#ケース10-マルチフレーム参照--ファストカット動画-by-heygentlewhale)
  - [ケース19: ストーリーボード優先コスト管理 (by @0xbisc)](#ケース19-ストーリーボード優先コスト管理-by-0xbisc)
- [📱 CM・商品](#-cm商品)
  - [ケース5: アプリMVPデモ動画 (by @Shin_Engineer)](#ケース5-アプリmvpデモ動画-by-shin_engineer)
  - [ケース6: 15秒CM (by @ai_mitosan)](#ケース6-15秒cm-by-ai_mitosan)
  - [ケース15: ラグジュアリーCM — ストーリーボードから映像へ (by @insmind_com)](#ケース15-ラグジュアリーcm--ストーリーボードから映像へ-by-insmind_com)
  - [ケース16: シネマティックフード動画 (by @kingofdairyque)](#ケース16-シネマティックフード動画-by-kingofdairyque)
  - [ケース26: 商品画像 → ショート動画広告 (by @insmind_com)](#ケース26-商品画像--ショート動画広告-by-insmind_com)
- [🎨 アニメーション・キャラクター](#-アニメーションキャラクター)
  - [ケース3: キャラクターシート → アニメーション (by @YaReYaRu30Life)](#ケース3-キャラクターシート--アニメーション-by-yareyaru30life)
  - [ケース4: アニメOPスタイル動画 (by @Toshi_nyaruo_AI)](#ケース4-アニメopスタイル動画-by-toshi_nyaruo_ai)
  - [ケース12: Claude Code × キャラクターシート → アニメーション (by @old_pgmrs_will)](#ケース12-claude-code--キャラクターシート--アニメーション-by-old_pgmrs_will)
  - [ケース13: ダンスシーケンスグリッド → ダンス動画 (by @Ciri_ai)](#ケース13-ダンスシーケンスグリッド--ダンス動画-by-ciri_ai)
  - [ケース14: コミックページ → アニメーション動画 (by @nimentrix)](#ケース14-コミックページ--アニメーション動画-by-nimentrix)
  - [ケース25: K-Popコレオグラフィー — 詳細コントロール (by @Kashberg_0)](#ケース25-k-popコレオグラフィー--詳細コントロール-by-kashberg_0)
  - [ケース27: キャラクター紹介アニメーション (by @0xbisc)](#ケース27-キャラクター紹介アニメーション-by-0xbisc)
- [🎵 ミュージックビデオ・ショートフィルム](#-ミュージックビデオショートフィルム)
  - [ケース7: Sunoを使ったミュージックビデオ (by @fukaborichannel)](#ケース7-sunoを使ったミュージックビデオ-by-fukaborichannel)
  - [ケース8: サイバーパンクスタイルショートフィルム (by @ponyodong)](#ケース8-サイバーパンクスタイルショートフィルム-by-ponyodong)
  - [ケース11: 日本語MV — フルAIツールチェーン (by @Tz_2022)](#ケース11-日本語mv--フルaiツールチェーン-by-tz_2022)
  - [ケース20: Claude ショットリスト → ミュージックビデオ (by @CoffeeVectors)](#ケース20-claude-ショットリスト--ミュージックビデオ-by-coffeevectors)
- [🎮 ゲームコンセプト](#-ゲームコンセプト)
  - [ケース9: ゲーム・インタラクティブコンテンツ (by @op7418)](#ケース9-ゲームインタラクティブコンテンツ-by-op7418)
  - [ケース17: ゲームインターフェースアニメーション — フルパイプライン (by @0xInk_)](#ケース17-ゲームインターフェースアニメーション--フルパイプライン-by-0xink_)
  - [ケース24: GTAスタイルシティゲームコンセプト (by @markgadala)](#ケース24-gtaスタイルシティゲームコンセプト-by-markgadala)
- [🛠 制作ツール](#-制作ツール)
  - [ケース18: シングルエージェント自動ワークフロー (by @venturetwins)](#ケース18-シングルエージェント自動ワークフロー-by-venturetwins)
  - [ケース21: キャスティンググリッド — 俳優オーディション (by @8fstudioz)](#ケース21-キャスティンググリッド--俳優オーディション-by-8fstudioz)
  - [ケース22: 3Dスカルプト → AIレンダー → アニメーション (by @_DAntunes_)](#ケース22-3dスカルプト--aiレンダー--アニメーション-by-_dantunes_)
- [💡 ヒント・テクニック](#-ヒントテクニック)
  - [一貫性ガイド](#一貫性ガイド)
  - [プロンプトテンプレート](#プロンプトテンプレート)
  - [トラブルシューティング](#トラブルシューティング)
- [🚀 Evolinkで試す](#-evolinkで試す)
- [🙏 謝辞](#-謝辞)


## 🎥 ストーリーボードテクニック

<!-- Case 1: Standard Storyboard → Video (by @kiyoshi_shin) -->
### ケース1: [標準ストーリーボード → 動画](https://x.com/kiyoshi_shin/status/2047133524403400847) (by [@kiyoshi_shin](https://x.com/kiyoshi_shin))

最も一般的なワークフローです。GPT Image 2 でストーリーボードパネルを生成し、Seedance 2.0 でアニメーション化します。プロモーション動画、ショートドラマ、アニメOPに最適です。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/storyboard_case1/input.jpg" width="280" alt="GPT Image 2で生成したストーリーボード"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/ac25fc3d-b6cb-4149-a8ba-e7e10c5b1faa" width="280" controls></video></td>
</tr></table>

**手順:**

1. GPT Image 2 にシーンを説明してストーリーボード画像を生成する
2. ストーリーボードを Seedance 2.0 の画像から動画モードでインポートする
3. 各クリップをエクスポートし、編集ソフトで組み立てる

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
> ストーリーボード画像は16:9で出力し、Seedanceの自動クロップを避けましょう。フレームレートは映画標準に合わせて24fpsに設定してください。各ストーリーボードパネルはシンプルに — コンテンツがシンプルなほど、モーション出力の精度が上がります。


<!-- Case 2: 3×3 Grid Storyboard Method (by @servasyy_ai) -->
### ケース2: [3×3グリッドストーリーボード手法](https://x.com/servasyy_ai/status/2047198012750143999) (by [@servasyy_ai](https://x.com/servasyy_ai))

コミュニティが発見した重要なテクニック：すべてのストーリーボードパネルを1枚の3×3グリッド画像にまとめてからSeedanceにインポートすると、フレームを1枚ずつインポートするよりも失敗率が大幅に低下します。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/storyboard_case2/output.jpg" width="400" alt="3×3グリッドストーリーボード出力"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/00f32388-a17b-4b9c-8da3-1956436ce91b" width="400" controls></video></td>
</tr></table>



**手順:**

1️⃣ 作りたいコンテンツ + ✅ プロンプト「Create a storyboard in a 3×3 grid format」を入力
2️⃣ 1の画像からChatGPTでプロンプトを作成
3️⃣ seedanceで1の画像を参照
4️⃣ 2で作成したプロンプトを入力

**GPT Image 2 プロンプト:**

```
[describe your scene] and Create a storyboard in a 3×3 grid format
```

**Seedance 2.0 プロンプト:**
この画像を動画にする
```
[Describe the motion and style. Example: Japanese full-color animation, fast cuts, high frame count, 24fps, dark fantasy anime OP style, intense battle scenes.]
```

> [!NOTE]
> **使用前にブラケット内のコンテンツを置き換えてください。** この手法が機能するのは、Seedanceが1枚の画像からモーションの意図を分析するためです。グリッドは方向性の参照を提供し、個別の画像よりも一貫性のあるモーションを生成します。


<!-- Case 10: Multi-Frame Reference Storyboard (by @heygentlewhale + @ai_gezgini) -->
### ケース10: [マルチフレーム参照 → ファストカット動画](https://x.com/heygentlewhale/status/2047969137969004946) (by [@heygentlewhale](https://x.com/heygentlewhale))

複数の参照フレームを含むストーリーボード画像をSeedance 2.0に入力し、シーケンス順に従うよう指示します。モデルはフレーム位置をシーンの手がかりとして読み取り、手動でのクリップ組み立てなしに一貫性のあるファストカット編集を出力します。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/storyboard_case10/input.jpg" width="280" alt="GPT Image 2 マルチフレームストーリーボード"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/4d7af334-4e49-4de4-899e-803f72116c21" width="280" controls></video></td>
<td align="center"><video src="https://github.com/user-attachments/assets/5def7e00-6fc6-4a4e-8075-5f37cb24b84c" width="280" controls></video></td>
</tr></table>

**手順:**

1. GPT Image 2 でマルチパネルストーリーボード画像を生成する（12フレーム、3×4または4×3グリッド）
2. ストーリーボードをSeedance 2.0の参照画像としてアップロードする
3. フレーム数と編集スタイルを指定するシーケンシングプロンプトを書く

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

**汎用シーケンシングプロンプト（[@ai_gezgini](https://x.com/ai_gezgini/status/2047349122315805016) 提供）:**

```
Use this storyboard to generate a video, follow the scene order, keep transitions smooth,
and preserve cinematic lighting and pacing.
[Add any extra visual details you want.]
```

> [!NOTE]
> このプロンプトはジャンルを問わず使えます — スタイルの説明をSF、ホラー、ドキュメンタリーなど好みのルックに入れ替えてください。キーフレーズは `follow the storyboard sequence of the [N] reference frames` です — これによりSeedanceはフレーム位置を単一の構図ではなくタイムラインとして扱います。


<!-- Case 19: Storyboard-First Cost Control (by @0xbisc) -->
### ケース19: [ストーリーボード優先コスト管理](https://x.com/0xbisc/status/2049100073481716076) (by [@0xbisc](https://x.com/0xbisc))

制作コストを意識したアプローチ：まずGPT Image 2でストーリーボードを反復改善し（低コスト）、構図が確定してから動画を生成します（高コスト）。動画の反復は画像の反復より10〜50倍のクレジットを消費するため、大幅なコスト削減になります。298いいね / 13K閲覧 / 291ブックマーク。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/storyboard_case19/output.jpg" width="400" alt="ストーリーボード優先ワークフロー出力"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/09e04d80-c0d1-4a8c-9b74-2efe474acfcd" width="400" controls></video></td>
</tr></table>

**手順:**

1. GPT Image 2 で8パネルのストーリーボードグリッドを生成する
2. 各パネルを確認 — 満足するまで個別のパネルを再生成または編集する
3. ストーリーボード全体が確定してから、Seedance 2.0にインポートする
4. 確定したストーリーボードから一発で動画を生成する

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
> **ストーリーボード優先がコスト面で有利な理由:** 動画の反復はクレジットを急速に消費します。ストーリーボードがあれば、ショットごとに微調整して問題を早期に発見できます。動画ステップは、コストのかかる試行錯誤ループではなく、最終レンダリング1回で済みます。コミュニティのフィードバックでも、長いシーケンスに対して最もコスト効率の良いワークフローであることが確認されています。


## 📱 CM・商品

<!-- Case 5: App MVP Demo Video (by @Shin_Engineer) -->
### ケース5: [アプリMVPデモ動画](https://x.com/Shin_Engineer/status/2047182050323812381) (by [@Shin_Engineer](https://x.com/Shin_Engineer))

GPT Image 2 を使って、まだ存在しないアプリの完成品のようなUIスクリーンショットを生成し、Seedance 2.0 でプロダクトデモにアニメーション化します。TikTokやSNSに投稿して、開発前に市場の反応をテストしましょう。

| 出力 |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/app_case5/output0.jpg" width="400" alt="GPT Image 2で生成したアプリUIスクリーンショット1"></a> |

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/app_case5/output1.jpg" width="220" alt="アプリUIスクリーンショット2"></a></td>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/app_case5/output2.jpg" width="220" alt="アプリUIスクリーンショット3"></a></td>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/app_case5/output3.jpg" width="220" alt="アプリUIスクリーンショット4"></a></td>
</tr></table>

**手順:**

1. GPT Image 2 にアプリのコンセプトとデザイン言語を説明する
2. 3〜5枚の主要UIスクリーンショットを生成する（ホーム、機能、プロフィールページ）
3. スクリーンショットをユーザーフロー順に並べ、Seedance 2.0にインポートする
4. デモ動画をエクスポートし、投稿して市場の反応をテストする

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
> **使用前にブラケット内のプレースホルダーを置き換えてください。** 動画のキャプションでは、AI生成とラベル付けしないでください — プロダクトデモとして投稿し、コメントでリアルなオーディエンスのフィードバックを観察しましょう。


<!-- Case 6: 15-Second Commercial (by @ai_mitosan) -->
### ケース6: [15秒CM](https://x.com/ai_mitosan/status/2047146600422846762) (by [@ai_mitosan](https://x.com/ai_mitosan))

2ステップワークフロー：GPT Image 2 でヒーロー画像とマッチするストーリーボードを生成し、Seedance 2.0 で各クリップをアニメーション化します。キャプションと音楽を加えて、完成した15秒スポットに仕上げます。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/commercial_case6/input1.jpg" width="280" alt="GPT Image 2 ヒーロー商品画像"></a></td>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/commercial_case6/input2.jpg" width="280" alt="GPT Image 2 ストーリーボード"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/09ae3c57-b8fb-4323-ba76-7777541fe4a3" width="280" controls></video></td>
</tr></table>

**手順:**

1. image2でメイン画像 + ストーリーボードを生成する
2. それをSeedance2.0に入力して動画にする

**ストーリーボード枚数ガイド:**

| 動画の長さ | パネル数 | クリップあたりの長さ |
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


<!-- Case 15: Luxury Commercial — Storyboard to Film (by @insmind_com) -->
### ケース15: [ラグジュアリーCM — ストーリーボードから映像へ](https://x.com/insmind_com/status/2049481439285223785) (by [@insmind_com](https://x.com/insmind_com))

GPT Image 2 でラグジュアリーフレグランス広告用の3×4ストーリーボードグリッド（12フレーム）を生成し、Seedance 2.0 でシネマティックなブランドレベルの映像にアニメーション化します。イントロ → リチュアル → トランスフォーメーション → 解決 → ブランドクロージングという構造化されたフローにより、1回の生成で完全なナラティブアークが生まれます。371いいね / 84K閲覧 / 255ブックマーク。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/luxury_case15/output.jpg" width="400" alt="ラグジュアリーCMストーリーボード"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/281fef1e-f42d-442c-b06e-44d7cff221ec" width="400" controls></video></td>
</tr></table>

**手順:**

1. GPT Image 2 で12フレームのストーリーボードグリッド（3×4）を生成する。エディトリアルレイアウトとラグジュアリーブランドの美学を使用
2. ストーリーボードグリッドを1枚の参照画像としてSeedance 2.0にインポートする
3. SeedanceにシネマティックなラグジュアリーCMとしてシーケンスをアニメーション化するようプロンプトする
4. 編集ソフトで音楽と最終カラーグレードを追加する

**GPT Image 2 プロンプト:**

```
Create a high-end 9:16 luxury fragrance pitch deck storyboard in 3x4 grid (12 frames), editorial layout, Aesop/Byredo style, beige + lavender palette. Structured flow: intro → ritual → transformation → resolution → brand closure. Each frame split: top cinematic image (no text) + bottom storyboard notes. Luxury minimal European aesthetic, calm femininity, slow living mood. Candle is the emotional center throughout
```

**Seedance 2.0 プロンプト:**

```
Animate the provided 3x4 storyboard into a smooth cinematic video. Preserve exact shot order and continuity. Use slow push-in, gentle pan, subtle orbit, and rack focus. Lighting transitions from soft morning glow to warm golden ambient light. Fragrance brand editorial aesthetic, minimal luxury, soft film grain. No new shots, no reordering, candle remains emotional focus in all scenes
```

> [!NOTE]
> エディトリアルピッチデッキレイアウト（各フレームにビジュアルディレクションノート付き）は、プレーンなグリッドよりもSeedanceに強いナラティブの手がかりを与えます。このワークフローはあらゆるラグジュアリー商品カテゴリー — スキンケア、時計、ファッション — にパレットと商品の参照を入れ替えるだけで適用できます。


<!-- Case 16: Cinematic Food Video (by @kingofdairyque) -->
### ケース16: [シネマティックフード動画](https://x.com/kingofdairyque/status/2049812014596599834) (by [@kingofdairyque](https://x.com/kingofdairyque))

GPT Image 2 + Seedance 2.0 を使って、タイムスタンプ付きショット説明による超リアルな料理動画を作成します。各タイムスタンプセグメント（0〜2秒、2〜4秒など）が特定のカメラアングルとアクションを定義し、Seedanceに15秒シーケンスの精密なコントロールを与えます。55いいね / 1K閲覧。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/food_case16/input.jpg" width="400" alt="フード動画ストーリーボード入力"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/30a20e57-8384-4117-adf7-4f92faebeb33" width="400" controls></video></td>
</tr></table>

**手順:**

1. 各2秒セグメントを説明する詳細なタイムスタンプ付きショットリストを書く
2. ショットリストに基づいてGPT Image 2でストーリーボード画像を生成する
3. 画像 + 完全なタイムスタンプ付きプロンプトをSeedance 2.0に入力する
4. モデルがタイムスタンプ構造に従って一貫性のある料理シーケンスを生成する

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
> タイムスタンプ付きプロンプトテクニックは、Seedanceに正確なショットごとのタイムラインを与えます。これはあらゆる商品やプロセス動画 — 開封、クラフト、カクテル作り — に使えます。各セグメントは2秒に抑え、カメラアングルとアクションの両方を記述すると最良の結果が得られます。


<!-- Case 26: Product Image → Short Video Ad (by @insmind_com) -->
### ケース26: [商品画像 → ショート動画広告](https://x.com/insmind_com/status/2049843814337306974) (by [@insmind_com](https://x.com/insmind_com))

静止画の商品画像をスクロールを止めるSNS動画に変換します。既存の商品写真をGPT Image 2の参照としてアップロードし、シーン構図を生成してから、Seedance 2.0でアニメーション化します。ECとSNSマーケティング向けに設計されており、既存の商品写真からTikTok/Reels対応コンテンツを制作できます。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/product_case26/output.jpg" width="400" alt="商品動画広告出力"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/880c0019-e45a-4eb9-be6f-638ff71a0e0f" width="400" controls></video></td>
</tr></table>

**手順:**

1. 商品画像を入力する
2. コアシーンを生成する
3. モーションと構造を定義する
4. スタイルと制約を設定する

> [!NOTE]
> ケース15（ラグジュアリーCM）との違いは、すべてをゼロから生成するのではなく、既存の商品写真から始める点です。すでに商品画像を持っていて、それを素早く動画広告に変換したいEC事業者に最適です。


## 🎨 アニメーション・キャラクター

<!-- Case 3: Character Sheet → Animation (by @YaReYaRu30Life) -->
### ケース3: [キャラクターシート → アニメーション](https://x.com/YaReYaRu30Life/status/2047203375314571501) (by [@YaReYaRu30Life](https://x.com/YaReYaRu30Life))

GPT Image 2 でキャラクターの三面図シート（正面、側面、背面）を生成し、Seedance 2.0 でのアニメーションのアンカーとして使用します。アニメキャラクター、ゲームキャラクター、フィギュアお披露目に最適です。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/character_case3/input0.jpg" width="260" alt="キャラクターシート正面"></a></td>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/character_case3/input1.jpg" width="260" alt="キャラクターシート側面"></a></td>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/character_case3/input2.jpg" width="260" alt="装備シート"></a></td>
</tr></table>

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/character_case3/output.jpg" width="400" alt="装備付きキャラクターシート統合"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/92a0aa56-441f-40db-b9c9-13410254cb3f" width="400" controls></video></td>
</tr></table>

**手順:**

1. 三面図（キャラクター）+ 装備の三面図2枚を作成。これを基に、各装備を装着した三面図を1枚の画像にまとめる。画像投稿数の都合上、キャラクターの添付は省略
2. この三面図を基にストーリーボードを作成する
3. ストーリーボードをSeedance2.0で動画にする

**GPT Image 2 プロンプト:**

```
Create a storyboard based on this three-view drawing  
```

**Seedance 2.0 プロンプト:**

```
Turn the storyboard into video using Seedance2.0
```


<!-- Case 4: Anime OP Style Video (by @Toshi_nyaruo_AI) -->
### ケース4: [アニメOPスタイル動画](https://x.com/Toshi_nyaruo_AI/status/2047216971184546231) (by [@Toshi_nyaruo_AI](https://x.com/Toshi_nyaruo_AI))

GPT Image 2 でシーン設定画像を作成し、Seedance 2.0 に自由にアニメーション化させます。制約付き（ストーリーボードガイド）と自由形式（プロンプトのみ）の出力を比較することで、ショットごとに適切なアプローチを判断できます。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/character_case4/output0.jpg" width="280" alt="アニメOP出力1"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/f08a2fee-89a7-4c7c-a58a-f1306f87419a" width="280" controls></video></td>
<td align="center"><video src="https://github.com/user-attachments/assets/09d81a41-b5c5-47f3-8c67-442b7a93b019" width="280" controls></video></td>
</tr></table>

**手順:**

1. Grokで架空のアニメオープニングの歌詞を考える
2. GPT-image2で歌詞をストーリーボードにする
3. seedance2で動画を生成する

**GPT Image 2 プロンプト:**

```
turn the lyrics into a storyboard
```

**Seedance 2.0 プロンプト:**

```
Japanese full-color anime, fast cuts, high frame count, 24fps. Dark fantasy anime OP style. Epic battle between protagonist and massive supernatural creatures. High-impact sequence of scenes. Only [character name] appears.
```

> [!NOTE]
> Seedanceがストーリーボード参照なしで自由にアニメーション化すると、結果はよりダイナミックになりますが、ソース画像との一貫性は低下します。キーキャラクターショットにはストーリーボードコントロールを、アクションシーケンスには自由アニメーションを使いましょう。


<!-- Case 12: Claude Code + Character Sheet → Animation (by @old_pgmrs_will) -->
### ケース12: [Claude Code × キャラクターシート → アニメーション](https://x.com/old_pgmrs_will/status/2045091769180914019) (by [@old_pgmrs_will](https://x.com/old_pgmrs_will))

Claude Codeで世界観設定とキャラクターの設定を書き、構造化された説明をGPT Image 2に渡してキャラクターのキービジュアルを生成し、Seedance 2.0でアニメーション化します。オリジナルIP制作のための開発者フレンドリーなワークフローです。191いいね / 7K閲覧。

<table><tr>
<td align="center"><a href="https://evolink.ai/seedance2?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/character_case12/output.jpg" width="400" alt="Claude Code + GPT Image 2 キャラクターキービジュアル"></a></td>
</tr></table>

**手順:**

1. Claude Codeで世界観設定ノートと構造化されたキャラクタースペック（名前、外見、性格、設定）を作成する
2. キャラクタースペックをGPT Image 2に直接入力し、キービジュアルまたはキャラクターシートを生成する
3. キービジュアルをSeedance 2.0の参照画像として使用し、アニメーション化する

> [!NOTE]
> Claude Codeは構造化テキスト — キャラクタースペック、シーン説明、ダイアログアウトライン — を出力し、GPT Image 2はこれを詳細なプロンプトとしてうまく処理します。このパイプラインはオリジナルストーリーIPに特に効果的です：コードで設定を構築し、GPT Image 2でビジュアル化し、Seedanceでアニメーション化します。


<!-- Case 13: Dance Sequence Grid → Dance Video (by @Ciri_ai) -->
### ケース13: [ダンスシーケンスグリッド → ダンス動画](https://x.com/Ciri_ai/status/2049034340160704643) (by [@Ciri_ai](https://x.com/Ciri_ai))

GPT Image 2 で4×4のダンスポーズグリッドを生成し、Seedance 2.0にモーション参照として入力します。モデルはグリッドを振り付けシーケンスとして読み取り、連続したダンス動画を出力します。上級バリアント：複数のキャラクター参照をアップロードして、ビートに合わせた衣装チェンジを実現。161いいね / 9K閲覧。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/dance_case13/output.jpg" width="400" alt="ダンスシーケンスグリッド出力"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/39376245-e7c7-4812-b770-9e81acf4eca2" width="400" controls></video></td>
</tr></table>

**手順:**

1. GPT Image 2 でキャラクターの連続ダンスポーズを示す4×4グリッド画像を生成する
2. グリッドをSeedance 2.0の参照画像としてアップロードする
3. Seedanceに参照画像のダンスシーケンスに従うようプロンプトする
4. （上級）衣装Aのキャラクター、衣装Bのキャラクター、ダンスグリッドの3つを参照としてアップロードし、ダンス中の衣装チェンジを実現する

**GPT Image 2 プロンプト:**

```
Transform the input image into a stylized K-pop dance tutorial poster with a fashion-forward streetwear aesthetic, keeping the exact 4x4 grid layout (16 panels) and choreography structure.
Core Composition
Maintain a 16-panel grid (4 columns × 4 rows) with clean spacing

Each panel shows the same female dancer performing sequential choreography

Preserve panel numbering (1–16) in bold, modern UI-style labels

Keep step titles and instructional captions, but redesign typography to feel like K-pop album graphics / dance practice overlays

Subject Styling (K-pop Idol Inspired)

Young female dancer with soft glam K-pop makeup (dewy skin, subtle shimmer, defined eyes)

Hair: long, sleek, slightly dynamic (motion-friendly, flowing during moves)

Expression: confident, charismatic stage presence

Outfit (streetwear-inspired):

Cropped hoodie or oversized zip-up jacket

Cargo pants or parachute pants with straps

Chunky sneakers or platform boots

Optional accessories: chain necklace, ear cuffs, fingerless gloves

Visual Style

Switch from plain grayscale → high-contrast + soft neon accents

Base palette: black, white, gray

Accent colors: neon pink, electric blue, or violet glow (subtle, not overpowering)

Lighting:

Studio lighting with a soft glow + rim light effect

Slight stage-light vibe, like a K-pop dance practice video

Graphics & Effects

Add dynamic motion trails and glow accents on arms, legs, and hair movement

Replace basic arrows with stylized motion graphics (neon strokes, swooshes)

Subtle light streaks or particle effects for energy

Optional faint floor reflection or glossy surface

Typography

Titles: bold, modern, slightly condensed sans-serif (K-pop album style)

Add subtle glow or gradient to titles

Instruction text: clean, minimal, slightly futuristic UI style

Panel numbers: inside rounded squares or pill shapes with neon outline

Camera & Framing

Full-body framing in each panel (consistent scale)

Straight-on angle, but with slight dynamic tilt or perspective energy

Maintain clarity of movement for instructional purpose

Mood & Energy

Feels like a K-pop dance practice meets fashion editorial

Clean but energetic

Stylish, rhythmic, performance-driven

Important Constraints

Keep choreography readable and sequential

Do NOT merge panels or change layout

Maintain consistency of dancer identity across all panels
```

**Seedance 2.0 プロンプト:**

```
Character from Image 1 performs the dance based on the breakdown in Image 3. Midway through the performance, they switch outfits on beat into the character from Image 2. Then, the character from Image 2 continues and completes the remaining dance steps from Image 3. Emphasize precise beat synchronization with the music
```

> [!NOTE]
> このテクニックはあらゆる動きのシーケンス — ダンス、武術、スポーツ — に使えます。4×4グリッドはSeedanceに補間するための16の参照フレームを与え、少ないパネルよりも滑らかなモーションを生成します。
>
> **コミュニティバリアント:** [@airina_xyz](https://x.com/airina_xyz/status/2049830199236190326) がストリートダンサーで基本ワークフローを実演。[@Kashberg_0](https://x.com/Kashberg_0/status/2049697925262102689) がキャラクターボード + モーション参照フレームでK-Popコレオグラフィーを実現（52いいね / 2K閲覧）。


<!-- Case 14: Comic Page → Animated Video (by @nimentrix) -->
### ケース14: [コミックページ → アニメーション動画](https://x.com/nimentrix/status/2049560412979708334) (by [@nimentrix](https://x.com/nimentrix))

GPT Image 2 でマルチパネルのコミックページを作成 — 斜めレイアウト、吹き出し、シネマティックなストーリーテリング — そしてSeedance 2.0でページ全体を動画にアニメーション化します。モデルはコミックパネルをナラティブシーケンスとして読み取り、連続したアニメーションショートを生成します。330いいね / 21K閲覧 / 360ブックマーク。

<table><tr>
<td align="center"><strong>GPT Image 2 入力</strong><br><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/comic_case14/input1.jpg" width="260" alt="キャラクター参照1 — ドラゴン"></a></td>
<td align="center"><br><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/comic_case14/input2.jpg" width="260" alt="キャラクター参照2 — 少年"></a></td>
<td align="center"><strong>Seedance 2.0 入力</strong><br><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/comic_case14/input3.jpg" width="260" alt="GPT Image 2で生成したコミックページ"></a></td>
</tr></table>

<table><tr>
<td align="center"><video src="https://github.com/user-attachments/assets/0b5038e2-dfca-4c65-b5d7-a719a74408b0" width="400" controls></video></td>
</tr></table>

**手順:**

1. GPT Image 2 でキャラクターデザインシート（正面、側面、背面ビュー）を作成し、キャラクターの外見を固定する
2. キャラクターを参照としてマルチパネルのコミックページを生成する
3. コミックページをSeedance 2.0にインポートしてアニメーション化する

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
> 斜めレイアウトと吹き出しは、Seedanceにパネルの境界と読み順の明確なビジュアルキューを与えます。最良の結果を得るには、各パネルのアクションをシンプルかつ明確にしてください。このワークフローはSunoと組み合わせて最終動画にサウンドトラックを追加するのにも適しています。


<!-- Case 25: K-Pop Choreography with Detailed Control (by @Kashberg_0) -->
### ケース25: [K-Popコレオグラフィー — 詳細コントロール](https://x.com/Kashberg_0/status/2049839091899088948) (by [@Kashberg_0](https://x.com/Kashberg_0))

ダンスアニメーションの最大限のコントロール：正確な動きの説明を含む16ステップの振り付けブレイクダウンを書き、GPT Image 2で参照グリッドを生成し、Seedance 2.0でアニメーション化します。各ステップは2〜3秒で、本格的なK-popの動きの質を持つ35〜50秒の連続ダンス動画を生成します。

<table><tr>

<td align="center"><video src="https://github.com/user-attachments/assets/1c088b5e-6305-4bf6-9377-97784d5f8fac" width="400" controls></video></td>
</tr></table>

**手順:**

1. 詳細な振り付けシーケンスを書く（具体的なダンスムーブを含む16ステップ）
2. GPT Image 2 で各ステップを示す参照グリッドを生成する
3. グリッド + 完全な振り付け説明をSeedance 2.0に入力する
4. モデルがスムーズなトランジションでステップシーケンスに従う


**Seedance 2.0 プロンプト:**

```
K-Pop Dance Sequence (16 Steps, Korean Street)
[PROJECT TYPE]
Cinematic K-pop dance video (instruction-to-performance translation)
[CORE REQUIREMENT — STRICT]
The video must faithfully follow the exact 16-step choreography shown in the reference sheet, in the same order, with accurate poses and transitions.
No steps added, removed, or rearranged.
🧍‍♀️ [CHARACTER]
Korean female dancer (K-pop idol aesthetic)
Slim, athletic build
Same consistent face and proportions throughout
Expressive, confident stage presence
Natural, fluid but sharp K-pop movement quality
👕 [WARDROBE — K-POP STYLE]
Fitted crop top
Loose high-waisted jeans
Sneakers
Modern idol styling (clean, trendy)
Fabric reacts naturally to movement (denim weight, subtle folds)
📍 [LOCATION / ENVIRONMENT]
Empty aesthetic Korean street (Seoul-inspired)
Clean urban design: narrow street, minimal signage, soft architecture
No people, no vehicles
Slight cinematic depth (buildings, street lights, textures)
Lighting:
Soft daylight or golden hour (ideal for K-pop vibe)
Balanced highlights + gentle shadows
🔢 [16-STEP CHOREOGRAPHY — LOCKED SEQUENCE]
Starting Pose
Step Touch Right
Step Touch Left
Hip Sway Combo
Body Roll Down
Back Step Sweep
Quarter Turn Pivot
Hair Flip & Pose
Side Step Drag
Cross Behind Unwind
Body Wave Up
Hip Circle
Step Lock Step
Arm Sweep Pose
Chest Pop & Hit
Final Pose (hold 2–3 sec)
🎥 [CAMERA DIRECTION]
Full-body framing at all times
Start: centered wide shot
Smooth tracking + subtle dolly movement
Slight angle variation (front → 3/4 → side for spins)
No fast cuts — continuous flow
Camera movement complements choreography, not distracts
💃 [MOVEMENT STYLE — IMPORTANT]
Authentic K-pop choreography feel
Mix of:
Sharp hits (chest pop, accents)
Smooth transitions (body waves, turns)
Clean isolations (hips, chest, arms)
Controlled spins, balanced footwork
No jitter, no unnatural speed
⏱️ [TIMING]
Each step: ~2–3 seconds
Total duration: ~35–50 seconds
Seamless transitions between steps
🎵 [MUSIC DIRECTION — VERY IMPORTANT]
Genre: K-pop / K-pop instrumental / dance-pop
Tempo: 100–115 BPM
Style:
Clean beat drops
Punchy percussion
Light synth melodies
Modern idol choreography vibe
Sync Notes:
Step transitions hit beats
Step 8 (Hair Flip) hits a musical accent
Step 15 (Chest Pop) synced with a strong beat hit
Final pose lands on a clean musical ending
🎨 [VISUAL STYLE]
Photorealistic
Slightly stylized K-pop MV tone
Soft cinematic grading
Clean, polished, high-end look
⚙️ [OUTPUT SETTINGS]
4K resolution
24–30 FPS
High motion clarity
No distortion, no artifacts
🚫 [RESTRICTIONS]
No extra dancers
No background crowd
No outfit changes
No deviation from choreography
No camera cuts that break continuity
```

> [!NOTE]
> ステップの説明が具体的であるほど、Seedanceは振り付けに忠実に従います。曖昧な説明ではなく、実際のダンスムーブ名（ボディロール、ヘアフリップ、チェストポップ）を使いましょう。このテクニックは武術の型、ヨガフロー、その他の連続した動きにも使えます。


<!-- Case 27: Character Intro Animation (by @0xbisc) -->
### ケース27: [キャラクター紹介アニメーション](https://x.com/0xbisc/status/2049496584283656690) (by [@0xbisc](https://x.com/0xbisc))

サイバーパンクAAAゲームスタイルのキャラクター紹介アニメーションを作成します。任意のキャラクター画像を取り、GPT Image 2でゲームキャラクターとしてリデザインし、シネマティックなイントロ画面を生成してから、Seedance 2.0でリビールをアニメーション化します。どんなキャラクターでも入れ替え可能 — ワークフローはキャラクターに依存しません。55いいね / 3K閲覧。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/intro_case27/output.jpg" width="400" alt="キャラクター紹介アニメーション出力"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/e52eaa0b-b2fa-4c35-b790-a92af05d0c82" width="400" controls></video></td>
</tr></table>

**手順:**

1. キャラクター画像から始める（自作アート、写真、またはAI生成）
2. GPT Image 2 でサイバーパンクAAAゲームキャラクターとしてリデザインする — 顔のアイデンティティを保持し、スタイルをアップグレード
3. キャラクターを使ったシネマティックなイントロ画面を生成する（暗い背景、ドラマチックなライティング、タイトルカードレイアウト）
4. Seedance 2.0 でイントロリビールをアニメーション化する

**GPT Image 2 プロンプト — キャラクターリデザイン:**

```
based on the provided image, redesign as a cyberpunk AAA game character, keep face identity, keep original outfit, hyper-realistic game character, near-photoreal but still game-rendered, cinematic realism, in-game cutscene quality, cinematic lighting, strong contrast, realistic materials, depth of field, subject in sharp focus, background slightly blurred, strong foreground-background separation, Night City inspired environment, dense futuristic megacity, neon signage, wet streets, reflections, industrial details, fully human appearance, clean natural skin, no mechanical lines, no implants, no cyber patterns, character holding a highly designed futuristic weapon, dynamic action-ready pose, confident and intense expression, 16:9 AAA key visual, strong composition, character dominant, no logo, generate a unique character name fitting the character personality, character name in graffiti-style typography, medium-to-small size, integrated into layout, not dominant, refined character info module, editorial layout style, minimal, no background panel, only 1–2 short traits, extremely concise labels, grid-aligned typography-driven layout, Cyberpunk style UI, neon yellow text only, flat geometric layout, strict alignment, only one info module, no additional graphics, clean image, no heavy grain, no film grain, smooth surfaces, high polish, no anime, illustration, raw photography, metallic UI, gold color, cluttered layout, dense UI, boxes, background panels, color blocks, arrows, mechanical skin lines, cyber patterns

```

**Seedance 2.0 プロンプト:**

```
industrial cyberpunk city at night, wet reflective ground, neon lights, distant explosions, floating sparks, cinematic atmosphere
camera always follows the character closely, no cuts, smooth tracking
motion continuity, no pose popping, no animation snapping, physically coherent transitions
0–2s:
character transitions into a low sliding movement
one hand brushing the ground for balance
sparks and debris react dynamically
weapon rotates forward in a smooth, deliberate motion
brief partial slow motion to emphasize control and flow
2–5s:
character raises weapon and fires while still moving forward
stylized compressed slow motion:
muzzle flash expands in layered light
face and muscles illuminated
subtle controlled recoil
shell casings eject in short slow-motion beats
particles and light distort around the shot
eyes focused strictly on target direction
final precise shot lands near the end of this phase
strong forward impact implied (sparks / explosion burst)
5–7s:
character motion fully stops, body settles naturally into final stance
character remains still, only subtle breathing motion
character lifts head and turns toward camera for the first time, then holds eye contact steadily
camera performs a subtle push-in
UI takes full visual focus:
UI builds progressively over the entire duration:
light glitch and scan effects
elements align into a clean layout
character name appears in graffiti handwritten animation, stroke-by-stroke reveal
secondary UI fades and slides in smoothly
```

> [!NOTE]
> このワークフローはキャラクターに依存しません — どんなキャラクター（アニメ、リアル、スタイライズド）でも入れ替えればパイプラインが適応します。ポイントはGPT Image 2の2段階プロセスです：まずターゲットスタイルに合わせてキャラクターをリデザインし、次にイントロ画面のレイアウトを構成します。


## 🎵 ミュージックビデオ・ショートフィルム

<!-- Case 7: Music Video with Suno (by @fukaborichannel) -->
### ケース7: [Sunoを使ったミュージックビデオ](https://x.com/fukaborichannel/status/2047206670020055317) (by [@fukaborichannel](https://x.com/fukaborichannel))

3つのツールの組み合わせ：GPT Image 2 でビジュアル、Seedance 2.0 でモーション、Sunoで音楽。まず音楽を制作してテンポと構成を固定し、次にビートに合わせたストーリーボードをデザインします。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/music_case7/input.jpg" width="280" alt="GPT Image 2で生成したMV用ストーリーボード"></a></td>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/music_case7/output.jpg" width="280" alt="ミュージックビデオ出力フレーム"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/fd4be5c7-cd02-4a77-ae07-6b80efeff201" width="280" controls></video></td>
</tr></table>

**手順:**

1. Sunoでターゲットスタイルの音楽を生成する — 曲の構成（イントロ / バース / コーラス）を確認
2. GPT Image 2 で曲のセクションごとにストーリーボードパネルをデザインする
3. Seedance 2.0 で各パネルをアニメーション化する — クリップの長さをビートに合わせる
4. 編集ソフトでクリップを音楽トラックに同期させる


> [!NOTE]
> まず音楽を制作しましょう。ストーリーボードをデザインする前にテンポと長さを把握しておくことで、パネルのタイミングをビートカットに正確に合わせることができます。


<!-- Case 8: Cyberpunk Style Short Film (by @ponyodong) -->
### ケース8: [サイバーパンクスタイルショートフィルム](https://x.com/ponyodong/status/2047210987263230133) (by [@ponyodong](https://x.com/ponyodong))

GPT Image 2 で一貫したビジュアルスタイル（サイバーパンク、ネオン、ランタン、フェミニンな美学）を確立し、Seedance 2.0 で各画像をアニメーション化して、壁紙、ポスター、ストーリーオープニングの間に位置するスタイリッシュなショートフィルムを制作します。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/cyberpunk_case8/input.jpg" width="280" alt="GPT Image 2で生成したサイバーパンクイラスト"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/db6ebb63-90dc-47c5-96c5-ab2fa53ed56d" width="280" controls></video></td>
</tr></table>

**手順:**

1. GPT Image 2 でビジュアルスタイルシステムを定義する — 色、ライティング、キャラクターの外見を固定
2. 同じムードを持つ4〜6枚の画像を生成する
3. Seedance 2.0 でスロー、アトモスフェリックなモーションプロンプトで各画像をアニメーション化する
4. クリップを並べて短いビジュアルナラティブを構築する


<!-- Case 11: Japanese MV Full Toolchain (by @Tz_2022) -->
### ケース11: [日本語MV — フルAIツールチェーン](https://x.com/Tz_2022/status/2047684399404056609) (by [@Tz_2022](https://x.com/Tz_2022))

完全な日本語スタイルのミュージックビデオを制作する4ツールパイプライン：GPT Image 2 でビジュアル → Seedance 2.0 でモーション → Suno 5.5 で音楽 → CapCutで最終編集。742いいね / 107K閲覧。

<table><tr>
<td align="center"><video src="https://github.com/user-attachments/assets/e5ce621c-7fa3-47b5-99a7-00df7741a651" width="400" controls></video></td>
</tr></table>

**手順:**

1. まずSuno 5.5で音楽を生成する — 曲の長さ、テンポ、ムードを固定
2. GPT Image 2 で曲のセクションに合わせたストーリーボードパネルをデザインする
3. Seedance 2.0 で各パネルをアニメーション化し、クリップの長さをビートに合わせる
4. ビデオクリップとSunoトラックをCapCutにインポートし、同期してエクスポートする


> [!NOTE]
> まず音楽を制作しましょう — ストーリーボードをデザインする前にビート構造を把握しておくことで、パネルのタイミングを曲のカットに正確に合わせることができます。これはケース7（シティポップMV）を拡張し、Sunoをループに追加して、パイプライン全体をポストアセンブリではなく同期された制作として扱います。


<!-- Case 20: Claude Shotlist → MV (by @CoffeeVectors) -->
### ケース20: [Claude ショットリスト → ミュージックビデオ](https://x.com/CoffeeVectors/status/2049592150581485757) (by [@CoffeeVectors](https://x.com/CoffeeVectors))

Claudeを使って詳細なショットリスト（異なるカメラアングルとアクションの15本の1秒クリップ）を生成し、GPT Image 2で1枚のポートレートを生成してから、Seedance 2.0で各ショットを制作します。クリップを自分のSuno音楽と合わせて編集すれば、完全なMVの完成です。AIがクリエイティブディレクションを書き、あなたは実行するだけです。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/shotlist_case20/input.jpg" width="400" alt="Claude ショットリストミュージックビデオ出力"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/d6ba86c4-65c3-4b1d-aa3c-846667f53b5e" width="400" controls></video></td>
</tr></table>

**手順:**

1. GPT Image 2 でビジュアルアンカーとなる1枚のキャラクターポートレートを生成する
2. Claudeに様々なアングルとアクションの15ショットのショットリスト（1ショット1秒）を書かせる
3. ポートレート + 各ショットの説明をSeedance 2.0に個別に入力する
4. すべてのクリップを編集し、音楽トラックに同期させる


**Seedance 2.0 プロンプト（ショットごと）:**

```
A 15-second prestige-TV sequence, one shot per second, scored to an apocalyptic sacred crescendo — low organ and dissonant brass through roaring choir, hammered bells, and earth-shaking timpani to a final shattering harmonic strike. Throughout: a pale young queen with white hair, a tall ornate gold filigree crown, a translucent gauze veil, and a heavily jeweled pale gown — channeler of divine fire from above. Shot entirely handheld — visible micro-shake, breath-rhythm sway, reactive whip-corrections to action, documentary-tense framing.
1 (0–1s) Sky Opens. Handheld wide low-angle, camera tilted up. Black clouds spiral and split in a tear of white-gold light. She stands small below. Organ slams.
2 (1–2s) Eyes To Heaven. Handheld tight close-up, slight float. Her eyes lifted, gold light on her face, a tear of fire tracking down her cheek. Choir enters.
3 (2–3s) Hand Raised. Handheld medium, slight push-in. She raises one palm to the sky. Clouds above twist toward her gesture. Strings climb.
4 (3–4s) First Bolt. Handheld wide. A colossal pillar of holy fire descends and splits a distant black tower. Camera jolts on impact. Hammer beat.
5 (4–5s) The Pointing. Handheld tight medium. She extends one ringed finger slowly toward the horizon. Camera barely breathing. Bells ring.
6 (5–6s) Bolts Rain. Handheld wide, panning to track strikes. Dozens of pillars of holy fire descend across a battlefield. Camera whips reactively to each impact. Drums hammer.
7 (6–7s) Cloaked In Light. Handheld low-angle medium. A shaft of holy fire engulfs her without burning. Camera trembles in the pressure wave. Choir doubles.
8 (7–8s) The Wicked Burn. Handheld tight medium. A robed figure raises a blade — consumed in white-gold fire from above, ash silhouette collapsing. Camera flinches with the strike. Bass hit.
9 (8–9s) Walking Forward. Handheld tracking wide, operator moving with her. She advances across cracked scorched earth, pillars of fire descending in her wake. Strings shriek.
10 (9–10s) Crown Of Lightning. Handheld tight on the crown, slight float. White-gold lightning arcs continuously between the spires. Hair lifts in charged air. Bells climb.
11 (10–11s) Closed Fist. Handheld tight close-up. Her hand closes slowly into a fist. Vast clap of thunder. Camera shakes hard. Sustained held chord.
12 (11–12s) The Cleansing. Handheld wide, operator on a high vantage with visible sway. A fortified city struck by a grid of descending holy fire pillars. She stands small below, untouched. Choir at full roar.
13 (12–13s) The Quiet After. Handheld medium, breathing slowly. She lowers her hand. The storm stills. Ash falls like snow around her. Music drops to near-silence.
14 (13–14s) Eyes Return. Handheld extreme close-up, slight float. Eyes still warm gold blink once slowly. Faintest exhale. Single sustained tone.
15 (14–15s) The Smiting. Handheld frontal wide at dusk, settling into stillness on the final hold. She stands at the center of a vast scorched circle, horizon reduced to smoking ruin. Torn sky still glowing above her. Final shattering harmonic strike sustains.

Style: Photorealistic dark holy fantasy, prestige-TV aesthetic. Anamorphic 35mm, shallow DoF, heavy volumetric atmosphere — smoke, ash, ember haze, heat distortion, charged air shimmer. Palette of scorched bone-white, ivory, ash-gray, storm-slate, and incandescent white-gold. Painterly compositions, fine detail against destruction, organic film grain, heavy highlight bloom on the divine fire. Handheld throughout — visible micro-shake, reactive whip-corrections, breath-rhythm sway, camera flinching with every impact. No tripod stillness until the final hold. Operatic, terrifying, sovereign. The sky itself as her instrument.
```

> [!NOTE]
> このワークフローはクリエイティブディレクション（Claude）とビジュアル実行（GPT Image 2 + Seedance）を分離します。同じキャラクターの多様なショットが必要なミュージックビデオに特に効果的です。アンカーとしての1枚のポートレートが、15クリップすべてにわたって一貫性を維持します。


## 🎮 ゲームコンセプト

<!-- Case 9: Game & Interactive Content (by @AbleGPT) -->
### ケース9: [ゲーム・インタラクティブコンテンツ](https://x.com/op7418/status/2046854932620525750) (by [@op7418](https://x.com/op7418))

GPT Image 2 でゲームスタイルのUI画像（HUD要素、スキルバー、選択オーバーレイ付き）を生成し、Seedance 2.0 でアニメーション化してインタラクティブなゲームシーケンスをシミュレートします。ゲームやイラストスタイルは、リアルな人物映像よりもSeedanceのコンテンツ制限が少なくなります。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/game_case9/input.jpg" width="400" alt="ゲームUI入力画像"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/3d5d7525-b469-4c3b-aab9-68dc47630fdd" width="400" controls></video></td>
</tr></table>

**手順:**

1. GPT Image 2 でHUD要素を含むARPGまたはゲームUIスタイルの画像を生成する
2. Seedance 2.0 にインポートし、インタラクションまたは戦闘シーケンスを説明する
3. ポストプロダクションエフェクト（パーティクル、グロー）を追加して仕上げる

**GPT Image 2 プロンプト-2:**

```
帮我生成一个以《金瓶梅》为主题的古代 ARPG MMO 开放世界游戏的截图
```
**GPT Image 2 プロンプト-2:**
```
出现 UI 选择 UI 之后变成第二张图的场景图
```

**Seedance 2.0 プロンプト:**

```
选择 UI 之后变成第二张图右边的场景
```

**バリアント — ARPGゲームシミュレーション (by [@0xbisc](https://x.com/0xbisc/status/2047315350862352715)):**

ワンピース、ストレンジャー・シングス、どんなIPでも — 存在しない世界のゲームスクリーンショットを生成し、Seedance 2.0でライブゲームプレイに拡張します。934いいね / 125K閲覧。

<table><tr>
<td align="center"><video src="https://github.com/user-attachments/assets/983b433a-88ea-4843-9047-fc01396752fe" width="400" controls></video></td>
</tr></table>

**GPT Image 2 プロンプト:**

```
Generate an ARPG dialogue game screenshot inspired by [film/series name]
```

**Seedance 2.0:** 画像から動画モードを使用。プロンプト不要 — SeedanceがHUDレイアウトを読み取り、自動的にゲームプレイシーケンスに拡張します。

> [!NOTE]
> Seedance 2.0 にはリアルな人物コンテンツに制限があります。ゲーム、アニメ、イラストスタイルはこれらの制限のほとんどを回避し、より幅広いクリエイティブ表現が可能です。


<!-- Case 17: Game Interface Animation Full Pipeline (by @0xInk_) -->
### ケース17: [ゲームインターフェースアニメーション — フルパイプライン](https://x.com/0xInk_/status/2048809000121360649) (by [@0xInk_](https://x.com/0xInk_))

このコレクションで最もバイラルになったワークフロー：完全なビデオゲームインターフェースアニメーションをゼロから作成します。Midjourneyで2Dキャラクターから始め、GPT Image 2で3Dゲーム対応ルックに変換し、フルゲームUI（HUD、ローディング画面、メニュー）をデザインしてから、Seedance 2.0ですべてをアニメーション化します。GPT Image 2はUIの細部を処理し、品質劣化なしに反復的な修正が可能なため、ここで真価を発揮します。2280いいね / 208K閲覧 / 2793ブックマーク。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/game_case17/output.jpg" width="400" alt="ゲームインターフェースアニメーション出力"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/b83da8f3-3dd6-44a3-bb27-b0d59cab381a" width="400" controls></video></td>
</tr></table>


> [!NOTE]
> 重要なポイント：GPT Image 2は品質劣化なしに画像を何度でも修正できます — UIレイアウトの反復に最適です。フルゲームインターフェースを一連の静止画面として構築し、Seedanceにそれらをシームレスなアニメーションに接続させましょう。


<!-- Case 24: GTA-Style City Game Concept (by @markgadala) -->
### ケース24: [GTAスタイルシティゲームコンセプト](https://x.com/markgadala/status/2048560337960489385) (by [@markgadala](https://x.com/markgadala))

5分で好きなバージョンのGTAを作れます。GPT Image 2で任意の都市（東京、ラゴス、ムンバイ）を舞台にしたゲームUIスクリーンショットを生成し、Seedance 2.0でゲームプレイ映像にアニメーション化します。結果は、存在しないゲームの本物のゲームトレーラーのように見えます。99いいね / 8.7K閲覧。

<table><tr>
<td align="center"><video src="https://github.com/user-attachments/assets/d3b0a7b9-827a-47f6-b24e-eabfacf3e892" width="400" controls></video></td>
</tr></table>

**手順:**

1. GTAバリアントを定義する — 都市、時代、ビジュアルスタイル
2. GPT Image 2 でゲームスクリーンショットを生成する：三人称視点、HUDオーバーレイ、都市環境
3. Seedance 2.0 にインポートしてゲームプレイ映像としてアニメーション化する
4. クリップをトレーラーに組み立てる


> [!NOTE]
> これはケース9のゲームコンセプトアプローチをオープンワールドシティゲームに特化して拡張したものです。HUD要素（ミニマップ、体力バー、手配度の星）が「本物のゲーム」の錯覚を売り込みます。どの都市でも使えます — ストリートレベルの詳細が具体的であるほど、結果は説得力を増します。


## 🛠 制作ツール

<!-- Case 18: Single Agent Automated Workflow (by @venturetwins) -->
### ケース18: [シングルエージェント自動ワークフロー](https://x.com/venturetwins/status/2048526911056613586) (by [@venturetwins](https://x.com/venturetwins))

手間ゼロのアプローチ：単一のAIエージェント（Glifなど）に欲しいものを伝えるだけで、GPT Image 2でのストーリーボード生成からSeedance 2.0でのアニメーション化まで、パイプライン全体を1つの会話で処理します。手動のファイル転送もステップごとのプロンプトエンジニアリングも不要です。934いいね / 70K閲覧。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/agent_case18/output.jpg" width="400" alt="シングルエージェント自動ワークフロー出力"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/cc01849d-ee9b-47af-a7b0-d13250a001e0" width="400" controls></video></td>
</tr></table>


<!-- Case 21: Casting Grid Actor Audition (by @8fstudioz) -->
### ケース21: [キャスティンググリッド — 俳優オーディション](https://x.com/8fstudioz/status/2049547426198151627) (by [@8fstudioz](https://x.com/8fstudioz))

1回の生成で4人の俳優をオーディションしてクレジットを節約。GPT Image 2で同じ役に異なる俳優を表示する4パネルのキャスティンググリッドを生成し、Seedance 2.0で同じセリフを使って各俳優をテストします。フル動画にクレジットを投入する前に、どの俳優に追加投資する価値があるかを見極めましょう。

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/casting_case21/input.jpg" width="400" alt="キャスティンググリッド入力"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/dcdd958f-70cd-43f6-b191-4e0715fe2472" width="400" controls></video></td>
</tr></table>

**手順:**

1. GPT Image 2 で4パネルのキャスティンググリッドを生成する — 同じ役、4人の異なる俳優
2. Seedance 2.0 で同じセリフとアクションを使って各俳優を個別にテストする
3. パフォーマンスの質を比較する（アイコンタクト、表情、動き）
4. 残りのクレジットは勝者の俳優にのみ投資する

**GPT Image 2 プロンプト:**

```
Create a 16:9 horizontal cinematic casting board showing 4 different actor candidates for the same role.

Style:
[INSERT VISUAL STYLE]
Examples: CGI AAA video game cinematic, photorealistic, anime, stylized 3D

Role brief:
[INSERT ROLE DESCRIPTION]
Describe the type of lead or character the user is casting for.

World / genre:
[INSERT WORLD OR GENRE]
Examples: spy-action thriller, fantasy RPG, sci-fi adventure, crime drama

Wardrobe:
[INSERT WARDROBE DESCRIPTION]
Describe the clothing or outfit direction all 4 actors should share.

Tone:
[INSERT TONE]
Examples: sleek, dangerous, adventurous, grounded, moody, confident

Visual direction:
[INSERT VISUAL RENDERING NOTES]
Describe the rendering quality, material detail, realism level, facial detail, costume detail, and overall look.

Cinematic look:
[INSERT CINEMATIC STYLE]
Examples: blockbuster trailer aesthetic, prestige drama look, AAA game cinematic look

Camera framing:
[INSERT FRAMING]
Examples: 3/4 body, full body, waist-up

Camera angle:
[INSERT CAMERA ANGLE]
Examples: eye-level, slight low angle, slight 3/4 angle

Lens:
[INSERT LENS]
Examples: 50mm cinematic lens, 85mm portrait lens

Depth of field:
[INSERT DEPTH OF FIELD]
Examples: shallow, shallow but controlled

Lighting:
[INSERT LIGHTING SETUP]
Describe the lighting style.

Background:
[INSERT BACKGROUND DESCRIPTION]
Describe the background environment or backdrop.

Colour treatment:
[INSERT COLOUR TREATMENT]
Describe the grading or colour tone.

Layout:
Arrange the 4 actor candidates in a 16:9 horizontal composition with 4 evenly spaced vertical panels across the frame, one actor per panel from left to right.

Character variation:
Each candidate should feel like a different casting choice for the same role. Vary facial structure, age feel, hairstyle, expression, posture, and energy, but keep them grounded in the same world, wardrobe logic, and tonal universe.

Important:
- Same role
- Same world
- Same wardrobe logic
- Same visual style
- Different actor interpretations
- No duplicated faces
- No text
- No labels
- No watermark

The final image should feel like a premium cinematic casting board for [INSERT PROJECT TYPE].
Examples: a film, a game, an animated short, a cinematic trailer
```

**Seedance 2.0 プロンプト（俳優ごと）:**

```
Use the uploaded 16:9 four-panel casting board as the source image.

Create a controlled 15-second cinematic casting audition reel for [INSERT ROLE OR PROJECT TYPE].

Animate the actors one by one in this exact order from left to right:

0.0–3.5 seconds: ONLY the far-left actor performs.
3.5–7.0 seconds: ONLY the second actor from the left performs.
7.0–10.5 seconds: ONLY the third actor from the left performs.
10.5–14.0 seconds: ONLY the far-right actor performs.
14.0–15.0 seconds: hold on the full four-panel board with all actors still.

Each actor delivers the same audition line:
"[INSERT DIALOGUE LINE]"

Performance direction:
Each actor should look directly into the camera while delivering the line, as if performing a screen test audition. Their eye line should stay locked to camera.

Each actor should deliver the line with:
[INSERT PERFORMANCE TRAITS]
Examples: calm control, quiet menace, emotional vulnerability, confidence, charm, intensity, humor

The performance should feel:
[INSERT PERFORMANCE TONE]
Examples: sleek, cinematic, believable, grounded, dramatic, stylized

Each actor should bring a slightly different interpretation of the same role.

Control rules:
ONLY the active actor moves during their assigned time window.
ONLY the active actor speaks during their assigned time window.
ONLY animate the active actor's mouth, eyes, facial expression, head, and subtle upper-body movement.
The active actor must look directly at the camera while speaking.
All other actors remain completely still like frozen reference images.
Do not animate multiple actors at the same time.
Do not change the panel layout.
Do not change actor positions.
Do not cut to a new scene.
Do not reframe into a different composition.
Do not change wardrobe.
Do not change background.
Do not change lighting.
Do not add new characters.
Do not add extra dialogue.
Do not add captions, subtitles, labels, or text.

Camera direction:
Keep the four-panel 16:9 casting board as the main composition. Use only [INSERT CAMERA MOVEMENT STYLE] toward the active actor during their performance window.
Examples: a subtle cinematic push-in, gentle focus emphasis, minimal controlled emphasis

Keep the movement [INSERT CAMERA BEHAVIOUR].
Examples: minimal, smooth, controlled

Keep the actor presented toward camera so the audition feels direct and comparable.

Audio / timing:
Each actor should speak the dialogue clearly within about 3.5 seconds.
The same line is repeated four times, once per actor.
No overlapping voices.
No background conversation.
No unnecessary sound effects.

Final result:
A clean casting audition reel where four actor candidates perform the same line one by one from left to right, each looking directly into the camera, making it easy to compare screen presence, facial acting, eye contact, posture, and dialogue delivery.
```

> [!NOTE]
> キャラクターは静止画では素晴らしく見えても、セリフ、アイコンタクト、パフォーマンスをテストすると完全に役を失うことがあります。このワークフローは、フルシーンにクレジットを費やす前にキャスティングの判断を前倒しします。


<!-- Case 22: 3D Sculpt → AI Render → Animation (by @_DAntunes_) -->
### ケース22: [3Dスカルプト → AIレンダー → アニメーション](https://x.com/_DAntunes_/status/2049142166232904078) (by [@_DAntunes_](https://x.com/_DAntunes_))

従来の3DモデリングとAI動画の橋渡し：Nomad Sculpt（または任意のスカルプティングアプリ）でラフな3Dクレイモデルを作成し、GPT Image 2で洗練されたイラストにレンダリングしてから、ComfyUI経由でSeedance 2.0でアニメーション化します。これにより、純粋なテキストプロンプトでは実現できないポーズと構図の精密なコントロールが得られます。

<table><tr>
<td align="center"><video src="https://github.com/user-attachments/assets/f5ecdb0c-d1ca-4291-91bc-eb88de91cd82" width="400" controls></video></td>
</tr></table>

**手順:**

1. Nomad Sculpt（またはBlender、ZBrushなど）でラフな3Dモデルをスカルプトする
2. 希望のカメラアングルからモデルのスクリーンショットをエクスポートする
3. GPT Image 2 で3Dモデルを洗練されたイラストまたはリアルな画像にレンダリングする
4. レンダリングされた画像をSeedance 2.0（ComfyUI経由またはダイレクト）にインポートしてアニメーション化する

> [!NOTE]
> 3Dモデルは、テキストプロンプトでは得られないものを提供します：ボディポーズ、手の位置、カメラアングルの正確なコントロールです。ラフなクレイモデルでも十分です — GPT Image 2がすべてのレンダリングとディテール作業を処理します。このパイプラインは、すでに3Dツールを使用していてAIアニメーションをワークフローに追加したいクリエイターに最適です。


## 💡 ヒント・テクニック

### 一貫性ガイド

GPT Image 2の出力間およびSeedance 2.0のアニメーション全体でビジュアルの一貫性を維持することが、最も一般的な課題です。以下のアプローチが各レイヤーに対応します。

**商品画像の一貫性**

Seedanceでの商品の歪みの根本原因は、モーション補間が細部を書き換えることです — ロゴ、テクスチャ、表面パターンが変更されます。

解決策:
- Seedanceプロンプトに `keep the product appearance completely unchanged, camera movement only, no rotation` を追加する
- 被写体のモーションではなくカメラモーション（プッシュイン、プルアウト）を選択する — 商品は静止させてカメラを動かす
- クリップの長さを3秒以内に抑える — 短いクリップほど歪みの蓄積が少ない

**キャラクターの一貫性**

- まず三面図キャラクターシートを生成し、後続のすべてのストーリーボードフレームのビジュアルアンカーとして使用する
- すべてのストーリーボードパネルプロンプトに簡潔なキャラクター説明（髪の色、服装、体格）を含める
- 1つのクリップ内でキャラクターの視点を切り替えない

**シーンの一貫性**

GPT Image 2で複数のストーリーボードパネルを生成する際、プロンプトの先頭でシーンパラメータを固定します：

```
Scene setting: [location], [time of day], [lighting direction], [fixed background elements].
Maintain this scene setting unchanged across all panels.
```

---

### プロンプトテンプレート

**GPT Image 2 → ストーリーボードテンプレート**

```
Create a [N]-panel storyboard for [subject]:
- Style: [realistic / anime / illustration / cinematic]
- Aspect ratio: 16:9 widescreen
- Each panel: include shot type (wide / medium / close-up) + action description
- Character: [fixed appearance description]
- Scene tone: [color palette / lighting / mood]
Output as a single image with [N] panels separated by thin lines.
```

**GPT Image 2 → 3×3グリッドテンプレート**

```
Output a single 3×3 grid storyboard image showing the following continuous action:
[describe the action sequence]
Requirements:
- 9 panels arranged left-to-right, top-to-bottom showing continuous motion
- Character position and scale consistent across all panels
- Background consistent throughout
- No text, labels, or content outside the panel borders
```

**Seedance 2.0 → アニメスタイルテンプレート**

```
Japanese full-color animation, high-speed editing, high frame count, 24fps.
[Scene description]. [Character description]. [Action description].
Strong camera work, high visual impact.
```

**Seedance 2.0 → CMスタイルテンプレート**

```
Cinematic commercial quality, [brand tone: premium / energetic / warm],
[product] centered in frame, slow camera push-in,
[lighting direction] highlights the product, clean background, no people.
Duration: 3 seconds.
```

**プロンプトの長さ — 短い方が勝つことが多い**

[@Iancu_ai](https://x.com/Iancu_ai/status/2047882924679168083) によるコミュニティ実験：1500語の映画品質Seedanceプロンプトが、たった1文に負けました。同じキャラクター、同じ15秒。短いプロンプトが勝ちました。Seedanceは網羅的な説明よりも方向性の明確さを評価します — シーンのすべての詳細ではなく、モーションの意図を書きましょう。

---

### トラブルシューティング

**Seedanceコンテンツモデレーションブロック**

原因：画像にセンシティブとフラグされたコンテンツが含まれている（リアルな暴力、特定のポーズの人物の顔）。
対処法：アニメまたはイラストスタイルに切り替えるか、プロンプトから人物の説明を削除する。

**出力モーションが混沌としている**

原因：ストーリーボード画像が複雑すぎる — Seedanceが主要なモーション方向を判断できない。
対処法：ストーリーボードパネルを1つのメイン被写体と1つの明確なアクションにシンプル化する。背景要素を減らす。

**商品画像が歪む**

上記の一貫性ガイド → 商品画像の一貫性セクションを参照してください。

**プラットフォーム入力フォーマット要件**

| プラットフォーム | 推奨入力サイズ | 対応フォーマット | 最大ファイルサイズ |
| :---: | :---: | :---: | :---: |
| Hailuo | 1280×720 または 720×1280 | JPG / PNG | 10 MB |
| Higgsfield | 1920×1080 | PNG | 20 MB |
| HitPaw | 任意の比率 | JPG / PNG / WEBP | 15 MB |

## 🚀 Evolinkで試す

Evolinkなら、GPT Image 2 と Seedance 2.0 を1つの場所で実行できます — プラットフォームの切り替えもファイルの再アップロードも不要です。

**Evolinkを選ぶ理由**

- GPT Image 2 と Seedance 2.0 の単一APIキー
- 同じインターフェースでの画像から動画への直接転送 — 画像を生成して「動画を生成」をクリックするだけ、ダウンロード不要
- バッチ処理 — 複数のストーリーボードパネルを順次動画生成のためにキューに入れる

**使い方**

```
Step 1: Open Evolink → select GPT Image 2 → generate your storyboard image
Step 2: Click "Generate Video" → Seedance 2.0 receives the image automatically
Step 3: Add your Seedance prompt → generate
```

<a href='https://evolink.ai/signup?utm_source=github&utm_medium=readme&utm_campaign=gptimage2-x-seedance2'><img src='https://img.shields.io/badge/🚀 Get%20Started-Evolink-black' height="25"></a>


## 🙏 謝辞

このリポジトリは、優れたオープンワークフローコレクションとコミュニティで共有された実験からインスピレーションを受けました。

ワークフローを公開で共有し、これらのケーススタディを可能にしてくれたクリエイターとコントリビューターに感謝します：
[@szounft](https://x.com/szounft) · [@Toshi_nyaruo_AI](https://x.com/Toshi_nyaruo_AI) · [@ponyodong](https://x.com/ponyodong) · [@servasyy_ai](https://x.com/servasyy_ai) · [@YaReYaRu30Life](https://x.com/YaReYaRu30Life) · [@fukaborichannel](https://x.com/fukaborichannel) · [@Shin_Engineer](https://x.com/Shin_Engineer) · [@ai_mitosan](https://x.com/ai_mitosan) · [@kiyoshi_shin](https://x.com/kiyoshi_shin) · [@AbleGPT](https://x.com/AbleGPT) · [@patata1216](https://x.com/patata1216) · [@peter6759](https://x.com/peter6759) · [@hibi_ai__](https://x.com/hibi_ai__) · [@heygentlewhale](https://x.com/heygentlewhale) · [@ai_gezgini](https://x.com/ai_gezgini) · [@Tz_2022](https://x.com/Tz_2022) · [@old_pgmrs_will](https://x.com/old_pgmrs_will) · [@0xbisc](https://x.com/0xbisc) · [@Iancu_ai](https://x.com/Iancu_ai) · [@Jake_Joseph](https://x.com/Jake_Joseph) · [@venturetwins](https://x.com/venturetwins) · [@0xInk_](https://x.com/0xInk_) · [@markgadala](https://x.com/markgadala) · [@Ankit_patel211](https://x.com/Ankit_patel211) · [@Ciri_ai](https://x.com/Ciri_ai) · [@nimentrix](https://x.com/nimentrix) · [@insmind_com](https://x.com/insmind_com) · [@kingofdairyque](https://x.com/kingofdairyque) · [@Kashberg_0](https://x.com/Kashberg_0) · [@airina_xyz](https://x.com/airina_xyz) · [@CoffeeVectors](https://x.com/CoffeeVectors) · [@mdmadeit](https://x.com/mdmadeit) · [@Morph_VGart](https://x.com/Morph_VGart) · [@MEnesKirca](https://x.com/MEnesKirca) · [@MrLarus](https://x.com/MrLarus) · [@AYi_AInotes](https://x.com/AYi_AInotes) · [@8fstudioz](https://x.com/8fstudioz) · [@_DAntunes_](https://x.com/_DAntunes_)

*すべてのケースがオリジナルのクリエイターに正しく帰属されていることを保証するものではありません。修正が必要な場合は、ご連絡いただければ更新いたします。*

さらに興味深いワークフローケースを共有したい方は、お気軽にご連絡ください。Evolinkワークフローライブラリの拡充にご協力ください。

[![Star History Chart](https://api.star-history.com/svg?repos=EvoLinkAI/GPT-Image-2-Seedance2-Workflow&type=Date)](https://www.star-history.com/#EvoLinkAI/GPT-Image-2-Seedance2-Workflow&Date)
