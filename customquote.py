from PIL import Image, ImageDraw, ImageFont
import urllib.request, json
from dictor import dictor

with urllib.request.urlopen("http://quotes.rest/qod.json?category=inspire") as url:
    data = json.loads(url.read().decode())
    quote = dictor(data, 'contents.quotes.0.quote', default="Missing Quote")
    length = dictor(data, 'contents.quotes.0.length', default="Missing Length")
    author = dictor(data, 'contents.quotes.0.author', default="Missing Author")

# Font, font size
fnt=ImageFont.truetype(r'C:\Windows\Fonts\segoescb.ttf', 20)

# Mode, (W,H), color
if length > 170:
    img=Image.new('RGB',(2048,100),color=(60,1,139))
    d=ImageDraw.Draw(img)
    # (x,y), Text, alignment, font, font color
    d.multiline_text((25,30),quote,align="center",font=fnt,fill=(255,255,255))
    d.multiline_text((950,50),author,align="center",font=fnt,fill=(255,255,255))
elif length > 150:
    img=Image.new('RGB',(1720,100),color=(60,1,139))
    d=ImageDraw.Draw(img)
    # (x,y), Text, alignment, font, font color
    d.multiline_text((25,30),quote,align="center",font=fnt,fill=(255,255,255))
    d.multiline_text((750,50),author,align="center",font=fnt,fill=(255,255,255))

img.save(r'C:\Users\Eric.M\Pictures\Quote.png')

