#!/usr/bin/env python3
"""Stage the descriptive practical and compatibility links to relocated Superstore cases."""
from pathlib import Path
from course_documents import PRACTICALS, SUPERSTORE
ROOT = Path(__file__).resolve().parents[1]
if __name__ == '__main__':
    destination = ROOT / '_build/website/practicals'
    destination.mkdir(parents=True, exist_ok=True)
    for name in PRACTICALS + SUPERSTORE + ['practical-01-cereals']:
        source = ROOT / '_build/practicals' / (name + '.html')
        text = source.read_text()
        text = text.replace('href="data/', 'href="../data/')
        text = text.replace('href="../website/', 'href="../')
        (destination / source.name).write_text(text)
    print('Staged descriptive practical and legacy Superstore links.')
