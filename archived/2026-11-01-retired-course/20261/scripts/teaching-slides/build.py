#!/usr/bin/env python3
"""Build a uniquely named revision of the two reduced teaching presentations."""
import argparse,os,shutil,subprocess,sys
from pathlib import Path
from PIL import Image
root=Path(__file__).resolve().parents[3]
runtime=Path.home()/'.cache/codex-runtimes/codex-primary-runtime/dependencies'
python=str(runtime/'python/bin/python3');node=str(runtime/'node/bin/node')
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--module',type=int,choices=[1,2],required=True)
parser.add_argument('--revision',required=True,help='Unique filename suffix, e.g. review-20261101')
args=parser.parse_args();m=args.module
if not args.revision.replace('-','').isalnum():parser.error('Use only letters, numbers, and hyphens in revision.')
scripts=root/'20261/scripts/teaching-slides';build=root/f'20261/_output/.module{m:02d}-teaching-build';build.mkdir(parents=True,exist_ok=True)
def run(*cmd,cwd=root,env=None):subprocess.run([str(c) for c in cmd],cwd=cwd,env=env,check=True)
if m==1:
    run('Rscript',scripts/'render-module01.R')
    with Image.open(root/'20261/assets/module01/grammar-of-graphics.gif') as im:
        im.seek(0);im.convert('RGB').save(build/'grammar-frame.png')
else:run('Rscript',scripts/'render-module02.R',cwd=root/'20261')
run(python,scripts/f'author-module{m:02d}.py')
run(python,scripts/'layout.py',m)
stem=('module01-introduction-to-r' if m==1 else 'module02-descriptive-statistics')+'-'+args.revision
env=dict(os.environ,DECK_FILENAME=stem+'.pptx')
run(node,scripts/'build.mjs',m,env=env)
run('libreoffice',f'-env:UserInstallation=file:///tmp/statistics-teaching-module{m}','--headless','--convert-to','pdf','--outdir',build,root/'20261/_output/teaching-slides'/(stem+'.pptx'))
run(python,scripts/'finish.py',m,stem)
print('Inspect the revised PPTX and PDF, then copy the approved revision to the stable publication filenames and stamp the manifest.')
