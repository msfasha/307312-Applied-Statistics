#!/usr/bin/env python3
"""Check preservation of the slide sequence and its single set of executable R cells."""
from pathlib import Path
import hashlib,json,re,subprocess,tempfile
ROOT=Path(__file__).resolve().parents[1]
BUILD=ROOT/'_build/part3-consolidation'


def check():
    source=(ROOT/'lessons/03-inferential-statistics.qmd').read_text()
    ids=re.findall(r'\.source-slide #(part3-[\w-]+)',source)
    expected=[f'part3-{deck:02}-slide-{slide:02}' for deck,n in enumerate([37,26,57,21],1) for slide in range(1,n+1)]
    assert ids==expected,'The original 141 teaching positions must stay in order'
    assert not re.search(r'Excel|CONFIDENCE[.]|NORM[.]DIST|BINOM[.]DIST|POISSON[.]DIST|```python',source)
    cells=re.findall(r'^```\{r\}\n(.*?)^```',source,re.M|re.S)
    codes=json.loads((ROOT/'scripts/inferential-r-examples.json').read_text())
    actual={}
    for cell in cells:
        match=re.match(r'#\| label: inferential-([\d-]+)\n(.*)',cell,re.S)
        assert match,'Every executable example needs a stable slide label'
        actual[match[1]]=match[2].strip()
    assert len(cells)==len(actual)==len(codes)==36
    assert actual=={k:v.strip() for k,v in codes.items()},'Canonical notebook R cells differ from the documented examples'
    manifest=json.loads((ROOT/'instructor/inferential-original-content-manifest.json').read_text())
    for block in re.split(r'(?=<!-- Original deck \d+, slide \d+ -->)',source)[1:]:
        m=re.match(r'<!-- Original deck (\d+), slide (\d+) -->',block);key='-'.join(m.groups())
        panel=re.search(r'\n<!-- BEGIN R EXAMPLE '+key+r' -->.*?<!-- END R EXAMPLE '+key+r' -->\n',block,re.S)
        if key in codes:
            assert panel and '**Before running:**' in panel[0] and '**Read the result:**' in panel[0],key
        if panel:block=block[:panel.start()]+block[panel.end():]
        if key in manifest.get('native_markdown_bodies', {}):
            assert hashlib.sha256(block.strip().encode()).hexdigest()==manifest['native_markdown_bodies'][key],('Native teaching content changed',key)
        elif key in manifest.get('authorized_visual_updates', {}):
            assert hashlib.sha256(block.strip().encode()).hexdigest()==manifest['authorized_visual_updates'][key]['sha256'],('Authorized slide changed',key)
        elif key in manifest['unchanged_slide_bodies_excluding_R']:
            assert hashlib.sha256(block.strip().encode()).hexdigest()==manifest['unchanged_slide_bodies_excluding_R'][key],('Original theory changed',key)
    extra=r'''
stopifnot(abs(dbinom(2,10,.5)-.0439453125)<1e-12)
stopifnot(abs(dpois(x=15,lambda=20)-.0516488535317584)<1e-12)
stopifnot(abs(punif(q=9,min=8,max=12)-.25)<1e-12)
stopifnot(abs(punif(q=10.1,min=9.8,max=10.2,lower.tail=FALSE)-.25)<1e-12)
stopifnot(abs(pnorm(90,70,6,lower.tail=FALSE)-.0004290603331968)<1e-12)
stopifnot(nrow(paired)==30,nrow(salaries)==30,nrow(majors)==30)
stopifnot(sum(beverages)==200,all(expected>5),abs(sum((beverages-expected)^2/expected)-8.42857142857143)<1e-10)
stopifnot(abs(chi$p.value-.01478287719483942)<1e-10)
stopifnot(nrow(methods)==15,nrow(teaching)==8,nrow(houses)==10)
stopifnot(all(is.finite(coef(simple))),all(is.finite(coef(multiple))),all(is.finite(aic)))
stopifnot(abs(summary(simple)$r.squared-.89546108625675147)<1e-10)
'''
    BUILD.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='part3-r-check-') as temp:
        p=Path(temp)
        # The source's optional MASS candidate fitting can issue optimiser warnings;
        # retain the calculation and check its final estimates/AIC for finiteness.
        code='options(digits=7)\npdf('+json.dumps(str(p/'plots.pdf'))+')\n'+'\n'.join(cells)+extra+'\ndev.off()\n'
        script=p/'check.R';script.write_text(code)
        result=subprocess.run(['Rscript','--vanilla',str(script)],cwd=ROOT,capture_output=True,text=True)
        (BUILD/'r-checks.log').write_text(result.stdout+result.stderr)
        if result.returncode:raise RuntimeError(result.stderr)
    report={'original_slide_positions':141,'explained_R_cells':36,'native_markdown_bodies_checked':len(manifest.get('native_markdown_bodies',{})),'unchanged_theory_bodies_checked':len(set(manifest['unchanged_slide_bodies_excluding_R'])-set(manifest.get('authorized_visual_updates',{}))),'authorized_slide_bodies_checked':len(manifest.get('authorized_visual_updates',{})),'numerical_checks':'passed'}
    (BUILD/'validation.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2),flush=True)

if __name__=='__main__':check()
