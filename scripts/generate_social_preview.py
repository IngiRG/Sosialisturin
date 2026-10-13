from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
im=Image.new('RGB',(1200,630),'#9d1c20')
d=ImageDraw.Draw(im)
cream='#f4f0e7'
sans='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
serif='/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'
d.rectangle((85,122,310,347),fill=cream)
d.text((197,226),'S',font=ImageFont.truetype(serif,160),fill='#9d1c20',anchor='mm')
d.text((85,445),'SOSIALISTURIN',font=ImageFont.truetype(sans,76),fill=cream)
d.rectangle((85,566,1115,572),fill=cream)
im.save(Path('public/social-preview.png'),optimize=True)
