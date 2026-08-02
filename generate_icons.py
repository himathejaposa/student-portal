from PIL import Image, ImageDraw, ImageFont

def create_icon(size, filename):
    img = Image.new('RGB', (size, size), color='#2c3e50')
    draw = ImageDraw.Draw(img)
    
    text = "SP"
    try:
        font = ImageFont.truetype("arial.ttf", size=int(size * 0.4))
    except:
        font = ImageFont.load_default()
    
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    position = ((size - text_width) / 2, (size - text_height) / 2 - bbox[1])
    
    draw.text(position, text, fill='white', font=font)
    img.save(f'static/{filename}')

create_icon(192, 'icon-192.png')
create_icon(512, 'icon-512.png')

print("Icons created successfully!")