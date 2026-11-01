"""Build PDFs and prepare the shared editable flashcard deck authoring script."""
from pathlib import Path
import json, textwrap, re
from xml.sax.saxutils import escape
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
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
# Verbatim source text, with typography and wrapping only. Markdown notation remains visible.
styles=getSampleStyleSheet();style=styles['BodyText'];style.fontName='Sans';style.fontSize=9;style.leading=13
style.spaceAfter=4
story=[]
for line in (source/'chapter01-original.txt').read_text().splitlines():
 if not line.strip():story.append(Spacer(1,5));continue
 # Keep the source's exact wording, including Markdown markers and tables.
 story.append(Paragraph(escape(line),style))
def footer(c,d):
 c.setFont('Sans',8);c.drawString(42,24,'Supplied chapter guide / original text');c.drawRightString(550,24,str(d.page))
SimpleDocTemplate(str(out/'chapter01-original.pdf'),rightMargin=42,leftMargin=42,topMargin=40,bottomMargin=42,title='Chapter 1: supplied original teaching guide').build(story,onFirstPage=footer,onLaterPages=footer)
print(out)
