#!/usr/bin/env python3
"""Convert historical HTML text/table panels to editable native Quarto Markdown.

Figures/SVG remain raw HTML. Conversion checks rendered wording, emphasis and
all table cells before writing, and preserves R cells byte for byte.
"""
from pathlib import Path
from html.parser import HTMLParser
from html import escape
import argparse, hashlib, json, re, subprocess
ROOT = Path(__file__).resolve().parents[1]
LESSONS = [ROOT/'lessons'/f'{n}.qmd' for n in ['02-descriptive-statistics','03-inferential-statistics']]
MANIFEST = ROOT/'instructor/native-markdown-conversion.json'
RAW = re.compile(r'^```\{=html\}\n(.*?)^```', re.M | re.S)

class Node:
    def __init__(self, tag='', attrs=(), children=None):
        self.tag,self.attrs,self.children=tag,dict(attrs),children or []
    def html(self):
        if not self.tag:return ''.join(c.html() if isinstance(c,Node) else escape(c) for c in self.children)
        attrs=''.join(' '+k+'="'+escape(v or '',quote=True)+'"' for k,v in self.attrs.items())
        return '<'+self.tag+attrs+'>'+Node(children=self.children).html()+('' if self.tag in ['br','img','hr'] else '</'+self.tag+'>')

class Tree(HTMLParser):
    def __init__(self,html):
        super().__init__(convert_charrefs=True);self.root=Node();self.stack=[self.root];self.feed(html)
    def handle_starttag(self,tag,attrs):
        n=Node(tag,attrs);self.stack[-1].children.append(n)
        if tag not in ['br','img','hr']:self.stack.append(n)
    def handle_endtag(self,tag):
        if self.stack[-1].tag==tag:self.stack.pop()
    def handle_data(self,data):self.stack[-1].children.append(data)

class Meaning(HTMLParser):
    def __init__(self,html):
        super().__init__(convert_charrefs=True);self.text=[];self.strong=[];self.em=[];self.cells=[];self.active=[];self.feed(html)
    def handle_starttag(self,tag,attrs):
        if tag in ['p','div','li','tr','td','th','br']:self.text.append(' ')
        if tag in ['strong','em','td','th']:self.active.append([tag,[]])
    def handle_endtag(self,tag):
        if tag in ['p','div','li','tr','td','th']:self.text.append(' ')
        for i in range(len(self.active)-1,-1,-1):
            if self.active[i][0]==tag:
                _,parts=self.active.pop(i);value=norm(''.join(parts))
                if tag=='strong':self.strong.append(value)
                elif tag=='em':self.em.append(value)
                else:self.cells.append(value)
                break
    def handle_data(self,data):
        self.text.append(data)
        for _,parts in self.active:parts.append(data)
    def result(self):return {'text':norm(''.join(self.text)), 'strong':re.sub(r'\s+','',''.join(self.strong)),'em':re.sub(r'\s+','',''.join(self.em)),'cells':self.cells}

def norm(s):return re.sub(r'\s+',' ',s).strip()
def pandoc(text,reader,writer):
    return subprocess.run(['quarto','pandoc','--from='+reader,'--to='+writer,'--wrap=none','--columns=160'],input=text,text=True,capture_output=True,check=True).stdout

def native_lists(node):
    for child in node.children:
        if isinstance(child,Node):native_lists(child)
    out=[];stack=[]
    for child in node.children:
        if isinstance(child,str) and not child.strip():
            if not stack:out.append(child)
            continue
        bullet=isinstance(child,Node) and child.tag=='p' and 'source-bullet' in child.attrs.get('class','')
        if not bullet:out.append(child);stack=[];continue
        level=int(re.search(r'source-level-(\d+)',child.attrs['class'])[1])
        if not stack:
            ul=Node('ul');out.append(ul);stack=[ul]
        target=min(level,len(stack) if stack[-1].children else len(stack)-1)
        while len(stack)>target+1:stack.pop()
        if target==len(stack):
            ul=Node('ul');stack[-1].children[-1].children.append(ul);stack.append(ul)
        stack[-1].children.append(Node('li',children=child.children))
    node.children=out
    # The original first row was styled as a header; retain that role natively.
    if node.tag=='table' and node.children and isinstance(node.children[0],Node) and node.children[0].tag=='tr':
        row=node.children[0]
        for c in row.children:
            if isinstance(c,Node) and c.tag=='td':c.tag='th'
        node.children[0]=Node('thead',children=[row])

def convert(html):
    before=Meaning(html).result()
    cleaned=html
    while True:
        cleaned,n=re.subn(r'<(strong|em)>\s*</\1>', ' ', cleaned)
        if not n:break
    tree=Tree(cleaned);native_lists(tree.root)
    markdown=pandoc(tree.root.html(),'html','markdown+fenced_divs-simple_tables-multiline_tables-pipe_tables+grid_tables')
    after=Meaning(pandoc(markdown,'markdown','html')).result()
    # Space around emphasis can be normalized by Pandoc; the words and emphasis
    # spans must remain identical, as must every table cell in reading order.
    assert before==after, {'before':before,'after':after}
    assert not re.search(r'<(?:div|p|table|tr|td)\b',markdown),markdown
    return markdown.strip()

def sha(s):return hashlib.sha256(s.encode()).hexdigest()
def without_r(block,key):return re.sub(r'\n<!-- BEGIN R EXAMPLE '+key+r' -->.*?<!-- END R EXAMPLE '+key+r' -->\n','',block,flags=re.S).strip()

def migrate():
    if not any(re.match(r'\s*<div class="source-(?:text|table)"', b)
               for path in LESSONS for b in RAW.findall(path.read_text())):
        print('Teaching panels are already native Markdown; nothing changed.')
        return
    prepared={}
    report={'purpose':'Format-only native Markdown conversion; wording/emphasis/table cells and R code checked','lessons':{}}
    for path in LESSONS:
        old=path.read_text();counts={'text':0,'tables':0}
        def replace(m):
            html=m[1]
            if not re.match(r'\s*<div class="source-(?:text|table)"',html):return m[0]
            kind='tables' if 'class="source-table"' in html else 'text';counts[kind]+=1
            return convert(html)
        new=RAW.sub(replace,old)
        # Leave generous outer fences for text panels, R panels and native tables.
        pieces=re.split(r'(?=<!-- Original (?:deck \d+, )?slide \d+ -->)',new)
        for i in range(1,len(pieces)):
            b=pieces[i];b=re.sub(r'^::: \{\.source-slide ',r':::::: {.source-slide ',b,flags=re.M)
            b=re.sub(r'\n:::\s*$', '\n::::::\n\n',b);pieces[i]=b
        new=''.join(pieces)
        assert re.findall(r'^```\{r\}\n.*?^```',old,re.M|re.S)==re.findall(r'^```\{r\}\n.*?^```',new,re.M|re.S)
        # Native paragraphs use Markdown's protected dollar/underscore literals.
        prepared[path]=new
        report['lessons'][path.name]={**counts,'source_before_sha256':sha(old),'source_after_sha256':sha(new)}
    for path,new in prepared.items():path.write_text(new)
    part3=LESSONS[1].read_text();f=ROOT/'instructor/inferential-original-content-manifest.json';m=json.loads(f.read_text())
    m['native_markdown_bodies']={}
    for b in re.split(r'(?=<!-- Original deck \d+, slide \d+ -->)',part3)[1:]:
        found=re.match(r'<!-- Original deck (\d+), slide (\d+) -->',b);key='-'.join(found.groups())
        m['native_markdown_bodies'][key]=sha(without_r(b,key))
    f.write_text(json.dumps(m,indent=2)+'\n');MANIFEST.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

def check():
    for path in LESSONS:
        for block in RAW.findall(path.read_text()):
            assert not re.match(r'\s*<div class="source-(?:text|table)"',block),path
    source=(ROOT/'lessons/01-introduction-to-r.qmd').read_text()
    assert 'echo: !expr' not in source,'Quarto echo settings must use valid booleans'
    print('Native teaching text/tables and valid introductory echo settings verified.')

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--convert',action='store_true');args=parser.parse_args()
    if args.convert:migrate()
    check()
