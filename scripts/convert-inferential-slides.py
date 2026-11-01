#!/usr/bin/env python3
"""Convert all four original inferential decks without changing source files."""
from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as ET
import html, re, json, subprocess, hashlib, csv, io, posixpath
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
from slide_source import NS, text, para, paragraphs, rect
DEST=ROOT/'assets/inferential-statistics';DEST.mkdir(exist_ok=True)
DATA=ROOT/'data/inferential-statistics';DATA.mkdir(exist_ok=True)
for p in DEST.glob('part-*-graphic-*.png'):p.unlink()
examples=json.loads((ROOT/'scripts/inferential-r-examples.json').read_text())
manifest=json.loads((ROOT/'slides/inferential-source-provenance.json').read_text())
titles=['Introduction to Probability Distributions','Introduction to Estimation in Statistics','Introduction to Hypothesis Testing','Introduction to Linear Regression']
q=['''---
title: "Part 3: Inferential Statistics"
subtitle: "307312 Applied Statistics — Masters Level"
format:
  html:
    toc: true
    toc-depth: 2
    code-tools: true
    code-copy: true
    code-overflow: wrap
    lightbox: true
    embed-resources: true
    html-math-method: mathml
execute:
  echo: true
  warning: false
  message: false
  fig-width: 7
  fig-height: 4.5
---

[Download this part as PDF](pdf/03-inferential-statistics.pdf){.pdf-download}

<div class="original-branding"><img src="assets/descriptive-statistics/original-branding.png" alt="Institute of Analytics and University of Petra" width="230"></div>

''']
audit=[];table_records={};csv_provenance=[]
def bounds(e):
    nodes=e.findall('.//p:spPr/a:xfrm',NS)+e.findall('.//p:xfrm',NS)+e.findall('.//p:grpSpPr/a:xfrm',NS)
    if e.tag.endswith('grpSp'):
        group=e.find('p:grpSpPr/a:xfrm',NS)
        if group is not None: nodes=[group]
    boxes=[]
    for n in nodes:
        off=n.find('a:off',NS);ext=n.find('a:ext',NS)
        if off is not None and ext is not None:boxes.append(tuple(int(a.get(k,'0')) for a,k in [(off,'x'),(off,'y'),(ext,'cx'),(ext,'cy')]))
    if not boxes:return rect(e)
    x=min(b[0] for b in boxes);y=min(b[1] for b in boxes)
    return x,y,max(b[0]+b[2] for b in boxes)-x,max(b[1]+b[3] for b in boxes)-y
for m in manifest:
    k=m['part'];ppt=ROOT/'slides'/(m['copy']+'.pptx');pdf=ppt.with_suffix('.pdf')
    m['sha256']=hashlib.sha256(ppt.read_bytes()).hexdigest()
    render_dir=ROOT/'_instructor/.inferential-render-cache/fresh-pdf'
    render_dir.mkdir(parents=True,exist_ok=True)
    pdf=render_dir/(m['copy']+'.pdf')
    marker=pdf.with_suffix('.source-sha256')
    if not pdf.exists() or not marker.exists() or marker.read_text()!=m['sha256']:
        subprocess.run(['soffice','-env:UserInstallation=file:///tmp/307312-inferential-lo-profile',
                        '--headless','--convert-to','pdf','--outdir',str(render_dir),str(ppt)],check=True)
        marker.write_text(m['sha256'])
    m['graphic_source']='Embedded pictures extracted directly; other figures use a fresh LibreOffice render. Historical companion PDF is not used.'
    cache=ROOT/f'_instructor/.inferential-render-cache/{k}';cache.mkdir(parents=True,exist_ok=True)
    fingerprint=hashlib.sha256(pdf.read_bytes()).hexdigest()
    if not (cache/'sha256').exists() or (cache/'sha256').read_text()!=fingerprint:
        subprocess.run(['pdftoppm','-scale-to','1600','-png',str(pdf),str(cache/'slide')],check=True)
        (cache/'sha256').write_text(fingerprint)
    with ZipFile(ppt) as z:
        size=ET.fromstring(z.read('ppt/presentation.xml')).find('p:sldSz',NS)
        sw=int(size.get('cx'));sh=int(size.get('cy'))
        for i in range(1,m['slides']+1):
            relationships=ET.fromstring(z.read(f'ppt/slides/_rels/slide{i}.xml.rels'))
            targets={r.get('Id'):posixpath.normpath('ppt/slides/'+r.get('Target','')) for r in relationships}
            tree=ET.fromstring(z.read(f'ppt/slides/slide{i}.xml')).find('p:cSld/p:spTree',NS)
            elements=[e for e in tree if e.tag.split('}')[-1] not in ['nvGrpSpPr','grpSpPr','extLst']]
            q.append(f'<!-- Original deck {k}, slide {i} -->\n\n::: {{.source-slide #part3-{k:02d}-slide-{i:02d}}}\n\n')
            if i==1:
                q.append(f'## 3.{k} {titles[k-1]} {{#part3-{k:02d}}}\n\n:::\n\n')
                audit.append({'part':k,'slide':i,'authorized_change':'Source cover replaced by current course identity and subsection title.'});continue
            title=None
            for e in elements:
                ph=e.find('p:nvSpPr/p:nvPr/p:ph',NS)
                if ph is not None and ph.get('type') in ['title','ctrTitle']:title=e;break
            if title is None:
                candidates=[e for e in elements if e.tag.endswith('}sp') and text(e).strip() and bounds(e)[1]<sh*.26 and len(text(e))<220]
                if candidates:title=min(candidates,key=lambda e:bounds(e)[1])
            if title is not None:
                titletext=' '.join(html.unescape(re.sub(r'<[^>]+>','',para(p).replace('<br>',' '))) for p in title.findall('p:txBody/a:p',NS))
                q.append('### '+titletext+f' {{#part3-title-{k:02d}-{i:02d}}}\n\n')
            page=Image.open(cache/f'slide-{i:02d}.png');native=[];graphic_text=[];count=0;tables=[]
            for j,e in enumerate(sorted(elements,key=lambda e:(bounds(e)[1],bounds(e)[0]))):
                runs=[t.text or '' for t in e.findall('.//a:t',NS)]
                if e is title:native.extend(runs);continue
                kind=e.tag.split('}')[-1];body=e.find('p:txBody',NS);table=e.find('.//a:tbl',NS)
                if body is not None and text(body).strip():
                    native.extend(runs)
                    if (k,i) in [(1,31),(2,16)] and ('import ' in text(body)):
                        code='\n'.join(html.unescape(re.sub(r'<[^>]+>','',para(p).replace('<br>','\n'))) for p in body.findall('a:p',NS))
                        q.append('#### Original Python example\n\n```python\n'+code.replace('\xa0',' ')+'\n```\n\n')
                    else:
                        q.append('```{=html}\n<div class="source-text">\n'+paragraphs(body)+'\n</div>\n```\n\n')
                elif table is not None:
                    native.extend(runs);rows=[];values=[]
                    for row in table.findall('a:tr',NS):
                        cells=row.findall('a:tc',NS)
                        values.append([text(c) for c in cells])
                        rows.append('<tr>'+''.join('<td>'+paragraphs(c.find('a:txBody',NS))+'</td>' for c in cells)+'</tr>')
                    tables.append(values)
                    q.append('```{=html}\n<div class="source-table"><table>'+''.join(rows)+'</table></div>\n```\n\n')
                elif kind in ['pic','graphicFrame','grpSp','AlternateContent'] or e.find('.//a:blip',NS) is not None:
                    graphic_text.extend(runs)
                    # A tiny ink compatibility fallback is not a visible teaching graphic.
                    if kind=='AlternateContent' and any(n.get('name','').startswith('Ink ') for n in e.iter()): continue
                    x,y,w,h=bounds(e)
                    if w<=0 or h<=0:continue
                    box=(max(0,round(x/sw*page.width)),max(0,round(y/sh*page.height)),min(page.width,round((x+w)/sw*page.width)),min(page.height,round((y+h)/sh*page.height)))
                    if box[2]<=box[0] or box[3]<=box[1]:continue
                    name=f'part-{k:02d}-slide-{i:02d}-graphic-{j:02d}.png'
                    graphic=None
                    if kind=='pic':
                        blip=e.find('.//a:blip',NS)
                        if blip is not None:
                            media=targets.get(blip.get('{'+NS['r']+'}embed'))
                            if media:
                                try:
                                    graphic=Image.open(io.BytesIO(z.read(media))).convert('RGBA')
                                    crop=e.find('p:blipFill/a:srcRect',NS)
                                    if crop is not None:
                                        l,t,r,b=[int(crop.get(v,'0'))/100000 for v in ['l','t','r','b']]
                                        graphic=graphic.crop((round(l*graphic.width),round(t*graphic.height),round((1-r)*graphic.width),round((1-b)*graphic.height)))
                                    transform=e.find('p:spPr/a:xfrm',NS)
                                    if transform is not None:
                                        if transform.get('flipH')=='1':graphic=graphic.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
                                        if transform.get('flipV')=='1':graphic=graphic.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
                                        if transform.get('rot'):graphic=graphic.rotate(-int(transform.get('rot'))/60000,expand=True)
                                except (OSError,ValueError): graphic=None
                    if graphic is None:graphic=page.crop(box)
                    graphic.save(DEST/name);count+=1
                    q.append(f'![](assets/inferential-statistics/{name}){{width="{max(30,min(100,round(w/sw*120)))}%" fig-alt="Original graphic, section 3.{k}, slide {i}"}}\n\n')
                else:graphic_text.extend(runs)
            table_records[f'{k}-{i}']=tables
            key=f'{k}-{i}'
            if key in examples:q.append(f'#### R equivalent (added)\n\n```{{r}}\n#| label: inferential-{key}\n'+examples[key]+'\n```\n\n')
            q.append(':::\n\n')
            source=[t.text or '' for t in tree.findall('.//a:t',NS)]
            assert sorted(t for t in source if t.strip())==sorted(t for t in native+graphic_text if t.strip()),f'Missing source text: {k}-{i}'
            audit.append({'part':k,'slide':i,'native_text_runs':len(native),'graphic_text_runs':len(graphic_text),'graphics':count,'source_text_accounted_for':True})
# Teaching CSVs are transcribed mechanically from the native source tables.
exports=[('3-27',2,2,'paired_scores.csv',['observation','score1','score2']),('3-29',0,1,'graduate_salaries.csv',['observation','male','female']),('3-31',0,1,'female_major_salaries.csv',['observation','political_science','social_science']),('3-53',0,1,'teaching_methods.csv',['student','group','score']),('3-56',0,1,'teaching_gender.csv',['gender','method','score']),('4-14',0,1,'houses.csv',['house_id','price','size','bedrooms','age','location'])]
for key,index,start,name,header in exports:
    candidates=table_records[key]
    selected=max(candidates,key=len)
    index=candidates.index(selected)
    rows=selected[1:] if key=='3-56' else [row for row in selected if row and row[0].isdigit()]
    clean=[[re.sub(r'[$,]','',v) for v in row] for row in rows]
    with (DATA/name).open('w',newline='') as f:
        writer=csv.writer(f);writer.writerow(header);writer.writerows(clean)
    with (DATA/name).open() as f:assert list(csv.reader(f))[1:]==clean
    csv_provenance.append({'file':name,'source_part_slide':key,'table_index':index,'rows':len(rows),'columns':header,'transformations':'Header labels simplified; dollar symbols and thousands separators removed. Row order and numeric precision retained. Salary currency conflict retained for instructor review.'})
(ROOT/'03-inferential-statistics.qmd').write_text(''.join(q))
(DATA/'provenance.json').write_text(json.dumps(csv_provenance,indent=2)+'\n')
(ROOT/'_instructor/inferential-conversion-audit.json').write_text(json.dumps({'sources':manifest,'slides':audit},indent=2)+'\n')
print(f'Converted {len(audit)} source slides, {sum(x.get("graphics",0) for x in audit)} graphics, {len(examples)} executable R cells; exported six checked CSVs.')
