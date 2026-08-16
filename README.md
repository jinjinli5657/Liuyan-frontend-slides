# Liuyan Frontend Slides

> **Bilingual docs / 中英双语文档:** a toggleable **中文 / English** interactive page is available at
> **https://jinjinli5657.github.io/Liuyan-frontend-slides/** (default English).

Create zero-dependency, animation-rich HTML presentations from scratch or by converting PowerPoint files.

[//]: # (Badge line kept compact)
![Templates](https://img.shields.io/badge/templates-34-FF6B6B)
![License](https://img.shields.io/badge/license-MIT-blue)
![Stage](https://img.shields.io/badge/stage-16:9%20fixed-22c55e)

**Liuyan Frontend Slides** is a WorkBuddy skill that turns a topic, outline, or `.pptx` file into a distinctive, single-file HTML deck. It ships with **34 bold slide templates**, a fixed 16:9 stage engine, inline editing, Vercel deployment, and PDF export — all without npm, build tools, or cloud dependencies.

## Highlights

- **Zero dependencies** — every deck is one self-contained HTML file with inline CSS/JS.
- **Fixed 16:9 stage** — the 1920×1080 canvas scales uniformly on every screen (no reflow on phones).
- **34 bold templates** — curated, high-contrast design systems from neon arcade to editorial print.
- **3-preview style discovery** — before building, you see three visual style previews for your content.
- **PPTX conversion** — extract text, images, speaker notes and rebuild in any chosen style.
- **Inline editing** — press **E** or hover the top-left hotzone to edit text, drag elements, change colors, then save.
- **Deploy & export** — push to Vercel for a live link, or export a PDF with one command.
- **Reduced-motion support** — animations respect `prefers-reduced-motion`.

## Quick Start

1. Ask WorkBuddy to create a presentation (or convert a `.pptx`).
2. The skill will ask about purpose, length, content readiness, and density (speaker-led vs reading-first).
3. It generates **three style previews** so you can pick a look.
4. After you choose, the full HTML deck is generated and opened in your browser.
5. Press **E** to edit in place, then **Ctrl+S / Cmd+S** to save your changes.

```bash
# Deploy the HTML deck to a live URL
bash scripts/deploy.sh ./my-deck.html

# Export the deck to PDF
bash scripts/export-pdf.sh ./my-deck.html

# Extract content from a PowerPoint file
python scripts/extract-pptx.py ./input.pptx ./output-dir
```

## Bold Template Gallery

Each card below uses the template's real color palette. Click any image to open the repo; the previews live under `previews/`.

| ![8-Bit Orbit](previews/8-bit-orbit.png) | ![Biennale Yellow](previews/biennale-yellow.png) |
|---|---|
| **8-Bit Orbit** — Pixel-art neon arcade aesthetic on a deep navy void. | **Biennale Yellow** — Solar yellow on warm parchment with deep indigo serif and atmospheric sun-glow gradients. |

| ![BlockFrame](previews/block-frame.png) | ![Blue Professional](previews/blue-professional.png) |
|---|---|
| **BlockFrame** — Neobrutalist deck with pastel-neon color blocks and chunky black borders. | **Blue Professional** — Cream paper background with electric cobalt blue accents; clean modern professional. |

| ![Bold Poster](previews/bold-poster.png) | ![Broadside](previews/broadside.png) |
|---|---|
| **Bold Poster** — Editorial poster aesthetic with massive Shrikhand display and a single fire-engine red accent. | **Broadside** — Dark editorial canvas with a single fire orange accent and bilingual Latin/Chinese type stack. |

| ![Capsule](previews/capsule.png) | ![Cartesian](previews/cartesian.png) |
|---|---|
| **Capsule** — Modular pill-shaped cards on warm bone with a full pastel-pop palette. | **Cartesian** — Quiet warm-neutral palette with classical Playfair serifs; tasteful and unhurried. |

| ![Cobalt Grid](previews/cobalt-grid.png) | ![Coral](previews/coral.png) |
|---|---|
| **Cobalt Grid** — Electric cobalt serifs on a graph-paper canvas, anchored by stair-stepped pixel-glitch decorations and slim hairline rules. | **Coral** — Cream and coral on near-black, set in oversized Bebas Neue. |

| ![Creative Mode](previews/creative-mode.png) | ![Daisy Days](previews/daisy-days.png) |
|---|---|
| **Creative Mode** — Cream paper canvas with confident multi-color (green, pink, orange, yellow) accents and Archivo Black display. | **Daisy Days** — Cheerful pastel deck with hand-drawn daisies, stars, and rainbows. Friendly, soft, and warm. |

| ![Editorial Forest](previews/editorial-forest.png) | ![Editorial Tri-Tone](previews/editorial-tri-tone.png) |
|---|---|
| **Editorial Forest** — Forest green, dusty pink, and warm cream meet Source Serif 4 in a quiet, intentional quarterly-review deck. | **Editorial Tri-Tone** — Three-color editorial system: dusty pink, mustard cream, and deep burgundy, set in Bricolage + Instrument Serif. |

| ![Emerald Editorial](previews/emerald-editorial.png) | ![Grove](previews/grove.png) |
|---|---|
| **Emerald Editorial** — A magazine-cover business deck: emerald + navy + paper, double-rule masthead ornaments, and a bold Bodoni-style display serif. | **Grove** — Forest-green canvas with cream type, classical Playfair serifs, and a single rust accent. |

| ![Long Table](previews/long-table.png) | ![Mat](previews/mat.png) |
|---|---|
| **Long Table** — Warm cream and rust-red supper-club aesthetic with bold uppercase grotesk headlines, Fraunces serifs, and pill-shaped outlined buttons. | **Mat** — Dark sage canvas with bone paper and burnt-orange accent; mid-century modern with wood undertones. |

| ![Monochrome](previews/monochrome.png) | ![Neo-Grid Bold](previews/neo-grid-bold.png) |
|---|---|
| **Monochrome** — Ivory ledger paper with all-black type; Lora serif headlines, Jost body, no color at all. | **Neo-Grid Bold** — Editorial neo-brutalism with a single neon yellow accent on off-white paper. |

| ![People's Platform (Block & Bold)](previews/peoples-platform.png) | ![Pin & Paper](previews/pin-and-paper.png) |
|---|---|
| **People's Platform (Block & Bold)** — Activist poster energy: blue, orange, red on cream, with Alfa Slab + Caveat Brush. | **Pin & Paper** — Yellow paper with safety-pin illustrations, ink-blue handwritten Caveat, paper-grain texture. |

| ![Pink Script — After Hours](previews/pink-script.png) | ![Playful](previews/playful.png) |
|---|---|
| **Pink Script — After Hours** — Black canvas, hot pink accent, pearl-cream paper, Instrument Serif headlines: late-night editorial luxury. | **Playful** — Sun-warm peach background with Syne display: a friendly indie launch deck. |

| ![Raw Grid](previews/raw-grid.png) | ![Retro Windows](previews/retro-windows.png) |
|---|---|
| **Raw Grid** — Neo-brutalist deck with thick borders, offset shadows, and a pink/sage/ink palette. | **Retro Windows** — Windows 95 chrome: gray title bars, MS Sans Serif, pixel typography, full nostalgia. |

| ![Retro Zine](previews/retro-zine.png) | ![Sakura Chroma](previews/sakura-chroma.png) |
|---|---|
| **Retro Zine** — Beige paper with green accent and Bebas Neue + Caveat: a riso-printed zine in HTML form. | **Sakura Chroma** — Vintage Japanese cassette-package aesthetic: cream paper, diagonal rainbow ribbons, condensed bold type, JIS-style spec checkboxes. |

| ![Scatterbrain](previews/scatterbrain.png) | ![Signal](previews/signal.png) |
|---|---|
| **Scatterbrain** — Post-it inspired: pastel sticky notes, Caveat handwriting, Shrikhand and Zilla Slab type stack. | **Signal** — Deep navy canvas with bone paper and a single muted-gold accent; institutional with quiet weight. |

| ![Soft Editorial](previews/soft-editorial.png) | ![Stencil & Tablet](previews/stencil-tablet.png) |
|---|---|
| **Soft Editorial** — Cormorant Garamond serif on warm paper with sage, blush, and lemon accents. | **Stencil & Tablet** — Bone paper with stencil-cut headlines and a six-color earth palette: archaeology meets brand. |

| ![Studio](previews/studio.png) | ![Vellum](previews/vellum.png) |
|---|---|
| **Studio** — Black canvas with electric-yellow type; high-voltage design studio aesthetic. | **Vellum** — Deep navy canvas with warm-yellow Cormorant serifs and a single dusty teal accent. A quiet, scholarly aesthetic. |

## Template Reference

| Template | Scheme | Formality | Density | Best for |
|---|---|---|---|---|
| 8-Bit Orbit | `dark` | low | medium | Anything that should feel like a CRT screen at 2am: cyberpunk, gaming, web… |
| Biennale Yellow | `light` | high | medium | Anything that should feel like an art-biennale poster or a museum's annual… |
| BlockFrame | `light` | medium-low | high | Anything that should feel pop-graphic and design-led: indie SaaS launches,… |
| Blue Professional | `light` | medium-high | medium | Anything that should feel modern-considered and lightly authoritative: B2B… |
| Bold Poster | `light` | medium | low | Anything that should land like a magazine cover: brand manifestos, founder… |
| Broadside | `dark` | medium-high | medium | Anything that should land like a broadside newspaper headline: brand manif… |
| Capsule | `light` | medium-low | medium | Anything that should feel modular, modern, and a little Y2K: lifestyle bra… |
| Cartesian | `light` | high | low | Anything that should feel quiet, considered, and grown-up: investment thes… |
| Cobalt Grid | `light` | high | medium | Anything that should feel like a quietly serious design / research bulleti… |
| Coral | `mixed` | medium | medium | Anything that should feel warm-graphic and editorial: fashion, beauty, fit… |
| Creative Mode | `light` | medium | medium-high | Anything that should feel design-led and confident: creative agency pitche… |
| Daisy Days | `light` | low | medium | Anything that should feel friendly, soft, and joyful: educational content,… |
| Editorial Forest | `mixed` | medium | medium | Anything that should feel like a considered editorial — quarterly reviews,… |
| Editorial Tri-Tone | `mixed` | medium-high | medium | Anything that should feel like a fashion-magazine spread: editorial pitche… |
| Emerald Editorial | `mixed` | medium-high | medium | Anything that should feel like the front of a serious magazine, including… |
| Grove | `mixed` | medium-high | medium | Anything that should feel organic, considered, and grown-up: sustainabilit… |
| Long Table | `light` | medium | medium | Anything that should feel like a warm, intimate, modern hospitality / comm… |
| Mat | `mixed` | medium | medium | Anything that should feel mid-century, tactile, and intentional: design st… |
| Monochrome | `light` | high | high | Anything that should feel like a hand-typeset ledger: user research synthe… |
| Neo-Grid Bold | `light` | medium | high | Anything that should feel confident and editorial-graphic: design-led pitc… |
| People's Platform (Block & Bold) | `light` | medium-low | medium-high | Anything that should feel honest, loud, and graphic: cultural commentary,… |
| Pin & Paper | `light` | medium | medium | Anything that should feel hand-crafted, warm, and literary: qualitative re… |
| Pink Script — After Hours | `dark` | medium-high | low | Anything that should feel nocturnal, intentional, and a little luxe: fashi… |
| Playful | `light` | low | medium | Anything that should feel warm, indie, and approachable: creator portfolio… |
| Raw Grid | `light` | medium-low | high | Anything that should feel direct and graphic-confident: founder pitches, a… |
| Retro Windows | `light` | low | medium | Anything that should feel knowingly nostalgic: retro gaming, Y2K-aesthetic… |
| Retro Zine | `light` | medium-low | medium | Anything that should feel printed, lo-fi, and crafted: indie zines and pub… |
| Sakura Chroma | `light` | low | medium | Anything that should feel like a vintage Japanese cassette package or a TD… |
| Scatterbrain | `light` | low | high | Anything that should feel like a designer's whiteboard: brainstorms, works… |
| Signal | `mixed` | high | high | Anything that should feel weighty, considered, and credibly institutional:… |
| Soft Editorial | `light` | high | low | Anything that should feel literary, elegant, and unhurried: editorial feat… |
| Stencil & Tablet | `light` | medium-high | medium | Anything that should feel archival, tactile, and weighty-graphic: museum a… |
| Studio | `dark` | medium | medium | Anything that should feel electric and design-led: studio credentials, cre… |
| Vellum | `dark` | high | low | Anything that should feel scholarly, literary, and quietly intelligent: re… |

## How it works

The skill follows a six-phase workflow:

1. **Detect mode** — new deck, PPTX conversion, or enhancement of an existing HTML deck.
2. **Content discovery** — gather purpose, length, content source, and density mode.
3. **Style discovery** — generate three visual previews (1 safe preset + 1 bold template + 1 wildcard) and let you pick.
4. **Generate presentation** — produce the full HTML deck using the selected style, real content, and fixed-stage rules.
5. **Delivery** — open the file, explain navigation and editing.
6. **Share & export** — optional Vercel deploy or PDF export.

## File Structure

```
Liuyan-frontend-slides/
├── SKILL.md                      # Skill metadata and full generation rules
├── README.md                     # English README
├── index.html                    # Bilingual interactive doc (中文 / English toggle)
├── build_index.py                # Re-generate the bilingual index.html
├── STYLE_PRESETS.md              # 12 safe, reusable visual presets
├── animation-patterns.md         # CSS/JS animation snippets and feeling guide
├── html-template.md              # HTML architecture, JS features, code standards
├── viewport-base.css             # Mandatory fixed-stage CSS (copied into every deck)
├── gen_previews.py               # Re-generate the style-demo gallery images
├── build_readme.py               # Re-generate this README from selection-index.json
├── previews/                     # 34 bold-template style demo images
├── scripts/
│   ├── extract-pptx.py           # Parse PPTX into text, images, and notes
│   ├── deploy.sh                 # Deploy to Vercel
│   └── export-pdf.sh             # Export HTML deck to PDF
└── bold-template-pack/
    ├── selection-index.json      # Compact metadata for all 34 bold templates
    └── templates/<slug>/
            ├── design.md         # Full design-system recipe
            └── preview.md        # Lightweight title-slide preview notes
```

## Scripts

### `scripts/deploy.sh <path>`
Uploads a folder (with `index.html`) or a single HTML file to Vercel. If you have images alongside the deck, prefer deploying the whole folder so relative paths resolve.

### `scripts/export-pdf.sh <path-to-html> [output.pdf]`
Opens the deck in a headless 1920×1080 browser, screenshots every `.slide`, and stitches them into a PDF. Add `--compact` to render at 1280×720 for a smaller file.

### `scripts/extract-pptx.py <input.pptx> <output-dir>`
Pulls text, layout structure, and embedded images out of a PowerPoint file so the deck can be rebuilt in any Liuyan style.

## Regenerating the Gallery

After adding or editing a template:

```bash
python gen_previews.py      # re-render previews/*.png
python build_readme.py      # re-render README.md
```

## License

[MIT License](./LICENSE) © 2026 jinjinli5657
