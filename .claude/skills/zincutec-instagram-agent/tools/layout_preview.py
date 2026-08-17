from PIL import Image, ImageDraw, ImageFont
W,H = 1080,1350
GROUND=(246,246,246); INK=(26,26,26); GREY=(122,122,122)
R="/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
I="/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf"
f=lambda p,s: ImageFont.truetype(p,s)
page=Image.new("RGB",(W,H),GROUND); d=ImageDraw.Draw(page)
M=80  # Seitenrand

def track(draw,xy,text,font,fill,sp=0,anchor_right=False):
    w=sum(draw.textlength(c,font=font)+sp for c in text)-sp
    x,y=xy
    if anchor_right: x-=w
    for c in text:
        draw.text((x,y),c,font=font,fill=fill); x+=draw.textlength(c,font=font)+sp
    return w

# Kopfzeile
track(d,(M,86),"ZinCuTec",f(R,19),INK,sp=3.2)
track(d,(W-M,86),"TURNING METAL INTO ART.",f(R,15),GREY,sp=1.9,anchor_right=True)

# Bild — volle Breite zwischen den Rändern, Proportion erhalten
im=Image.open("kinko35.jpg").convert("RGB")
iw=W-2*M; ih=round(iw*im.height/im.width)
page.paste(im.resize((iw,ih),Image.LANCZOS),(M,210))

# Textspalte, rechtsbündig, große vertikale Abstände
base=210+ih
d.text((W-M,base+150),"KINKO",font=f(R,104),fill=INK,anchor="ra")
d.text((W-M,base+292),"Messing brüniert",font=f(R,31),fill=INK,anchor="ra")
d.text((W-M,base+404),"Neun Platten, eine Achse.",font=f(I,37),fill=GREY,anchor="ra")

page.save("KINKO_4x5_layout.jpg",quality=94)
print("ok  Bildhöhe:",ih,"| Textbeginn y:",base)
