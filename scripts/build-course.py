#!/usr/bin/env python3
"""Build and validate all student outputs locally; never push or publish."""
from pathlib import Path
import argparse
import shutil
import subprocess
from course_documents import EXTENDED, DOCUMENTS, NAVIGATION_PAGES, R_INTRODUCTION_ALIASES, DESCRIPTIVE_PRACTICAL_ALIAS, INFERENTIAL_REDIRECTS, INFERENTIAL_PDF_ALIASES, INFERENTIAL_SOURCE_DOWNLOADS, STUDENT_PROJECT_ZIP, LEGACY_STUDENT_PROJECT_ZIP

ROOT = Path(__file__).resolve().parents[1]

def validate(site):
    required=[n+'.html' for n in NAVIGATION_PAGES]
    required += ['index.html','lessons/02-descriptive-statistics.html','lessons/03-inferential-statistics.html','lessons/01-introduction-to-r.html']
    required += [f'{folder}/{name}.html' for folder, name in DOCUMENTS]
    required += ['pdf/'+name+'.pdf' for _, name in DOCUMENTS]
    required += ['pdf/'+name+'.pdf' for name in R_INTRODUCTION_ALIASES]
    required += ['pdf/'+DESCRIPTIVE_PRACTICAL_ALIAS+'.pdf']
    required += ['pdf/'+n+'.pdf' for n in INFERENTIAL_PDF_ALIASES]
    required += ['pdf/'+p+'.pdf' for p in ['01-introduction-to-r','02-descriptive-statistics','03-inferential-statistics']]
    required += ['extended-cases/superstore/index.html']
    required += ['extended-cases/'+p+'.html' for p in EXTENDED]+['pdf/'+p+'.pdf' for p in EXTENDED]
    import re
    required += re.findall(r'^    - (data/[^\n]+)', (ROOT/'_quarto.yml').read_text(), re.M)
    required += ['data/business/'+p for p in ['superstore-lines.csv','cola.csv','consumer.csv','README.md']]
    required += ['downloads/'+STUDENT_PROJECT_ZIP,'downloads/applied-statistics-pdfs.zip']
    required += ['downloads/'+n for n in INFERENTIAL_SOURCE_DOWNLOADS]
    required += ['downloads/'+LEGACY_STUDENT_PROJECT_ZIP]
    for name in required:
        if not (site/name).exists():raise RuntimeError('Missing generated page: '+name)
    forbidden=[p for p in site.rglob('*') if p.is_file() and (any(t in p.relative_to(site).parts for t in ['instructor','archived','books','sources','_includes']) or p.suffix.lower() in ['.xlsx','.xls'])]
    if forbidden:raise RuntimeError('Local-only files in generated site: '+str(forbidden[:5]))
    expected = {
        'lessons/01-introduction-to-r.html': ['Getting started', 'Variables and atomic data types', 'Working with a classical data frame', 'Preparing data with dplyr', 'Build a meaningful business pipeline', 'Understanding ggplot2', 'Map a group to colour and shape', 'Filter data then draw a histogram', 'Summarise data then draw a bar chart'],
        'lessons/02-descriptive-statistics.html': ['What is Statistics?', 'source-title-87'],
        'lessons/03-inferential-statistics.html': ['part3-01-slide-01', 'part3-04-slide-21'],
    }
    for page, markers in expected.items():
        content = (site/page).read_text()
        if not all(marker in content for marker in markers):
            raise RuntimeError('Incomplete course: '+page)
    # Guard the restored core against future replacement by practical/case rewrites.
    descriptive = (site/'lessons/02-descriptive-statistics.html').read_text()
    # Five redundant/empty outlier slides removed after the 8 November review.
    removed_descriptive = {77, 80, 83, 84, 85, 88}
    if any(f'id="slide-{i:02d}"' not in descriptive
           for i in range(1, 89) if i not in removed_descriptive):
        raise RuntimeError('Incomplete retained descriptive slides')
    if any(f'id="slide-{i:02d}"' in descriptive for i in removed_descriptive):
        raise RuntimeError('Removed redundant or cross-course descriptive slide reintroduced')
    for addition in ['line-chart', 'dot-plot']:
        if f'id="slide-added-{addition}"' not in descriptive:
            raise RuntimeError('Missing added descriptive chart: ' + addition)
    if len(re.findall(r'<!-- BEGIN TRY IN R [\w-]+ -->', descriptive)) != 20:
        raise RuntimeError('Combined Part 2 must contain 20 executed R examples')
    landing = (site/'course/part-2.html').read_text()
    if 'descriptive-statistics-r-practical.html' in landing:
        raise RuntimeError('Part 2 landing page still presents a separate practical')
    inferential = (site/'lessons/03-inferential-statistics.html').read_text()
    if any(f'id="part3-{k:02d}-slide-{i:02d}"' not in inferential
           for k, count in enumerate([37, 26, 57, 21], 1) for i in range(1, count+1)):
        raise RuntimeError('Incomplete original inferential slides: expected 141')
    if len(re.findall(r'<!-- BEGIN R EXAMPLE [\d-]+ -->',inferential)) != 36:
        raise RuntimeError('Part 3 must include 36 executable R examples')
    if any(term in (site/'course/part-3.html').read_text() for term in ['original core slides','Revised 3.1','Open practical','coming soon','forthcoming']):
        raise RuntimeError('Part 3 must present one combined resource')

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--skip-render', action='store_true',
                        help='Reuse a completed full HTML build; refresh practicals and all downloads.')
    args = parser.parse_args()
    subprocess.run(['python3', str(ROOT/'scripts/render-descriptive-chart-additions.py')], cwd=ROOT, check=True)
    subprocess.run(['python3', str(ROOT/'scripts/sync-descriptive-r-references.py'), '--check'], cwd=ROOT, check=True)
    subprocess.run(['python3', str(ROOT/'scripts/check-practicals.py')], cwd=ROOT, check=True)
    shutil.rmtree(ROOT/'_build/practicals', ignore_errors=True)
    if args.skip_render:
        subprocess.run(['python3', str(ROOT/'scripts/preview-practicals.py')], cwd=ROOT, check=True)
        subprocess.run(['python3', str(ROOT/'scripts/stage-practicals.py')], cwd=ROOT, check=True)
    else:
        site = ROOT/'_build/website'
        if site.exists():
            shutil.rmtree(site)
        quarto = shutil.which('quarto') or 'quarto'
        subprocess.run([quarto, 'render', '--quiet'], cwd=ROOT, check=True)
    # Re-stage the explicit data allowlist even when Quarto reuses a resource cache.
    # A previous partial render may have removed files that the cache marks copied.
    import re
    for name in re.findall(r'^    - (data/[^\n]+)', (ROOT/'_quarto.yml').read_text(), re.M):
        target = ROOT/'_build/website'/name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT/name, target)
    subprocess.run(['python3', str(ROOT/'scripts/build-student-downloads.py')], cwd=ROOT, check=True)
    validate(ROOT/'_build/website')
    subprocess.run(['python3', str(ROOT/'scripts/validate-student-site.py')], cwd=ROOT, check=True)
    print(f'Local build verified: {len(DOCUMENTS)} notebooks, {len(DOCUMENTS)} PDFs and both student bundles. Nothing published.', flush=True)

if __name__ == '__main__':
    main()
