"""Record Arabic paragraph direction and language without flattening editable text."""
import re,sys,zipfile
from lxml import etree as ET
ns={'a':'http://schemas.openxmlformats.org/drawingml/2006/main','p':'http://schemas.openxmlformats.org/presentationml/2006/main'}
with zipfile.ZipFile(sys.argv[1]) as src, zipfile.ZipFile(sys.argv[2],'w',zipfile.ZIP_DEFLATED) as dst:
    for name in src.namelist():
        data=src.read(name)
        if re.match(r'ppt/slides/slide\d+[.]xml$',name):
            tree=ET.fromstring(data)
            for shape in tree.findall('.//p:sp',ns):
                prop=shape.find('p:nvSpPr/p:cNvPr',ns)
                if prop is not None and prop.get('name')=='case-narration-ar':
                    for p in shape.findall('.//a:p',ns):
                        pr=p.find('a:pPr',ns)
                        if pr is None:
                            pr=ET.Element('{'+ns['a']+'}pPr');p.insert(0,pr)
                        pr.set('rtl','1');pr.set('algn','r')
                        for r in p.findall('a:r',ns):
                            rp=r.find('a:rPr',ns)
                            if rp is None:
                                rp=ET.Element('{'+ns['a']+'}rPr');r.insert(0,rp)
                            rp.set('lang','ar-JO')
            data=ET.tostring(tree,xml_declaration=True,encoding='UTF-8',standalone=True)
        dst.writestr(name,data)
