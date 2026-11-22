#!/usr/bin/env python3
"""Check approved website/download contents and local navigation before release."""
from pathlib import Path
from html import unescape
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import re
import zipfile
import hashlib
import yaml

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / '_build/website'
from student_project import student_path, RUNNABLE_DOCUMENTS, project_files
from course_documents import LESSONS, DOCUMENTS, NAVIGATION_PAGES, R_CODE_DOWNLOADS, STUDENT_PROJECT_ZIP

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name == 'id' and value:
                self.ids.add(value)
            if name == 'href' and value:
                self.hrefs.append(value)

if __name__ == '__main__':
    pages = [SITE/(n+'.html') for n in NAVIGATION_PAGES]
    pages += [SITE/folder/(n+'.html') for folder, n in DOCUMENTS]
    parsed = {}
    for path in SITE.rglob('*.html'):
        links = Links()
        links.feed(path.read_text())
        parsed[path.resolve()] = links
    for page in pages:
        text = page.read_text()
        assert 'class="cell-output cell-output-error"' not in text, page
        links = parsed[page.resolve()]
        for href in links.hrefs:
            target = urlsplit(unescape(href))
            if target.scheme or target.netloc or target.path.startswith('/'):
                continue
            path = (page.parent/unquote(target.path)).resolve() if target.path else page.resolve()
            assert path.exists(), (page.name, href)
            if target.fragment and path.suffix == '.html':
                assert unquote(target.fragment) in parsed[path].ids, (page.name, href, 'missing fragment')
    from r_code_files import r_code_files, r_code_source
    scripts = r_code_files()
    for name, code in scripts.items():
        assert (SITE/'downloads'/name).read_text() == code
    assert len(DOCUMENTS)==13 and len(RUNNABLE_DOCUMENTS)==13
    assert not (SITE/'practicals').exists(), 'Obsolete practical entry pages returned'
    assert {p.name for p in (SITE/'pdf').iterdir()} == {n+'.pdf' for _, n in DOCUMENTS}, 'Unexpected duplicate PDF downloads'
    assert {p.name for p in (SITE/'downloads').iterdir()} == {STUDENT_PROJECT_ZIP, 'applied-statistics-pdfs.zip', *R_CODE_DOWNLOADS}, 'Unexpected duplicate downloads'
    for folder in ['lessons', 'course']:
        expected = {SITE/(n+'.html') for n in NAVIGATION_PAGES if n.startswith(folder+'/')}
        expected |= {SITE/f/(n+'.html') for f,n in DOCUMENTS if f == folder}
        assert set((SITE/folder).glob('*.html')) == expected, 'Obsolete '+folder+' pages returned'
    assert not (SITE/'.vscode').exists(), 'Editor preferences belong in the student ZIP only'
    assert not (SITE/'data/practicals').exists(), 'Retired practical data leaked into site'
    for path in SITE.rglob('*'):
        if not path.is_file():
            continue
        assert not set(path.relative_to(SITE).parts) & {'instructor', 'books', 'sources', 'archived', '_includes'}, path
        if path.relative_to(SITE).as_posix() not in {'downloads/'+n for n in R_CODE_DOWNLOADS}:
            assert path.suffix.lower() not in {'.xls', '.xlsx', '.pptx', '.qmd', '.r', '.rproj'}, path
    with zipfile.ZipFile(SITE/'downloads/applied-statistics-pdfs.zip') as bundle:
        assert set(bundle.namelist()) == {n+'.pdf' for _, n in DOCUMENTS}
    with zipfile.ZipFile(SITE/'downloads'/STUDENT_PROJECT_ZIP) as bundle:
        names = set(bundle.namelist())
        assert '.vscode/settings.json' in names
        for name in LESSONS[2:]:
            lesson = 'lessons/'+name+'.qmd'
            assert bundle.read(student_path(lesson)) == (ROOT/lesson).read_bytes(), 'Same Quarto source required: '+name
        assert not any('inferential-statistics-r-practical' in n or 'probability-distributions-draft' in n or 'inferential-statistics-integrated' in n for n in names)
        for image in ['pipe_operator.png', 'clipboard-834917176.png']:
            original = 'assets/introduction-to-r/' + image
            assert original in names, original
            assert bundle.read(original) == (ROOT/original).read_bytes(), original

        import json
        settings = json.loads(bundle.read('.vscode/settings.json'))
        assert settings['quarto.inlineOutput.enabled'] is False
        assert not any(n.lower().endswith('.rproj') for n in names)
        for name in names:
            if Path(name).suffix.lower() in {'.qmd', '.r', '.md'}:
                assert 'rstudio' not in bundle.read(name).decode().lower(), name

        script_paths = {str(Path(student_path(r_code_source(n))).with_suffix('.R')) for n in scripts}
        jupyter_paths = {str(Path(student_path(f'{f}/{n}.qmd')).with_suffix('.ipynb'))
                         for f,n in RUNNABLE_DOCUMENTS}
        assert names == {student_path(n) for n in project_files()} | {'README.md', '_quarto.yml'} | script_paths | jupyter_paths
        from jupyter_notebooks import validate_notebook
        for name in jupyter_paths:
            notebook = json.loads(bundle.read(name))
            validate_notebook(notebook)
            source = notebook['metadata']['course']['source']
            assert notebook['metadata']['course']['source_sha256'] == hashlib.sha256(bundle.read(source)).hexdigest()
        for name, code in scripts.items():
            from student_project import rewrite
            source = r_code_source(name)
            assert bundle.read(str(Path(student_path(source)).with_suffix('.R'))).decode() == rewrite(source, code, project_files())
        config = yaml.safe_load(bundle.read('_quarto.yml'))
        assert 'website' not in config
        assert config['project']['execute-dir'] == 'project'
        assert set(config['project']['render']) == {student_path(f'{f}/{n}.qmd') for f,n in RUNNABLE_DOCUMENTS}
        assert {student_path(f'{folder}/{n}.qmd') for folder, n in RUNNABLE_DOCUMENTS} <= names
        # Packaging may relocate helper paths, but must preserve teaching R code.
        for folder, notebook in RUNNABLE_DOCUMENTS:
            source = f'{folder}/{notebook}.qmd'
            def teaching_chunks(text):
                return [c for c in re.findall(r'```\{r[^\n]*\}\n(.*?)```', text, re.S)
                        if 'label: render-project-root' not in c]
            original = teaching_chunks((ROOT/source).read_text())
            original = [c.replace('lessons/_includes/', 'support/') for c in original]
            assert original == teaching_chunks(bundle.read(student_path(source)).decode()), source
        allowed_data = {n for n in project_files() if n.startswith('data/')}
        assert allowed_data <= set(re.findall(r'^    - (data/[^\n]+)', (ROOT/'_quarto.yml').read_text(), re.M))
        assert {n for n in names if n.startswith('data/')} == allowed_data
        for name in allowed_data:
            expected = hashlib.sha256((ROOT/name).read_bytes()).digest()
            assert hashlib.sha256(bundle.read(name)).digest() == expected, (name, 'ZIP data mismatch')
            assert hashlib.sha256((SITE/name).read_bytes()).digest() == expected, (name, 'site data mismatch')
        assert {'data/business/superstore-lines.csv', 'data/business/cola.csv',
                'data/business/README.md', 'support/course-tools.R',
                'assets/practical-print.css'} <= names
        assert not any(n.startswith(('lessons/', 'practicals/', 'scripts/', 'course/')) for n in names)
        assert {n for n in names if n.endswith('.qmd') and not n.startswith('support/')} == {student_path(f'{f}/{n}.qmd') for f,n in RUNNABLE_DOCUMENTS}
        assert not any(n.startswith('data/practicals/') for n in names)
        assert 'data/descriptive-statistics/students.csv' in names
        assert not any(set(Path(n).parts) & {'instructor', 'books', 'sources', 'archived', '_build'} for n in names)
        assert not any(Path(n).suffix.lower() in {'.xls', '.xlsx', '.pptx'} for n in names)
    print(f'Student site links, {len(DOCUMENTS)}-PDF bundle and {len(RUNNABLE_DOCUMENTS)}-notebook Positron package verified.')
