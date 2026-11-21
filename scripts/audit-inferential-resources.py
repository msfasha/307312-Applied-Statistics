#!/usr/bin/env python3
"""Read original PPTX links and decode their embedded QR codes; write audit output under _build/.
Maintainer dependencies: lxml, pillow, zxing-cpp. Original source decks are never changed.
Run from the course root.
"""
from zipfile import ZipFile
from pathlib import Path
from lxml import etree
import re,json,io,posixpath
from PIL import Image
import zxingcpp
ns={'a':'http://schemas.openxmlformats.org/drawingml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
Path('_build').mkdir(exist_ok=True)
records=[]; qr=[]
for k in range(1,5):
 with ZipFile(f'sources/slides/307102-inferential-{k:02}-original.pptx') as z:
  decoded={}
  for n in z.namelist():
   if n.startswith('ppt/media/'):
    try:
     raw=Image.open(io.BytesIO(z.read(n))).convert('RGBA')
     im=Image.new('RGB',raw.size,'white');im.paste(raw,mask=raw.getchannel('A'))
     codes=zxingcpp.read_barcodes(im)
     if not codes and im.width<800:codes=zxingcpp.read_barcodes(im.resize((im.width*3,im.height*3)))
     if codes:decoded[n]=[c.text for c in codes]
    except Exception:pass
  for n in z.namelist():
   m=re.fullmatch(r'ppt/slides/slide(\d+).xml',n)
   if not m:continue
   num=int(m[1]);t=etree.fromstring(z.read(n));texts=t.xpath('//a:t/text()',namespaces=ns)
   urls=[]
   rel=f'ppt/slides/_rels/slide{num}.xml.rels'
   if rel in z.namelist():
    for r in etree.fromstring(z.read(rel)):
     if r.get('Type','').endswith('/hyperlink'):urls.append(r.get('Target'))
     if r.get('Type','').endswith('/image'):
      media=posixpath.normpath(posixpath.join('ppt/slides',r.get('Target')))
      for code in decoded.get(media,[]):
       qr.append({'deck':k,'slide':num,'media':media,'url':code});urls.append(code)
   for text in texts:urls+=re.findall(r'https?://[^\s<>]+',text)
   for url in dict.fromkeys(urls):records.append({'deck':k,'slide':num,'title':texts[0] if texts else '', 'url':url})
Path('_build/original-inferential-link-audit.json').write_text(json.dumps(records,indent=2)+'\n')
Path('_build/original-inferential-qr-audit.json').write_text(json.dumps(qr,indent=2)+'\n')
print('Occurrences:',len(records),'Unique URLs:',len(set(r['url'] for r in records)))
for r in qr: print('QR:',r)
for u in dict.fromkeys(r['url'] for r in records):print(u)

# The converter retained picture pixels but re-encoded the PNGs, so match pixels,
# rather than file bytes, when recovering click targets on original References icons.
import hashlib

def pixel_key(data):
    image=Image.open(io.BytesIO(data)).convert('RGBA')
    return (image.size,hashlib.sha256(image.tobytes()).hexdigest())

assets={}
for path in Path('assets/inferential-statistics').glob('part-*.png'):
    assets.setdefault(pixel_key(path.read_bytes()),[]).append(path.as_posix())
picture_links=[]
for deck in range(1,5):
    with ZipFile(f'sources/slides/307102-inferential-{deck:02}-original.pptx') as archive:
        for name in archive.namelist():
            match=re.fullmatch(r'ppt/slides/slide(\d+).xml',name)
            if not match:continue
            slide=int(match[1]);rel=f'ppt/slides/_rels/slide{slide}.xml.rels'
            if rel not in archive.namelist():continue
            relationships={r.attrib['Id']:r.attrib for r in etree.fromstring(archive.read(rel))}
            tree=etree.fromstring(archive.read(name))
            for pic in tree.xpath('//*[local-name()="pic"]'):
                clicks=pic.findall('.//a:hlinkClick',ns);blip=pic.find('.//a:blip',ns)
                if not clicks or blip is None:continue
                embed=blip.get('{'+ns['r']+'}embed')
                if embed not in relationships:continue
                media=posixpath.normpath(posixpath.join('ppt/slides',relationships[embed]['Target']))
                try:candidates=assets.get(pixel_key(archive.read(media)),[])
                except Exception:continue
                candidates=[p for p in candidates if f'part-{deck:02}-slide-{slide:02}-' in p]
                for click in clicks:
                    url=relationships.get(click.get('{'+ns['r']+'}id'),{}).get('Target')
                    if url and candidates:picture_links.append({'slide_key':f'{deck}-{slide}','original_url':url,'retained_image_paths':candidates})
Path('_build/original-inferential-picture-links.json').write_text(json.dumps(picture_links,indent=2)+'\n')
print('Original linked pictures matched:',len(picture_links))
