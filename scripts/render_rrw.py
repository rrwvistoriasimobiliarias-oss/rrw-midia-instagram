#!/usr/bin/env python3
"""RRW: produces original animated Reels directly in GitHub Actions.
Only the official logo is extracted from an existing branded cover; no Lovable videos are used.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path
import math, random, subprocess, json, os, io, base64

W,H=720,1280
NAVY=(10,27,49); LIME=(155,212,54); WHITE=(250,252,255); MUTED=(190,207,225)
FONT="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SEED=42
OUT=Path("instagram/reels"); OUT.mkdir(parents=True,exist_ok=True)
SPECS=[
 {"id":"01-vistoria-entrada","topic":"VISTORIA DE ENTRADA","hook":["Essa fissura","já estava aqui?"],"body":["Sem registro,","surgem dúvidas."],"cta":"Documentação faz diferença.","duration":7,"art":"crack"},
 {"id":"02-vistoria-saida","topic":"VISTORIA DE SAÍDA","hook":["Devolver as chaves","encerra tudo?"],"body":["A vistoria de saída","também importa."],"cta":"Compare os registros.","duration":6,"art":"keys"},
 {"id":"03-registro-fotografico","topic":"LAUDO FOTOGRÁFICO","hook":["Só descrever","basta?"],"body":["Fotos dão clareza","ao laudo."],"cta":"Registre cada detalhe.","duration":7,"art":"camera"},
 {"id":"04-apoio-operacional","topic":"APOIO A IMOBILIÁRIAS","hook":["Muitas vistorias.","Pouco tempo?"],"body":["A RRW apoia","sua operação."],"cta":"Apoio em demandas extras.","duration":6,"art":"schedule"},
 {"id":"05-vistoria-profissional","topic":"VISTORIA PROFISSIONAL","hook":["Vistoria não","é só olhar."],"body":["É observar, registrar","e documentar."],"cta":"Qualidade em cada laudo.","duration":7,"art":"checklist"}
]
def font(n,b=True): return ImageFont.truetype(BOLD if b else FONT,n)
def txt(d,xy,s,size=42,color=WHITE,b=True,anchor=None):
    d.text(xy,s,font=font(size,b),fill=color,anchor=anchor,stroke_width=0)
def ease(x):
    x=max(0.,min(1.,x));return x*x*(3-2*x)
def rounded(d,box,r,fill,outline=None,width=1):d.rounded_rectangle(box,radius=r,fill=fill,outline=outline,width=width)
def branding():
    # Asset permanently stored IN THIS REPOSITORY. Independent of Lovable media.
    # Obtained once from RRW's previous official branded material and versioned.
    p=Path("assets/rrw-logo.png")
    if not p.exists():
        raise RuntimeError("Ativo oficial ausente: assets/rrw-logo.png")
    im=Image.open(p).convert("RGBA")
    im.thumbnail((124,100),Image.Resampling.LANCZOS)
    return im
LOGO=branding()

def backdrop(kind):
    im=Image.new("RGB",(W,H),NAVY); d=ImageDraw.Draw(im)
    # refined navy gradients
    for y in range(H):
        f=y/H
        d.line((0,y,W,y), fill=(int(10+f*2),int(27+f*9),int(49+f*11)))
    # quiet geometric detail
    for r in range(130,450,54):
        d.arc((W-190-r,80-r,W-190+r,80+r),195,340,fill=(33,65,88),width=1)
    d.line((52,174,275,174),fill=LIME,width=3)
    d.line((275,174,668,174),fill=(62,85,110),width=2)
    # distinct illustration zone, no logo overlapping illustration
    if kind=="crack":
        # Foto original sintetizada para esta campanha: parede, rodape e fissura
        # capilar. O arquivo-base e versionado no GitHub, sem Lovable.
        source=Path("assets/parede-fissura-fotografica.b64")
        if not source.exists():
            raise RuntimeError("Imagem fotografica original nao encontrada")
        photo=Image.open(io.BytesIO(base64.b64decode(source.read_text().strip()))).convert("RGB")
        # Inserir foto em area separada da marca, preservando proporcao.
        from PIL import ImageOps
        photo=ImageOps.fit(photo,(590,394),method=Image.Resampling.LANCZOS,centering=(0.5,0.52))
        mask=Image.new("L",(590,394),0)
        ImageDraw.Draw(mask).rounded_rectangle((0,0,589,393),radius=20,fill=255)
        im.paste(photo,(65,602),mask)
        d=ImageDraw.Draw(im)
        d.rounded_rectangle((65,602,655,996),radius=20,outline=(95,119,140),width=3)
        txt(d,(79,1026),"IMAGEM ILUSTRATIVA",19,MUTED)
    elif kind=="keys":
        rounded(d,(65,600,655,1010),22,(20,47,74),(65,98,128),2)
        d.rounded_rectangle((340,670,565,940),radius=9,fill=(25,55,80),outline=(190,205,216),width=5)
        d.line((340,670,400,691),fill=(190,205,216),width=5)
        d.ellipse((310,790,405,885),outline=LIME,width=13)
        d.line((396,838,510,838),fill=LIME,width=13)
        d.line((478,838,478,873),fill=LIME,width=12)
        d.line((505,838,505,860),fill=LIME,width=12)
    elif kind=="camera":
        rounded(d,(65,600,655,1010),22,(19,46,72),(65,95,122),2)
        for x in range(80,640,85):
            d.line((x,650,x,970),fill=(38,73,100),width=2)
        d.rounded_rectangle((192,716,530,916),radius=22,fill=(25,59,85),outline=(197,212,220),width=7)
        d.rounded_rectangle((252,685,390,722),radius=8,fill=(197,212,220))
        d.ellipse((292,745,430,883),outline=LIME,width=14)
        d.ellipse((331,784,391,844),outline=(204,215,224),width=5)
        d.ellipse((468,760,493,785),fill=LIME)
    elif kind=="schedule":
        rounded(d,(65,600,655,1010),22,(20,46,72),(67,95,125),2)
        for i in range(4):
            for j in range(5):
                x=104+j*103;y=662+i*78
                d.rounded_rectangle((x,y,x+78,y+54),radius=10,outline=(95,125,151),width=2)
                d.line((x+15,y+20,x+59,y+20),fill=(90,119,143),width=3)
                d.line((x+15,y+35,x+47,y+35),fill=(90,119,143),width=3)
        d.ellipse((444,754,604,914),outline=WHITE,width=6)
        d.line((524,834,568,805),fill=WHITE,width=7)
        d.line((524,834,472,841),fill=LIME,width=7)
        d.ellipse((517,827,531,841),fill=LIME)
    else:
        rounded(d,(65,600,655,1010),22,(19,46,73),(64,96,121),2)
        for i,s in enumerate(["OBSERVAR","REGISTRAR","DOCUMENTAR"]):
            y=696+i*87
            d.ellipse((111,y-16,152,y+25),outline=LIME,width=4)
            d.line((119,y+4,129,y+13),fill=LIME,width=4)
            d.line((129,y+13,146,y-11),fill=LIME,width=4)
            txt(d,(186,y-10),s,30,WHITE)
    return im
def build(spec):
    dur=spec["duration"]; art=spec["art"]; stem=spec["id"]
    bg=backdrop(art)
    base=bg.copy();d=ImageDraw.Draw(base)
    # Stable safe header; logo confined to dedicated region, never over art/text
    rounded(d,(49,32,197,143),20,(17,41,68))
    base.paste(LOGO,(59+(126-LOGO.width)//2,38+(98-LOGO.height)//2),LOGO)
    txt(d,(224,70),"@rrwvistoriasimobiliarias",21,MUTED)
    rounded(d,(52,215,580,267),22,(31,67,76))
    txt(d,(74,227),spec["topic"],23,LIME)
    txt(d,(75,1120),"RRW Vistorias Imobiliárias",31,WHITE)
    txt(d,(75,1164),"Porto Alegre e Região Metropolitana",21,MUTED,b=False)
    # Stop line separating brand signature and CTA
    d.line((75,1090,646,1090),fill=(70,100,124),width=2)
    output=OUT/(stem+".mp4")
    command=["ffmpeg","-hide_banner","-loglevel","error","-y","-f","rawvideo","-pixel_format","rgb24","-video_size",f"{W}x{H}","-framerate","24","-i","-",
    "-f","lavfi","-i","anullsrc=r=44100:cl=stereo",
    "-vf","scale=1080:1920:flags=lanczos,format=yuv420p",
    "-c:v","libx264","-preset","veryfast","-crf","23","-pix_fmt","yuv420p",
    "-c:a","aac","-b:a","96k","-t",str(dur),"-movflags","+faststart","-shortest",str(output)]
    p=subprocess.Popen(command,stdin=subprocess.PIPE)
    total=dur*24
    for i in range(total):
        t=i/24.
        im=base.copy();d=ImageDraw.Draw(im)
        if t<2:
            lines=spec["hook"]; start=2
            fade=ease(min((t+.1)/.42,1))*min(1,(2.04-t)/.24)
            yy=338 + int((1-ease(t/.5))*25)
            size=43 if max(len(x) for x in lines)>19 else 48
            for idx,line in enumerate(lines):
                color=tuple(int(v*fade + NAVY[k]*(1-fade)) for k,v in enumerate(WHITE if idx==0 else LIME))
                txt(d,(75,yy+idx*68),line,size,color)
            # lime accent beneath hook
            d.rounded_rectangle((75,yy+150,75+int(218*ease(t/.7)),yy+156),radius=3,fill=LIME)
        elif t<5:
            fade=ease((t-2)/.35)*min(1,(5.06-t)/.25)
            size=44
            for idx,line in enumerate(spec["body"]):
                color=tuple(int(v*fade + NAVY[k]*(1-fade)) for k,v in enumerate(WHITE if idx==0 else LIME))
                txt(d,(75,358+idx*69),line,size,color)
        else:
            fade=ease((t-5)/.45)
            color=tuple(int(v*fade + NAVY[k]*(1-fade)) for k,v in enumerate(WHITE))
            txt(d,(75,354),"RRW Vistorias",49,color)
            txt(d,(75,422),"Imobiliárias",49,color)
            txt(d,(75,510),spec["cta"],22,LIME)
        # subtle animated scan progress moves across top of image, no moving logo
        prog=(t/dur)
        d.rounded_rectangle((72,1060,72+int(572*prog),1065),radius=2,fill=LIME)
        try: p.stdin.write(im.tobytes())
        except BrokenPipeError: raise RuntimeError("ffmpeg rendering failed")
    p.stdin.close()
    if p.wait()!=0: raise RuntimeError("ffmpeg exit nonzero for "+stem)
    # First-frame cover is deliberately designed for legibility, not a random outro.
    cover=base.copy();d=ImageDraw.Draw(cover)
    for j,line in enumerate(spec["hook"]): txt(d,(75,338+j*68),line,43 if max(map(len,spec["hook"]))>19 else 48,WHITE if j==0 else LIME)
    d.rounded_rectangle((75,486,315,492),radius=3,fill=LIME)
    cover.resize((1080,1920),Image.Resampling.LANCZOS).save(OUT/(stem+".jpg"),quality=94,subsampling=0)
    print(json.dumps({"file":str(output),"duration":dur,"size":output.stat().st_size}))
for s in SPECS: build(s)
