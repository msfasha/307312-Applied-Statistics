"""Build PDFs and prepare the shared editable flashcard deck authoring script."""
from pathlib import Path
import json, shutil, subprocess, tempfile
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
ROOT=Path(__file__).resolve().parents[2]
source=ROOT/'book-chapters/basic-business-statistics-13e'
out=ROOT/'_output/book-chapters/basic-business-statistics-13e'; out.mkdir(parents=True,exist_ok=True)
build=ROOT/'_output/.chapter01-build'
for name,file in [('Sans','DejaVuSans.ttf'),('Bold','DejaVuSans-Bold.ttf')]:
 pdfmetrics.registerFont(TTFont(name,'/usr/share/fonts/truetype/dejavu/'+file))
cards=json.loads((source/'chapter01-cards.json').read_text())
c=canvas.Canvas(str(out/'chapter01-flashcards.pdf'),pagesize=(960,540))
c.setTitle(f'Chapter 1: {len(cards)} recall cards / {1+2*len(cards)} pages')
def text(value,top,size=36,color='#2F343B',font='Sans'):
 c.setFillColor(HexColor(color)); c.setFont(font,size*.75)
 for i,line in enumerate(value.splitlines()):
  assert pdfmetrics.stringWidth(line,font,size*.75)<=840,(line,size)
  y=540-(top+size+i*size*1.3)*.75
  assert y>40
  c.drawString(60,y,line)
def bg(color):
 c.setFillColor(HexColor(color)); c.rect(0,0,960,540,fill=1,stroke=0)
bg('#F5EDF4');text('BASIC BUSINESS STATISTICS / 13TH EDITION',65,25)
text('Defining and Collecting Data',170,50,'#493347','Bold');text(f'Chapter 1: {len(cards)} recall cards',290,36)
text(f'{1+2*len(cards)} pages: cover + question and answer pages',350,24)
text('Recall the answer, then advance one page.\nCompanion to the supplied chapter guide.',400,28);c.showPage()
for i,card in enumerate(cards,1):
 for side in ['question','answer']:
  bg('#F5EDF4' if side=='question' else '#FFFFFF')
  text(f'CHAPTER 1     {i:02d} / {len(cards)}     {side.upper()}',46,22,'#56616D')
  text(card['topic'],107,40,'#493347','Bold')
  text(card[side],210,36)
  text('Recall your answer, then advance.' if side=='question' else card['cue'],638,20,'#56616D'); c.showPage()
c.save()
# Render Markdown semantically; the supplied text remains unchanged on disk.
# Use an isolated project so no student website configuration affects this PDF.
quarto=shutil.which('quarto') or '/usr/lib/rstudio/resources/app/bin/quarto/bin/quarto'
with tempfile.TemporaryDirectory(prefix='chapter-summary-') as directory:
 draft=Path(directory)/'summary.qmd'
 # Explicit column widths let long Markdown table cells wrap within the page.
 (Path(directory)/'tables.lua').write_text('''function Table(tbl)
  local width = 1 / #tbl.colspecs
  for i, spec in ipairs(tbl.colspecs) do
    tbl.colspecs[i] = {spec[1], width}
  end
  return tbl
end
''')
 header="""---
filters:
  - tables.lua
format:
  pdf:
    pdf-engine: xelatex
    lang: en
    dir: ltr
    papersize: a4
    geometry: margin=20mm
    mainfont: DejaVu Sans
    sansfont: DejaVu Sans
    monofont: DejaVu Sans Mono
    fontsize: 10pt
    toc: true
    toc-depth: 2
    colorlinks: true
    linkcolor: PetraLink
    urlcolor: PetraLink
    include-in-header: HEADER_PATH
---

""".replace('HEADER_PATH', json.dumps(str(ROOT/'assets/pdf/petra-print.tex')))
 markdown=(source/'chapter01-original.txt').read_text()
 for delimiter in ['[', ']', '(', ')']:
  markdown=markdown.replace('\\'*2+delimiter, '\\'+delimiter)
 # Normalize standard LaTeX math delimiters for Pandoc in the build copy only.
 markdown=markdown.replace(r'\[', '$$').replace(r'\]', '$$')
 markdown=markdown.replace(r'\(', '$').replace(r'\)', '$')
 draft.write_text(header+markdown)
 subprocess.run([quarto,'render',str(draft),'--to','pdf'],check=True,cwd=directory)
 shutil.copy2(draft.with_suffix('.pdf'),out/'chapter01-original.pdf')
print(out)
