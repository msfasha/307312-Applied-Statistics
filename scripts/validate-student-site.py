#!/usr/bin/env python3
"""Check approved website/download contents and local navigation before release."""
from pathlib import Path
from html import unescape
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import re
import zipfile
import hashlib

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / '_build/website'
from course_documents import LESSONS, PRACTICALS, EXTENDED, DOCUMENTS, SUPERSTORE

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
    pages = [SITE/'index.html', SITE/'extended-cases/superstore/index.html']
    pages += [SITE/folder/(n+'.html') for folder, n in DOCUMENTS]
    pages += [SITE/'practicals'/(n+'.html') for n in SUPERSTORE]
    parsed = {}
    for path in SITE.rglob('*.html'):
        links = Links()
        links.feed(path.read_text())
        parsed[path.resolve()] = links
    for page in pages:
        text = page.read_text()
        if page.name == 'r-02-basic-concepts.html':
            # Two explicit error=T source demonstrations emit three expected errors.
            assert text.count('class="cell-output cell-output-error"') == 3, page
        else:
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
    assert not (SITE/'data/practicals').exists(), 'Retired practical data leaked into site'
    for path in SITE.rglob('*'):
        if not path.is_file():
            continue
        assert not set(path.relative_to(SITE).parts) & {'instructor', 'books', 'sources', 'archived', '_includes'}, path
        assert path.suffix.lower() not in {'.xls', '.xlsx', '.pptx', '.qmd', '.r'}, path
    with zipfile.ZipFile(SITE/'downloads/applied-statistics-pdfs.zip') as bundle:
        assert set(bundle.namelist()) == {n+'.pdf' for _, n in DOCUMENTS}
    with zipfile.ZipFile(SITE/'downloads/applied-statistics-rstudio.zip') as bundle:
        names = set(bundle.namelist())
        assert {f'practicals/{n}.qmd' for n in PRACTICALS} <= names
        assert {f'{folder}/{n}.qmd' for folder, n in DOCUMENTS} <= names
        assert 'extended-cases/superstore/index.qmd' in names
        allowed_data = set(re.findall(r'^    - (data/[^\n]+)', (ROOT/'_quarto.yml').read_text(), re.M))
        assert {n for n in names if n.startswith('data/')} == allowed_data
        for name in allowed_data:
            expected = hashlib.sha256((ROOT/name).read_bytes()).digest()
            assert hashlib.sha256(bundle.read(name)).digest() == expected, (name, 'ZIP data mismatch')
            assert hashlib.sha256((SITE/name).read_bytes()).digest() == expected, (name, 'site data mismatch')
        assert {'data/business/superstore-lines.csv', 'data/business/cola.csv', 'data/business/consumer.csv',
                'data/business/README.md', 'lessons/_includes/course-tools.R',
                'practicals/_includes/petra-plots.R', 'assets/practical-print.css', 'scripts/stage-practicals.py',
                'scripts/preview-practicals.py', 'scripts/finalize-practical-preview.py'} <= names
        assert not any(n.startswith('data/practicals/') for n in names)
        assert {'lessons/_includes/data-collection-and-surveys.qmd',
                'lessons/_includes/diagrams/09-types-of-data.qmd',
                'data/descriptive-statistics/students.csv',
                'data/inferential-statistics/houses.csv'} <= names
        assert not any(set(Path(n).parts) & {'instructor', 'books', 'sources', 'archived', '_build'} for n in names)
        assert not any(Path(n).suffix.lower() in {'.xls', '.xlsx', '.pptx'} for n in names)
    print('Student site links, sixteen-PDF bundle and complete RStudio package verified.')
