#!/usr/bin/env python3
"""Build the active course and publish its generated site to gh-pages."""
from pathlib import Path
import argparse,subprocess,shutil,tempfile,json,datetime
ROOT=Path(__file__).resolve().parents[1]
def run(*args,cwd=ROOT):
    return subprocess.run(args,cwd=cwd,check=True,text=True,capture_output=True).stdout.strip()
def validate(site):
    required=['index.html','02-descriptive-statistics.html','03-inferential-statistics.html','modules/01-introduction-to-r/index.html']
    for name in required:
        if not (site/name).exists():raise RuntimeError('Missing generated page: '+name)
    for name in ['paired_scores.csv','graduate_salaries.csv','female_major_salaries.csv','teaching_methods.csv','teaching_gender.csv','houses.csv']:
        if not (site/'data/inferential-statistics'/name).exists():raise RuntimeError('Missing teaching CSV: '+name)
    if not (site/'data/307102/students.csv').exists():raise RuntimeError('Missing descriptive teaching CSV')
    forbidden=[p for p in site.rglob('*') if p.is_file() and (any(t in p.relative_to(site).parts for t in ['_instructor','archived','books']) or p.suffix.lower() in ['.xlsx','.xls'])]
    if forbidden:raise RuntimeError('Local-only files in generated site: '+str(forbidden[:5]))
    infer=(site/'03-inferential-statistics.html').read_text()
    if sum(f'id="part3-{k:02d}-slide-{i:02d}"' in infer for k,n in enumerate([37,26,57,21],1) for i in range(1,n+1))!=141:raise RuntimeError('Incomplete Part 3')
parser=argparse.ArgumentParser();parser.add_argument('--skip-render',action='store_true');args=parser.parse_args()
if not args.skip_render:
    quarto=shutil.which('quarto') or '/usr/lib/rstudio/resources/app/bin/quarto/bin/quarto'
    subprocess.run([quarto,'render','--quiet'],cwd=ROOT,check=True)
site=ROOT/'_preview';validate(site)
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
        run('git','commit','-m','Publish three-part Masters course with inferential statistics',cwd=checkout)
        print(run('git','push','origin','HEAD:gh-pages',cwd=checkout))
        print('Published source commit:',source)
        print('Website: https://msfasha.github.io/307312-Applied-Statistics/')
    finally:run('git','worktree','remove','--force',str(checkout))
