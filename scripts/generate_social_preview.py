from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import subprocess

# Reproduce the favicon's cream Georgia S on a plain red background.
im = Image.new('RGB', (1200, 630), '#9d1c20')
draw = ImageDraw.Draw(im)
font_path = subprocess.check_output(['fc-match', '-f', '%{file}', 'Georgia:style=Bold'], text=True).strip()
font = ImageFont.truetype(font_path, 480)
draw.text((600, 315), 'S', font=font, fill='#f4f0e7', anchor='mm')
im.save(Path('public/social-preview.png'), optimize=True)
