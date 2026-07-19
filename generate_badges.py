import os
import json
from PIL import Image, ImageDraw, ImageFont

config_json = '''{
  "resolutions": [
    { "id": "4320p_8k", "label": "8K", "bg_color": "#141619", "text_color": "#4EA8DE", "border_color": "#4EA8DE" },
    { "id": "2160p_4k", "label": "4K", "bg_color": "#141619", "text_color": "#5E60CE", "border_color": "#5E60CE" },
    { "id": "1440p", "label": "1440P", "bg_color": "#141619", "text_color": "#64DFDF", "border_color": "#64DFDF" },
    { "id": "1080p", "label": "1080P", "bg_color": "#141619", "text_color": "#72EFDD", "border_color": "#72EFDD" },
    { "id": "720p", "label": "720P", "bg_color": "#141619", "text_color": "#80FFDB", "border_color": "#80FFDB" },
    { "id": "576p", "label": "576P", "bg_color": "#141619", "text_color": "#A0E7E5", "border_color": "#A0E7E5" },
    { "id": "480p", "label": "480P", "bg_color": "#141619", "text_color": "#B4F8C8", "border_color": "#B4F8C8" }
  ],
  "quality": [
    { "id": "uhd_bluray", "label": "UHD BLURAY", "bg_color": "#141619", "text_color": "#B5179E", "border_color": "#B5179E" },
    { "id": "bluray_remux", "label": "REMUX", "bg_color": "#141619", "text_color": "#7209B7", "border_color": "#7209B7" },
    { "id": "bluray", "label": "BLURAY", "bg_color": "#141619", "text_color": "#560BAD", "border_color": "#560BAD" },
    { "id": "web_dl", "label": "WEB-DL", "bg_color": "#141619", "text_color": "#4895EF", "border_color": "#4895EF" },
    { "id": "webrip", "label": "WEBRIP", "bg_color": "#141619", "text_color": "#4CC9F0", "border_color": "#4CC9F0" },
    { "id": "bdrip", "label": "BDRIP", "bg_color": "#141619", "text_color": "#3F37C9", "border_color": "#3F37C9" },
    { "id": "brrip", "label": "BRRIP", "bg_color": "#141619", "text_color": "#4361EE", "border_color": "#4361EE" },
    { "id": "dvdrip", "label": "DVDRIP", "bg_color": "#141619", "text_color": "#A2D2FF", "border_color": "#A2D2FF" },
    { "id": "hdtv", "label": "HDTV", "bg_color": "#141619", "text_color": "#BDE0FE", "border_color": "#BDE0FE" },
    { "id": "cam", "label": "CAM", "bg_color": "#141619", "text_color": "#F72585", "border_color": "#F72585" },
    { "id": "ts", "label": "TS", "bg_color": "#141619", "text_color": "#E01E37", "border_color": "#E01E37" },
    { "id": "tc", "label": "TC", "bg_color": "#141619", "text_color": "#B7094C", "border_color": "#B7094C" }
  ],
  "visual_tags": [
    { "id": "dolby_vision", "label": "DOLBY VISION", "bg_color": "#141619", "text_color": "#FF9F1C", "border_color": "#FF9F1C" },
    { "id": "dv_hdr10", "label": "DV HDR10", "bg_color": "#141619", "text_color": "#FFB703", "border_color": "#FFB703" },
    { "id": "hdr10_plus", "label": "HDR10+", "bg_color": "#141619", "text_color": "#FB8500", "border_color": "#FB8500" },
    { "id": "hdr10", "label": "HDR10", "bg_color": "#141619", "text_color": "#F15BB5", "border_color": "#F15BB5" },
    { "id": "hdr", "label": "HDR", "bg_color": "#141619", "text_color": "#EE6C4D", "border_color": "#EE6C4D" },
    { "id": "imax_enhanced", "label": "IMAX ENHANCED", "bg_color": "#141619", "text_color": "#E29578", "border_color": "#E29578" },
    { "id": "hlg", "label": "HLG", "bg_color": "#141619", "text_color": "#FFDDD2", "border_color": "#FFDDD2" },
    { "id": "sdr", "label": "SDR", "bg_color": "#141619", "text_color": "#83C5BE", "border_color": "#83C5BE" }
  ],
  "audio_tags": [
    { "id": "dolby_atmos", "label": "DOLBY ATMOS", "bg_color": "#141619", "text_color": "#2ECC71", "border_color": "#2ECC71" },
    { "id": "truehd_atmos", "label": "TRUEHD ATMOS", "bg_color": "#141619", "text_color": "#27AE60", "border_color": "#27AE60" },
    { "id": "truehd", "label": "TRUEHD", "bg_color": "#141619", "text_color": "#1ABC9C", "border_color": "#1ABC9C" },
    { "id": "dd_plus", "label": "DD+", "bg_color": "#141619", "text_color": "#16A085", "border_color": "#16A085" },
    { "id": "dolby_digital", "label": "DOLBY DIGITAL", "bg_color": "#141619", "text_color": "#2CEAA3", "border_color": "#2CEAA3" },
    { "id": "dts_x", "label": "DTS:X", "bg_color": "#A7F3D0", "text_color": "#A7F3D0", "border_color": "#A7F3D0" },
    { "id": "dts_hd_ma", "label": "DTS-HD MA", "bg_color": "#141619", "text_color": "#10B981", "border_color": "#10B981" },
    { "id": "dts_hd_hr", "label": "DTS-HD HR", "bg_color": "#141619", "text_color": "#059669", "border_color": "#059669" },
    { "id": "dts", "label": "DTS", "bg_color": "#141619", "text_color": "#047857", "border_color": "#047857" },
    { "id": "flac", "label": "FLAC", "bg_color": "#141619", "text_color": "#52B788", "border_color": "#52B788" },
    { "id": "aac", "label": "AAC", "bg_color": "#141619", "text_color": "#74C69D", "border_color": "#74C69D" },
    { "id": "pcm", "label": "PCM", "bg_color": "#141619", "text_color": "#95D5B2", "border_color": "#95D5B2" },
    { "id": "lpcm", "label": "LPCM", "bg_color": "#141619", "text_color": "#B7E4C7", "border_color": "#B7E4C7" },
    { "id": "opus", "label": "OPUS", "bg_color": "#141619", "text_color": "#D8F3DC", "border_color": "#D8F3DC" },
    { "id": "mp3", "label": "MP3", "bg_color": "#141619", "text_color": "#E8F5E9", "border_color": "#E8F5E9" }
  ],
  "audio_channels": [
    { "id": "ch_9_1", "label": "9.1", "bg_color": "#141619", "text_color": "#00F5D4", "border_color": "#00F5D4" },
    { "id": "ch_7_1", "label": "7.1", "bg_color": "#141619", "text_color": "#01F9C6", "border_color": "#01F9C6" },
    { "id": "ch_5_1", "label": "5.1", "bg_color": "#141619", "text_color": "#00B4D8", "border_color": "#00B4D8" },
    { "id": "ch_2_1", "label": "2.1", "bg_color": "#141619", "text_color": "#0077B6", "border_color": "#0077B6" },
    { "id": "stereo_2_0", "label": "2.0 STEREO", "bg_color": "#141619", "text_color": "#03045E", "border_color": "#03045E" },
    { "id": "mono_1_0", "label": "1.0 MONO", "bg_color": "#141619", "text_color": "#90E0EF", "border_color": "#90E0EF" }
  ],
  "languages": [
    { "id": "en", "label": "EN", "bg_color": "#141619", "text_color": "#E5E5E5", "border_color": "#4A4A4A" },
    { "id": "ja", "label": "JA", "bg_color": "#141619", "text_color": "#E5E5E5", "border_color": "#4A4A4A" },
    { "id": "ko", "label": "KO", "bg_color": "#141619", "text_color": "#E5E5E5", "border_color": "#4A4A4A" },
    { "id": "zh", "label": "ZH", "bg_color": "#141619", "text_color": "#E5E5E5", "border_color": "#4A4A4A" },
    { "id": "hi", "label": "HI", "bg_color": "#141619", "text_color": "#E5E5E5", "border_color": "#4A4A4A" },
    { "id": "ta", "label": "TA", "bg_color": "#141619", "text_color": "#E5E5E5", "border_color": "#4A4A4A" },
    { "id": "te", "label": "TE", "bg_color": "#141619", "text_color": "#E5E5E5", "border_color": "#4A4A4A" },
    { "id": "ml", "label": "ML", "bg_color": "#141619", "text_color": "#E5E5E5", "border_color": "#4A4A4A" },
    { "id": "kn", "label": "KN", "bg_color": "#141619", "text_color": "#E5E5E5", "border_color": "#4A4A4A" },
    { "id": "bn", "label": "BN", "bg_color": "#141619", "text_color": "#E5E5E5", "border_color": "#4A4A4A" },
    { "id": "pa", "label": "PA", "bg_color": "#141619", "text_color": "#E5E5E5", "border_color": "#4A4A4A" },
    { "id": "mr", "label": "MR", "bg_color": "#141619", "text_color": "#E5E5E5", "border_color": "#4A4A4A" },
    { "id": "gu", "label": "GU", "bg_color": "#141619", "text_color": "#E5E5E5", "border_color": "#4A4A4A" },
    { "id": "ur", "label": "UR", "bg_color": "#141619", "text_color": "#E5E5E5", "border_color": "#4A4A4A" },
    { "id": "ar", "label": "AR", "bg_color": "#141619", "text_color": "#E5E5E5", "border_color": "#4A4A4A" },
    { "id": "fr", "label": "FR", "bg_color": "#141619", "text_color": "#E5E5E5", "border_color": "#4A4A4A" },
    { "id": "de", "label": "DE", "bg_color": "#141619", "text_color": "#E5E5E5", "border_color": "#4A4A4A" },
    { "id": "it", "label": "IT", "bg_color": "#141619", "text_color": "#E5E5E5", "border_color": "#4A4A4A" },
    { "id": "es", "label": "ES", "bg_color": "#141619", "text_color": "#E5E5E5", "border_color": "#4A4A4A" },
    { "id": "pt", "label": "PT", "bg_color": "#141619", "text_color": "#E5E5E5", "border_color": "#4A4A4A" },
    { "id": "ru", "label": "RU", "bg_color": "#141619", "text_color": "#E5E5E5", "border_color": "#4A4A4A" },
    { "id": "uk", "label": "UK", "bg_color": "#141619", "text_color": "#E5E5E5", "border_color": "#4A4A4A" },
    { "id": "tr", "label": "TR", "bg_color": "#141619", "text_color": "#E5E5E5", "border_color": "#4A4A4A" },
    { "id": "nl", "label": "NL", "bg_color": "#141619", "text_color": "#E5E5E5", "border_color": "#4A4A4A" },
    { "id": "pl", "label": "PL", "bg_color": "#141619", "text_color": "#E5E5E5", "border_color": "#4A4A4A" },
    { "id": "cs", "label": "CS", "bg_color": "#141619", "text_color": "#E5E5E5", "border_color": "#4A4A4A" },
    { "id": "sv", "label": "SV", "bg_color": "#141619", "text_color": "#E5E5E5", "border_color": "#4A4A4A" },
    { "id": "no", "label": "NO", "bg_color": "#141619", "text_color": "#E5E5E5", "border_color": "#4A4A4A" },
    { "id": "da", "label": "DA", "bg_color": "#141619", "text_color": "#E5E5E5", "border_color": "#4A4A4A" },
    { "id": "fi", "label": "FI", "bg_color": "#141619", "text_color": "#E5E5E5", "border_color": "#4A4A4A" },
    { "id": "th", "label": "TH", "bg_color": "#141619", "text_color": "#E5E5E5", "border_color": "#4A4A4A" },
    { "id": "vi", "label": "VI", "bg_color": "#141619", "text_color": "#E5E5E5", "border_color": "#4A4A4A" },
    { "id": "id", "label": "ID", "bg_color": "#141619", "text_color": "#E5E5E5", "border_color": "#4A4A4A" },
    { "id": "ms", "label": "MS", "bg_color": "#141619", "text_color": "#E5E5E5", "border_color": "#4A4A4A" },
    { "id": "tl", "label": "TL", "bg_color": "#141619", "text_color": "#E5E5E5", "border_color": "#4A4A4A" }
  ]
}'''

badge_data = json.loads(config_json)
base_output_dir = "nuvio_badges"
os.makedirs(base_output_dir, exist_ok=True)

with open(f"{base_output_dir}/badges.json", "w") as f:
    f.write(config_json)

PADDING_X = 18
PADDING_Y = 8
CORNER_RADIUS = 3
BORDER_WIDTH = 1

for category, badges in badge_data.items():
    category_dir = os.path.join(base_output_dir, category)
    os.makedirs(category_dir, exist_ok=True)
    
    for badge in badges:
        text = badge["label"]
        bg_color = badge["bg_color"]
        text_color = badge["text_color"]
        border_color = badge.get("border_color", text_color)
        
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
        
        draw.rounded_rectangle(
            [(0, 0), (badge_w, badge_h)],
            radius=CORNER_RADIUS,
            outline=border_color,
            width=BORDER_WIDTH
        )
        
        text_x = (badge_w - text_w) // 2
        text_y = (badge_h - text_h) // 2 - bbox[1]
        draw.text((text_x, text_y), text, fill=text_color, font=font)
        
        filename = os.path.join(category_dir, f"{badge['id']}.png")
        img.save(filename, "PNG")

print("Premium asset pipeline generation routines completely executed.")
