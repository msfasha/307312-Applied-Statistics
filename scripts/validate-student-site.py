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
from course_documents import LESSONS, PRACTICALS, EXTENDED, DOCUMENTS, SUPERSTORE, NAVIGATION_PAGES, R_INTRODUCTION_ALIASES, STUDENT_PROJECT_ZIP, LEGACY_STUDENT_PROJECT_ZIP

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
    pages += [SITE/'practicals'/(n+'.html') for n in SUPERSTORE]
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
    for alias in R_INTRODUCTION_ALIASES:
        assert (SITE/'pdf'/(alias+'.pdf')).read_bytes() == (SITE/'pdf/01-introduction-to-r.pdf').read_bytes(), alias
        assert '01-introduction-to-r.html' in (SITE/'lessons'/(alias+'.html')).read_text(), alias
    assert (SITE/'downloads/inferential-statistics-r-practical.qmd').read_bytes() == (ROOT/'practicals/inferential-statistics-r-practical.qmd').read_bytes()
    assert not (SITE/'.vscode').exists(), 'Editor preferences belong in the student ZIP only'
    assert not (SITE/'data/practicals').exists(), 'Retired practical data leaked into site'
    for path in SITE.rglob('*'):
        if not path.is_file():
            continue
        assert not set(path.relative_to(SITE).parts) & {'instructor', 'books', 'sources', 'archived', '_includes'}, path
        if path.relative_to(SITE).as_posix() != 'downloads/inferential-statistics-r-practical.qmd':
            assert path.suffix.lower() not in {'.xls', '.xlsx', '.pptx', '.qmd', '.r', '.rproj'}, path
    with zipfile.ZipFile(SITE/'downloads/applied-statistics-pdfs.zip') as bundle:
        assert set(bundle.namelist()) == {n+'.pdf' for _, n in DOCUMENTS}
    with zipfile.ZipFile(SITE/'downloads'/STUDENT_PROJECT_ZIP) as bundle:
        names = set(bundle.namelist())
        assert '.vscode/settings.json' in names
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
        assert (SITE/'downloads'/STUDENT_PROJECT_ZIP).read_bytes() == (SITE/'downloads'/LEGACY_STUDENT_PROJECT_ZIP).read_bytes()

        assert names == {student_path(n) for n in project_files()} | {'README.md', '_quarto.yml'}
        config = yaml.safe_load(bundle.read('_quarto.yml'))
        assert 'website' not in config
        assert config['project']['execute-dir'] == 'project'
        assert set(config['project']['render']) == {student_path(f'{f}/{n}.qmd') for f,n in RUNNABLE_DOCUMENTS}
        assert {student_path(f'practicals/{n}.qmd') for n in PRACTICALS} <= names
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
