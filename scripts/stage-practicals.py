#!/usr/bin/env python3
"""Copy only the approved self-contained practical HTML into the course site."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
NAMES = ['practical-01-categorical-business-data', 'practical-02-numerical-business-data',
         'practical-03-association-and-groups']

if __name__ == '__main__':
    destination = ROOT / '_build/website/practicals'
    destination.mkdir(parents=True, exist_ok=True)
    for name in NAMES + ['practical-01-cereals']:
        source = ROOT / '_build/practicals' / (name + '.html')
        text = source.read_text()
        text = text.replace('href="data/business/', 'href="../data/business/')
        text = text.replace('href="../website/lessons/', 'href="../lessons/')
        text = text.replace('href="../website/pdf/', 'href="../pdf/')
        text = text.replace('href="../website/downloads/', 'href="../downloads/')
        (destination / source.name).write_text(text)
    for name in ['superstore-lines.csv', 'cola.csv', 'consumer.csv', 'README.md']:
        target = ROOT / '_build/website/data/business' / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / 'data/business' / name, target)
    print('Staged three approved practicals and their student data.')
