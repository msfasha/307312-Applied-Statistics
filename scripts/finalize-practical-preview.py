#!/usr/bin/env python3
"""Copy pilot downloads from canonical data and resolve local-preview links."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
PREVIEW = ROOT / '_build/practicals'
page = PREVIEW / 'practical-01-cereals.html'
if not page.exists():
    raise RuntimeError('Missing rendered CEREALS practical')
text = page.read_text()
text = text.replace('href="../data/practicals/', 'href="data/practicals/')
text = text.replace('href="../lessons/02-descriptive-statistics.qmd"',
                    'href="../website/lessons/02-descriptive-statistics.html"')
page.write_text(text)
for name in ['cereals.csv', 'README.md']:
    destination = PREVIEW / 'data/practicals' / name
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / 'data/practicals' / name, destination)
