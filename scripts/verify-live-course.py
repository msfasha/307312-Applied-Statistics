#!/usr/bin/env python3
"""Verify the deployed source revision and every approved student download."""
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError
import hashlib
import json
import re
import subprocess
import time

from course_documents import DOCUMENTS

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT/'_build/website'
BASE = 'https://msfasha.github.io/307312-Applied-Statistics/'

def fetch(name, revision):
    request = Request(BASE+name+'?release='+revision, headers={'Cache-Control': 'no-cache'})
    with urlopen(request, timeout=45) as response:
        assert response.status == 200, (name, response.status)
        return response.read()

if __name__ == '__main__':
    revision = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
    # GitHub Pages deployment is asynchronous; wait for this source revision.
    for attempt in range(40):
        try:
            deployed = json.loads(fetch('deployment.json', revision))
            if deployed['source_commit'] == revision:
                break
        except (URLError, json.JSONDecodeError, AssertionError):
            pass
        if attempt == 39:
            raise RuntimeError('Live deployment did not reach source revision '+revision)
        if attempt % 4 == 0:
            print('Waiting for GitHub Pages deployment of', revision[:8], flush=True)
        time.sleep(15)
    names = ['index.html'] + [folder+'/'+name+'.html' for folder, name in DOCUMENTS]
    names += ['pdf/'+name+'.pdf' for _, name in DOCUMENTS]
    names += ['downloads/applied-statistics-rstudio.zip', 'downloads/applied-statistics-pdfs.zip']
    names += re.findall(r'^    - (data/[^\n]+)', (ROOT/'_quarto.yml').read_text(), re.M)
    verified = []
    for name in names:
        data = fetch(name, revision)
        # Compare actual deployed bytes, including both ZIPs and every PDF/CSV.
        expected = (SITE/name).read_bytes()
        assert hashlib.sha256(data).digest() == hashlib.sha256(expected).digest(), (name, 'live content mismatch')
        if name.endswith('.pdf'):
            assert data.startswith(b'%PDF-'), name
        if name.endswith('.zip'):
            assert data.startswith(b'PK'), name
        verified.append({'path': name, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()})
        print('Verified live:', name, flush=True)
    report = {'source_commit': revision, 'deployment': deployed, 'verified': verified}
    output = ROOT/'_build/extended-review/live-verification.json'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2)+'\n')
    print('Verified live revision, 12 notebook pages, 12 PDFs, both ZIPs and all approved data.', flush=True)
