"""Shared DrawingML text and geometry helpers for the course converters."""
import html

NS = {'p':'http://schemas.openxmlformats.org/presentationml/2006/main',
      'a':'http://schemas.openxmlformats.org/drawingml/2006/main',
      'r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
def txt(e):
    return ''.join(e.itertext()) if e is not None else ''
def text(e):
    return ''.join(t.text or '' for t in e.findall('.//a:t',NS))
def para(p):
    out=[]
    for e in p:
        kind=e.tag.split('}')[-1]
        if kind=='br': out.append('<br>')
        elif kind in ['r','fld']:
            val=html.escape(text(e)); props=e.find('a:rPr',NS)
            if props is not None:
                if props.get('b')=='1': val='<strong>'+val+'</strong>'
                if props.get('i')=='1': val='<em>'+val+'</em>'
                if props.get('baseline') and int(props.get('baseline'))>0: val='<sup>'+val+'</sup>'
            out.append(val)
    return ''.join(out)
def paragraphs(e):
    out=[]
    for p in e.findall('a:p',NS):
        content=para(p)
        if not content.strip(): continue
        pp=p.find('a:pPr',NS)
        bullet=pp is not None and (pp.find('a:buChar',NS) is not None or pp.find('a:buAutoNum',NS) is not None)
        level=int(pp.get('lvl','0')) if pp is not None else 0
        out.append('<p'+(f' class="source-bullet source-level-{level}"' if bullet else '')+'>'+content+'</p>')
    return '\n'.join(out)
def rect(e):
    x=e.find('p:spPr/a:xfrm',NS)
    if x is None: x=e.find('p:xfrm',NS)
    if x is None: return (0,0,0,0)
    off=x.find('a:off',NS); ext=x.find('a:ext',NS)
    return tuple(int(n.get(k,'0')) for n,k in [(off,'x'),(off,'y'),(ext,'cx'),(ext,'cy')])

