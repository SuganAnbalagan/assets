#!/usr/bin/env python3

"""
Elite Nuvio Badge Generator
Generates:
- SVG badges
- badges.json

Edit BADGES below to add/remove badges.
"""

from pathlib import Path
import json
import re

# ===========================
# CONFIG
# ===========================

OUT = Path("output")
SVG = OUT / "svg"

OUT.mkdir(exist_ok=True)
SVG.mkdir(exist_ok=True)

FONT = "Inter,Segoe UI,Arial,sans-serif"
HEIGHT = 28
RADIUS = 8

# ===========================
# BADGES
# ===========================

BADGES = {

    "resolution": {
        "color": "#2563EB",
        "items": [
            ("480P", r"(?i)\b480p\b"),
            ("576P", r"(?i)\b576p\b"),
            ("720P", r"(?i)\b720p\b"),
            ("1080P", r"(?i)\b1080p\b"),
            ("1440P", r"(?i)\b1440p\b"),
            ("2160P", r"(?i)\b(?:2160p|4k|uhd)\b"),
            ("4320P", r"(?i)\b(?:4320p|8k)\b"),
        ]
    },

    "quality": {
        "color": "#7C3AED",
        "items": [
            ("WEB-DL", r"(?i)\bweb.?dl\b"),
            ("WEBRIP", r"(?i)\bweb.?rip\b"),
            ("REMUX", r"(?i)\bremux\b"),
            ("BLURAY", r"(?i)\bblu.?ray\b"),
            ("BDRIP", r"(?i)\bbdrip\b"),
            ("BRRIP", r"(?i)\bbrrip\b"),
            ("HDTV", r"(?i)\bhdtv\b"),
        ]
    },

    "visual": {
        "color": "#F59E0B",
        "items": [
            ("HDR", r"(?i)\bhdr\b"),
            ("HDR10", r"(?i)\bhdr10\b"),
            ("HDR10+", r"(?i)\bhdr10\+\b"),
            ("DOLBY VISION", r"(?i)(dolby.?vision|\bdv\b)"),
        ]
    },

    "audio": {
        "color": "#16A34A",
        "items": [
            ("ATMOS", r"(?i)\batmos\b"),
            ("TRUEHD", r"(?i)\btruehd\b"),
            ("DTS:X", r"(?i)dts.?x"),
            ("DTS-HD MA", r"(?i)dts.?hd.?ma"),
            ("AAC", r"(?i)\baac\b"),
            ("FLAC", r"(?i)\bflac\b"),
        ]
    },

    "channels": {
        "color": "#0D9488",
        "items": [
            ("2.0", r"\b2\.0\b"),
            ("5.1", r"\b5\.1\b"),
            ("7.1", r"\b7\.1\b"),
        ]
    },

    "languages": {
        "color": "#64748B",
        "items": [
            ("EN", r"(?i)\benglish\b|\ben\b"),
            ("JA", r"(?i)\bjapanese\b|\bja\b"),
            ("HI", r"(?i)\bhindi\b|\bhi\b"),
            ("TA", r"(?i)\btamil\b|\bta\b"),
        ]
    }

}

# ===========================
# SVG
# ===========================

SVG_TEMPLATE = """<svg xmlns="http://www.w3.org/2000/svg"
width="{width}" height="{height}" viewBox="0 0 {width} {height}">
<defs>
<linearGradient id="g" x1="0" x2="1">
<stop offset="0%" stop-color="{color}"/>
<stop offset="100%" stop-color="#111827"/>
</linearGradient>
</defs>

<rect
width="{width}"
height="{height}"
rx="{radius}"
fill="url(#g)"/>

<text
x="50%"
y="50%"
dominant-baseline="middle"
text-anchor="middle"
font-size="13"
font-weight="700"
font-family="{font}"
fill="white">{text}</text>

</svg>
"""

# ===========================
# HELPERS
# ===========================

def estimate_width(label):
    return max(64, len(label) * 9 + 24)

badges_json = []

for category, info in BADGES.items():

    color = info["color"]

    for label, regex in info["items"]:

        width = estimate_width(label)

        filename = (
            label.lower()
            .replace("+", "plus")
            .replace(":", "")
            .replace(" ", "-")
            + ".svg"
        )

        svg = SVG_TEMPLATE.format(
            width=width,
            height=HEIGHT,
            radius=RADIUS,
            color=color,
            font=FONT,
            text=label,
        )

        (SVG / filename).write_text(svg, encoding="utf-8")

        badges_json.append({

            "category": category,
            "label": label,
            "regex": regex,
            "icon": f"svg/{filename}"

        })

# validate regex
for badge in badges_json:
    re.compile(badge["regex"])

with open(OUT / "badges.json", "w", encoding="utf-8") as f:
    json.dump(badges_json, f, indent=2)

print("Done!")
print(f"Generated {len(badges_json)} badges.")