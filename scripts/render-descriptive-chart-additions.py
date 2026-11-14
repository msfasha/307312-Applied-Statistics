#!/usr/bin/env python3
"""Reproduce the added slide charts from the practical's canonical R cells."""
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]

def render():
    notebook = (ROOT/'practicals/descriptive-statistics-r-practical.qmd').read_text()
    commands = ['students <- read.csv("data/descriptive-statistics/students.csv", stringsAsFactors = FALSE)']
    for kind in ['line-chart', 'dot-plot']:
        code = re.search(r'^```\{r\}\n#\| label: r-slide-added-' + kind + r'\n(.*?)^```', notebook, re.M | re.S)[1]
        commands += [f'svg(filename = "assets/descriptive-statistics/added-{kind}.svg", width = 7, height = 4.5)', code, 'dev.off()']
    subprocess.run(['Rscript', '--vanilla', '-e', '\n'.join(commands)], cwd=ROOT, check=True)

if __name__ == '__main__':
    render()
