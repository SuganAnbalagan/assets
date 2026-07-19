import os
import json
from PIL import Image, ImageDraw, ImageFont

config_json = '''{
  "resolutions": [
    { "id": "4320p_8k", "label": "8K", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "2160p_4k", "label": "4K", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "1440p", "label": "1440p", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "1080p", "label": "1080p", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "720p", "label": "720p", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "576p", "label": "576p", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "480p", "label": "480p", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" }
  ],
  "quality": [
    { "id": "uhd_bluray", "label": "UHD BluRay", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "bluray_remux", "label": "Remux", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "bluray", "label": "BluRay", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "web_dl", "label": "WebDL", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "webrip", "label": "WebRip", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "bdrip", "label": "BDRip", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "brrip", "label": "BRRip", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "dvdrip", "label": "DVDRip", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "hdtv", "label": "HDTV", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "cam", "label": "CAM", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "ts", "label": "TS", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "tc", "label": "TC", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" }
  ],
  "visual_tags": [
    { "id": "dolby_vision", "label": "Vision", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "dv_hdr10", "label": "DV HDR10", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "hdr10_plus", "label": "HDR10+", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "hdr10", "label": "HDR10", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "hdr", "label": "HDR", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "imax_enhanced", "label": "IMAX", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "hlg", "label": "HLG", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "sdr", "label": "SDR", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" }
  ],
  "audio_tags": [
    { "id": "dolby_atmos", "label": "Atmos", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "truehd_atmos", "label": "TrueHD Atmos", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "truehd", "label": "TrueHD", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "dd_plus", "label": "DD+", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "dolby_digital", "label": "Dolby Digital", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "dts_x", "label": "DTS:X", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "dts_hd_ma", "label": "DTS-HD MA", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "dts_hd_hr", "label": "DTS-HD HR", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "dts", "label": "DTS", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "flac", "label": "FLAC", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "aac", "label": "AAC", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "pcm", "label": "PCM", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "lpcm", "label": "LPCM", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "opus", "label": "Opus", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "mp3", "label": "MP3", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" }
  ],
  "audio_channels": [
    { "id": "ch_9_1", "label": "9.1", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "ch_7_1", "label": "7.1", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "ch_5_1", "label": "5.1", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "ch_2_1", "label": "2.1", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "stereo_2_0", "label": "2.0", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "mono_1_0", "label": "1.0", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" }
  ],
  "languages": [
    { "id": "en", "label": "EN", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "ja", "label": "JA", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "ko", "label": "KO", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "zh", "label": "ZH", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "hi", "label": "HI", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "ta", "label": "TA", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "te", "label": "TE", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "ml", "label": "ML", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "kn", "label": "KN", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "bn", "label": "BN", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "pa", "label": "PA", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "mr", "label": "MR", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "gu", "label": "GU", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "ur", "label": "UR", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "ar", "label": "AR", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "fr", "label": "FR", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "de", "label": "DE", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "it", "label": "IT", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "es", "label": "ES", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "pt", "label": "PT", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "ru", "label": "RU", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "uk", "label": "UK", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "tr", "label": "TR", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "nl", "label": "NL", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "pl", "label": "PL", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "cs", "label": "CS", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "sv", "label": "SV", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "no", "label": "NO", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "da", "label": "DA", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "fi", "label": "FI", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "th", "label": "TH", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "vi", "label": "VI", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "id", "label": "ID", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "ms", "label": "MS", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" },
    { "id": "tl", "label": "TL", "bg_color": "#000000", "text_color": "#FFFFFF", "border_color": "#FFFFFF" }
  ]
}'''

badge_data = json.loads(config_json)
base_output_dir = "nuvio_badges"
os.makedirs(base_output_dir, exist_ok=True)

with open(f"{base_output_dir}/badges.json", "w") as f:
    f.write(config_json)

PADDING_X = 14
PADDING_Y = 6
CORNER_RADIUS = 7
BORDER_WIDTH = 2

for category, badges in badge_data.items():
    category_dir = os.path.join(base_output_dir, category)
    os.makedirs(category_dir, exist_ok=True)
    
    for badge in badges:
        text = badge["label"]
        bg_color = badge["bg_color"]
        text_color = badge["text_color"]
        border_color = badge["border_color"]
        
        font = ImageFont.load_default()
        
        dummy_img = Image.new("RGBA", (1, 1))
        draw_dummy = ImageDraw.Draw(dummy_img)
        bbox = draw_dummy.textbbox((0, 0), text, font=font)
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]
        
        badge_w = text_w + (PADDING_X * 2)
        badge_h = text_h + (PADDING_Y * 2)
        
        img = Image.new("RGBA", (badge_w, badge_h), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        draw.rounded_rectangle(
            [(0, 0), (badge_w, badge_h)],
            radius=CORNER_RADIUS,
            fill=bg_color
        )
        
        draw.rounded_rectangle(
            [(1, 1), (badge_w - 1, badge_h - 1)],
            radius=CORNER_RADIUS,
            outline=border_color,
            width=BORDER_WIDTH
        )
        
        text_x = (badge_w - text_w) // 2
        text_y = (badge_h - text_h) // 2 - bbox[1]
        draw.text((text_x, text_y), text, fill=text_color, font=font)
        
        filename = os.path.join(category_dir, f"{badge['id']}.png")
        img.save(filename, "PNG")

print("Elite monochrome badge templates rendered successfully.")
