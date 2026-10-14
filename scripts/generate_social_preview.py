"""Render the actual favicon SVG into a social-preview PNG, without redrawing the S."""
from io import BytesIO
from pathlib import Path
import cairosvg
from PIL import Image

favicon = Path('public/favicon.svg')
svg_png = cairosvg.svg2png(bytestring=favicon.read_bytes(), output_width=630, output_height=630)
icon = Image.open(BytesIO(svg_png)).convert('RGB')
preview = Image.new('RGB', (1200, 630), '#9d1c20')
preview.paste(icon, ((1200 - 630) // 2, 0))
preview.save('public/social-preview.png', optimize=True)
