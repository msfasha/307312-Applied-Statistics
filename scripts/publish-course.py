#!/usr/bin/env python3
"""Build the active course and publish its generated site to gh-pages."""
from pathlib import Path
import argparse,subprocess,shutil,tempfile,json,datetime
ROOT=Path(__file__).resolve().parents[1]
def run(*args,cwd=ROOT):
    return subprocess.run(args,cwd=cwd,check=True,text=True,capture_output=True).stdout.strip()
parser=argparse.ArgumentParser();parser.add_argument('--skip-render',action='store_true');args=parser.parse_args()
build_args = ['python3', str(ROOT/'scripts/build-course.py')]
if args.skip_render:
    build_args.append('--skip-render')
subprocess.run(build_args, cwd=ROOT, check=True)
site=ROOT/'_build/website'
source=run('git','rev-parse','HEAD')
(site/'deployment.json').write_text(json.dumps({'source_commit':source,'course':'307312 Applied Statistics','published_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()},indent=2)+'\n')
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
        run('git','commit','-m','Publish Part 3 probability section, R practical and refreshed downloads',cwd=checkout)
        print(run('git','push','origin','HEAD:gh-pages',cwd=checkout))
        print('Published source commit:',source)
        print('Website: https://msfasha.github.io/307312-Applied-Statistics/')
    finally:run('git','worktree','remove','--force',str(checkout))
