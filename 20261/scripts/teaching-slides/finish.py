"""Add lesson bookmarks to the converted teaching PDF; retain one page per slide."""
import json,sys
from pathlib import Path
from pypdf import PdfReader,PdfWriter
root=Path(__file__).resolve().parents[2]
module=int(sys.argv[1]);stem=sys.argv[2]
build=root/f'_output/.module{module:02d}-teaching-build'
slides=json.loads((build/'slides.json').read_text())
reader=PdfReader(build/(stem+'.pdf'))
assert len(reader.pages)==len(slides)
writer=PdfWriter();writer.append(reader,import_outline=False)
writer.add_metadata({'/Title':f'Module {module}: Teaching slides','/Author':'Applied Statistics course','/Subject':'Concise companion to the extended Quarto lessons'})
for s in slides:
    if s['kind']=='divider' and s['title'].startswith('Lesson '):writer.add_outline_item(s['title'],s['number']-1)
target=root/'_output/teaching-slides'/(stem+'.pdf')
if target.exists():raise SystemExit('Use a new revision filename; the final PDF already exists.')
with target.open('wb') as f:writer.write(f)
print(f'{len(reader.pages)} PDF pages with lesson bookmarks: {target}')
