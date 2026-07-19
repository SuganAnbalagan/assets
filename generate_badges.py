import os
import json
from PIL import Image, ImageDraw, ImageFont

config_json = '''{
  "resolutions": [
    { "id": "8k_uhd", "label": "8K UHD", "bg_color": "#D4AF37", "text_color": "#000000" },
    { "id": "4k_uhd", "label": "4K UHD", "bg_color": "#E50914", "text_color": "#FFFFFF" },
    { "id": "1440p_qhd", "label": "1440p QHD", "bg_color": "#2C3E50", "text_color": "#FFFFFF" },
    { "id": "1080p_fhd", "label": "1080p FHD", "bg_color": "#007BFF", "text_color": "#FFFFFF" },
    { "id": "720p_hd", "label": "720p HD", "bg_color": "#6C757D", "text_color": "#FFFFFF" }
  ],
  "quality": [
    { "id": "bluray", "label": "Blu-ray", "bg_color": "#00A8E8", "text_color": "#FFFFFF" },
    { "id": "web_dl", "label": "WEB-DL", "bg_color": "#2ECC71", "text_color": "#FFFFFF" },
    { "id": "webrip", "label": "WEBRip", "bg_color": "#27AE60", "text_color": "#FFFFFF" },
    { "id": "hdtv", "label": "HDTV", "bg_color": "#7F8C8D", "text_color": "#FFFFFF" }
  ],
  "visual_tags": [
    { "id": "hdr10_plus", "label": "HDR10+", "bg_color": "#111111", "text_color": "#FFCC00" },
    { "id": "dolby_vision", "label": "Dolby Vision", "bg_color": "#000000", "text_color": "#FFFFFF" },
    { "id": "hevc_h265", "label": "HEVC H.265", "bg_color": "#34495E", "text_color": "#FFFFFF" },
    { "id": "av1", "label": "AV1", "bg_color": "#E67E22", "text_color": "#FFFFFF" }
  ],
  "audio_tags": [
    { "id": "dolby_atmos", "label": "Dolby Atmos", "bg_color": "#000000", "text_color": "#FFFFFF" },
    { "id": "dts_x", "label": "DTS:X", "bg_color": "#FF5722", "text_color": "#FFFFFF" },
    { "id": "dts_hd_ma", "label": "DTS-HD MA", "bg_color": "#D35400", "text_color": "#FFFFFF" },
    { "id": "aac", "label": "AAC", "bg_color": "#9B59B6", "text_color": "#FFFFFF" },
    { "id": "flac", "label": "FLAC", "bg_color": "#1ABC9C", "text_color": "#FFFFFF" }
  ],
  "audio_channels": [
    { "id": "ch_7_1_4", "label": "7.1.4 CH", "bg_color": "#4A154B", "text_color": "#FFFFFF" },
    { "id": "ch_5_1", "label": "5.1 CH", "bg_color": "#3F51B5", "text_color": "#FFFFFF" },
    { "id": "ch_2_0", "label": "2.0 Stereo", "bg_color": "#795548", "text_color": "#FFFFFF" }
  ],
  "languages": [
    { "id": "dual_audio", "label": "Dual Audio", "bg_color": "#9C27B0", "text_color": "#FFFFFF" },
    { "id": "multi_audio", "label": "Multi-Audio", "bg_color": "#673AB7", "text_color": "#FFFFFF" },
    { "id": "softsubs", "label": "Softsubs", "bg_color": "#E91E63", "text_color": "#FFFFFF" }
  ]
}'''

badge_data = json.loads(config_json)
os.makedirs("nuvio_badges", exist_ok=True)

# Save the raw JSON data file alongside images
with open("nuvio_badges/badges.json", "w") as f:
    f.write(config_json)

PADDING_X = 14
PADDING_Y = 6
CORNER_RADIUS = 4

for category, badges in badge_data.items():
    for badge in badges:
        text = badge["label"]
        bg_color = badge["bg_color"]
        text_color = badge["text_color"]
        
        font = ImageFont.load_default()
        
        dummy_img = Image.new("RGBA", (1, 1))
        draw_dummy = ImageDraw.Draw(dummy_img)
        bbox = draw_dummy.textbbox((0, 0), text, font=font)
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]
        
        badge_w = text_w + (PADDING_X * 2)
        badge_h = text_h + (PADDING_Y * 2)
        
        img = Image.new("RGBA", (badge_w, badge_h), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        
        draw.rounded_rectangle(
            [(0, 0), (badge_w, badge_h)],
            radius=CORNER_RADIUS,
            fill=bg_color
        )
        
        text_x = (badge_w - text_w) // 2
        text_y = (badge_h - text_h) // 2 - bbox[1]
        draw.text((text_x, text_y), text, fill=text_color, font=font)
        
        filename = f"nuvio_badges/{category}_{badge['id']}.png"
        img.save(filename, "PNG")

print("Generated completely.")
