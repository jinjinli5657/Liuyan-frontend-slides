#!/usr/bin/env python3
"""Build README.md for Liuyan-frontend-slides from selection-index + previews."""
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))
idx = json.load(open(os.path.join(ROOT, "bold-template-pack", "selection-index.json"), encoding="utf-8"))
tpls = idx["templates"]

def trunc(s, n=75):
    return s if len(s) <= n else s[:n-1].rstrip() + "…"

gallery_rows = []
for i in range(0, len(tpls), 2):
    a = tpls[i]
    b = tpls[i+1] if i+1 < len(tpls) else None
    img_a = f"previews/{a['slug']}.png"
    cap_a = f"**{a['name']}** — {a['tagline']}"
    if b:
        img_b = f"previews/{b['slug']}.png"
        cap_b = f"**{b['name']}** — {b['tagline']}"
        gallery_rows.append(f"| ![{a['name']}]({img_a}) | ![{b['name']}]({img_b}) |\n|---|---|\n| {cap_a} | {cap_b} |")
    else:
        gallery_rows.append(f"| ![{a['name']}]({img_a}) |\n|---|\n| {cap_a} |")

gallery = "\n\n".join(gallery_rows)

ref_rows = "\n".join(
    f"| {t['name']} | `{t['scheme']}` | {t.get('formality','—')} | {t.get('density','—')} | {trunc(t.get('best_for',''))} |"
    for t in tpls
)

readme = f"""# Liuyan Frontend Slides

Create zero-dependency, animation-rich HTML presentations from scratch or by converting PowerPoint files.

[//]: # (Badge line kept compact)
![Templates](https://img.shields.io/badge/templates-{len(tpls)}-FF6B6B)
![License](https://img.shields.io/badge/license-MIT-blue)
![Stage](https://img.shields.io/badge/stage-16:9%20fixed-22c55e)

**Liuyan Frontend Slides** is a WorkBuddy skill that turns a topic, outline, or `.pptx` file into a distinctive, single-file HTML deck. It ships with **{len(tpls)} bold slide templates**, a fixed 16:9 stage engine, inline editing, Vercel deployment, and PDF export — all without npm, build tools, or cloud dependencies.

## Highlights

- **Zero dependencies** — every deck is one self-contained HTML file with inline CSS/JS.
- **Fixed 16:9 stage** — the 1920×1080 canvas scales uniformly on every screen (no reflow on phones).
- **{len(tpls)} bold templates** — curated, high-contrast design systems from neon arcade to editorial print.
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

{gallery}

## Template Reference

| Template | Scheme | Formality | Density | Best for |
|---|---|---|---|---|
{ref_rows}

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
├── README.md                     # This file
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
"""

open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8").write(readme)
print("README.md written")
