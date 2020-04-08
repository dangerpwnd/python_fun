from PIL import Image, ImageDraw, ImageFont
import urllib.request, json
from dictor import dictor

with urllib.request.urlopen("http://quotes.rest/qod.json?category=inspire") as url:
    data = json.loads(url.read().decode())
    quote = dictor(data, 'contents.quotes.0.quote', default="Missing Quote")
    author = dictor(data, 'contents.quotes.0.author', default="Missing Author")


fnt=ImageFont.truetype(r'C:\Windows\Fonts\segoepr.ttf', 24)
fntsizequote=list(fnt.getsize(quote))
fntsizeauthor=list(fnt.getsize(author))
fntsizew=fntsizequote[0]
fntsizeh=fntsizequote[1] + fntsizeauthor[1]
fntsizea=fntsizequote[0] - fntsizeauthor[0] - 25
img=Image.new('RGB', (fntsizew,fntsizeh), (255,255,255))
draw=ImageDraw.Draw(img)
draw.multiline_text((0,0),quote,font=fnt,fill=(0,0,0))
draw.multiline_text((fntsizea,30),author,font=fnt,fill=(0,0,0))
img.save(r'C:\Users\Eric.M\Pictures\Quote.png')
