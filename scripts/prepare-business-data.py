#!/usr/bin/env python3
"""Reproduce approved CSVs only from the pinned, unchanged source workbooks."""
from pathlib import Path
import hashlib
import json
import subprocess

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT/'instructor/business-data-provenance.json').read_text())
for name, record in manifest['datasets'].items():
    path = ROOT/record['source_file']
    if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest() != record['source_sha256']:
        raise RuntimeError(f'Pinned source absent or changed: {name}; review a new version before export.')
subprocess.run(['Rscript', str(ROOT/'scripts/prepare-business-data.R')], cwd=ROOT, check=True)
for name, record in manifest['datasets'].items():
    path = ROOT/record['output_file']
    if hashlib.sha256(path.read_bytes()).hexdigest() != record['output_sha256']:
        raise RuntimeError(f'Export differs from the approved CSV: {name}')
print('Pinned sources and reproduced CSV hashes agree.')
