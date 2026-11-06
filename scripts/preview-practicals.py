#!/usr/bin/env python3
"""Render the independent Part 2 practicals without publishing them."""
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
QUARTO = shutil.which('quarto') or '/usr/lib/rstudio/resources/app/bin/quarto/bin/quarto'
if __name__ == '__main__':
    subprocess.run([QUARTO, 'render', 'practicals', '--to', 'html'], cwd=ROOT, check=True)
    print('Practical previews:', ROOT / '_build/practicals')
