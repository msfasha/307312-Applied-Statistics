#!/usr/bin/env python3
"""Resolve links and copy canonical teaching data for standalone practical previews."""
from pathlib import Path
import re
import shutil
ROOT = Path(__file__).resolve().parents[1]
PREVIEW = ROOT / '_build/practicals'
for page in PREVIEW.glob('*.html'):
    text = page.read_text()
    text = re.sub(r'href="../(lessons|extended-cases)/([^"#]+)\.qmd',
                  r'href="../website/\1/\2.html', text)
    text = re.sub(r'href="([^"/#]+)\.qmd', r'href="\1.html', text)
    text = text.replace('href="../data/', 'href="data/')
    text = text.replace('href="../pdf/', 'href="../website/pdf/')
    text = text.replace('href="../downloads/', 'href="../website/downloads/')
    page.write_text(text)
for folder in ['business', 'descriptive-statistics']:
    for source in (ROOT / 'data' / folder).iterdir():
        if source.suffix not in ['.csv', '.md']:
            continue
        destination = PREVIEW / 'data' / folder / source.name
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
