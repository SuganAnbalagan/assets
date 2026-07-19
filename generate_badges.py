import os
import json
from PIL import Image, ImageDraw, ImageFont

config_json = '''... (Paste the complete JSON structure snippet from section 1 right here) ...'''

badge_data = json.loads(config_json)
base_output_dir = "nuvio_badges"
os.makedirs(base_output_dir, exist_ok=True)

with open(f"{base_output_dir}/badges.json", "w") as f:
    f.write(config_json)

# Elite layout metrics based directly on the visual template image
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
        
        # Geometry math engine
        dummy_img = Image.new("RGBA", (1, 1))
        draw_dummy = ImageDraw.Draw(dummy_img)
        bbox = draw_dummy.textbbox((0, 0), text, font=font)
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]
        
        badge_w = text_w + (PADDING_X * 2)
        badge_h = text_h + (PADDING_Y * 2)
        
        # Rendering pipeline canvas setup
        img = Image.new("RGBA", (badge_w, badge_h), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Base fill layer
        draw.rounded_rectangle(
            [(0, 0), (badge_w, badge_h)],
            radius=CORNER_RADIUS,
            fill=bg_color
        )
        
        # Heavy minimalist border outline offset calculation
        draw.rounded_rectangle(
            [(1, 1), (badge_w - 1, badge_h - 1)],
            radius=CORNER_RADIUS,
            outline=border_color,
            width=BORDER_WIDTH
        )
        
        # Center-align font typography perfectly inside the border bounds
        text_x = (badge_w - text_w) // 2
        text_y = (badge_h - text_h) // 2 - bbox[1]
        draw.text((text_x, text_y), text, fill=text_color, font=font)
        
        filename = os.path.join(category_dir, f"{badge['id']}.png")
        img.save(filename, "PNG")

print("Elite monochrome badge templates rendered successfully.")
