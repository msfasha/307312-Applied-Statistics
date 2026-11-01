"""Measure slide text before authoring; preserve large readable type."""
import json, re, sys
from pathlib import Path
from PIL import Image, ImageFont
MODULE=int(sys.argv[1]) if len(sys.argv)>1 else 1
ROOT=Path.cwd(); BUILD=ROOT/f'20261/_output/.module{MODULE:02d}-teaching-build'
slides=json.loads((BUILD/'slides.json').read_text())
fonts=Path('/usr/share/fonts/truetype/dejavu')
COLORS=dict(plum='#493347',ink='#2F343B',muted='#56616D',pale='#F5EDF4',blue='#356B8C')
def font(size,face):
    return ImageFont.truetype(str(fonts/({'sans':'DejaVuSans.ttf','bold':'DejaVuSans-Bold.ttf','mono':'DejaVuSansMono.ttf'}[face])),size)
def wrap(value,size,face,width):
    f=font(size,face); result=[]
    for line in value.split('\n'):
        if not line: result.append(''); continue
        if f.getlength(line)<=width: result.append(line); continue
        words=line.split(' '); row=''
        for word in words:
            trial=(row+' '+word).strip()
            if f.getlength(trial)>width and row:
                result.append(row); row=word
            else: row=trial
        if row: result.append(row)
    return result
layouts=[]
for slide in slides:
    boxes=[]
    def put(value,x,y,width,size=34,face='sans',color='ink',leading=None,rtl=False,fill=None):
        lines=wrap(value,size,face,width)
        step=leading or round(size*1.32)
        for j,line in enumerate(lines):
            measured=font(size,face).getlength(line)
            assert measured<=width+1,(slide['number'],line,measured,width)
            if line:
                boxes.append(dict(text=line,x=x,y=y+j*step,w=width,h=step,size=size,face=face,color=COLORS[color],rtl=rtl,fill=fill))
        return y+len(lines)*step
    divider=slide['kind']=='divider'
    put(f"MODULE {MODULE}    LESSON {slide['lesson']}",80,34,1300,24,color='muted')
    if divider:
        y=put(slide['title'],80,160,1440,60,'bold','plum',leading=76)
        put(slide['body'],80,y+55,1400,38,leading=58)
    else:
        y=put(slide['title'],80,96,1440,44,'bold','plum',leading=57)
        y=put(slide['body'],80,y+34,1440,32,leading=44)
        if slide['arabic']:
            y=put(slide['arabic'],80,y+16,1440,30,color='ink',leading=43,rtl=True)
        if slide['code']:
            y+=24
            code=[]
            code_size=28 if MODULE==2 and slide.get('code_chunk') else 25
            for line in slide['code'].splitlines():
                if line.startswith('# '):
                    parts=wrap(line[2:],code_size,'mono',1390)
                    code.extend('# '+p for p in parts)
                else:
                    assert font(code_size,'mono').getlength(line)<=1440,(slide['number'],'wrap the Quarto code line',line)
                    code.append(line)
            step=36 if code_size==28 else 32
            if y+len(code)*step>799:
                # Give code more vertical room by keeping prose light, not by shrinking it.
                step=34 if code_size==28 else 30
            assert y+len(code)*step<=802,(slide['number'],slide['title'],y,len(code),step)
            for line in code:
                y=put(line,80,y,1440,code_size,'mono','muted' if line.startswith('#') else 'blue',leading=step)
        if slide['hint'] and not slide['plot'] and not slide['image']:
            hintlines=wrap(slide['hint'],23,'sans',1440)
            # Cues occupy a separate readable band above the source footer.
            hint_y=max(y+20,756)
            assert hint_y+len(hintlines)*30<=842,(slide['number'],'hint',hint_y,hintlines)
            put(slide['hint'],80,hint_y,1440,23,color='muted',leading=30)
        path=None
        if slide['plot']:
            path=f'20261/assets/module{MODULE:02d}/teaching-slides/'+slide['plot']+'.png'
        elif slide['image']:
            path=slide['image']
        if path:
            top=y+18
            bottom=805 if not slide['hint'] else 777
            if slide['hint']: put(slide['hint'],80,791,1440,20,color='muted',leading=25)
            image_path=ROOT/path
            if image_path.suffix=='.svg':
                import cairosvg
                target=BUILD/(image_path.stem+'.png')
                cairosvg.svg2png(url=str(image_path),write_to=str(target),output_width=1800)
                path=str(target.relative_to(ROOT))
            w,h=Image.open(ROOT/path).size
            ratio=min(1440/w,(bottom-top)/h)
            assert ratio>0,(slide['number'],top,bottom)
            iw,ih=w*ratio,h*ratio
            slide['image_layout']=dict(path=path,x=80+(1440-iw)/2,y=top,w=iw,h=ih)
        if slide.get('table'):
            rows=len(slide['table'])
            height=min(500,(740 if slide["hint"] else 792)-y-24)
            assert height/rows>=38,(slide['number'],'table rows',rows,height)
            slide['table_layout']=dict(x=80,y=y+24,w=1440,h=height)
        if slide['kind']=='patient-table':
            slide['table_layout']=dict(x=80,y=y+35,w=1440,h=310)
    label=re.sub(r'[`*]','',slide['heading'])
    if label.startswith('Miscellaneous Related Topics'): label='Miscellaneous related topics'
    if label=='__intro__': label='Overview'
    footer=f"Quarto: {slide['source'][:-4]} / {label}"
    put(footer,80,860,1355,18,color='muted',leading=22)
    put(str(slide['number']),1470,856,60,23,color='muted')
    for b in boxes:
        assert b['y']+b['h']<=900 and b['x']+b['w']<=1600,(slide['number'],b)
    layouts.append(dict(**slide,boxes=boxes))
(BUILD/'layouts.json').write_text(json.dumps(layouts,ensure_ascii=False,indent=2))
print('Measured',len(layouts),'slides; text fits the intended slide frames.')
