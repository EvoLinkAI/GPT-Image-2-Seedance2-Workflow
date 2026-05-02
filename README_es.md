<div align="center">

<a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=banner&utm_campaign=gptimage2-x-seedance2"><img src="images/logo.png" alt="Guia de flujo de trabajo GPT Image 2 x Seedance 2.0"></a>

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




## 🎬 Introduccion

Bienvenido al repositorio de flujos de trabajo GPT Image 2 x Seedance 2.0! 🤗

**Recopilamos flujos de trabajo probados, plantillas de prompts y ejemplos reales de creadores para combinar GPT Image 2 y Seedance 2.0 y producir videos de IA de alta calidad.**

GPT Image 2 se encarga de "que dibujar" y de la consistencia visual. Seedance 2.0 se encarga de "como moverlo", animando esas imagenes hasta convertirlas en video. Juntos forman uno de los pipelines de video con IA mas capaces disponibles hoy.

La mayoria de los casos de este repositorio provienen de creadores de X/Twitter, experimentos de la comunidad y flujos de produccion reales.

Pruebalo: [GPT Image 2 + Seedance 2.0](https://evolink.ai?utm_source=github&utm_medium=readme&utm_campaign=gptimage2-x-seedance2)

Si te resulta util, considera darle una estrella. ⭐



## 📰 Novedades

- **1 de mayo de 2026:** Agregados los Casos 13-27 (cuadricula de secuencia de baile, animacion de pagina de comic, comercial de lujo, video gastronomico cinematografico, pipeline de interfaz de juego, flujo de un unico agente, control de costes con storyboard primero, MV con shotlist de Claude, cuadricula de casting, pipeline de escultura 3D, remake cyberpunk de IP, concepto de ciudad GTA, coreografia K-Pop, anuncio de video de producto, animacion de presentacion de personaje)
- **25 de abril de 2026:** Agregados los Casos 10-12 (storyboard multiframe, toolchain de MV japones, Claude Code x hoja de personaje), Caso 9 ampliado con variantes de simulacion ARPG, showcase de comunidad agregado a la Galeria
- **23 de abril de 2026:** Lanzamiento del repositorio con 9 casos de flujo de trabajo curados

## 📑 Menu

- [🎬 Introduccion](#-introduccion)
- [📰 Novedades](#-novedades)
- [📑 Menu](#-menu)
- [🎥 Tecnicas de Storyboard](#-tecnicas-de-storyboard)
  - [Caso 1: Storyboard estandar → Video (por @kiyoshi_shin)](#caso-1-storyboard-estandar--video-por-kiyoshi_shin)
  - [Caso 2: Metodo de storyboard en cuadricula 3x3 (por @servasyy_ai)](#caso-2-metodo-de-storyboard-en-cuadricula-33-por-servasyy_ai)
  - [Caso 10: Referencia multiframe → Video de corte rapido (por @heygentlewhale)](#caso-10-referencia-multiframe--video-de-corte-rapido-por-heygentlewhale)
  - [Caso 19: Control de costes con storyboard primero (por @0xbisc)](#caso-19-control-de-costes-con-storyboard-primero-por-0xbisc)
- [📱 Comercial y Producto](#-comercial-y-producto)
  - [Caso 5: Video demo de MVP de app (por @Shin_Engineer)](#caso-5-video-demo-de-mvp-de-app-por-shin_engineer)
  - [Caso 6: Comercial de 15 segundos (por @ai_mitosan)](#caso-6-comercial-de-15-segundos-por-ai_mitosan)
  - [Caso 15: Comercial de lujo — Del storyboard al film (por @insmind_com)](#caso-15-comercial-de-lujo--del-storyboard-al-film-por-insmind_com)
  - [Caso 16: Video gastronomico cinematografico (por @kingofdairyque)](#caso-16-video-gastronomico-cinematografico-por-kingofdairyque)
  - [Caso 26: Imagen de producto → Anuncio de video corto (por @insmind_com)](#caso-26-imagen-de-producto--anuncio-de-video-corto-por-insmind_com)
- [🎨 Animacion y Personaje](#-animacion-y-personaje)
  - [Caso 3: Hoja de personaje → Animacion (por @YaReYaRu30Life)](#caso-3-hoja-de-personaje--animacion-por-yareyaru30life)
  - [Caso 4: Video estilo opening de anime (por @Toshi_nyaruo_AI)](#caso-4-video-estilo-opening-de-anime-por-toshi_nyaruo_ai)
  - [Caso 12: Claude Code x Hoja de personaje → Animacion (por @old_pgmrs_will)](#caso-12-claude-code--hoja-de-personaje--animacion-por-old_pgmrs_will)
  - [Caso 13: Cuadricula de secuencia de baile → Video de baile (por @Ciri_ai)](#caso-13-cuadricula-de-secuencia-de-baile--video-de-baile-por-ciri_ai)
  - [Caso 14: Pagina de comic → Video animado (por @nimentrix)](#caso-14-pagina-de-comic--video-animado-por-nimentrix)
  - [Caso 25: Coreografia K-Pop — Control detallado (por @Kashberg_0)](#caso-25-coreografia-k-pop--control-detallado-por-kashberg_0)
  - [Caso 27: Animacion de presentacion de personaje (por @0xbisc)](#caso-27-animacion-de-presentacion-de-personaje-por-0xbisc)
- [🎵 Video Musical y Cortometraje](#-video-musical-y-cortometraje)
  - [Caso 7: Video musical con Suno (por @fukaborichannel)](#caso-7-video-musical-con-suno-por-fukaborichannel)
  - [Caso 8: Cortometraje estilo cyberpunk (por @ponyodong)](#caso-8-cortometraje-estilo-cyberpunk-por-ponyodong)
  - [Caso 11: MV japones — Toolchain completo de IA (por @Tz_2022)](#caso-11-mv-japones--toolchain-completo-de-ia-por-tz_2022)
  - [Caso 20: Shotlist de Claude → Video musical (por @CoffeeVectors)](#caso-20-shotlist-de-claude--video-musical-por-coffeevectors)
- [🎮 Concepto de Juego](#-concepto-de-juego)
  - [Caso 9: Juegos y contenido interactivo (por @op7418)](#caso-9-juegos-y-contenido-interactivo-por-op7418)
  - [Caso 17: Animacion de interfaz de juego — Pipeline completo (por @0xInk_)](#caso-17-animacion-de-interfaz-de-juego--pipeline-completo-por-0xink_)
  - [Caso 24: Concepto de juego de ciudad estilo GTA (por @markgadala)](#caso-24-concepto-de-juego-de-ciudad-estilo-gta-por-markgadala)
- [🛠 Herramientas de Produccion](#-herramientas-de-produccion)
  - [Caso 18: Flujo automatizado de un unico agente (por @venturetwins)](#caso-18-flujo-automatizado-de-un-unico-agente-por-venturetwins)
  - [Caso 21: Cuadricula de casting — Audicion de actores (por @8fstudioz)](#caso-21-cuadricula-de-casting--audicion-de-actores-por-8fstudioz)
  - [Caso 22: Escultura 3D → Render con IA → Animacion (por @_DAntunes_)](#caso-22-escultura-3d--render-con-ia--animacion-por-_dantunes_)
- [💡 Consejos y Tecnicas](#-consejos-y-tecnicas)
  - [Guia de consistencia](#guia-de-consistencia)
  - [Plantillas de prompts](#plantillas-de-prompts)
  - [Solucion de problemas](#solucion-de-problemas)
- [🚀 Pruebalo en Evolink](#-pruebalo-en-evolink)
- [🙏 Agradecimientos](#-agradecimientos)


## 🎥 Tecnicas de Storyboard

<!-- Case 1: Standard Storyboard → Video (by @kiyoshi_shin) -->
### Caso 1: [Storyboard estandar → Video](https://x.com/kiyoshi_shin/status/2047133524403400847) (por [@kiyoshi_shin](https://x.com/kiyoshi_shin))

El flujo de trabajo mas comun. Usa GPT Image 2 para generar un panel de storyboard y luego animalo con Seedance 2.0. Ideal para videos promocionales, dramas cortos y openings de animacion.

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/storyboard_case1/input.jpg" width="280" alt="Storyboard generado con GPT Image 2"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/ac25fc3d-b6cb-4149-a8ba-e7e10c5b1faa" width="280" controls></video></td>
</tr></table>

**Pasos:**

1. Describe tu escena a GPT Image 2 y genera una imagen de storyboard
2. Importa el storyboard en Seedance 2.0 usando el modo Image-to-Video
3. Exporta cada clip y ensamblalos en tu software de edicion

**Prompt para GPT Image 2:**

```
Create a 6-panel storyboard for a 15-second brand promotional video. Label each panel with a shot description.
Style: cinematic, cool color tone, widescreen 16:9.
Content: the journey of a product from factory to the customer's hands.
```

**Prompt para Seedance 2.0:**

```
Cinematic brand advertisement, slow camera push-in, product centered in frame, warm side lighting, soft background blur, no people, 3 seconds.
```

> [!NOTE]
> Genera las imagenes del storyboard en 16:9 para evitar el recorte automatico de Seedance. Configura la tasa de fotogramas a 24fps para ajustarte al estandar cinematografico. Manten cada panel del storyboard simple: cuanto mas simple sea el contenido, mas preciso sera el movimiento generado.


<!-- Case 2: 3×3 Grid Storyboard Method (by @servasyy_ai) -->
### Caso 2: [Metodo de storyboard en cuadricula 3x3](https://x.com/servasyy_ai/status/2047198012750143999) (por [@servasyy_ai](https://x.com/servasyy_ai))

Una tecnica clave descubierta por la comunidad: componer todos los paneles del storyboard en una sola imagen de cuadricula 3x3 antes de importarla a Seedance reduce significativamente la tasa de fallos en comparacion con importar los fotogramas uno por uno.

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/storyboard_case2/output.jpg" width="400" alt="Storyboard en cuadricula 3x3"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/00f32388-a17b-4b9c-8da3-1956436ce91b" width="400" controls></video></td>
</tr></table>



**Pasos:**

1️⃣ Introduce el contenido que quieres crear + el prompt ✅ "Create a storyboard in a 3x3 grid format"
2️⃣ Crea un prompt a partir de la imagen del paso 1 con ChatGPT
3️⃣ Usa la imagen del paso 1 como referencia en Seedance
4️⃣ Introduce el prompt creado en el paso 2.

**Prompt para GPT Image 2:**

```
[describe your scene] and Create a storyboard in a 3×3 grid format
```

**Prompt para Seedance 2.0:**
convierte esta imagen en video
```
[Describe the motion and style. Example: Japanese full-color animation, fast cuts, high frame count, 24fps, dark fantasy anime OP style, intense battle scenes.]
```

> [!NOTE]
> **Sustituye el contenido entre corchetes antes de usarlo.** Este metodo funciona porque Seedance analiza la intencion de movimiento a partir de una sola imagen. La cuadricula proporciona una referencia direccional y produce un movimiento mas coherente que imagenes separadas.


<!-- Case 10: Multi-Frame Reference Storyboard (by @heygentlewhale + @ai_gezgini) -->
### Caso 10: [Referencia multiframe → Video de corte rapido](https://x.com/heygentlewhale/status/2047969137969004946) (por [@heygentlewhale](https://x.com/heygentlewhale))

Proporciona a Seedance 2.0 una imagen de storyboard con multiples fotogramas de referencia e instruyelo a seguir el orden de la secuencia. El modelo lee las posiciones de los fotogramas como senales de escena y genera una edicion de corte rapido coherente, sin necesidad de ensamblar clips manualmente.

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/storyboard_case10/input.jpg" width="280" alt="Storyboard multiframe de GPT Image 2"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/4d7af334-4e49-4de4-899e-803f72116c21" width="280" controls></video></td>
<td align="center"><video src="https://github.com/user-attachments/assets/5def7e00-6fc6-4a4e-8075-5f37cb24b84c" width="280" controls></video></td>
</tr></table>

**Pasos:**

1. Genera una imagen de storyboard multipanel en GPT Image 2 (12 fotogramas, cuadricula 3x4 o 4x3)
2. Sube el storyboard como imagen de referencia en Seedance 2.0
3. Escribe un prompt de secuenciacion que indique el numero de fotogramas y el estilo de edicion

**Prompt para GPT Image 2:**

```
Create a 12-panel storyboard grid for a [N]-second [genre] film:
- 4 columns × 3 rows, left-to-right, top-to-bottom reading order
- Each panel: [shot type] + [action description]
- Location: [setting], Time: [day/night], Mood: [atmosphere]
- Consistent character design and scene across all panels
- No text labels, no panel borders
Output as a single image.
```

**Prompt para Seedance 2.0:**

```
Follow the storyboard sequence of the 12 reference frames in image1, edited as a fast-cut memory montage.
[Describe visual style — example below:]
A nostalgic romance film set in 1990s Singapore, shot on 35mm film in Kodak Portra 800 style.
Soft grain, dreamy blur, warm highlights, and slight color shifts create a vintage cinematic atmosphere.
```

**Prompt de secuenciacion universal (via [@ai_gezgini](https://x.com/ai_gezgini/status/2047349122315805016)):**

```
Use this storyboard to generate a video, follow the scene order, keep transitions smooth,
and preserve cinematic lighting and pacing.
[Add any extra visual details you want.]
```

> [!NOTE]
> Este prompt funciona en cualquier genero: cambia la descripcion de estilo por ciencia ficcion, terror, documental o cualquier otro look. La frase clave es `follow the storyboard sequence of the [N] reference frames`, que indica a Seedance que trate las posiciones de los fotogramas como una linea de tiempo en lugar de una composicion unica.


<!-- Case 19: Storyboard-First Cost Control (by @0xbisc) -->
### Caso 19: [Control de costes con storyboard primero](https://x.com/0xbisc/status/2049100073481716076) (por [@0xbisc](https://x.com/0xbisc))

Un enfoque con mentalidad de produccion: itera primero el storyboard en GPT Image 2 (barato) y genera video solo cuando la composicion este cerrada (caro). Esto ahorra muchos creditos porque las iteraciones de video consumen entre 10x y 50x mas que las iteraciones de imagen. 298 likes / 13K vistas / 291 marcadores.

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/storyboard_case19/output.jpg" width="400" alt="Salida del flujo de storyboard primero"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/09e04d80-c0d1-4a8c-9b74-2efe474acfcd" width="400" controls></video></td>
</tr></table>

**Pasos:**

1. Genera una cuadricula de storyboard de 8 paneles con GPT Image 2
2. Revisa cada panel: regenera o edita paneles individuales hasta quedar satisfecho
3. Solo cuando el storyboard completo este cerrado, importalo en Seedance 2.0
4. Genera el video de una sola vez a partir del storyboard finalizado

**Prompt para GPT Image 2:**

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

**Prompt para Seedance 2.0:**

```
Generate video based strictly on storyboard @ image1. Follow the storyboard exactly as shown, matching each panel's composition, framing, and action. Keep perfect visual continuity with no errors or inconsistencies.
```

> [!NOTE]
> **Por que empezar por el storyboard gana en coste:** Las iteraciones de video queman creditos rapido. Con un storyboard puedes ajustar plano a plano y detectar problemas a tiempo. El paso de video se convierte en un unico render final en lugar de un costoso bucle de prueba y error. La comunidad confirma que es el flujo mas eficiente en presupuesto para secuencias largas.


## 📱 Comercial y Producto

<!-- Case 5: App MVP Demo Video (by @Shin_Engineer) -->
### Caso 5: [Video demo de MVP de app](https://x.com/Shin_Engineer/status/2047182050323812381) (por [@Shin_Engineer](https://x.com/Shin_Engineer))

Usa GPT Image 2 para generar capturas de interfaz con acabado realista de una app que aun no existe y despues animalas con Seedance 2.0 para crear una demo de producto. Publicala en TikTok o redes sociales para validar interes de mercado antes de construirla.

| Salida |
| :----: |
| <a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/app_case5/output0.jpg" width="400" alt="Captura de UI de app generada por GPT Image 2 1"></a> |

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/app_case5/output1.jpg" width="220" alt="Captura de UI de app 2"></a></td>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/app_case5/output2.jpg" width="220" alt="Captura de UI de app 3"></a></td>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/app_case5/output3.jpg" width="220" alt="Captura de UI de app 4"></a></td>
</tr></table>

**Pasos:**

1. Describe tu concepto de app y lenguaje de diseno a GPT Image 2
2. Genera de 3 a 5 capturas clave de UI (inicio, funcionalidad, perfil)
3. Ordenalas segun el flujo de usuario e importalas en Seedance 2.0
4. Exporta el video demo y publicalo para medir la reaccion del mercado

**Prompt para GPT Image 2:**

```
Design [N] UI screenshots for a "[app concept]" app:
1. [Page 1 name and description]
2. [Page 2 name and description]
3. [Page 3 name and description]
Style: [iOS/Android] native design language, [primary color] accent, [light/dark] mode.
Output as realistic app screenshots, not wireframes or mockups.
```

**Prompt para Seedance 2.0:**

```
Smooth app UI transition animation, screen tap interaction, natural interface motion, clean and modern feel, 3 seconds.
```

> [!NOTE]
> **Sustituye los marcadores entre corchetes antes de usarlo.** En el texto del video, no lo etiquetes como generado por IA: publicalo como una demo de producto y observa la reaccion real de la audiencia en los comentarios.


<!-- Case 6: 15-Second Commercial (by @ai_mitosan) -->
### Caso 6: [Comercial de 15 segundos](https://x.com/ai_mitosan/status/2047146600422846762) (por [@ai_mitosan](https://x.com/ai_mitosan))

Flujo en dos pasos: GPT Image 2 genera la imagen principal y el storyboard correspondiente, luego Seedance 2.0 anima cada clip. Ensambla con subtitulos y musica para obtener un anuncio completo de 15 segundos.

<table><tr>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/commercial_case6/input1.jpg" width="280" alt="Imagen principal de producto generada por GPT Image 2"></a></td>
<td align="center"><a href="https://evolink.ai/gpt-image-2-prompts?utm_source=github&utm_medium=picture&utm_campaign=gptimage2-x-seedance2"><img src="images/commercial_case6/input2.jpg" width="280" alt="Storyboard de GPT Image 2"></a></td>
<td align="center"><video src="https://github.com/user-attachments/assets/09ae3c57-b8fb-4323-ba76-7777541fe4a3" width="280" controls></video></td>
</tr></table>

**Pasos:**

1. Genera la imagen principal + storyboard con image2  
2. Pasalo a Seedance2.0 para convertirlo en video  

**Guia de cantidad de paneles:**

| Duracion del video | Paneles | Duracion por clip |
| :---: | :---: | :---: |
| 15 segundos | 4-5 | 3-4 segundos |
| 30 segundos | 8-10 | 3 segundos |
| 60 segundos | 15-18 | 3-4 segundos |

**Prompt para GPT Image 2:**

```
夜カフェ　深夜スイーツをテーマにした15秒CMを作るので、絵コンテを作って。 
プロの映像クリエイターによる15秒、８カット、マルチショット、ライティング重視。
```

**Prompt para Seedance 2.0:**

```
15秒、８カット、マルチショット、ライティング重視
```

<!-- PLACEHOLDER_CASE15 -->
