# -*- coding: utf-8 -*-
import json, io, html

SRC = "bold-template-pack/selection-index.json"
OUT = "index.html"

d = json.load(open(SRC, encoding="utf-8"))
tpls = d["templates"]  # 34

# Chinese tagline translations (caption for gallery)
ZH_TAG = {
    "8-bit-orbit": "深蓝虚空上的像素霓虹街机风",
    "biennale-yellow": "暖羊皮纸上的太阳黄 + 深靛蓝衬线 + 光晕渐变",
    "block-frame": "新野兽派：粉彩霓虹色块 + 粗黑边框",
    "blue-professional": "奶白纸面 + 电光钴蓝点缀，干净现代",
    "bold-poster": "杂志海报感：超大 Shrikhand 标题 + 单一火红",
    "broadside": "深色编辑画布 + 火橙点缀 + 中英双语字体",
    "capsule": "暖骨色底上的药丸形卡片 + 全套粉彩",
    "cartesian": "安静暖中性色 + 古典 Playfair 衬线，雅致从容",
    "cobalt-grid": "电光钴蓝衬线 + 方格纸 + 像素故障装饰",
    "coral": "近黑底上的奶油与珊瑚色，超大 Bebas Neue",
    "creative-mode": "奶白纸面 + 多彩（绿粉橙黄）点缀 + Archivo Black",
    "daisy-days": "手绘雏菊星星彩虹的粉彩卡，友好温暖",
    "editorial-forest": "森林绿 + 灰粉 + 暖奶油，季度复盘风",
    "editorial-tri-tone": "三色编辑系统：灰粉 + 芥末奶油 + 深酒红",
    "emerald-editorial": "杂志封面商务风：祖母绿 + 藏青 + 纸，双线刊头",
    "grove": "森林绿画布 + 奶油字 + 古典 Playfair + 锈红点缀",
    "long-table": "暖奶油 + 锈红晚宴俱乐部风，Fraunces 衬线",
    "mat": "深鼠尾草绿 + 骨色纸 + 焦橙点缀，中世纪现代",
    "monochrome": "象牙账本纸 + 全黑字，Lora 标题，无彩色",
    "neo-grid-bold": "新野兽派编辑风，米白纸上单一霓虹黄",
    "peoples-platform": "行动主义海报能量：蓝橙红 + Alfa Slab",
    "pin-and-paper": "黄纸 + 别针插画 + 墨水蓝手写 Caveat",
    "pink-script": "黑底 + 亮粉点缀 + 珍珠奶油纸，深夜编辑奢华",
    "playful": "阳光蜜桃底 + Syne 字体，友好独立发布风",
    "raw-grid": "新野兽派：粗边框 + 偏移阴影 + 粉/鼠尾草/墨色",
    "retro-windows": "Win95 窗口风：灰标题栏 + MS Sans Serif",
    "retro-zine": "米色纸 + 绿色点缀 + Bea Sas Neue，riso 印刷 zine",
    "sakura-chroma": "复古日式卡带包装：奶油纸 + 斜向彩虹条",
    "scatterbrain": "便利贴风：粉彩贴纸 + Caveat 手写 + Shrikhand",
    "signal": "深藏青画布 + 骨色纸 + 单一暗金点缀，沉稳机构感",
    "soft-editorial": "暖纸上 Cormorant 衬线 + 鼠尾草/胭脂/柠檬",
    "stencil-tablet": "骨色纸 + 模切标题 + 六色大地色板，考古亦品牌",
    "studio": "黑底 + 电光黄字，高电压设计工作室风",
    "vellum": "深藏青画布 + 暖黄 Cormorant 衬线 + 灰青点缀，安静学者气",
}

# Chinese best_for (concise) for reference table
ZH_BEST = {
    "8-bit-orbit": "适合像凌晨 2 点的 CRT 屏幕：赛博朋克、游戏、web3、独立开发工具、黑客松。",
    "biennale-yellow": "适合艺术双年展海报、美术馆年报一类的内容。",
    "block-frame": "适合波普图形、设计主导：独立 SaaS 发布、创意提案。",
    "blue-professional": "适合现代克制、略带权威：B2B、企业汇报。",
    "bold-poster": "适合像杂志封面一样落地：品牌宣言、创始人叙事。",
    "broadside": "适合像报纸头条一样落地：品牌宣言、重磅发布。",
    "capsule": "适合模块化、现代、带点 Y2K：生活方式品牌、产品介绍。",
    "cartesian": "适合安静、克制、成熟：投资报告、研究综述。",
    "cobalt-grid": "适合安静而认真的设计 / 研究通报。",
    "coral": "适合温暖图形、编辑感：时尚、美妆、健身。",
    "creative-mode": "适合设计主导、自信：创意机构提案、作品集。",
    "daisy-days": "适合友好、柔软、欢乐：教育内容、活动宣传。",
    "editorial-forest": "适合有想法的编辑风：季度复盘、品牌内刊。",
    "editorial-tri-tone": "适合像时尚杂志跨页：编辑提案、品牌故事。",
    "emerald-editorial": "适合像严肃杂志封面：企业内刊、行业报告。",
    "grove": "适合有机、克制、成熟：可持续、自然品牌。",
    "long-table": "适合温暖、亲密、现代：餐饮 / 社区品牌。",
    "mat": "适合中世纪、有触感、有意为之：设计工作室、品牌。",
    "monochrome": "适合像手工排版的账本：用户研究综述、年报。",
    "neo-grid-bold": "适合自信、编辑图形感：设计主导提案。",
    "peoples-platform": "适合真诚、响亮、图形化：文化评论、社群运动。",
    "pin-and-paper": "适合手作、温暖、文学：定性研究、随笔。",
    "pink-script": "适合夜间、有意为之、略奢华：时尚、生活方式。",
    "playful": "适合温暖、独立、亲和：创作者作品集、产品发布。",
    "raw-grid": "适合直接、图形自信：创始人提案、活动。",
    "retro-windows": "适合心照不宣的怀旧：复古游戏、Y2K 美学。",
    "retro-zine": "适合印刷、低保真、手工感：独立 zine、出版物。",
    "sakura-chroma": "适合复古日式卡带包装、TDD 一类。",
    "scatterbrain": "适合设计师白板：头脑风暴、工作坊。",
    "signal": "适合有分量、克制、可信赖机构：政策、白皮书。",
    "soft-editorial": "适合文学、优雅、从容：编辑特稿、品牌故事。",
    "stencil-tablet": "适合档案感、有触感、图形厚重：博物馆、考古。",
    "studio": "适合电力十足、设计主导：工作室作品、创意提案。",
    "vellum": "适合学者气、文学、安静聪慧：研究、长文。",
}

SCH_ZH = {"dark": "深色", "light": "浅色", "mixed": "混合"}
FORM_ZH = {"low": "低", "medium-low": "中低", "medium": "中", "medium-high": "中高", "high": "高"}
DENS_ZH = {"low": "低", "medium": "中", "high": "高"}

def esc(s): return html.escape(str(s))

# ---- gallery (2-col table) ----
rows = []
for i in range(0, len(tpls), 2):
    pair = tpls[i:i+2]
    cells = []
    for t in pair:
        slug = t["slug"]
        name = esc(t["name"])
        cap_en = esc(t["tagline"].rstrip("."))
        cap_zh = esc(ZH_TAG.get(slug, ""))
        cells.append(
            f'''<td><img loading="lazy" src="previews/{esc(slug)}.png" alt="{name}">
<div class="cap" data-lang="en"><b>{name}</b> — {cap_en}</div>
<div class="cap" data-lang="zh"><b>{name}</b> — {cap_zh}</div></td>'''
        )
    rows.append("<tr>" + "".join(cells) + "</tr>")
gallery_html = "\n".join(rows)

# ---- reference tables (separate EN / ZH tables, no data-lang on td) ----
ref_en, ref_zh = [], []
for t in tpls:
    slug = t["slug"]
    name = esc(t["name"])
    scheme = t["scheme"]
    form = t["formality"]
    dens = t["density"]
    best_en = esc(t.get("best_for", ""))
    best_zh = esc(ZH_BEST.get(slug, best_en))
    ref_en.append(
        f"<tr><td><b>{name}</b></td>"
        f"<td><code>{esc(scheme)}</code></td>"
        f"<td>{esc(form)}</td>"
        f"<td>{esc(dens)}</td>"
        f"<td>{best_en}</td></tr>"
    )
    ref_zh.append(
        f"<tr><td><b>{name}</b></td>"
        f"<td>{SCH_ZH.get(scheme,scheme)}</td>"
        f"<td>{FORM_ZH.get(form,form)}</td>"
        f"<td>{DENS_ZH.get(dens,dens)}</td>"
        f"<td>{best_zh}</td></tr>"
    )
ref_en_html = "\n".join(ref_en)
ref_zh_html = "\n".join(ref_zh)

HTML = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Liuyan Frontend Slides · 流宴前端幻灯片</title>
<style>
  :root{{
    --bg:#ffffff; --text:#23272e; --muted:#6b7280; --accent:#ff5a5f;
    --line:#e8e8ec; --panel:#f7f7f9; --ink:#1a1a2e;
  }}
  *{{box-sizing:border-box}}
  body{{margin:0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Hiragino Sans GB","STHeiti","Microsoft YaHei",sans-serif;
    background:var(--bg);color:var(--text);line-height:1.7;font-size:16px}}
  .topbar{{position:sticky;top:0;z-index:10;display:flex;align-items:center;justify-content:space-between;
    gap:12px;padding:14px 20px;background:rgba(255,255,255,.92);backdrop-filter:blur(8px);
    border-bottom:1px solid var(--line)}}
  .brand{{font-weight:700;color:var(--ink);font-size:15px;white-space:nowrap}}
  .brand small{{display:block;font-weight:400;color:var(--muted);font-size:12px}}
  .lang-switch{{display:flex;border:1px solid var(--accent);border-radius:999px;overflow:hidden}}
  .lang-switch button{{border:0;background:transparent;color:var(--ink);padding:7px 16px;font-size:14px;cursor:pointer;font-weight:600}}
  .lang-switch button.active{{background:var(--accent);color:#fff}}
  .wrap{{max-width:920px;margin:0 auto;padding:32px 20px 80px}}
  h1{{font-size:30px;margin:.2em 0 .1em;color:var(--ink)}}
  h2{{font-size:22px;margin:2em 0 .6em;color:var(--ink);border-left:4px solid var(--accent);padding-left:10px}}
  h3{{font-size:17px;margin:1.2em 0 .4em}}
  p{{margin:.6em 0}}
  a{{color:var(--accent);text-decoration:none;border-bottom:1px solid rgba(255,90,95,.4)}}
  a:hover{{color:#e0474b}}
  blockquote{{margin:1em 0;padding:12px 16px;background:var(--panel);border-left:4px solid var(--accent);border-radius:6px;color:var(--muted)}}
  code{{background:var(--panel);padding:2px 6px;border-radius:4px;font-size:14px;font-family:"SF Mono",Menlo,Consolas,monospace}}
  pre{{background:#1f2933;color:#e6e6e6;padding:16px;overflow:auto;border-radius:8px;font-size:13.5px;line-height:1.5}}
  pre code{{background:transparent;color:inherit;padding:0}}
  table{{border-collapse:collapse;width:100%;margin:1em 0;font-size:14px}}
  th,td{{border:1px solid var(--line);padding:8px 10px;text-align:left;vertical-align:top}}
  th{{background:var(--panel);color:var(--ink)}}
  .gallery{{border:0;table-layout:fixed}}
  .gallery td{{border:0;width:50%;padding:8px 10px;vertical-align:top}}
  .gallery img{{width:100%;border:1px solid var(--line);border-radius:8px}}
  .gallery .cap{{font-size:12.5px;color:var(--muted);margin-top:6px}}
  .hero{{background:linear-gradient(135deg,#1a1a2e,#3a2a4a);color:#fff;border-radius:12px;padding:22px 24px;margin-bottom:8px}}
  .hero h1{{color:#fff}}
  .hero .coral{{color:#ff8a8d}}
  .hero p{{color:#dfe3ec}}
  footer{{margin-top:3em;border-top:1px solid var(--line);padding-top:1.2em;color:var(--muted);font-size:14px}}
  [data-lang]{{display:none}}
  body.lang-zh [data-lang="zh"]{{display:block}}
  body.lang-en [data-lang="en"]{{display:block}}
  /* inline spans */
  body.lang-zh .i-zh{{display:inline}}
  body.lang-en .i-zh{{display:none}}
</style>
</head>
<body class="lang-en">
<div class="topbar">
  <div class="brand">Liuyan Frontend Slides<small>流宴前端幻灯片 · 动画丰富的 HTML 演示生成器</small></div>
  <div class="lang-switch">
    <button id="btn-zh" onclick="setLang('zh')">中文</button>
    <button id="btn-en" class="active" onclick="setLang('en')">English</button>
  </div>
</div>

<div class="wrap">

  <!-- HERO -->
  <div class="hero">
    <div data-lang="en"><h1>Liuyan Frontend Slides</h1>
      <p>Create zero-dependency, animation-rich HTML presentations from scratch or by converting PowerPoint files.</p></div>
    <div data-lang="zh"><h1>流宴前端幻灯片</h1>
      <p>从零开始、或把 PowerPoint 转成 <span class="coral">零依赖、动画丰富</span> 的单文件 HTML 演示。</p></div>
  </div>

  <!-- SKILL NOTE -->
  <div data-lang="en"><blockquote>A WorkBuddy / CodeBuddy Skill: it turns a topic, outline, or <code>.pptx</code> into a distinctive single-file HTML deck — <b>34 bold slide templates</b>, a fixed 16:9 stage, inline editing, Vercel deploy, and PDF export, with no npm, build tools, or cloud dependencies.</blockquote></div>
  <div data-lang="zh"><blockquote>WorkBuddy / CodeBuddy 的 Skill：把主题、大纲或 <code>.pptx</code> 转成独特的单文件 HTML 演示——<b>34 套 bold 幻灯片模板</b>、固定的 16:9 舞台、内联编辑、Vercel 部署、PDF 导出，无需 npm、构建工具或云依赖。</blockquote></div>

  <!-- HIGHLIGHTS -->
  <h2 data-lang="en">Highlights</h2>
  <h2 data-lang="zh">功能亮点</h2>
  <div data-lang="en">
    <ul>
      <li><b>Zero dependencies</b> — every deck is one self-contained HTML file with inline CSS/JS.</li>
      <li><b>Fixed 16:9 stage</b> — the 1920×1080 canvas scales uniformly on every screen (no reflow on phones).</li>
      <li><b>34 bold templates</b> — curated, high-contrast design systems from neon arcade to editorial print.</li>
      <li><b>3-preview style discovery</b> — before building, you see three visual style previews for your content.</li>
      <li><b>PPTX conversion</b> — extract text, images, speaker notes and rebuild in any chosen style.</li>
      <li><b>Inline editing</b> — press <b>E</b> or hover the top-left hotzone to edit text, drag elements, change colors, then save.</li>
      <li><b>Deploy &amp; export</b> — push to Vercel for a live link, or export a PDF with one command.</li>
      <li><b>Reduced-motion support</b> — animations respect <code>prefers-reduced-motion</code>.</li>
    </ul>
  </div>
  <div data-lang="zh">
    <ul>
      <li><b>零依赖</b>——每套演示都是内联 CSS/JS 的自包含 HTML 单文件。</li>
      <li><b>固定 16:9 舞台</b>——1920×1080 画布在各屏幕等比缩放（手机上不重排）。</li>
      <li><b>34 套 bold 模板</b>——从霓虹街机到编辑印刷的高对比设计系统。</li>
      <li><b>三预览风格探索</b>——生成前先看三种视觉风格预览。</li>
      <li><b>PPTX 转换</b>——抽取文字、图片、演讲备注，用任意风格重建。</li>
      <li><b>内联编辑</b>——按 <b>E</b> 或悬停左上热区即可改字、拖元素、换色，然后保存。</li>
      <li><b>部署 &amp; 导出</b>——一键推到 Vercel 拿在线链接，或导出 PDF。</li>
      <li><b>减弱动效支持</b>——动画尊重 <code>prefers-reduced-motion</code>。</li>
    </ul>
  </div>

  <!-- QUICK START -->
  <h2 data-lang="en">Quick Start</h2>
  <h2 data-lang="zh">快速开始</h2>
  <div data-lang="en">
    <ol>
      <li>Ask WorkBuddy to create a presentation (or convert a <code>.pptx</code>).</li>
      <li>The skill asks about purpose, length, content readiness, and density (speaker-led vs reading-first).</li>
      <li>It generates <b>three style previews</b> so you can pick a look.</li>
      <li>After you choose, the full HTML deck is generated and opened in your browser.</li>
      <li>Press <b>E</b> to edit in place, then <b>Ctrl+S / Cmd+S</b> to save.</li>
    </ol>
    <pre><code># Deploy the HTML deck to a live URL
bash scripts/deploy.sh ./my-deck.html

# Export the deck to PDF
bash scripts/export-pdf.sh ./my-deck.html

# Extract content from a PowerPoint file
python scripts/extract-pptx.py ./input.pptx ./output-dir</code></pre>
  </div>
  <div data-lang="zh">
    <ol>
      <li>让 WorkBuddy 生成一套演示（或转换 <code>.pptx</code>）。</li>
      <li>Skill 会询问用途、长度、内容就绪度、密度（演讲主导 vs 阅读主导）。</li>
      <li>它会生成 <b>三种风格预览</b>，供你挑一个样子。</li>
      <li>选完后生成完整 HTML 演示并在浏览器打开。</li>
      <li>按 <b>E</b> 就地编辑，再按 <b>Ctrl+S / Cmd+S</b> 保存。</li>
    </ol>
    <pre><code># 把 HTML 演示部署成在线链接
bash scripts/deploy.sh ./my-deck.html

# 导出 PDF
bash scripts/export-pdf.sh ./my-deck.html

# 从 PowerPoint 抽取内容
python scripts/extract-pptx.py ./input.pptx ./output-dir</code></pre>
  </div>

  <!-- GALLERY -->
  <h2 data-lang="en">Bold Template Gallery (34 sets)</h2>
  <h2 data-lang="zh">Bold 模板样式画廊（34 套）</h2>
  <div data-lang="en"><p>Each card uses the template's real color palette (rendered from its <code>design.md</code>). Click an image to open the repo; the source files live under <code>previews/</code>.</p></div>
  <div data-lang="zh"><p>每张图都使用模板的真实配色（从 <code>design.md</code> 渲染）。点图打开仓库；源文件在 <code>previews/</code> 下。</p></div>

  <table class="gallery">
{gallery_html}
  </table>

  <!-- REFERENCE -->
  <h2 data-lang="en">Template Reference</h2>
  <h2 data-lang="zh">模板参考表</h2>
  <div data-lang="en">
    <table>
      <tr><th>Template</th><th>Scheme</th><th>Formality</th><th>Density</th><th>Best for</th></tr>
{ref_en_html}
    </table>
  </div>
  <div data-lang="zh">
    <table>
      <tr><th>模板</th><th>明度</th><th>正式度</th><th>密度</th><th>适合场景</th></tr>
{ref_zh_html}
    </table>
  </div>

  <!-- HOW IT WORKS -->
  <h2 data-lang="en">How it works</h2>
  <h2 data-lang="zh">工作流程</h2>
  <div data-lang="en"><p>The skill follows a six-phase workflow:</p>
    <ol>
      <li><b>Detect mode</b> — new deck, PPTX conversion, or enhancement of an existing HTML deck.</li>
      <li><b>Content discovery</b> — gather purpose, length, content source, and density mode.</li>
      <li><b>Style discovery</b> — generate three visual previews (1 safe preset + 1 bold template + 1 wildcard) and let you pick.</li>
      <li><b>Generate presentation</b> — produce the full HTML deck using the selected style, real content, and fixed-stage rules.</li>
      <li><b>Delivery</b> — open the file, explain navigation and editing.</li>
      <li><b>Share &amp; export</b> — optional Vercel deploy or PDF export.</li>
    </ol>
  </div>
  <div data-lang="zh"><p>Skill 按六个阶段运作：</p>
    <ol>
      <li><b>识别模式</b>——新建演示、转换 PPTX，或增强已有 HTML 演示。</li>
      <li><b>内容探询</b>——收集用途、长度、内容来源、密度模式。</li>
      <li><b>风格探索</b>——生成三种视觉预览（1 个稳妥预设 + 1 个 bold 模板 + 1 个开放项）让你选。</li>
      <li><b>生成演示</b>——用所选风格、真实内容、固定舞台规则产出完整 HTML。</li>
      <li><b>交付</b>——打开文件，讲解导航与编辑。</li>
      <li><b>分享 &amp; 导出</b>——可选的 Vercel 部署或 PDF 导出。</li>
    </ol>
  </div>

  <!-- FILE STRUCTURE -->
  <h2 data-lang="en">File Structure</h2>
  <h2 data-lang="zh">文件结构</h2>
  <pre><code>Liuyan-frontend-slides/
├── SKILL.md                      # Skill metadata and full generation rules
├── README.md                     # English README
├── index.html                    # Bilingual interactive doc (this page)
├── LICENSE                       # MIT License
├── gen_previews.py               # Re-generate the style-demo gallery images
├── build_readme.py               # Re-generate README.md
├── build_index.py                # Re-generate this bilingual index.html
├── previews/                     # 34 bold-template style demo images
├── scripts/
│   ├── extract-pptx.py           # Parse PPTX into text, images, and notes
│   ├── deploy.sh                 # Deploy to Vercel
│   └── export-pdf.sh             # Export HTML deck to PDF
└── bold-template-pack/
    ├── selection-index.json      # Compact metadata for all 34 bold templates
    └── templates/&lt;slug&gt;/
            ├── design.md         # Full design-system recipe
            └── preview.md        # Lightweight title-slide preview notes</code></pre>

  <!-- SCRIPTS -->
  <h2 data-lang="en">Scripts</h2>
  <h2 data-lang="zh">脚本说明</h2>
  <div data-lang="en">
    <h3><code>scripts/deploy.sh &lt;path&gt;</code></h3>
    <p>Uploads a folder (with <code>index.html</code>) or a single HTML file to Vercel. If you have images alongside the deck, prefer deploying the whole folder so relative paths resolve.</p>
    <h3><code>scripts/export-pdf.sh &lt;path-to-html&gt; [output.pdf]</code></h3>
    <p>Opens the deck in a headless 1920×1080 browser, screenshots every <code>.slide</code>, and stitches them into a PDF. Add <code>--compact</code> to render at 1280×720 for a smaller file.</p>
    <h3><code>scripts/extract-pptx.py &lt;input.pptx&gt; &lt;output-dir&gt;</code></h3>
    <p>Pulls text, layout structure, and embedded images out of a PowerPoint file so the deck can be rebuilt in any Liuyan style.</p>
  </div>
  <div data-lang="zh">
    <h3><code>scripts/deploy.sh &lt;path&gt;</code></h3>
    <p>把文件夹（含 <code>index.html</code>）或单个 HTML 传到 Vercel。若演示旁有图片，建议整文件夹部署，相对路径才能解析。</p>
    <h3><code>scripts/export-pdf.sh &lt;path-to-html&gt; [output.pdf]</code></h3>
    <p>在无头 1920×1080 浏览器打开演示，逐张截 <code>.slide</code> 并拼成 PDF。加 <code>--compact</code> 按 1280×720 渲染，文件更小。</p>
    <h3><code>scripts/extract-pptx.py &lt;input.pptx&gt; &lt;output-dir&gt;</code></h3>
    <p>从 PowerPoint 抽取文字、版式结构与内嵌图片，便于用任意流宴风格重建演示。</p>
  </div>

  <!-- REGEN -->
  <h2 data-lang="en">Regenerating the Gallery</h2>
  <h2 data-lang="zh">重新生成画廊</h2>
  <div data-lang="en"><p>After adding or editing a template:</p></div>
  <div data-lang="zh"><p>新增或编辑模板后：</p></div>
  <pre><code>python gen_previews.py      # re-render previews/*.png
python build_readme.py      # re-render README.md
python build_index.py       # re-render this bilingual index.html</code></pre>

  <!-- LICENSE -->
  <h2 data-lang="en">License</h2>
  <h2 data-lang="zh">许可证</h2>
  <div data-lang="en"><p><a href="./LICENSE">MIT License</a> © 2026 jinjinli5657</p></div>
  <div data-lang="zh"><p><a href="./LICENSE">MIT License</a> © 2026 jinjinli5657</p></div>

  <footer>
    <div data-lang="en">Liuyan Frontend Slides · A WorkBuddy Skill for animation-rich HTML presentations.</div>
    <div data-lang="zh">流宴前端幻灯片 · 用于动画丰富 HTML 演示的 WorkBuddy Skill。</div>
  </footer>
</div>

<script>
  function setLang(lang){{
    document.body.className = 'lang-' + lang;
    document.getElementById('btn-zh').classList.toggle('active', lang==='zh');
    document.getElementById('btn-en').classList.toggle('active', lang==='en');
    try{{ localStorage.setItem('lyf-lang', lang); }}catch(e){{}}
  }}
  (function(){{
    var saved = null;
    try{{ saved = localStorage.getItem('lyf-lang'); }}catch(e){{}}
    if(saved==='zh' || saved==='en'){{ setLang(saved); }}
    else {{ setLang('en'); }} // default English
  }})();
</script>
</body>
</html>
'''

open(OUT, "w", encoding="utf-8").write(HTML)
print("written", OUT, "bytes:", len(HTML.encode("utf-8")), "| templates:", len(tpls))
