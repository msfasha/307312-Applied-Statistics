#!/usr/bin/env python3
"""Rebuild extension CSVs from unchanged local ninth-edition publisher workbooks."""
from pathlib import Path
import hashlib
import json
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BOOK = 'books/2-Basic business statistics  concepts and applications/'
SOURCE = BOOK + 'BusStats Excel/'
FILES = {
    'extended-herald-calls.csv': 'SH2.XLS',
    'extended-herald-marketing.csv': 'SH13.xls',
    'extended-herald-subscriptions.csv': 'SH16.xls',
    'extended-parachute.csv': 'Parachute.xls',
    'extended-potato.csv': 'potato.xls',
    'extended-harnswell.csv': 'HARNSWELL.xls',
}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

if __name__ == '__main__':
    subprocess.run(['Rscript', '--vanilla', '-e', r'''
library(readxl)
p <- "books/2-Basic business statistics  concepts and applications/BusStats Excel/"
out <- "data/business/"
save <- function(x, file) write.csv(x, paste0(out, file), row.names = FALSE, na = "")
d <- read_excel(paste0(p, "SH2.XLS"))
save(data.frame(day = d$Days, calls = d$Calls), "extended-herald-calls.csv")
d <- read_excel(paste0(p, "SH13.xls"))
save(data.frame(hours = d$Hours, new_subscriptions = d[["New Subscriptions"]]),
     "extended-herald-marketing.csv")
d <- read_excel(paste0(p, "SH16.xls"))
save(data.frame(month = d$Month, subscriptions = d$Subscriptions),
     "extended-herald-subscriptions.csv")
d <- suppressMessages(read_excel(paste0(p, "Parachute.xls")))
stopifnot(all(!is.na(as.matrix(d[1:5, 1:4]))), all(is.na(d[6, 1:4])))
save(data.frame(supplier = rep(paste("Supplier", 1:4), each = 5),
                strength = as.vector(as.matrix(d[1:5, 1:4]))), "extended-parachute.csv")
d <- read_excel(paste0(p, "potato.xls"))
names(d) <- c("solids", "ph", "lower_pressure", "upper_pressure", "cake_thickness",
              "varidriv_speed", "drum_speed")
save(d, "extended-potato.csv")
d <- read_excel(paste0(p, "HARNSWELL.xls"))
names(d) <- c("batch", "diameter")
save(d, "extended-harnswell.csv")
# Printed p. 302: reported inputs, not reconstructed raw observations.
save(data.frame(n = 25, sample_mean_g = 372.5, population_sd_g = 15,
                target_mean_g = 368, alpha = .05), "extended-oxford-summary.csv")
'''], cwd=ROOT, check=True)
    import csv
    manifest = {'reviewed': '2026-11-07', 'datasets': {}}
    for name, source in FILES.items():
        output = ROOT/'data/business'/name
        rows = list(csv.DictReader(output.open()))
        manifest['datasets'][name] = {
            'source_file': SOURCE + source, 'source_sha256': sha(ROOT/SOURCE/source),
            'output_file': str(output.relative_to(ROOT)), 'output_sha256': sha(output),
            'rows': len(rows), 'columns': list(rows[0]),
            'transformation': ('First five measurement rows only; suppliers stacked column-wise; '
                               'summary rows excluded.' if 'parachute' in name else
                               'Observation values preserved; headers standardized; SH2 chart helpers excluded.')}
    output = ROOT/'data/business/extended-oxford-summary.csv'
    source = ROOT/BOOK/'9th-Basic business statistics concepts and applications (Berenson, Mark L, Levine, David M. etc.).pdf'
    manifest['datasets'][output.name] = {
        'source_file': str(source.relative_to(ROOT)), 'source_sha256': sha(source),
        'source_page': 'Printed p. 302; PDF viewer p. 328',
        'output_file': str(output.relative_to(ROOT)), 'output_sha256': sha(output),
        'rows': 1, 'columns': list(next(csv.DictReader(output.open()))),
        'transformation': 'Transcribed summary inputs; no individual weights invented.'}
    (ROOT/'instructor/extended-cases-provenance.json').write_text(json.dumps(manifest, indent=2)+'\n')
    print('Prepared seven canonical extension CSVs and instructor provenance manifest.')
