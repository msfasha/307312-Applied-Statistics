#!/usr/bin/env python3
"""Read-only extraction of original inferential slide titles and heading labels."""
from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as ET
import re, json, hashlib, posixpath
ROOT=Path(__file__).resolve().parents[1]
NS={'p':'http://schemas.openxmlformats.org/presentationml/2006/main',
    'a':'http://schemas.openxmlformats.org/drawingml/2006/main',
    'r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}

def paragraph(p):
    out=[]
    for e in p:
        tag=e.tag.split('}')[-1]
        if tag=='br':out.append('\n')
        elif tag in ['r','fld']:out.append(''.join(t.text or '' for t in e.findall('.//a:t',NS)))
    return ''.join(out)

def compact(s):return re.sub(r'\s+',' ',s).strip()
def unique(values):return list(dict.fromkeys(v for v in values if v))
def display(s):return s.replace('|','\\|').replace('\n','<br>')

all_decks=[]
for part,count in enumerate([37,26,57,21],1):
    path=ROOT/f'sources/slides/307102-inferential-{part:02}-original.pptx'
    before=hashlib.sha256(path.read_bytes()).hexdigest()
    with ZipFile(path) as z:
        pres=ET.fromstring(z.read('ppt/presentation.xml'))
        rels=ET.fromstring(z.read('ppt/_rels/presentation.xml.rels'))
        targets={r.get('Id'):posixpath.normpath('ppt/'+r.get('Target')) for r in rels}
        ordered=[targets[s.get('{'+NS['r']+'}id')] for s in pres.findall('p:sldIdLst/p:sldId',NS)]
        assert len(ordered)==count
        slides=[]
        for number,name in enumerate(ordered,1):
            root=ET.fromstring(z.read(name));titles=[];subtitles=[];labels=[];native=[]
            for sp in root.findall('.//p:sp',NS):
                body=sp.find('p:txBody',NS)
                if body is None:continue
                paragraphs=body.findall('a:p',NS)
                raw='\n'.join(paragraph(p) for p in paragraphs if paragraph(p).strip())
                if not raw.strip():continue
                ph=sp.find('p:nvSpPr/p:nvPr/p:ph',NS)
                typ=ph.get('type','body') if ph is not None else 'text box'
                native.append({'placeholder_type':typ,'text':raw})
                if typ in ['title','ctrTitle']:titles.append(raw);continue
                if typ=='subTitle':subtitles.append(raw);continue
                if 'import numpy' in raw or 'from distfit' in raw:continue
                for p in paragraphs:
                    whole=paragraph(p).strip()
                    if re.match(r'^[1-5]\.\s+[A-Z]',whole) and len(whole)<90 and not whole.endswith('.'):
                        labels.append(whole);continue
                    buf='';started=False
                    for run in p.findall('a:r',NS):
                        text=''.join(t.text or '' for t in run.findall('a:t',NS))
                        props=run.find('a:rPr',NS)
                        if not text.strip():
                            if started:buf+=text
                            continue
                        if props is not None and props.get('b')=='1':buf+=text;started=True
                        else:break
                    label=compact(buf)
                    # Keep short leading labels, not complete bold instructions/code.
                    if label and len(label)<120 and not label.endswith('.') and not label.startswith(('Excel Function','Confidence level=')):
                        labels.append(label)
                # Divider body subtitles are explicit short text blocks.
                if typ=='body' and len(paragraphs)==1 and len(compact(raw))<125 and not raw.endswith('.'):
                    if (part,number) in [(1,7),(1,11),(3,11)]:subtitles.append(raw)
            # Actual table category labels are useful subheadings, not invented titles.
            if part==3 and number in [4,5]:
                for table in root.findall('.//a:tbl',NS):
                    for row in table.findall('a:tr',NS)[1:]:
                        first=row.find('a:tc',NS)
                        val=compact(''.join(t.text or '' for t in first.findall('.//a:t',NS))) if first is not None else ''
                        if val:labels.append(val)
            note=''
            if not titles:
                if (part,number)==(1,32):
                    titles=['Z-Tables'];note='Visible divider title in an ordinary text box, verified against the source render.'
                elif (part,number)==(3,5):note='No slide title. Continuation of the business-example table on slide 4; verified against the source render.'
                else:note='No native title placeholder; inspect visual source before assigning a title.'
            # Multi-line title placeholders preserve their separate lines as given.
            title_lines=[line for title in titles for line in title.split('\n') if line.strip()]
            if part==2 and number==14:note='Duplicated/corrupted title text is present in the original; preserved verbatim.'
            slides.append({'slide':number,'title_text':titles,'title_lines':title_lines,
                'subtitle_text':unique(subtitles),'internal_heading_labels':unique(labels),
                'note':note,'native_text_blocks':native})
    assert hashlib.sha256(path.read_bytes()).hexdigest()==before
    all_decks.append({'part':part,'source':str(path.relative_to(ROOT)),'sha256':before,
        'slide_count':count,'section_title':compact(slides[0]['subtitle_text'][0]),'slides':slides})

out=ROOT/'instructor/inferential-original-slide-outline'
out.with_suffix('.json').write_text(json.dumps(all_decks,ensure_ascii=False,indent=2)+'\n')
lines=['# Original inferential slides: titles, subtitles and sequence','',
'Extracted directly from the four unchanged original PPTX decks, in presentation order. This is an extraction of the source structure, not the revised lesson.', '',
'## How to read this outline','',
'- The four deck subtitles identify the four main sections. Their shared cover title is the historical source-course identity, not the current course identity.',
'- Title line breaks are retained as separate lines. Repeated titles, original capitalization and source mistakes are preserved.',
'- “Subtitle / internal labels” distinguishes explicit subtitles from short leading labels inside the slide. Labels are not promoted to new sections.',
'- The extraction excludes body explanations, formulas, chart axes, data-table values and ordinary bullet text. The JSON companion also retains the native text blocks for checking.',
'- Text baked into images is not presented as a verified exhaustive subtitle extraction. Two structural exceptions were visually checked: probability slide 32 and hypothesis-testing slide 5.', '',
'## Deck sequence','', '| Order | Original deck subtitle | Slides |', '|---|---|---|']
for d in all_decks:lines.append(f'| {d["part"]} | {d["section_title"]} | {d["slide_count"]} |')
for d in all_decks:
    lines += ['',f'## {d["part"]}. {d["section_title"]}', '',f'Source: `{d["source"]}`. Slide numbering restarts at 1 in this deck.', '',
              '| Slide | Original title / title lines | Subtitle / internal labels | Source note |','|---|---|---|---|']
    for s in d['slides']:
        title='<br>'.join(display(t) for t in s['title_text']) or '—'
        subs=['**Subtitle:** '+display(t) for t in s['subtitle_text']]
        if s['internal_heading_labels']:subs.append('**Inside slide:** '+'; '.join(display(t) for t in s['internal_heading_labels']))
        lines.append(f'| {s["slide"]} | {title} | {"<br>".join(subs) or "—"} | {s["note"]} |')
lines += ['', '## Extraction notes for the next stage','',
'- The backbone is the topic sequence. A repeated heading can cover a definition, example, software implementation and interpretation across adjacent slides.',
'- Keep those teaching roles visible when planning the rewrite; the title alone does not always identify the role.',
'- Probability slides 14, 16, 18 and 22 contain multi-line title hierarchies. Those lines are not separate slides.',
'- Hypothesis-testing slide 5 has no heading. It must not be silently assigned a new source title.',
'- Estimation slide 14 contains a corrupted heading, and slide 16 calls a simulation an “Empirical Proof”. These are source wording issues to revisit later, not wording adopted as validated.',
'- Several regression slides share “Assumptions of Linear Regression”; their internal labels supply the five distinct assumptions and diagnostic sequence.',
'- No course notebook, teaching content or source presentation was edited by this extraction.']
out.with_suffix('.md').write_text('\n'.join(lines)+'\n')
print('Extracted',sum(d['slide_count'] for d in all_decks),'slides into',out.with_suffix('.md'))
