#!/usr/bin/env python3
"""Verify all twelve business notebooks, pinned data and isolated interactive imports."""
import csv
import hashlib
import json
import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
from course_documents import EXTENDED
NOTEBOOKS = sorted((ROOT/'lessons').glob('*.qmd')) + [ROOT/'practicals'/name for name in [
    'practical-01-categorical-business-data.qmd', 'practical-02-numerical-business-data.qmd',
    'practical-03-association-and-groups.qmd']]
NOTEBOOKS += [ROOT/'extended-cases'/(name+'.qmd') for name in EXTENDED]

def run_r(code, cwd, warnings_as_errors=True):
    code = 'pdf(file = tempfile(fileext = ".pdf"))\noptions(warn = '+str(2 if warnings_as_errors else 1)+')\n' + code + '\ndev.off()\n'
    with tempfile.NamedTemporaryFile(mode='w', suffix='.R') as stream:
        stream.write(code)
        stream.flush()
        result = subprocess.run(['Rscript', '--vanilla', stream.name], cwd=cwd,
                                text=True, capture_output=True)
    if result.returncode:
        raise RuntimeError(result.stdout + result.stderr)

def verify_data():
    datasets = {}
    for name in ['business-data-provenance.json', 'extended-cases-provenance.json']:
        datasets.update(json.loads((ROOT/'instructor'/name).read_text())['datasets'])
    for stem, entry in datasets.items():
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
        assert imports and worked, notebook.name
        for cwd in [ROOT, notebook.parent]:
            for import_cell in imports:
                run_r(import_cell, cwd)
            # Preserve original MASS optimization examples, whose intermediate
            # parameter trials can warn even when the final fit succeeds.
            run_r('\n'.join(worked), cwd,
                  warnings_as_errors=not notebook.name.startswith('03-inferential'))
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
    extension_sources = ROOT/'books/2-Basic business statistics  concepts and applications/BusStats Excel'
    if extension_sources.exists():
        run_r('''
library(readxl)
p <- 'books/2-Basic business statistics  concepts and applications/BusStats Excel/'
get <- function(n) read.csv(file.path('data/business',paste0('extended-',n,'.csv')))
z <- read_excel(paste0(p,'SH2.XLS')); stopifnot(all(as.matrix(z[1:2]) == as.matrix(get('herald-calls'))))
z <- read_excel(paste0(p,'SH13.xls')); stopifnot(all(as.matrix(z) == as.matrix(get('herald-marketing'))))
z <- read_excel(paste0(p,'SH16.xls')); stopifnot(all(as.matrix(z) == as.matrix(get('herald-subscriptions'))))
z <- read_excel(paste0(p,'potato.xls')); stopifnot(all(as.matrix(z) == as.matrix(get('potato'))))
z <- read_excel(paste0(p,'HARNSWELL.xls')); stopifnot(all(as.matrix(z) == as.matrix(get('harnswell'))))
z <- suppressMessages(read_excel(paste0(p,'Parachute.xls')))
v <- get('parachute')
for (j in 1:4) stopifnot(all(v$strength[v$supplier == paste('Supplier',j)] == z[[j]][1:5]))
''', ROOT)
    run_r((ROOT/'instructor/extended-cases-answer-key.R').read_text(), ROOT)
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
