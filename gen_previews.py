#!/usr/bin/env python3
"""Generate a representative 16:9 style-demo PNG for every bold template.

Reads each template's real palette from design.md and its scheme/name/tagline
from selection-index.json, then renders a compact "first slide" thumbnail that
conveys the look & feel (background, accent, typography mood, color swatches).
"""
import json, re, os, glob
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(ROOT, "bold-template-pack", "templates")
INDEX = os.path.join(ROOT, "bold-template-pack", "selection-index.json")
OUT = os.path.join(ROOT, "previews")
os.makedirs(OUT, exist_ok=True)

W, H = 1280, 720
LATIN_BOLD = "/System/Library/Fonts/Supplemental/Arial Black.ttf"
LATIN = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
CJK = "/System/Library/Fonts/Hiragino Sans GB.ttc"

def font(path, size, idx=0):
    try:
        if path.endswith(".ttc"):
            return ImageFont.truetype(path, size, index=idx)
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()

def hex2rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def lum(rgb):
    r, g, b = [c / 255 for c in rgb]
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def sat(rgb):
    r, g, b = [c / 255 for c in rgb]
    mx, mn = max(r, g, b), min(r, g, b)
    if mx == 0:
        return 0
    return (mx - mn) / mx

def contrast(a, b):
    la, lb = lum(a) + 0.05, lum(b) + 0.05
    return max(la, lb) / min(la, lb)

def parse_colors(dm_path):
    txt = open(dm_path, encoding="utf-8").read()
    pairs = re.findall(r'^\s*([a-z0-9\-]+):\s*"(#[0-9A-Fa-f]{6})"', txt, re.M)
    return [(k, hex2rgb(v)) for k, v in pairs]

def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def pick(bg, fg, colors):
    others = [c for c in colors if contrast(c, bg) > 1.25 and contrast(c, fg) > 1.15]
    # most vivid first
    others.sort(key=lambda c: sat(c) * 0.7 + (1 - lum(c)) * 0.3, reverse=True)
    return others[:4]

def render(slug, name, scheme, tagline, colors):
    # colors is a list of (label, rgb_tuple)
    rgb_list = [c for _, c in colors]
    # bg / fg by scheme
    sorted_by_lum = sorted(rgb_list, key=lum)
    if scheme == "dark":
        bg = sorted_by_lum[0]
        fg = max(rgb_list, key=lambda c: (contrast(c, bg), sat(c)))
        if lum(fg) < 0.5:
            fg = (235, 235, 235)
    else:
        bg = sorted_by_lum[-1]
        fg = min(rgb_list, key=lambda c: (lum(c), -sat(c)))
        if lum(fg) > 0.5:
            fg = (20, 20, 20)
    accents = pick(bg, fg, rgb_list)
    title_col = accents[0] if accents else fg
    accent2 = accents[1] if len(accents) > 1 else title_col

    img = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(img)

    # subtle background texture
    if scheme == "dark":
        for x in range(0, W, 48):
            d.line([(x, 0), (x, H)], fill=(255, 255, 255), width=1)
        for y in range(0, H, 48):
            d.line([(0, y), (W, y)], fill=(255, 255, 255), width=1)
        d.rectangle([0, 0, W, H], outline=None)
        img = Image.blend(img, Image.new("RGB", (W, H), bg), 0.86)  # fade grid
        d = ImageDraw.Draw(img)
        # neon squares
        import random
        random.seed(hash(slug) & 0xffffffff)
        for _ in range(5):
            s = random.choice([8, 12, 16])
            x = random.randint(40, W - 60)
            y = random.randint(40, H - 200)
            d.rectangle([x, y, x + s, y + s], fill=random.choice(accents) if accents else None)
    else:
        # soft accent block corner
        d.rectangle([0, 0, 26, H], fill=accent2)
        d.rectangle([W - 26, 0, W, H], fill=accent2)
        d.rectangle([40, 40, W - 40, 80], outline=accent2, width=4)

    # kicker pill
    kicker = f"{scheme.upper()}  ·  {name.split()[0].upper()}"
    kf = font(LATIN, 22)
    kw = d.textlength(kicker, font=kf) + 36
    d.rounded_rectangle([60, 70, 60 + kw, 70 + 46], radius=23, fill=title_col if scheme == "light" else accent2)
    d.text((60 + 18, 70 + 11), kicker, font=kf, fill=bg if scheme == "light" else bg)

    # title
    tf = font(LATIN_BOLD, 74)
    # glow / shadow
    d.text((63, 163), name, font=tf, fill=accent2 if scheme == "dark" else (0, 0, 0))
    d.text((60, 160), name, font=tf, fill=title_col)

    # tagline
    bf = font(LATIN, 26)
    lines = wrap(d, tagline, bf, W - 160)
    y = 300
    for ln in lines[:3]:
        d.text((62, y), ln, font=bf, fill=tuple(int(c * 0.82 + 30) for c in fg))
        y += 38

    # swatches
    n = len(colors)
    pad = 60
    sw = (W - pad * 2) / n
    y0 = H - 150
    for i, (label, c) in enumerate(colors):
        x = pad + i * sw
        d.rounded_rectangle([x + 4, y0, x + sw - 4, y0 + 90], radius=8, fill=c,
                            outline=(0, 0, 0) if lum(c) > 0.8 else None)
        hf = font(LATIN, 16)
        d.text((x + 10, y0 + 98), "#%02X%02X%02X" % c, font=hf, fill=fg)

    out = os.path.join(OUT, f"{slug}.png")
    img.save(out, optimize=True)
    return out

def main():
    idx = json.load(open(INDEX, encoding="utf-8"))
    done = 0
    for t in idx["templates"]:
        slug = t["slug"]
        dm = os.path.join(TEMPLATES_DIR, slug, "design.md")
        colors = parse_colors(dm)
        if not colors:
            continue
        render(slug, t.get("name", slug), t.get("scheme", "light"),
               t.get("tagline", ""), colors)
        done += 1
    print(f"generated {done} preview images -> {OUT}")

if __name__ == "__main__":
    main()
