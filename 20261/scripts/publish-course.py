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
import sys
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
sys.path.insert(0,str(ROOT/'scripts/teaching-slides'))
from materials import copy_to as copy_teaching_materials
import importlib.util
_chapter_spec=importlib.util.spec_from_file_location('chapter_materials', ROOT/'scripts/book-chapters/materials.py')
_chapter_module=importlib.util.module_from_spec(_chapter_spec)
_chapter_spec.loader.exec_module(_chapter_module)
copy_chapter_materials=_chapter_module.copy_to


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


def package_student_project(project_zip):
    """Package R lessons without maintainer Python scripts or local-only sources."""
    config = (ROOT/'_quarto.yml').read_text()
    if 'pre-render:' in config or 'post-render:' in config:
        raise SystemExit('Keep maintainer render hooks out of the student configuration.')
    project_zip.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='statistics-student-project-') as directory:
        project = Path(directory)/'Applied-Statistics-20261'
        project.mkdir()
        for source in student_sources():
            target = project/source.relative_to(ROOT)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source,target)
        for name in ['data','assets']:
            shutil.copytree(ROOT/name,project/name,ignore=shutil.ignore_patterns('*_files','*_cache','.DS_Store','*.ipynb','.quarto','.Rproj.user','__pycache__'))
        copy_teaching_materials(project)
        copy_chapter_materials(project)
        for name in ['20261.Rproj','index.qmd','_quarto.yml','_quarto-pdf.yml','LICENSE']:
            shutil.copy2(ROOT/name,project/name)
        (project/'scripts').mkdir()
        for name in ['pdf-layout.lua']:
            shutil.copy2(ROOT/'scripts'/name,project/'scripts'/name)
        (project/'README.md').write_text('''# Applied Statistics: student RStudio project

1. Extract the entire ZIP to a writable folder.
2. Install R (4.1 or newer), RStudio Desktop, and Quarto if they are not installed.
3. Open `20261.Rproj` in RStudio. Keep it open while working with lesson files.
4. Open `setup.R` and run it once to install the required R packages. This needs internet access.
5. Open `index.qmd`, or a numbered lesson under `modules/`. Use Render to create its HTML page.
6. Save your own exercises and reports in a new folder such as `my-work/`.

HTML rendering does not require Python or LaTeX. Run individual R chunks while
practicing, and click Render when you want an HTML page. Rebuilding the whole
website is optional: run `quarto render` in RStudio's Terminal.

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
        zip_tree(project,project_zip,project.name)


def package():
    # Source mtimes are a quick guard; manifest hashes identify the exact source content.
    sources = student_sources()
    for source in sources:
        for folder, suffix in [('_site','.html'),('_output/pdf','.pdf')]:
            output = ROOT/folder/source.relative_to(ROOT).with_suffix(suffix)
            if not output.exists() or output.stat().st_mtime < source.stat().st_mtime:
                raise SystemExit(f'Missing or older export: {output}. Run without --package-only.')
    teaching_materials=copy_teaching_materials(ROOT/'_site')
    chapter_materials=copy_chapter_materials(ROOT/'_site')
    pdf_root = ROOT/'_output/pdf-modules'
    pdf_manifest = json.loads((pdf_root/'module-pdf-manifest.json').read_text())
    for name, digest in pdf_manifest['inputs'].items():
        if hashlib.sha256((ROOT/name).read_bytes()).hexdigest() != digest:
            raise SystemExit(f'Stale module PDF input: {name}. Rebuild the PDFs.')
    for name, digest in pdf_manifest['outputs'].items():
        if hashlib.sha256((pdf_root/name).read_bytes()).hexdigest() != digest:
            raise SystemExit(f'Module PDF differs from its checked build: {name}')
    for name, digest in pdf_manifest['topic_exports'].items():
        if hashlib.sha256((ROOT/'_output/pdf'/name).read_bytes()).hexdigest() != digest:
            raise SystemExit(f'Topic export changed after module assembly: {name}. Reassemble the PDFs.')
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
        archive_pdfs = {name for name in archive.namelist() if name.endswith('.pdf') and (name.startswith('modules/') or name.startswith('resources/') or name == 'index.pdf')}
        if archive_pdfs != set(pdf_manifest['outputs']):
            raise SystemExit('PDF archive must contain exactly one PDF per module plus course/resource pages.')
        for relative in pdf_manifest['outputs']:
            if archive.read(relative) != (pdf_root/relative).read_bytes():
                raise SystemExit(f'Stale PDF in archive: {relative}')
        for record in teaching_materials.values():
            for name,digest in record['outputs'].items():
                if hashlib.sha256(archive.read('teaching-slides/'+name)).hexdigest()!=digest:
                    raise SystemExit(f'Stale teaching material in PDF archive: {name}')
        for name,digest in chapter_materials.items():
            if hashlib.sha256(archive.read(name)).hexdigest()!=digest:
                raise SystemExit(f'Stale chapter material in PDF archive: {name}')
    shutil.copy2(pdf_zip,downloads/pdf_zip.name)
    package_student_project(downloads/'applied-statistics-rstudio-project.zip')
    # Separate, focused downloads for the two supplementary categories.
    with zipfile.ZipFile(downloads/'applied-statistics-reduced-review.zip', 'w', zipfile.ZIP_DEFLATED) as archive:
        for p in sorted((stage/'teaching-slides').glob('*.pdf')):
            archive.write(p, p.relative_to(stage))
        for p in sorted((stage/'book-chapters').rglob('*-flashcards.pdf')):
            archive.write(p, p.relative_to(stage))
    with zipfile.ZipFile(downloads/'applied-statistics-book-chapters.zip', 'w', zipfile.ZIP_DEFLATED) as archive:
        for p in sorted((stage/'book-chapters').rglob('*')):
            if p.is_file() and p.suffix in {'.pdf', '.txt'}:
                archive.write(p, p.relative_to(stage))

    # Publish the module PDFs and resource pages, with the same paths as the ZIP.
    pdf_stage = stage/'pdf'
    with zipfile.ZipFile(pdf_zip) as archive: archive.extractall(pdf_stage)
    # Enforce the instructor-only PowerPoint policy on every distribution.
    if list(stage.rglob('*.pptx')):
        raise SystemExit('Editable PowerPoints must remain local.')
    for bundle in downloads.glob('*.zip'):
        with zipfile.ZipFile(bundle) as archive:
            if archive.testzip() or any(name.lower().endswith('.pptx') for name in archive.namelist()):
                raise SystemExit(f'Damaged archive or public PowerPoint: {bundle.name}')
    manifest = {
        'source_commit':run('git','rev-parse','HEAD',cwd=REPO,capture=True).strip(),
        'source_worktree_dirty':bool(run('git','status','--porcelain',cwd=REPO,capture=True).strip()),
        'student_pages':len(sources),'website':URL,
        'source_sha256':{str(s.relative_to(ROOT)):hashlib.sha256(s.read_bytes()).hexdigest() for s in sources},
        'downloads':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in downloads.glob('*.zip')},
        'chapter_materials':chapter_materials,
        'module_pdfs':pdf_manifest['outputs'],
        'teaching_materials':{name:digest for record in teaching_materials.values() for name,digest in record['outputs'].items()},
    }
    (stage/'publication-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    (stage/'.nojekyll').touch()
    print(f'Prepared {len(sources)} HTML pages, PDFs, and five student downloads in {stage}',flush=True)
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
    print('Published-site links, including all five download targets, passed local validation.',flush=True)


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
    parser.add_argument('--student-project-only',action='store_true',help='Create only the student project ZIP; no site/PDF build')
    parser.add_argument('--publish',action='store_true',help='Push generated gh-pages branch and enable Pages hosting')
    args=parser.parse_args()
    if args.student_project_only:
        if args.publish or args.package_only:
            parser.error('--student-project-only cannot be combined with other options')
        target = ROOT/'_output/applied-statistics-rstudio-project.zip'
        package_student_project(target)
        print(f'Prepared student RStudio project: {target}',flush=True)
        return
    if args.publish and run('git','status','--porcelain',cwd=REPO,capture=True).strip():
        raise SystemExit('Commit source changes before publishing so the manifest identifies a clean source commit.')
    if not args.package_only:
        run('python3','scripts/audit-code-documentation.py')
        run('python3','scripts/build-pdfs.py')
        run(QUARTO,'render')
    stage=package()
    validate_stage(stage)
    if args.publish:publish(stage)


if __name__=='__main__':main()
