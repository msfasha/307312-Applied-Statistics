#!/usr/bin/env python3
"""Verify all six business notebooks, pinned data and isolated interactive imports."""
import csv
import hashlib
import json
import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = sorted((ROOT/'lessons').glob('*.qmd')) + [ROOT/'practicals'/name for name in [
    'practical-01-categorical-business-data.qmd', 'practical-02-numerical-business-data.qmd',
    'practical-03-association-and-groups.qmd']]

def run_r(code, cwd):
    code = 'pdf(file = tempfile(fileext = ".pdf"))\noptions(warn = 2)\n' + code + '\ndev.off()\n'
    with tempfile.NamedTemporaryFile(mode='w', suffix='.R') as stream:
        stream.write(code)
        stream.flush()
        result = subprocess.run(['Rscript', '--vanilla', stream.name], cwd=cwd,
                                text=True, capture_output=True)
    if result.returncode:
        raise RuntimeError(result.stdout + result.stderr)

def verify_data():
    manifest = json.loads((ROOT/'instructor/business-data-provenance.json').read_text())
    for stem, entry in manifest['datasets'].items():
        path = ROOT/entry['output_file']
        assert hashlib.sha256(path.read_bytes()).hexdigest() == entry['output_sha256'], stem
        with path.open(newline='') as stream:
            rows = list(csv.DictReader(stream))
        assert len(rows) == entry['rows'] and list(rows[0]) == entry['columns']
        assert all(all(v != '' for v in r.values()) for r in rows), stem
        source = ROOT/entry['source_file']
        if source.exists():
            assert hashlib.sha256(source.read_bytes()).hexdigest() == entry['source_sha256'], stem

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
        print('Passed isolated import and worked cells from both locations:', notebook.name, flush=True)
    run_r('''
source('lessons/_includes/course-tools.R')
x <- read.csv('data/business/superstore-lines.csv', colClasses = c(postal_code = 'character'))
o <- make_orders(x)
c <- read.csv('data/business/cola.csv')
u <- read.csv('data/business/consumer.csv')
stopifnot(nrow(x) == 6682, nrow(o) == 3322, n_distinct(o$customer_id) == 782,
          !anyNA(x), !anyDuplicated(x$row_id), all(x$country == 'United States'),
          all(as.Date(x$order_date) >= as.Date('2023-01-01')),
          all(as.Date(x$order_date) <= as.Date('2025-12-31')),
          sum(x$profit < 0) == 1251, sum(o$loss_order) == 671, sum(o$listed_return) == 191,
          isTRUE(all.equal(sum(x$sales), sum(o$sales))),
          isTRUE(all.equal(sum(x$profit), sum(o$profit))),
          abs(mean(o$sales) - 470.796354003612) < .01,
          abs(median(o$sales) - 153.982) < .0001,
          nrow(c) == 20, nrow(u) == 50)
end <- c$weekly_cases[c$display == 'End aisle']
normal <- c$weekly_cases[c$display == 'Normal']
t <- t.test(end, normal)
stopifnot(abs(mean(end) - mean(normal) - 21.7) < 1e-10,
          abs(t$p.value - .007848949) < 1e-6,
          all(abs(t$conf.int - c(6.568701,36.831299)) < 1e-5))
m <- lm(card_charges ~ income_thousands + household_size, data = u)
stopifnot(all(abs(coef(m) - c(1304.9048,33.1330,356.2962)) < .01),
          abs(summary(m)$adj.r.squared - .8181) < .0001)
''', ROOT)
    # Full numerical source-cell checks, when maintainer source workbooks are present.
    if (ROOT/'books/tableau/sample_-_superstore.xls').exists():
        run_r('''
library(readxl)
d <- as.data.frame(read_excel('books/tableau/sample_-_superstore.xls', sheet = 'Orders'))
x <- read.csv('data/business/superstore-lines.csv', colClasses = c(postal_code = 'character'))
d <- d[d[['Country/Region']] == 'United States' & as.Date(d[['Order Date']]) >= as.Date('2023-01-01') &
       as.Date(d[['Order Date']]) < as.Date('2026-01-01'), ]
d[['Order Date']] <- as.character(as.Date(d[['Order Date']]))
d[['Ship Date']] <- as.character(as.Date(d[['Ship Date']]))
stopifnot(nrow(d) == nrow(x))
for (j in seq_len(21)) stopifnot(isTRUE(all.equal(as.character(d[[j]]), as.character(x[[j]]))))
r <- read_excel('books/tableau/sample_-_superstore.xls', sheet = 'Returns')
stopifnot(all((x$return_status == 'Listed return') == (x$order_id %in% r[['Order ID']])))
p <- 'books/2-Basic business statistics  concepts and applications/Data-9th e/browse/Data_Files/Excel/COLA.XLS'
z <- read_excel(p, sheet = 'Data'); c <- read.csv('data/business/cola.csv')
stopifnot(all(c$weekly_cases == c(z$Normal,z$EndAisle)))
p <- 'books/1-Modern Business Statistics-Organized-Data/7th-Data - Modern Business Statistics with Microsoft Excel Anderson Sweeney Williams/Chapter 15 Multiple Regression/Consumer.xls'
z <- read_excel(p); u <- read.csv('data/business/consumer.csv')
stopifnot(all(as.matrix(z) == as.matrix(u)))
''', ROOT)
    print(f'{checks} fresh-session execution checks passed; source cells, hashes and key results verified.')
