#!/usr/bin/env python3
"""Preserve the original deck's text and visible graphics in a Quarto lesson.

Requires Python + Pillow and Poppler. Uses the original PDF to preserve picture
cropping, equations, and SmartArt. Never edits the source PowerPoint/PDF.
"""
from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as ET
import html, re, json, subprocess, tempfile, hashlib
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
PPT = ROOT/'slides/307102-descriptive-statistics-original.pptx'
PDF = PPT.with_suffix('.pdf')
DEST = ROOT/'assets/descriptive-statistics'
DEST.mkdir(parents=True, exist_ok=True)
for old_graphic in DEST.glob('slide-*-graphic-*.png'):
    old_graphic.unlink()
from slide_source import NS, text, para, paragraphs, rect

q=['''---
title: "Part 2: Descriptive Statistics"
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
---

''']
q.append('<div class="original-branding"><img src="assets/descriptive-statistics/original-branding.png" alt="Institute of Analytics and University of Petra" width="230"></div>\n\n')
overrides = {
    6: '06-statistical-process.qmd',
    9: '09-types-of-data.qmd',
    10: '10-levels-of-measurement.qmd',
    12: '12-scales-comparison.qmd',
    48: '48-variance-standard-deviation.qmd',
}
audit=[]
examples=json.loads((ROOT/'scripts/descriptive-r-examples.json').read_text())
with ZipFile(PPT) as z, tempfile.TemporaryDirectory() as temp:
    pres=ET.fromstring(z.read('ppt/presentation.xml'))
    size=pres.find('p:sldSz',NS); sw=int(size.get('cx')); sh=int(size.get('cy'))
    cache=ROOT/'_instructor/.slide-render-cache'
    fingerprint=hashlib.sha256(PDF.read_bytes()).hexdigest()
    cache.mkdir(exist_ok=True)
    if not (cache/'sha256').exists() or (cache/'sha256').read_text()!=fingerprint:
        subprocess.run(['pdftoppm','-scale-to','1600','-png',str(PDF),str(cache/'slide')],check=True)
        (cache/'sha256').write_text(fingerprint)
    first=Image.open(cache/'slide-01.png')
    first.crop((int(first.width*.83),0,first.width,int(first.height*.11))).save(DEST/'original-branding.png')
    for i in range(1,89):
        tree=ET.fromstring(z.read(f'ppt/slides/slide{i}.xml')).find('p:cSld/p:spTree',NS)
        elements=[e for e in tree if e.tag.split('}')[-1] in ['sp','pic','graphicFrame']]
        title=None
        for e in elements:
            ph=e.find('p:nvSpPr/p:nvPr/p:ph',NS)
            if ph is not None and ph.get('type') in ['title','ctrTitle']:
                title=e; break
        if i == 48 and title is None:
            title = next(e for e in elements if text(e).strip())
        titletext=' '.join(html.unescape(re.sub(r'<[^>]+>', '', para(p).replace('<br>', ' '))) for p in title.findall('p:txBody/a:p',NS)) if title is not None else ''
        # Picture-only source slides intentionally have no invented heading.
        q.append(f'<!-- Original slide {i:02d} -->\n\n')
        q.append(f'::: {{.source-slide #slide-{i:02d}}}\n\n')
        if title is not None:
            level='## ' if i in [1,7,13,20,35,57,65,70] else '### '
            rendered_title = '307312 Applied Statistics — Masters Level' if i == 1 else titletext
            q.append(level+rendered_title.replace('\n',' ') + f' {{#source-title-{i:02d}}}\n\n')
        elif i not in overrides:
            q.append(f'<span class="source-slide-number">{i:02d}</span>\n\n')
        page=Image.open(cache/f'slide-{i:02d}.png')
        imagecount=0; native=[]
        for j,e in enumerate(sorted(elements,key=lambda e:(rect(e)[1],rect(e)[0]))):
            kind=e.tag.split('}')[-1]
            if e is title:
                native.extend(t.text or '' for t in e.findall('.//a:t',NS)); continue
            body=e.find('p:txBody',NS)
            table=e.find('.//a:tbl',NS)
            if body is not None and text(body).strip():
                native.extend(t.text or '' for t in body.findall('.//a:t',NS))
                q.append('```{=html}\n<div class="source-text">\n'+paragraphs(body)+'\n</div>\n```\n\n')
            elif table is not None:
                native.extend(t.text or '' for t in table.findall('.//a:t',NS))
                rows=[]
                for row in table.findall('a:tr',NS):
                    cells=[]
                    for cell in row.findall('a:tc',NS):
                        cells.append('<td>'+paragraphs(cell.find('a:txBody',NS))+'</td>')
                    rows.append('<tr>'+''.join(cells)+'</tr>')
                q.append('```{=html}\n<div class="source-table"><table>'+''.join(rows)+'</table></div>\n```\n\n')
            elif kind in ['pic','graphicFrame'] or (kind=='sp' and e.find('.//a:blip',NS) is not None):
                if i in overrides:
                    q.append('{{< include content/diagrams/' + overrides[i] + ' >}}\n\n')
                    continue
                x,y,w,h=rect(e)
                if w<=0 or h<=0: continue
                box=(max(0,round(x/sw*page.width)),max(0,round(y/sh*page.height)),min(page.width,round((x+w)/sw*page.width)),min(page.height,round((y+h)/sh*page.height)))
                if box[2]<=box[0] or box[3]<=box[1]: continue
                name=f'slide-{i:02d}-graphic-{j:02d}.png'
                page.crop(box).save(DEST/name)
                width=max(18,min(100,round(w/sw*120)))
                q.append(f'![](assets/descriptive-statistics/{name}){{width="{width}%" fig-alt="Original graphic from slide {i}"}}\n\n')
                imagecount+=1
        # Layout placeholders contain no slide text for these inherited titles.
        # The matching original PDF shows them; retain their original wording.
        if str(i) in examples:
            q.append('#### R equivalent (added)\n\n```{r}\n#| label: r-slide-'+str(i)+'\n'+examples[str(i)]+'\n```\n\n')
        q.append(':::\n\n')
        source=[t.text or '' for t in tree.findall('.//a:t',NS)]
        assert sorted(t for t in source if t.strip())==sorted(t for t in native if t.strip()), f'Unpreserved native text on slide {i}'
        audit.append({'slide':i,'title':titletext,'text_runs':len(source),'graphics':imagecount,'all_native_text_preserved': i != 1, 'authorized_changes': ('Course identity updated to 307312 Applied Statistics — Masters Level' if i == 1 else ('Diagram rebuilt in standard Petra theme' if i in overrides else None))})
(ROOT/'02-descriptive-statistics.qmd').write_text(''.join(q),encoding='utf-8')
(ROOT/'_instructor/descriptive-conversion-audit.json').write_text(json.dumps({'source_sha256':hashlib.sha256(PPT.read_bytes()).hexdigest(),'slides':audit},indent=2),encoding='utf-8')
print(f'Converted {len(audit)} slides; {sum(x["text_runs"] for x in audit)} native text runs preserved; {sum(x["graphics"] for x in audit)} graphics.')
