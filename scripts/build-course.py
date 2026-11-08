#!/usr/bin/env python3
"""Build and validate all student outputs locally; never push or publish."""
from pathlib import Path
import argparse
import shutil
import subprocess
from course_documents import EXTENDED, DOCUMENTS, NAVIGATION_PAGES

ROOT = Path(__file__).resolve().parents[1]

def validate(site):
    required=[n+'.html' for n in NAVIGATION_PAGES]
    required += ['index.html','lessons/02-descriptive-statistics.html','lessons/03-inferential-statistics.html','lessons/01-introduction-to-r.html']
    required += [f'{folder}/{name}.html' for folder, name in DOCUMENTS]
    required += ['pdf/'+name+'.pdf' for _, name in DOCUMENTS]
    required += ['pdf/'+p+'.pdf' for p in ['01-introduction-to-r','02-descriptive-statistics','03-inferential-statistics']]
    required += ['extended-cases/superstore/index.html']
    required += ['extended-cases/'+p+'.html' for p in EXTENDED]+['pdf/'+p+'.pdf' for p in EXTENDED]
    import re
    required += re.findall(r'^    - (data/[^\n]+)', (ROOT/'_quarto.yml').read_text(), re.M)
    required += ['data/business/'+p for p in ['superstore-lines.csv','cola.csv','consumer.csv','README.md']]
    required += ['downloads/applied-statistics-rstudio.zip','downloads/applied-statistics-pdfs.zip', 'downloads/inferential-statistics-r-practical.qmd']
    for name in required:
        if not (site/name).exists():raise RuntimeError('Missing generated page: '+name)
    forbidden=[p for p in site.rglob('*') if p.is_file() and (any(t in p.relative_to(site).parts for t in ['instructor','archived','books','sources','_includes']) or p.suffix.lower() in ['.xlsx','.xls'])]
    if forbidden:raise RuntimeError('Local-only files in generated site: '+str(forbidden[:5]))
    expected = {
        'lessons/01-introduction-to-r.html': ['History of R', 'Installing R'],
        'lessons/02-descriptive-statistics.html': ['What is Statistics?', 'source-title-87'],
        'lessons/03-inferential-statistics.html': ['part3-01-slide-01', 'part3-04-slide-21'],
    }
    for page, markers in expected.items():
        content = (site/page).read_text()
        if not all(marker in content for marker in markers):
            raise RuntimeError('Incomplete course: '+page)
    # Guard the restored core against future replacement by practical/case rewrites.
    descriptive = (site/'lessons/02-descriptive-statistics.html').read_text()
    if any(f'id="slide-{i:02d}"' not in descriptive for i in range(1, 88)):
        raise RuntimeError('Incomplete retained descriptive slides')
    if 'id="slide-88"' in descriptive:
        raise RuntimeError('Removed cross-course Practice Datasets slide reintroduced')
    inferential = (site/'lessons/03-inferential-statistics.html').read_text()
    if any(f'id="part3-{k:02d}-slide-{i:02d}"' not in inferential
           for k, count in enumerate([37, 26, 57, 21], 1) for i in range(1, count+1)):
        raise RuntimeError('Incomplete original inferential slides: expected 141')

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--skip-render', action='store_true',
                        help='Reuse a completed full HTML build; refresh practicals and all downloads.')
    args = parser.parse_args()
    subprocess.run(['python3', str(ROOT/'scripts/sync-descriptive-r-references.py'), '--check'], cwd=ROOT, check=True)
    subprocess.run(['python3', str(ROOT/'scripts/check-practicals.py')], cwd=ROOT, check=True)
    if args.skip_render:
        subprocess.run(['python3', str(ROOT/'scripts/preview-practicals.py')], cwd=ROOT, check=True)
        subprocess.run(['python3', str(ROOT/'scripts/stage-practicals.py')], cwd=ROOT, check=True)
    else:
        site = ROOT/'_build/website'
        if site.exists():
            shutil.rmtree(site)
        quarto = shutil.which('quarto') or '/usr/lib/rstudio/resources/app/bin/quarto/bin/quarto'
        subprocess.run([quarto, 'render', '--quiet'], cwd=ROOT, check=True)
    subprocess.run(['python3', str(ROOT/'scripts/build-student-downloads.py')], cwd=ROOT, check=True)
    validate(ROOT/'_build/website')
    subprocess.run(['python3', str(ROOT/'scripts/validate-student-site.py')], cwd=ROOT, check=True)
    print(f'Local build verified: {len(DOCUMENTS)} notebooks, {len(DOCUMENTS)} PDFs and both student bundles. Nothing published.', flush=True)

if __name__ == '__main__':
    main()
