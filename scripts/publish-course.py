#!/usr/bin/env python3
"""Build the active course and publish its generated site to gh-pages."""
from pathlib import Path
import argparse,subprocess,shutil,tempfile,json,datetime
ROOT=Path(__file__).resolve().parents[1]
def run(*args,cwd=ROOT):
    return subprocess.run(args,cwd=cwd,check=True,text=True,capture_output=True).stdout.strip()
def validate(site):
    required=['index.html','lessons/02-descriptive-statistics.html','lessons/03-inferential-statistics.html','lessons/01-introduction-to-r.html']
    required += ['pdf/'+p+'.pdf' for p in ['01-introduction-to-r','02-descriptive-statistics','03-inferential-statistics']]
    practicals=['practical-01-categorical-business-data','practical-02-numerical-business-data','practical-03-association-and-groups']
    required += ['practicals/'+p+'.html' for p in practicals]+['pdf/'+p+'.pdf' for p in practicals]
    required += ['data/business/'+p for p in ['superstore-lines.csv','cola.csv','consumer.csv','README.md']]
    required += ['downloads/applied-statistics-rstudio.zip','downloads/applied-statistics-pdfs.zip']
    for name in required:
        if not (site/name).exists():raise RuntimeError('Missing generated page: '+name)
    forbidden=[p for p in site.rglob('*') if p.is_file() and (any(t in p.relative_to(site).parts for t in ['instructor','archived','books','sources','_includes']) or p.suffix.lower() in ['.xlsx','.xls'])]
    if forbidden:raise RuntimeError('Local-only files in generated site: '+str(forbidden[:5]))
    expected = {
        'lessons/01-introduction-to-r.html': ['Superstore', 'category_summary'],
        'lessons/02-descriptive-statistics.html': ['Superstore', '2.9 Put the evidence together'],
        'lessons/03-inferential-statistics.html': ['COLA', 'Consumer', '3.10 Your inferential business briefing'],
    }
    for page, markers in expected.items():
        content = (site/page).read_text()
        if not all(marker in content for marker in markers):
            raise RuntimeError('Incomplete business course: '+page)
parser=argparse.ArgumentParser();parser.add_argument('--skip-render',action='store_true');args=parser.parse_args()
if not args.skip_render:
    previous=ROOT/'_build/website'
    if previous.exists():shutil.rmtree(previous)
    quarto=shutil.which('quarto') or '/usr/lib/rstudio/resources/app/bin/quarto/bin/quarto'
    subprocess.run([quarto,'render','--quiet'],cwd=ROOT,check=True)
if args.skip_render:
    subprocess.run(['python3',str(ROOT/'scripts/preview-practicals.py')],cwd=ROOT,check=True)
    subprocess.run(['python3',str(ROOT/'scripts/stage-practicals.py')],cwd=ROOT,check=True)
site=ROOT/'_build/website'
subprocess.run(['python3',str(ROOT/'scripts/build-student-downloads.py')],cwd=ROOT,check=True)
validate(site)
subprocess.run(['python3',str(ROOT/'scripts/validate-student-site.py')],cwd=ROOT,check=True)
source=run('git','rev-parse','HEAD')
(site/'deployment.json').write_text(json.dumps({'source_commit':source,'course':'307312 Applied Statistics - Masters Level','published_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()},indent=2)+'\n')
(site/'.nojekyll').touch()
run('git','fetch','origin','gh-pages')
with tempfile.TemporaryDirectory(prefix='307312-pages-') as temp:
    checkout=Path(temp)/'site'
    run('git','worktree','add','--detach',str(checkout),'origin/gh-pages')
    try:
        for p in checkout.iterdir():
            if p.name=='.git':continue
            if p.is_dir():shutil.rmtree(p)
            else:p.unlink()
        shutil.copytree(site,checkout,dirs_exist_ok=True)
        run('git','add','--all',cwd=checkout)
        run('git','commit','-m','Publish Superstore business course and refreshed student downloads',cwd=checkout)
        print(run('git','push','origin','HEAD:gh-pages',cwd=checkout))
        print('Published source commit:',source)
        print('Website: https://msfasha.github.io/307312-Applied-Statistics/')
    finally:run('git','worktree','remove','--force',str(checkout))
