#!/usr/bin/env python3
"""Verify core practical data, worked R cells and interactive import locations."""
import csv
import hashlib
import json
import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = [ROOT / 'practicals' / name for name in [
    'practical-01-categorical-business-data.qmd',
    'practical-02-numerical-business-data.qmd',
    'practical-03-association-and-groups.qmd']]

def run_r(code, cwd):
    # Route any noninteractive charts away from the editable workspace.
    code = 'pdf(file = tempfile(fileext = ".pdf"))\n' + code + '\ndev.off()\n'
    with tempfile.NamedTemporaryFile(mode='w', suffix='.R') as stream:
        stream.write(code)
        stream.flush()
        result = subprocess.run(['Rscript', '--vanilla', stream.name], cwd=cwd,
                                text=True, capture_output=True)
    if result.returncode:
        raise RuntimeError(result.stdout + result.stderr)

def verify_data():
    for stem, key in [('funds2002', 'output_sha256'), ('cereals', 'csv_sha256')]:
        path = ROOT / 'data/practicals' / (stem + '.csv')
        manifest = json.loads(path.with_name(stem + '-provenance.json').read_text())
        assert hashlib.sha256(path.read_bytes()).hexdigest() == manifest[key], stem
        with path.open(newline='') as stream:
            rows = list(csv.DictReader(stream))
        assert len(rows) == manifest['rows'] and all(all(v != '' for v in r.values()) for r in rows)
    # Recheck the derived fund extract against publisher text when available.
    manifest = json.loads((ROOT / 'data/practicals/funds2002-provenance.json').read_text())
    source = ROOT / manifest['source_file']
    if source.exists():
        assert hashlib.sha256(source.read_bytes()).hexdigest() == manifest['source_sha256']
        with source.open(newline='') as stream:
            rows = list(csv.reader(stream, delimiter='\t'))[1:]
        for row in rows:
            row[1] = row[1].strip()
        with (ROOT / manifest['output_file']).open(newline='') as stream:
            assert list(csv.reader(stream))[1:] == rows

if __name__ == '__main__':
    verify_data()
    checks = 0
    for notebook in NOTEBOOKS:
        chunks = re.findall(r'^```\{r\}[^\n]*\n(.*?)^```\s*$', notebook.read_text(), re.M | re.S)
        worked = [c for c in chunks if not re.search(r'^#\|\s*eval:\s*false', c, re.M)]
        imports = [c for c in worked if 'data_dir <-' in c]
        assert len(imports) == 1 and worked, notebook.name
        for cwd in [ROOT, notebook.parent]:
            run_r(imports[0], cwd)
            run_r('\n'.join(worked), cwd)
            checks += 2
        print('Passed worked cells and isolated import from both locations:', notebook.name)
    run_r('''
d <- read.csv("data/practicals/funds2002.csv")
c <- read.csv("data/practicals/cereals.csv")
near <- function(x, y) length(x) == length(y) && all(abs(as.numeric(x) - as.numeric(y)) <= 1e-7)
stopifnot(nrow(d) == 259, ncol(d) == 13, !anyNA(d),
          sum(d$objective == "Growth") == 158, sum(d$objective == "Value") == 101,
          sum(d$risk %in% c("very low", "low", "average")) == 164,
          sum(d$turnover %in% c("very low", "low")) == 93,
          sum(d$risk == "high" & d$sales_charge == "Yes") == 35,
          near(cor(d$expense_ratio_pct, d$return_5yr_pct), 0.1416481),
          near(tapply(d$return_5yr_pct, d$objective, mean), c(10.1487341772, 11.6940594059)),
          near(cor(subset(d, objective == "Growth")$expense_ratio_pct,
                   subset(d, objective == "Growth")$return_5yr_pct), 0.1069140671),
          near(cor(subset(d, objective == "Value")$expense_ratio_pct,
                   subset(d, objective == "Value")$return_5yr_pct), 0.2445624229),
          nrow(c) == 33, !anyNA(c), near(mean(c$cost_per_ounce), 0.1706060606),
          near(sd(c$cost_per_ounce), 0.0469001195), near(IQR(c$cost_per_ounce), 0.07),
          nrow(subset(c, cost_per_ounce <= .15)) == 14,
          near(IQR(subset(c, cost_per_ounce <= .15)$cost_per_ounce), .035))
''', ROOT)
    print(f'{checks} R execution checks passed; dataset hashes, source cells and key teaching results agree.')
