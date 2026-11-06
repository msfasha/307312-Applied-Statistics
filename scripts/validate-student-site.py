#!/usr/bin/env python3
"""Check approved website/download contents and local navigation before release."""
from pathlib import Path
from html import unescape
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / '_build/website'
LESSONS = ['01-introduction-to-r', '02-descriptive-statistics', '03-inferential-statistics']
PRACTICALS = ['practical-01-categorical-business-data', 'practical-02-numerical-business-data',
              'practical-03-association-and-groups']

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name == 'href' and value:
                self.hrefs.append(value)

if __name__ == '__main__':
    pages = [SITE/'index.html'] + [SITE/'lessons'/(n+'.html') for n in LESSONS]
    pages += [SITE/'practicals'/(n+'.html') for n in PRACTICALS]
    for page in pages:
        text = page.read_text()
        assert 'class="cell-output cell-output-error"' not in text, page
        links = Links()
        links.feed(text)
        for href in links.hrefs:
            target = urlsplit(unescape(href))
            if target.scheme or target.netloc or not target.path or target.path.startswith('/'):
                continue
            assert (page.parent/unquote(target.path)).exists(), (page.name, href)
    for path in SITE.rglob('*'):
        if not path.is_file():
            continue
        assert not set(path.relative_to(SITE).parts) & {'instructor', 'books', 'sources', 'archived', '_includes'}, path
        assert path.suffix.lower() not in {'.xls', '.xlsx', '.pptx', '.qmd', '.r'}, path
    with zipfile.ZipFile(SITE/'downloads/applied-statistics-pdfs.zip') as bundle:
        assert set(bundle.namelist()) == {n+'.pdf' for n in LESSONS+PRACTICALS}
    with zipfile.ZipFile(SITE/'downloads/applied-statistics-rstudio.zip') as bundle:
        names = set(bundle.namelist())
        assert {f'practicals/{n}.qmd' for n in PRACTICALS} <= names
        assert {'data/practicals/funds2002.csv', 'data/practicals/cereals.csv',
                'practicals/_includes/petra-plots.R', 'assets/practical-print.css', 'scripts/stage-practicals.py',
                'scripts/preview-practicals.py', 'scripts/finalize-practical-preview.py'} <= names
        assert not any(set(Path(n).parts) & {'instructor', 'books', 'sources', 'archived', '_build'} for n in names)
        assert not any(Path(n).suffix.lower() in {'.xls', '.xlsx', '.pptx'} for n in names)
    print('Student site links, six-PDF bundle and complete RStudio package verified.')
