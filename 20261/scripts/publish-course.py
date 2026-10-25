#!/usr/bin/env python3
"""Build, package, and optionally publish the student course to GitHub Pages.

Generated files live on gh-pages; editable sources remain on main. The default
build runs both Quarto exports. --package-only reuses verified current exports.
"""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import subprocess
import tempfile
import zipfile
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent
REMOTE = 'https://github.com/msfasha/307312-Applied-Statistics.git'
SLUG = 'msfasha/307312-Applied-Statistics'
URL = 'https://msfasha.github.io/307312-Applied-Statistics/'
QUARTO = shutil.which('quarto') or '/usr/lib/rstudio/resources/app/bin/quarto/bin/quarto'


def run(*args, cwd=ROOT, capture=False, input=None):
    return subprocess.run(args, cwd=cwd, check=True, text=True, input=input,
                          stdout=subprocess.PIPE if capture else None).stdout


def student_sources():
    return [ROOT/'index.qmd'] + sorted((ROOT/'modules').rglob('*.qmd')) + sorted((ROOT/'resources').rglob('*.qmd')) + sorted((ROOT/'resources').rglob('*.Rmd'))


def zip_tree(folder, target, prefix=''):
    with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(folder.rglob('*')):
            if path.is_file():
                archive.write(path, str(Path(prefix)/path.relative_to(folder)))


def package():
    # Source mtimes are a quick guard; manifest hashes identify the exact source content.
    sources = student_sources()
    for source in sources:
        for folder, suffix in [('_site','.html'),('_output/pdf','.pdf')]:
            output = ROOT/folder/source.relative_to(ROOT).with_suffix(suffix)
            if not output.exists() or output.stat().st_mtime < source.stat().st_mtime:
                raise SystemExit(f'Missing or older export: {output}. Run without --package-only.')
    run('python3','scripts/validate-course.py')
    run('python3','scripts/audit-code-documentation.py')
    stage = ROOT/'_output/publish-site'
    if stage.exists(): shutil.rmtree(stage)
    shutil.copytree(ROOT/'_site',stage)
    # The website ZIP is made before download archives are added, avoiding recursive bundles.
    website_zip = ROOT/'_output/applied-statistics-website.zip'
    zip_tree(stage,website_zip)
    downloads = stage/'downloads'
    downloads.mkdir(exist_ok=True)
    shutil.copy2(website_zip,downloads/website_zip.name)
    pdf_zip = ROOT/'_output/applied-statistics-student-pdfs.zip'
    with zipfile.ZipFile(pdf_zip) as archive:
        if archive.testzip(): raise SystemExit('Damaged PDF archive')
        for source in sources:
            relative = str(source.relative_to(ROOT).with_suffix('.pdf'))
            if archive.read(relative) != (ROOT/'_output/pdf'/relative).read_bytes():
                raise SystemExit(f'Stale PDF in archive: {relative}')
    shutil.copy2(pdf_zip,downloads/pdf_zip.name)
    project_zip = downloads/'applied-statistics-rstudio-project.zip'
    with tempfile.TemporaryDirectory(prefix='statistics-student-project-') as directory:
        project = Path(directory)/'Applied-Statistics-20261'
        project.mkdir()
        for name in ['modules','resources','data','assets']:
            shutil.copytree(ROOT/name,project/name,ignore=shutil.ignore_patterns('*_files','*_cache','.DS_Store'))
        for name in ['20261.Rproj','index.qmd','_quarto.yml','_quarto-pdf.yml','LICENSE']:
            shutil.copy2(ROOT/name,project/name)
        # Student HTML rendering requires R/Quarto, without the maintainer's Python audit hooks.
        config = project/'_quarto.yml'
        config.write_text(config.read_text().replace(
            '  pre-render:\n    - python3 scripts/audit-code-documentation.py\n', '').replace(
            '  post-render:\n    - python3 scripts/validate-course.py\n', ''))
        (project/'scripts').mkdir()
        for name in ['audit-code-documentation.py','validate-course.py','build-pdfs.py','pdf-layout.lua']:
            shutil.copy2(ROOT/'scripts'/name,project/'scripts'/name)
        (project/'README.md').write_text('''# Applied Statistics: student RStudio project

1. Extract the entire ZIP to a writable folder.
2. Install R (4.1 or newer), RStudio Desktop, and Quarto if they are not installed.
3. Open `20261.Rproj` in RStudio. Keep it open while working with lesson files.
4. Open `setup.R` and run it once to install the required R packages. This needs internet access.
5. Open `index.qmd`, or a numbered lesson under `modules/`. Use Render to create its HTML page.
6. For the complete website, run `quarto render` in RStudio's Terminal; open `_site/index.html` afterward.
7. Save your own exercises and reports in a new folder such as `my-work/`.

The included CSVs are ready for lesson use. Local instructor textbook PDFs, publisher
workbooks, original measurement workbooks, instructor answers, and instructor-only
verification scripts are not required and are not included. Provenance notes identify
those original sources; paths to them describe the instructor's local collection.

Reading the website or supplied PDFs does not require R or RStudio. Individual PDF
rendering additionally needs the LaTeX/fonts documented by your instructor; use the
separate ready-made PDF download if you only want to read or print.

Course website: https://msfasha.github.io/307312-Applied-Statistics/
Student downloads: https://msfasha.github.io/307312-Applied-Statistics/resources/downloads.html

Keep attribution and source notices with redistributed material. Third-party teaching
data and textbook excerpts retain their original rights and are not relicensed by this project.
''')
        (project/'setup.R').write_text('''# c() combines package names into a character vector for the installation step.
# install.packages() downloads these packages from the specified CRAN repository; run this once online.
packages <- c("knitr", "rmarkdown", "ggplot2", "dplyr", "tidyr", "readr", "stringr")
install.packages(packages, repos = "https://cloud.r-project.org")
''')
        run('python3','scripts/audit-code-documentation.py',cwd=project)
        zip_tree(project,project_zip,project.name)
    # Publish individual PDFs as well as the ZIP, preserving cross-document links.
    pdf_stage = stage/'pdf'
    with zipfile.ZipFile(pdf_zip) as archive: archive.extractall(pdf_stage)
    manifest = {
        'source_commit':run('git','rev-parse','HEAD',cwd=REPO,capture=True).strip(),
        'source_worktree_dirty':bool(run('git','status','--porcelain',cwd=REPO,capture=True).strip()),
        'student_pages':len(sources),'website':URL,
        'source_sha256':{str(s.relative_to(ROOT)):hashlib.sha256(s.read_bytes()).hexdigest() for s in sources},
        'downloads':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in downloads.glob('*.zip')},
    }
    (stage/'publication-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    (stage/'.nojekyll').touch()
    print(f'Prepared {len(sources)} HTML pages, PDFs, and three student downloads in {stage}',flush=True)
    return stage



def validate_stage(stage):
    """Resolve both relative links and absolute links to this Pages site locally."""
    class Links(HTMLParser):
        def __init__(self):
            super().__init__()
            self.values=[]
        def handle_starttag(self, tag, attrs):
            self.values.extend(value for key,value in attrs if key in {'href','src'} and value)
    published=urlparse(URL)
    errors=[]
    for page in stage.rglob('*.html'):
        parser=Links()
        parser.feed(page.read_text())
        for value in parser.values:
            uri=urlparse(value)
            if uri.netloc==published.netloc and uri.path.startswith(published.path):
                target=stage/unquote(uri.path[len(published.path):])
            elif not uri.scheme and not uri.netloc and uri.path:
                target=page.parent/unquote(uri.path)
            else:
                continue
            if not target.exists():errors.append(f'{page.relative_to(stage)} -> {value}')
    if errors:raise SystemExit('Broken publication links:\n'+'\n'.join(errors))
    print('Published-site links, including the three download targets, passed local validation.',flush=True)


def publish(stage):
    # Isolate the generated branch in a temporary checkout; never change the working source branch.
    with tempfile.TemporaryDirectory(prefix='statistics-pages-') as directory:
        checkout = Path(directory)
        run('git','init','--initial-branch=gh-pages',str(checkout),cwd=REPO)
        run('git','remote','add','origin',REMOTE,cwd=checkout)
        exists = run('git','ls-remote','--heads','origin','gh-pages',cwd=checkout,capture=True).strip()
        if exists:
            run('git','fetch','--depth=1','origin','gh-pages',cwd=checkout)
            run('git','checkout','-B','gh-pages','FETCH_HEAD',cwd=checkout)
            for path in checkout.iterdir():
                if path.name=='.git':continue
                if path.is_dir():shutil.rmtree(path)
                else:path.unlink()
        shutil.copytree(stage,checkout,dirs_exist_ok=True)
        for key in ['user.name','user.email']:
            value = run('git','config',key,cwd=REPO,capture=True).strip()
            run('git','config',key,value,cwd=checkout)
        run('git','add','--all',cwd=checkout)
        unchanged = subprocess.run(['git','diff','--cached','--quiet'],cwd=checkout).returncode==0
        if not unchanged:
            run('git','commit','-m','Publish verified student course and downloads',cwd=checkout)
            run('git','push','origin','gh-pages',cwd=checkout)
    status = subprocess.run(['gh','api',f'repos/{SLUG}/pages'],cwd=REPO,capture_output=True,text=True)
    if status.returncode and '404' not in status.stderr:
        raise SystemExit(status.stderr)
    method = 'POST' if status.returncode else 'PUT'
    run('gh','api',f'repos/{SLUG}/pages','--method',method,'--input','-',cwd=REPO,
        input=json.dumps({'build_type':'legacy','source':{'branch':'gh-pages','path':'/'}}))
    print(f'Published branch; GitHub Pages deployment status must be checked at {URL}',flush=True)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--package-only',action='store_true',help='Reuse existing exports after freshness checks')
    parser.add_argument('--publish',action='store_true',help='Push generated gh-pages branch and enable Pages hosting')
    args=parser.parse_args()
    if args.publish and run('git','status','--porcelain',cwd=REPO,capture=True).strip():
        raise SystemExit('Commit source changes before publishing so the manifest identifies a clean source commit.')
    if not args.package_only:
        run('python3','scripts/build-pdfs.py')
        run(QUARTO,'render')
    stage=package()
    validate_stage(stage)
    if args.publish:publish(stage)


if __name__=='__main__':main()
