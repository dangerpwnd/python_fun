from PIL import Image, ImageDraw, ImageFont
import requests, json
import random
from dictor import dictor

ran=random.randrange(1,1643)

with requests.get("https://type.fit/api/quotes", headers={'User-agent': 'Mozilla/5.0'}) as url:
    data=json.loads(url.text)
    quote=dictor(data, str(ran) + '.text', default="Missing Quote")
    author=dictor(data, str(ran) + '.author', default="Missing Author")


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
img.save(r'C:\Users\eric.m\AppData\Roaming\Microsoft\Signatures\Eric SysAdmin_files\image001.png')
img.save(r'C:\Users\eric.m\AppData\Roaming\Microsoft\Signatures\Eric SysAdmin_files\image002.jpg')

