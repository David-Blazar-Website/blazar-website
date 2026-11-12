"""Generate the SVG visuals used on the Research and Media pages and in the home-page carousel.

Run from the repo root:  python3 scripts/make_thumbnails.py
It reads data/research.yml and data/media.yml and writes images/research/*.svg and images/media/*.svg,
plus portrait copies of featured items in images/*/tall/ for the home-page carousel.

- A research item with a `finding` block gets a key-finding bar chart drawn from the numbers in that block.
  Only use numbers that appear in the published paper.
- Any other research item gets a topic icon (set `topic:` to one of the keys in TOPICS).
- Media items get a typographic card: the outlet name, set over a color for the item type.
Images that already exist and are listed in KEEP are left alone, so a hand-made figure can replace a generated one.
"""
import html
import os
import yaml

W, H = 800, 500
CREAM = "#FAF6EF"
INK = "#1F2421"
MUTED = "#6B6B6B"
SERIF = "Georgia, 'Times New Roman', serif"
SANS = "'Helvetica Neue', Helvetica, Arial, sans-serif"

# Topic -> (background, accent, label)
TOPICS = {
    "diversity":   ("#F3E3D9", "#B5502D", "Educator diversity"),
    "pipeline":    ("#E6ECE4", "#4F6B52", "Teacher pipeline"),
    "coaching":    ("#E4EAF0", "#3E5C76", "Coaching & development"),
    "evaluation":  ("#F2EAD8", "#9A6B1F", "Evaluation & incentives"),
    "observation": ("#ECE6EF", "#6A4C7A", "Classroom observation"),
    "instruction": ("#E9EFEA", "#3F6B5E", "Effective teaching"),
    "curriculum":  ("#F4E6DE", "#9C4A2C", "Curriculum"),
    "sel":         ("#F5E4E4", "#A4434A", "Social-emotional outcomes"),
    "inequality":  ("#EDE8DF", "#5E5145", "Investment & inequality"),
    "districts":   ("#E3E9EE", "#46617A", "School districts"),
    "methods":     ("#EAEAE6", "#4D5450", "Research design"),
    "literature":  ("#F1E7DB", "#8A5A35", "Teaching English"),
    "pay":         ("#EEF0E2", "#5F6B2A", "Teacher pay"),
    "attendance":  ("#E6EAF1", "#4A5D7A", "Student attendance"),
}

MEDIA_TYPES = {
    "opinion": ("#B5502D", "Opinion"),
    "podcast": ("#3E5C76", "Podcast"),
    "news":    ("#1F2421", "In the news"),
    "brief":   ("#4F6B52", "Policy brief"),
}

CAROUSEL = False  # True while drawing the carousel copies (no type label: the carousel shows it as a tag)

KEEP = set()  # e.g. {"images/research/jpam-2026-tam.svg"} once a hand-made figure exists


def esc(s):
    return html.escape(str(s), quote=True)


def wrap(text, width):
    words, lines, cur = str(text).split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > width and cur:
            lines.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        lines.append(cur)
    return lines


def svg_open(bg):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img">'
            f'<rect width="{W}" height="{H}" fill="{bg}"/>')


# ---------- topic glyphs (drawn in a 240x240 box centred at cx, cy) ----------
def glyph(topic, c, cx=400, cy=215):
    g = f'<g transform="translate({cx-120},{cy-120})" fill="none" stroke="{c}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round">'
    if topic == "diversity":
        for x, op in ((60, 0.55), (120, 1), (180, 0.75)):
            g += f'<circle cx="{x}" cy="95" r="26" fill="{c}" fill-opacity="{op}" stroke="none"/>'
            g += f'<path d="M{x-42} 200 q0 -62 42 -62 q42 0 42 62" fill="{c}" fill-opacity="{op}" stroke="none"/>'
    elif topic == "pipeline":
        g += '<path d="M20 170 C 80 170, 90 70, 150 70 L 205 70"/><path d="M185 50 L 210 70 L 185 90"/>'
        for x, y in ((20, 170), (85, 128), (150, 70)):
            g += f'<circle cx="{x}" cy="{y}" r="14" fill="{c}" stroke="none"/>'
    elif topic == "coaching":
        g += '<rect x="20" y="40" width="130" height="90" rx="22"/><path d="M55 130 L 45 165 L 85 130"/>'
        g += f'<rect x="95" y="110" width="125" height="85" rx="22" fill="{c}" stroke="none"/>'
        g += f'<path d="M185 195 L 200 225 L 160 195" fill="{c}" stroke="none"/>'
    elif topic == "evaluation":
        g += '<rect x="45" y="25" width="150" height="195" rx="16"/>'
        for i, y in enumerate((80, 125, 170)):
            g += f'<path d="M70 {y} l14 14 l26 -28"/><path d="M130 {y+2} h40" stroke-opacity="0.6"/>'
    elif topic == "observation":
        g += '<path d="M15 120 Q 120 20 225 120 Q 120 220 15 120 Z"/>'
        g += f'<circle cx="120" cy="120" r="38" fill="{c}" stroke="none"/><circle cx="120" cy="120" r="14" fill="#fff" stroke="none"/>'
    elif topic == "instruction":
        g += '<rect x="20" y="30" width="200" height="135" rx="10"/><path d="M120 165 v40 M80 215 h80"/>'
        g += '<path d="M50 130 L 95 90 L 130 112 L 185 62" stroke-width="9"/>'
    elif topic == "curriculum":
        g += '<path d="M120 60 C 90 40, 50 40, 20 50 V 200 C 50 190, 90 190, 120 210 C 150 190, 190 190, 220 200 V 50 C 190 40, 150 40, 120 60 Z"/><path d="M120 60 V 210"/>'
    elif topic == "sel":
        g += f'<path d="M120 205 C 40 150, 15 110, 30 70 C 45 30, 100 30, 120 75 C 140 30, 195 30, 210 70 C 225 110, 200 150, 120 205 Z" fill="{c}" fill-opacity="0.9" stroke="none"/>'
    elif topic == "inequality":
        for x, h, op in ((40, 60, 0.45), (100, 110, 0.7), (160, 175, 1)):
            g += f'<rect x="{x}" y="{215-h}" width="44" height="{h}" rx="6" fill="{c}" fill-opacity="{op}" stroke="none"/>'
        g += '<path d="M20 222 H 222" stroke-width="6"/>'
    elif topic == "districts":
        g += '<path d="M25 210 V 110 L 75 75 L 125 110 V 210"/><path d="M125 210 V 60 H 215 V 210"/><path d="M15 212 H 225"/>'
        for x in (150, 185):
            for y in (90, 130, 170):
                g += f'<rect x="{x-8}" y="{y-8}" width="16" height="16" fill="{c}" stroke="none"/>'
    elif topic == "methods":
        g += '<path d="M25 25 V 215 H 220" stroke-width="7"/>'
        for x, y in ((60, 180), (85, 150), (110, 160), (135, 115), (160, 120), (185, 80), (205, 70)):
            g += f'<circle cx="{x}" cy="{y}" r="9" fill="{c}" stroke="none"/>'
        g += '<path d="M45 195 L 215 60" stroke-opacity="0.55" stroke-width="7"/>'
    elif topic == "literature":
        g += f'<text x="120" y="190" text-anchor="middle" font-family="{SERIF}" font-size="230" fill="{c}" stroke="none">“</text>'
    elif topic == "attendance":
        g += '<rect x="25" y="45" width="190" height="165" rx="14"/><path d="M25 90 H 215 M70 25 v40 M170 25 v40"/>'
        for i, (x, y) in enumerate(((70, 125), (120, 125), (170, 125), (70, 170), (120, 170))):
            g += f'<circle cx="{x}" cy="{y}" r="11" fill="{c}" fill-opacity="{0.35 if i == 3 else 1}" stroke="none"/>'
    elif topic == "pay":
        g += f'<circle cx="120" cy="120" r="92"/><text x="120" y="160" text-anchor="middle" font-family="{SERIF}" font-weight="700" font-size="120" fill="{c}" stroke="none">$</text>'
    return g + "</g>"


def topic_card(item):
    bg, c, label = TOPICS[item.get("topic", "methods")]
    s = svg_open(bg) + glyph(item.get("topic", "methods"), c, cx=W / 2, cy=H * 0.43)
    fs = 30 if W > H else 25
    s += f'<text x="{W/2:.0f}" y="{H*0.84:.0f}" text-anchor="middle" font-family="{SANS}" font-size="{fs}" font-weight="600" letter-spacing="2" fill="{c}">{esc(label.upper())}</text>'
    return s + "</svg>"


def finding_chart(item):
    """Horizontal bars, one hue, values labelled directly. finding: {title, unit, note, bars: [[label, value], ...]}"""
    f = item["finding"]
    c = TOPICS[item.get("topic", "methods")][1]
    bars = f["bars"]
    if H > W:
        return finding_chart_tall(item, f, c, bars)
    s = svg_open(CREAM)
    y0 = 48
    for line in wrap(f["title"], 44):
        s += f'<text x="40" y="{y0}" font-family="{SERIF}" font-size="32" font-weight="600" fill="{INK}">{esc(line)}</text>'
        y0 += 40
    top, bottom = y0 + 22, H - 58
    n = len(bars)
    slot = (bottom - top) / n
    bh = min(46, slot * 0.62)
    label_w = min(380, max(150, 12.6 * max(len(str(b[0])) for b in bars) + 20))
    x0, x1 = 40 + label_w, W - 130
    vmax = max(b[1] for b in bars)
    unit = f.get("unit", "")
    for i, bar in enumerate(bars):
        lab, v = bar[0], bar[1]
        fill = c if len(bar) < 3 or bar[2] == "a" else MUTED
        y = top + i * slot + (slot - bh) / 2
        w = max(6, (x1 - x0) * v / vmax)
        s += f'<text x="{x0-16}" y="{y+bh/2+9}" text-anchor="end" font-family="{SANS}" font-size="25" fill="{INK}">{esc(lab)}</text>'
        s += f'<path d="M{x0} {y} h{w-4} a4 4 0 0 1 4 4 v{bh-8} a4 4 0 0 1 -4 4 h{-(w-4)} Z" fill="{fill}"/>'
        val = f"{v:g}{unit}"
        s += f'<text x="{x0+w+12}" y="{y+bh/2+10}" font-family="{SANS}" font-size="28" font-weight="700" fill="{INK}">{esc(val)}</text>'
    s += f'<line x1="{x0}" y1="{top-6}" x2="{x0}" y2="{bottom+4}" stroke="{MUTED}" stroke-opacity="0.5" stroke-width="2"/>'
    if f.get("note"):
        s += f'<text x="40" y="{H-22}" font-family="{SANS}" font-size="20" fill="{MUTED}">{esc(f["note"])}</text>'
    return s + "</svg>"


def finding_chart_tall(item, f, c, bars):
    """Portrait version for the home-page carousel: title on top, each label above its bar."""
    s = svg_open(CREAM)
    y0 = 64
    for line in wrap(f["title"], 30):
        s += f'<text x="40" y="{y0}" font-family="{SERIF}" font-size="34" font-weight="600" fill="{INK}">{esc(line)}</text>'
        y0 += 42
    note_lines = wrap(f["note"], 44) if f.get("note") else []
    top, bottom = y0 + 30, H - 40 - 28 * len(note_lines)
    n = len(bars)
    slot = min(150, (bottom - top) / n)
    top += ((bottom - top) - slot * n) / 2
    bh = min(52, slot * 0.4)
    x0, x1 = 40, W - 150
    vmax = max(b[1] for b in bars)
    unit = f.get("unit", "")
    for i, bar in enumerate(bars):
        lab, v = bar[0], bar[1]
        fill = c if len(bar) < 3 or bar[2] == "a" else MUTED
        ly = top + i * slot + 30
        s += f'<text x="{x0}" y="{ly:.0f}" font-family="{SANS}" font-size="27" fill="{INK}">{esc(lab)}</text>'
        y = ly + 14
        w = max(6, (x1 - x0) * v / vmax)
        s += f'<path d="M{x0} {y:.1f} h{w-4:.1f} a4 4 0 0 1 4 4 v{bh-8:.1f} a4 4 0 0 1 -4 4 h{-(w-4):.1f} Z" fill="{fill}"/>'
        s += f'<text x="{x0+w+14:.1f}" y="{y+bh/2+11:.1f}" font-family="{SANS}" font-size="32" font-weight="700" fill="{INK}">{esc(f"{v:g}{unit}")}</text>'
    y = H - 40 - 28 * (len(note_lines) - 1)
    for line in note_lines:
        s += f'<text x="40" y="{y:.0f}" font-family="{SANS}" font-size="21" fill="{MUTED}">{esc(line)}</text>'
        y += 28
    return s + "</svg>"


def stat_card(item):
    """A single headline number. finding: {kind: stat, value, caption}"""
    f = item["finding"]
    bg, c, label = TOPICS[item.get("topic", "methods")]
    s = svg_open(bg)
    s += f'<text x="48" y="78" font-family="{SANS}" font-size="24" font-weight="600" letter-spacing="2" fill="{c}">{esc(label.upper())}</text>'
    size = min(150, int((W - 90) / (0.6 * len(f["value"]))))
    tall = H > W
    vy = H * 0.42 if tall else 250
    s += f'<text x="44" y="{vy:.0f}" font-family="{SERIF}" font-size="{size}" font-weight="700" fill="{c}">{esc(f["value"])}</text>'
    y = vy + (90 if tall else 70)
    for line in wrap(f["caption"], 34 if tall else 46)[:7 if tall else 4]:
        s += f'<text x="48" y="{y}" font-family="{SANS}" font-size="27" fill="{INK}">{esc(line)}</text>'
        y += 38
    return s + "</svg>"


def list_card(item):
    """Two to four short findings or ideas. finding: {kind: list, title, items: [...]}"""
    f = item["finding"]
    bg, c, label = TOPICS[item.get("topic", "methods")]
    tall = H > W
    s = svg_open(bg)
    s += f'<text x="48" y="{70 if tall else 62}" font-family="{SANS}" font-size="22" font-weight="600" letter-spacing="2" fill="{c}">{esc(label.upper())}</text>'
    y = 136 if tall else 122
    tsize = 40 if tall else 40
    for line in wrap(f["title"], 24 if tall else 32):
        s += f'<text x="48" y="{y}" font-family="{SERIF}" font-size="{tsize}" font-weight="700" fill="{INK}">{esc(line)}</text>'
        y += tsize + 8
    items = f["items"]
    isize = 30 if tall else 31
    width = 30 if tall else 42
    lines = [wrap(it, width) for it in items]
    y += 56 if tall else 26
    for block in lines:
        s += f'<rect x="48" y="{y - isize * 0.72:.0f}" width="8" height="{len(block) * (isize + 8) - 10}" rx="3" fill="{c}"/>'
        for line in block:
            s += f'<text x="76" y="{y:.0f}" font-family="{SANS}" font-size="{isize}" fill="{INK}">{esc(line)}</text>'
            y += isize + 8
        y += 26 if tall else 12
    return s + "</svg>"


def idea_card(item):
    """A key idea in words, for papers without a headline number. finding: {kind: idea, headline, caption}"""
    f = item["finding"]
    bg, c, label = TOPICS[item.get("topic", "methods")]
    tall = H > W
    s = svg_open(bg)
    s += f'<text x="48" y="78" font-family="{SANS}" font-size="24" font-weight="600" letter-spacing="2" fill="{c}">{esc(label.upper())}</text>'
    hl = wrap(f["headline"], 12 if tall else 20)
    hsize = min(96 if tall else 88, int((W - 100) / (0.55 * max(len(l) for l in hl))))
    y = (H * 0.40 if tall else 200) - (len(hl) - 1) * hsize * 0.5
    for line in hl:
        s += f'<text x="44" y="{y:.0f}" font-family="{SERIF}" font-style="italic" font-weight="700" font-size="{hsize}" fill="{c}">{esc(line)}</text>'
        y += hsize * 1.08
    y += 30
    for line in wrap(f["caption"], 34 if tall else 48)[:6]:
        s += f'<text x="48" y="{y:.0f}" font-family="{SANS}" font-size="{27 if tall else 25}" fill="{INK}">{esc(line)}</text>'
        y += 37
    return s + "</svg>"


def media_card(item):
    color, label = MEDIA_TYPES[item["type"]]
    s = svg_open(color)
    s += f'<rect x="28" y="28" width="{W-56}" height="{H-56}" fill="none" stroke="#FFFFFF" stroke-opacity="0.35" stroke-width="2"/>'
    if not CAROUSEL:
        s += f'<text x="64" y="104" font-family="{SANS}" font-size="26" font-weight="600" letter-spacing="3" fill="#FFFFFF" fill-opacity="0.85">{esc(label.upper())}</text>'
    outlet = item.get("outlet_short", item["outlet"])
    lines = wrap(outlet, 12 if H > W else 16)
    # size the outlet name so the longest line fits inside the frame (about 0.62 em per character)
    longest = max(len(l) for l in lines)
    size = min(92 if len(lines) == 1 else (76 if H > W else 70), int((W - 150) / (0.62 * longest)))
    y = H * 0.58 - (len(lines) - 1) * size * 0.55
    for line in lines:
        s += f'<text x="64" y="{y:.0f}" font-family="{SERIF}" font-size="{size}" font-weight="600" fill="#FFFFFF">{esc(line)}</text>'
        y += size * 1.1
    s += f'<text x="64" y="{H-64}" font-family="{SANS}" font-size="24" fill="#FFFFFF" fill-opacity="0.8">{esc(item.get("date_label") or "")}</text>'
    return s + "</svg>"


def tall_path(path):
    """images/media/x.svg -> images/media/tall/x.svg (portrait copy used by the home-page carousel)."""
    folder, name = os.path.split(path)
    return os.path.join(folder, "tall", name)


def write_tall(item, make):
    """Carousel copies of a featured item: a 600x1000 portrait (images/*/tall/) for wide screens and,
    for media, a label-free standard card (images/media/plain/) for narrow screens."""
    global W, H, CAROUSEL
    CAROUSEL = True
    try:
        W, H = 600, 1000
        out = tall_path(item["image"])
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, "w").write(make(item))
        W, H = 800, 500
        if "status" not in item:
            folder, name = os.path.split(item["image"])
            out = os.path.join(folder, "plain", name)
            os.makedirs(os.path.dirname(out), exist_ok=True)
            open(out, "w").write(make(item))
    finally:
        W, H, CAROUSEL = 800, 500, False


def research_svg(item):
    f = item.get("finding")
    if not f:
        return topic_card(item)
    kind = f.get("kind")
    return {"stat": stat_card, "list": list_card, "idea": idea_card}.get(kind, finding_chart)(item)


def main():
    os.makedirs("images/research", exist_ok=True)
    os.makedirs("images/media", exist_ok=True)
    # portrait copies are regenerated from scratch, so un-featured items drop out
    for folder in ("images/research/tall", "images/media/tall", "images/media/plain"):
        if os.path.isdir(folder):
            for name in os.listdir(folder):
                os.remove(os.path.join(folder, name))
    for item in yaml.safe_load(open("data/research.yml")):
        out = item["image"]
        if out in KEEP:
            continue
        open(out, "w").write(research_svg(item))
        if item.get("featured"):
            write_tall(item, research_svg)
    for item in yaml.safe_load(open("data/media.yml")):
        out = item["image"]
        if out in KEEP:
            continue
        open(out, "w").write(media_card(item))
        if item.get("featured"):
            write_tall(item, media_card)


if __name__ == "__main__":
    main()
