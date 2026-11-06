#!/usr/bin/env python3
"""Export the historical publisher fund table without changing observations."""
import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'books/2-Basic business statistics  concepts and applications/BusStats Excel/FUNDS2002.txt'
OUTPUT = ROOT / 'data/practicals/funds2002.csv'
NAMES = ['fund', 'type', 'objective', 'assets_million_dollars', 'sales_charge',
         'expense_ratio_pct', 'return_2001_pct', 'return_3yr_pct', 'return_5yr_pct',
         'turnover', 'risk', 'best_quarter_pct', 'worst_quarter_pct']

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

if __name__ == '__main__':
    with SOURCE.open(newline='') as stream:
        rows = list(csv.reader(stream, delimiter='\t'))
    assert len(rows) == 260 and all(len(row) == 13 for row in rows)
    original_headers = rows[0]
    records = [row[:] for row in rows[1:]]
    trimmed = sum(row[1] != row[1].strip() for row in records)
    for row in records:
        row[1] = row[1].strip()
    assert len({row[0] for row in records}) == 259
    assert all(all(value.strip() for value in row) for row in records)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open('w', newline='') as stream:
        writer = csv.writer(stream, lineterminator='\n')
        writer.writerow(NAMES)
        writer.writerows(records)
    with OUTPUT.open(newline='') as stream:
        exported = list(csv.reader(stream))
    assert exported[1:] == records
    provenance = {
        'dataset': 'FUNDS2002', 'source_book': 'Basic Business Statistics: Concepts and Applications, ninth edition',
        'source_file': str(SOURCE.relative_to(ROOT)), 'source_sha256': sha(SOURCE),
        'output_file': str(OUTPUT.relative_to(ROOT)), 'output_sha256': sha(OUTPUT),
        'rows': 259, 'columns': 13, 'column_mapping': dict(zip(original_headers, NAMES)),
        'transformations': [f'Trimmed surrounding whitespace in Type in {trimmed} rows.',
                            'Renamed columns; preserved fund labels, source order and all numeric text values.'],
        'validation': 'Every exported cell compared with source text after the documented Type trim; no missing cells; unique fund labels.',
        'source_definitions': 'Printed pp. 40 and 75 (PDF viewer pp. 66 and 101); team projects pp. 130–131.',
        'provenance_limit': 'Publisher companion data verified; original collection method and probability sampling not established.',
        'reviewed_on': '2026-11-06'
    }
    OUTPUT.with_name('funds2002-provenance.json').write_text(json.dumps(provenance, indent=2) + '\n')
    print('Verified export:', OUTPUT, '259 records, 13 variables')
