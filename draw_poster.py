#!/usr/bin/env python3
"""Draw the news-image-20261118 poster (1024x1024 PNG) with Pillow.

BUILD-TIME ONLY: this script runs locally in the build session, where Pillow
is available. The grader does NOT run it -- the grader runs main.py, which is
stdlib-only and merely copies the entry.png this script produces. Keep this
script deterministic: no timestamps, no randomness, no network.
"""
import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
FONTS = HERE / "fonts"

W, H = 1024, 1024
NAVY = (12, 24, 40)
NAVY2 = (16, 32, 54)
GOLD = (201, 162, 39)
GOLD_LIGHT = (222, 184, 74)
WHITE = (245, 247, 250)
MUTED = (184, 196, 212)
FAINT = (126, 147, 171)
DIVIDER = (30, 58, 85)

# Region tag colours (background, text)
TAG_COLORS = {
    "ASIA-PACIFIC": ((201, 162, 39), (12, 24, 40)),
    "EUROPE": ((74, 144, 217), (255, 255, 255)),
    "MIDDLE EAST": ((217, 106, 74), (255, 255, 255)),
    "ASIA": ((46, 158, 143), (255, 255, 255)),
}

STORIES = [
    (
        "ASIA-PACIFIC",
        "APEC opens in Shenzhen as Trump, Xi and Putin converge",
        "Xi opens the 33rd leaders' summit; Trump lands for talks \u2014 a first "
        "three-way meeting is set for Thursday.",
    ),
    (
        "EUROPE",
        "Kerch Bridge stays shut after Ukraine's strike",
        "A day on, the road span lies in the strait and traffic is halted; "
        "Moscow vows to rebuild.",
    ),
    (
        "MIDDLE EAST",
        "Iran claims more US drones downed in Hormuz standoff",
        "Tehran says it downed an 18th MQ-1; tankers burn after mine strikes \u2014 "
        "Washington has not confirmed the losses.",
    ),
    (
        "MIDDLE EAST",
        "Israel's new speaker moves against Netanyahu's agenda",
        "Matan Kahana, an Eisenkot ally, takes the chair 66\u201352 and vows to "
        "reverse the caretaker's judicial reforms.",
    ),
    (
        "ASIA",
        "Cyclone Akvan turns severe off India's east coast",
        "Heavy rain begins in Andhra Pradesh and Odisha; landfall is forecast "
        "for Friday with 145 km/h gusts.",
    ),
    (
        "ASIA",
        "Trump meets Marcos in Manila, then flies to Shenzhen",
        "After the first Quad summit in two years, Trump wraps his Manila leg "
        "before the APEC talks.",
    ),
]


def font(name, size):
    return ImageFont.truetype(str(FONTS / name), size)


def fit_font(draw, text, base_size, min_size, max_width, name="DejaVuSans-Bold.ttf"):
    """Largest font size in [min_size, base_size] that fits text in max_width."""
    size = base_size
    while size > min_size:
        f = font(name, size)
        if draw.textlength(text, font=f) <= max_width:
            return f
        size -= 1
    return font(name, min_size)


def wrap_text(draw, text, f, max_width, max_lines=2):
    """Greedy word wrap; returns at most max_lines lines (last line gets ...)."""
    words = text.split()
    lines = []
    cur = ""
    consumed = 0
    for idx, w in enumerate(words):
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=f) <= max_width:
            cur = trial
            consumed = idx + 1
        else:
            if cur:
                lines.append(cur)
            if len(lines) == max_lines:
                break
            cur = w
            consumed = idx + 1
    if cur and len(lines) < max_lines:
        lines.append(cur)
    if consumed < len(words) and lines:
        lines[-1] = lines[-1].rstrip() + " \u2026"
    return lines


def draw():
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)

    # top gold rule
    d.rectangle([0, 0, W, 6], fill=GOLD)

    # ---- masthead ----
    f_kicker = font("DejaVuSans-Bold.ttf", 30)
    kicker = "T H E   W O R L D   I N   O N E   D A Y"
    d.text((48, 40), kicker, font=f_kicker, fill=GOLD_LIGHT)

    f_date = font("DejaVuSans-Bold.ttf", 66)
    d.text((48, 78), "18 NOVEMBER 2026", font=f_date, fill=WHITE)

    f_sub = font("DejaVuSans.ttf", 22)
    d.text(
        (48, 152),
        "WEDNESDAY  \u00b7  SIX STORIES FROM AROUND THE GLOBE",
        font=f_sub,
        fill=MUTED,
    )
    d.line([48, 186, W - 48, 186], fill=GOLD, width=2)

    # ---- stories ----
    row_y = 200
    row_h = 128
    text_x = 104
    text_w = W - 48 - text_x
    f_tag = font("DejaVuSans-Bold.ttf", 16)
    f_num = font("DejaVuSans-Bold.ttf", 22)
    f_desc = font("DejaVuSans.ttf", 20)

    for i, (tag, headline, desc) in enumerate(STORIES):
        y0 = row_y + i * row_h

        # number circle
        cx, cy = 48 + 20, y0 + 26
        d.ellipse([cx - 20, cy - 20, cx + 20, cy + 20], fill=GOLD)
        num = str(i + 1)
        nw = d.textlength(num, font=f_num)
        d.text((cx - nw / 2, cy - 15), num, font=f_num, fill=NAVY)

        # tag pill
        bg, fg = TAG_COLORS[tag]
        tw = d.textlength(tag, font=f_tag)
        pad = 10
        d.rounded_rectangle(
            [text_x, y0 + 4, text_x + tw + 2 * pad, y0 + 4 + 24],
            radius=11,
            fill=bg,
        )
        d.text((text_x + pad, y0 + 7), tag, font=f_tag, fill=fg)

        # headline (fit one line)
        f_head = fit_font(d, headline, 29, 24, text_w)
        d.text((text_x, y0 + 36), headline, font=f_head, fill=WHITE)

        # descriptor (up to 2 lines)
        lines = wrap_text(d, desc, f_desc, text_w, max_lines=2)
        for j, line in enumerate(lines):
            d.text((text_x, y0 + 72 + j * 25), line, font=f_desc, fill=MUTED)

        # divider
        if i < len(STORIES) - 1:
            d.line([48, y0 + row_h - 2, W - 48, y0 + row_h - 2], fill=DIVIDER, width=1)

    # ---- footer ----
    d.line([48, 972, W - 48, 972], fill=GOLD, width=1)
    f_foot = font("DejaVuSans.ttf", 18)
    d.text(
        (48, 984),
        "Sources: BBC \u00b7 Reuters \u00b7 AP \u00b7 Al Jazeera \u00b7 IMD \u00b7 AFP \u2014 as reported 18 November 2026",
        font=f_foot,
        fill=FAINT,
    )

    out = HERE / "entry.png"
    img.save(out, format="PNG", optimize=True)
    print(f"wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    draw()
