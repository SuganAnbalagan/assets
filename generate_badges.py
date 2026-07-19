import os
import json
from PIL import Image, ImageDraw, ImageFont

# 1. Master JSON string configuration mapping
config_json = '''... (Paste the complete JSON configuration snippet block from section 1 directly here) ...'''

badge_data = json.loads(config_json)
base_output_dir = "nuvio_badges"
os.makedirs(base_output_dir, exist_ok=True)

# Write configuration out for structural schema imports
with open(f"{base_output_dir}/badges.json", "w") as f:
    f.write(config_json)

# Fine-grained visual constants for rendering upscale premium layouts
PADDING_X = 18
PADDING_Y = 8
CORNER_RADIUS = 3
BORDER_WIDTH = 1

for category, badges in badge_data.items():
    # Sort assets into domain specific folders inside target folder path
    category_dir = os.path.join(base_output_dir, category)
    os.makedirs(category_dir, exist_ok=True)
    
    for badge in badges:
        text = badge["label"]
        bg_color = badge["bg_color"]
        text_color = badge["text_color"]
        border_color = badge.get("border_color", text_color)
        
        # Instantiate fallback engine cleanly across headless server instances
        font = ImageFont.load_default()
        
        # Execution bounds computation engine
        dummy_img = Image.new("RGBA", (1, 1))
        draw_dummy = ImageDraw.Draw(dummy_img)
        bbox = draw_dummy.textbbox((0, 0), text, font=font)
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]
        
        badge_w = text_w + (PADDING_X * 2)
        badge_h = text_h + (PADDING_Y * 2)
        
        # Instantiate master pixel matrices mapping context layers
        img = Image.new("RGBA", (badge_w, badge_h), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        
        # Render clean foundational solid backdrop shape
        draw.rounded_rectangle(
            [(0, 0), (badge_w, badge_h)],
            radius=CORNER_RADIUS,
            fill=bg_color
        )
        
        # Render explicit 1px crisp elegant border frame boundaries
        draw.rounded_rectangle(
            [(0, 0), (badge_w, badge_h)],
            radius=CORNER_RADIUS,
            outline=border_color,
            width=BORDER_WIDTH
        )
        
        # Balance absolute centering positions against custom metrics text layout
        text_x = (badge_w - text_w) // 2
        text_y = (badge_h - text_h) // 2 - bbox[1]
        draw.text((text_x, text_y), text, fill=text_color, font=font)
        
        # Compile direct asset file outputs inside separate domains
        filename = os.path.join(category_dir, f"{badge['id']}.png")
        img.save(filename, "PNG")

print("Premium asset pipeline generation routines completely executed.")
