#!/usr/bin/env python3
"""Compatibility helper: preview the extended cereals practical and its old entry page."""
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
QUARTO = shutil.which('quarto') or '/usr/lib/rstudio/resources/app/bin/quarto/bin/quarto'
if __name__ == '__main__':
    for name in ['practical-02-numerical-business-data.qmd', 'practical-01-cereals.qmd']:
        subprocess.run([QUARTO, 'render', str(Path('practicals') / name), '--to', 'html'],
                       cwd=ROOT, check=True)
    print('Cereals preview:', ROOT / '_build/practicals/practical-02-numerical-business-data.html')
