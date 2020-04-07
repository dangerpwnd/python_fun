from PIL import Image, ImageDraw, ImageFont
import urllib.request, json
from dictor import dictor

with urllib.request.urlopen("http://quotes.rest/qod.json?category=inspire") as url:
    data = json.loads(url.read().decode())
    quote = dictor(data, 'contents.quotes.0.quote', default="Missing Quote")
    length = int(dictor(data, 'contents.quotes.0.length', default="Missing Length"))
    author = dictor(data, 'contents.quotes.0.author', default="Missing Author")

# Font, font size
fnt=ImageFont.truetype(r'C:\Windows\Fonts\segoepr.ttf', 20)

# Mode, (W,H), color
if length > 170:
    img=Image.new('RGB',(2000,100),color=(255,255,255))
    d=ImageDraw.Draw(img)
    # (x,y), Text, alignment, font, font color
    d.multiline_text((35,30),quote,align="center",font=fnt,fill=(0,0,0))
    d.multiline_text((950,60),author,align="center",font=fnt,fill=(0,0,0))
elif length > 150:
    img=Image.new('RGB',(1720,100),color=(255,255,255))
    d=ImageDraw.Draw(img)
    # (x,y), Text, alignment, font, font color
    d.multiline_text((25,30),quote,align="center",font=fnt,fill=(0,0,0))
    d.multiline_text((750,60),author,align="center",font=fnt,fill=(0,0,0))

img.save(r'C:\Users\Eric.M\Pictures\Quote.png')

