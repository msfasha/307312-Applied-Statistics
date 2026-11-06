#!/usr/bin/env python3
"""Render the same independent practical project used by RStudio Preview."""
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
QUARTO = shutil.which('quarto') or '/usr/lib/rstudio/resources/app/bin/quarto/bin/quarto'

if __name__ == '__main__':
    subprocess.run([QUARTO, 'render', 'practicals/practical-01-cereals.qmd',
                    '--to', 'html'], cwd=ROOT, check=True)
    print('Pilot preview:', ROOT / '_build/practicals/practical-01-cereals.html')
