#!/usr/bin/env python3
"""Copy canonical student data and resolve standalone practical-preview links."""
from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
PREVIEW = ROOT / '_build/practicals'
for page in PREVIEW.glob('*.html'):
    text = page.read_text()
    text = text.replace('href="../data/practicals/', 'href="data/practicals/')
    text = re.sub(r'href="../lessons/([^"#]+)\.qmd',
                  r'href="../website/lessons/\1.html', text)
    text = re.sub(r'href="(practical-[^"#]+)\.qmd', r'href="\1.html', text)
    page.write_text(text)
for name in ['cereals.csv', 'funds2002.csv', 'README.md']:
    destination = PREVIEW / 'data/practicals' / name
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / 'data/practicals' / name, destination)
