#!/usr/bin/env python3
"""Check preservation of the slide sequence and its single set of executable R cells."""
from pathlib import Path
import hashlib,json,re,subprocess,tempfile
ROOT=Path(__file__).resolve().parents[1]
BUILD=ROOT/'_build/part3-consolidation'


def check():
    from course_documents import LESSONS
    sources = {name: (ROOT/'lessons'/(name+'.qmd')).read_text() for name in LESSONS[2:]}
    source='\n'.join(sources.values())
    ids=re.findall(r'\.source-slide #(part3-[\w-]+)',source)
    expected=[f'part3-{deck:02}-slide-{slide:02}' for deck,n in enumerate([37,26,57,21],1) for slide in range(1,n+1)]
    assert len(ids)==141 and set(ids)==set(expected), 'Preserve every original teaching position once'
    manifest=json.loads((ROOT/'instructor/inferential-original-content-manifest.json').read_text())
    from course_sections import inferential_blocks
    for name, text in sources.items():
        assert [key for key,_ in inferential_blocks(text)] == manifest['teaching_order_2026_11_20'][name], ('Approved teaching order changed', name)
    assert sources['04-statistical-inference-and-estimation'].index('#inference-sampling-distributions') < sources['04-statistical-inference-and-estimation'].index('#part3-02-slide-12') < sources['04-statistical-inference-and-estimation'].index('#part3-02-slide-06'), 'Sampling distributions and CLT must precede confidence intervals'
    probability = sources['03-probability-foundations']
    markers = ['#probability-outcomes-events', '#probability-event-rules', '#probability-combining-events', '#probability-events-to-variables', '#part3-01-slide-07', '#part3-01-slide-11']
    positions = [probability.index(marker) for marker in markers]
    assert positions == sorted(positions), 'Teach events before random variables and distributions'
    assert '#probability-dice-sums' not in probability and '#probability-binomial-arrangements' not in probability
    assert 'binomial-three-toss-arrangements.svg' in probability
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
    from course_sections import inferential_blocks, r_panel
    for key, block in (pair for text in sources.values() for pair in inferential_blocks(text)):
        panel=r_panel(block)
        if key in codes:
            assert panel and '**Before running:**' in panel[0] and '**Read the result:**' in panel[0],key
        if panel:block=block[:panel.start()]+block[panel.end():]
        if key in manifest.get('native_markdown_bodies', {}):
            assert hashlib.sha256(block.strip().encode()).hexdigest()==manifest['native_markdown_bodies'][key],('Native teaching content changed',key)
        elif key in manifest.get('authorized_visual_updates', {}):
            assert hashlib.sha256(block.strip().encode()).hexdigest()==manifest['authorized_visual_updates'][key]['sha256'],('Authorized slide changed',key)
        elif key in manifest['unchanged_slide_bodies_excluding_R']:
            assert hashlib.sha256(block.strip().encode()).hexdigest()==manifest['unchanged_slide_bodies_excluding_R'][key],('Original theory changed',key)
    # Every recovered source resource remains attached to its original teaching position.
    catalog=json.loads((ROOT/'instructor/inferential-resource-recovery.json').read_text())
    blocks=dict(pair for text in sources.values() for pair in inferential_blocks(text))
    recovered=set()
    for resource in catalog['resources']:
        for key in resource['placements']:
            assert resource['active_url'] in blocks[key], ('Missing recovered URL',key,resource['id'])
            image='clt-video-qr.svg' if resource['id']=='clt-video' else 'resources/'+resource['id']+'.svg'
            assert image in blocks[key] and (ROOT/'assets/inferential-statistics'/image).exists(), ('Missing recovered QR',key,resource['id'])
            for original_image in resource.get('linked_original_images',{}).get(key,[]):
                if '../'+original_image in blocks[key]:
                    pattern=r'\[!\[[^\]]*\]\(\.\./'+re.escape(original_image)+r'\)(?:\{[^}]*\})?\]\('+re.escape(resource['active_url'])+r'\)'
                    assert re.search(pattern,blocks[key]), ('Original image link missing',key,original_image)
            recovered.add((key,resource['id']))
    assert len(catalog['resources'])==15 and len(recovered)==21
    extra=r'''
stopifnot(choose(3,2)==3, choose(10,2)==45, abs(dbinom(2,3,.5)-3/8)<1e-12)
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
