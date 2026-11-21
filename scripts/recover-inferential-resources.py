#!/usr/bin/env python3
"""Restore audited original resources as native Quarto URL/QR panels.
Maintainer dependency: qrcode. No new student R dependency.
Run audit-inferential-resources.py to re-read the original decks before updating the catalog.
"""
from pathlib import Path
import sys,json,re,hashlib,argparse
import qrcode
from qrcode.image.svg import SvgPathImage
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from course_sections import inferential_blocks,r_panel
LESSONS=['03-probability-foundations','04-statistical-inference-and-estimation']
CATALOG=ROOT/'instructor/inferential-resource-recovery.json'

def resources():return json.loads(CATALOG.read_text())['resources']

def panel(key, entries):
 lines=[f'::::: {{.recovered-resources #original-resources-{key}}}','']
 for r in entries:
  lines += [':::: {.recovered-resource}','::: {.resource-description}',f"**{r['title']}**",'',r['purpose'],'',f"<{r['active_url']}>",':::','', '::: {.resource-qr}',f"[![](../assets/inferential-statistics/resources/{r['id']}.svg){{.compact-resource-qr width=\"144\" fig-alt=\"QR code: {r['title']}\"}}]({r['active_url']})",':::','::::','']
 return '\n'.join(lines+[':::::',''])

def check():
 rs=resources();found=set()
 for stem in LESSONS:
  text=(ROOT/'lessons'/(stem+'.qmd')).read_text()
  for key,block in inferential_blocks(text):
   for r in rs:
    if key not in r['placements']:continue
    if r['id']=='clt-video':assert r['active_url'] in block and 'clt-video-qr.svg' in block
    else:assert r['active_url'] in block and f"resources/{r['id']}.svg" in block,(key,r['id'])
    found.add((key,r['id']))
 assert len(found)==21,len(found)
 print('Verified all 15 original resources across 21 teaching placements.')

def apply():
 rs=resources();target=ROOT/'assets/inferential-statistics/resources';target.mkdir(parents=True,exist_ok=True)
 for r in rs:
  if r['id']=='clt-video':continue
  q=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M,box_size=8,border=4)
  q.add_data(r['active_url']);q.make(fit=True);q.make_image(image_factory=SvgPathImage).save(str(target/(r['id']+'.svg')))
 manifest_file=ROOT/'instructor/inferential-original-content-manifest.json';manifest=json.loads(manifest_file.read_text())
 changed=[]
 for stem in LESSONS:
  p=ROOT/'lessons'/(stem+'.qmd');text=p.read_text();before_cells=re.findall(r'```\{r\}\n(.*?)\n```',text,re.S)
  for key,original in list(inferential_blocks(text)):
   entries=[r for r in rs if key in r['placements'] and r['id']!='clt-video']
   if not entries:continue
   body=re.sub(r'^::::: \{\.recovered-resources[^\n]*\}\n.*?^:::::\s*\n?','',original,flags=re.M|re.S)
   # Remove URL-only panels, not original teaching explanations or scientific content.
   for r in entries:
    body=re.sub(r'::: source-text\s*\n'+re.escape(r['original_url'])+r'\s*\n:::\s*\n','',body)
    if key=='2-12' and r['id']=='sampling-statkey':
     body=body.replace('**Interactive sampling tool — StatKey:**\n\n<'+r['original_url']+'>\n','')
   for r in rs:
    for image in r.get('linked_original_images',{}).get(key,[]):
     # Restore the original picture hyperlink without changing the picture bytes or size.
     pattern=r'(?<!\[)(!\[[^\]]*\]\(\.\./'+re.escape(image)+r'\)(?:\{[^}]*\})?)'
     body=re.sub(pattern,lambda match:'['+match[1]+']('+r['active_url']+')',body)
   addition=panel(key,entries)
   at=body.find('\n:::: {.try-in-r')
   if at<0:at=body.rfind('\n::::::')
   assert at>=0,key
   body=body[:at].rstrip()+'\n\n'+addition.rstrip()+'\n\n'+body[at:].lstrip('\n')
   text=text.replace(original,body,1);changed.append(key)
   stripped=body;rp=r_panel(body)
   if rp:stripped=body[:rp.start()]+body[rp.end():]
   manifest['native_markdown_bodies'][key]=hashlib.sha256(stripped.strip().encode()).hexdigest()
  assert re.findall(r'```\{r\}\n(.*?)\n```',text,re.S)==before_cells,'R code must remain byte-identical'
  p.write_text(text)
 manifest.setdefault('resource_restorations',{})['complete-recovery-2026-11-21']={'catalog':str(CATALOG.relative_to(ROOT)),'resources':15,'original_placements':21,'updated_slide_keys':changed,'note':'Original article/calculator/tutorial links restored with explicit labels, URLs and QR codes. Two obsolete Iowa links updated to the original author\'s verified current applets. Existing teaching prose, slide order and R cells preserved.'}
 manifest_file.write_text(json.dumps(manifest,indent=2)+'\n')
 check()

if __name__=='__main__':
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--check',action='store_true');args=ap.parse_args()
 check() if args.check else apply()
