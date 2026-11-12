"""Generate the SVG visuals used on the Research and Media pages and in the home-page carousel.

Run from the repo root:  python3 scripts/make_thumbnails.py
It reads data/research.yml and data/media.yml and writes images/research/*.svg and images/media/*.svg.

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
}

MEDIA_TYPES = {
    "opinion": ("#B5502D", "Opinion"),
    "podcast": ("#3E5C76", "Podcast"),
    "news":    ("#1F2421", "In the news"),
    "brief":   ("#4F6B52", "Policy brief"),
}

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
    elif topic == "pay":
        g += f'<circle cx="120" cy="120" r="92"/><text x="120" y="160" text-anchor="middle" font-family="{SERIF}" font-weight="700" font-size="120" fill="{c}" stroke="none">$</text>'
    return g + "</g>"


def topic_card(item):
    bg, c, label = TOPICS[item.get("topic", "methods")]
    s = svg_open(bg) + glyph(item.get("topic", "methods"), c)
    s += f'<text x="400" y="420" text-anchor="middle" font-family="{SANS}" font-size="30" font-weight="600" letter-spacing="2" fill="{c}">{esc(label.upper())}</text>'
    return s + "</svg>"


def finding_chart(item):
    """Horizontal bars, one hue, values labelled directly. finding: {title, unit, note, bars: [[label, value], ...]}"""
    f = item["finding"]
    c = TOPICS[item.get("topic", "methods")][1]
    bars = f["bars"]
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


def stat_card(item):
    """A single headline number. finding: {kind: stat, value, caption}"""
    f = item["finding"]
    bg, c, label = TOPICS[item.get("topic", "methods")]
    s = svg_open(bg)
    s += f'<text x="48" y="78" font-family="{SANS}" font-size="24" font-weight="600" letter-spacing="2" fill="{c}">{esc(label.upper())}</text>'
    size = 150 if len(f["value"]) <= 8 else 112
    s += f'<text x="44" y="250" font-family="{SERIF}" font-size="{size}" font-weight="700" fill="{c}">{esc(f["value"])}</text>'
    y = 320
    for line in wrap(f["caption"], 46)[:4]:
        s += f'<text x="48" y="{y}" font-family="{SANS}" font-size="27" fill="{INK}">{esc(line)}</text>'
        y += 38
    return s + "</svg>"


def media_card(item):
    color, label = MEDIA_TYPES[item["type"]]
    s = svg_open(color)
    s += f'<rect x="28" y="28" width="{W-56}" height="{H-56}" fill="none" stroke="#FFFFFF" stroke-opacity="0.35" stroke-width="2"/>'
    s += f'<text x="64" y="104" font-family="{SANS}" font-size="26" font-weight="600" letter-spacing="3" fill="#FFFFFF" fill-opacity="0.85">{esc(label.upper())}</text>'
    outlet = item.get("outlet_short", item["outlet"])
    lines = wrap(outlet, 16)
    size = 92 if len(lines) == 1 and len(outlet) <= 14 else 70
    y = 290 - (len(lines) - 1) * size * 0.55
    for line in lines:
        s += f'<text x="64" y="{y:.0f}" font-family="{SERIF}" font-size="{size}" font-weight="600" fill="#FFFFFF">{esc(line)}</text>'
        y += size * 1.1
    s += f'<text x="64" y="{H-64}" font-family="{SANS}" font-size="24" fill="#FFFFFF" fill-opacity="0.8">{esc(item.get("date_label") or "")}</text>'
    return s + "</svg>"


def main():
    os.makedirs("images/research", exist_ok=True)
    os.makedirs("images/media", exist_ok=True)
    for item in yaml.safe_load(open("data/research.yml")):
        out = item["image"]
        if out in KEEP:
            continue
        f = item.get("finding")
        svg = (stat_card(item) if f.get("kind") == "stat" else finding_chart(item)) if f else topic_card(item)
        open(out, "w").write(svg)
    for item in yaml.safe_load(open("data/media.yml")):
        out = item["image"]
        if out in KEEP:
            continue
        open(out, "w").write(media_card(item))


if __name__ == "__main__":
    main()
