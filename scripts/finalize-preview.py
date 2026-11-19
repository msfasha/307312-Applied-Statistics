#!/usr/bin/env python3
"""Keep Quarto lightbox targets embedded, just like their image elements."""
from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
for page in [root/'_build/website/lessons/01-introduction-to-r.html', root/'_build/website/lessons/02-descriptive-statistics.html', root/'_build/website/lessons/03-inferential-statistics.html']:
    if not page.exists(): continue
    content=page.read_text()
    pattern=re.compile(r'(<a\b[^>]*\bhref=")([^"]+)("[^>]*class="[^"]*lightbox[^>]*>\s*<img\b[^>]*\bsrc=")(data:image/[^\"]+)(")')
    content=pattern.sub(lambda m:m[1]+m[4]+m[3]+m[4]+m[5],content)
    content=re.sub(r'<a\b[^>]*class="[^"]*lightbox[^>]*>',
                   lambda m: m[0] if 'data-type=' in m[0] else m[0][:-1]+' data-type="image">', content)
    page.write_text(content)

# Preserve bookmarks after moving editable lessons into lessons/.
for name in ['01-introduction-to-r', '02-descriptive-statistics', '03-inferential-statistics']:
    target = f"lessons/{name}.html"
    (root / '_build/website' / f"{name}.html").write_text(
        f'<!doctype html><html><head><meta charset="utf-8"><title>Course lesson</title>'
        f'<meta http-equiv="refresh" content="0; url={target}"></head>'
        f'<body><a href="{target}">Open lesson</a>'
        f'<script>location.replace("{target}" + location.search + location.hash)</script></body></html>')


# Retired Part 3 URLs forward to the one current notebook, without another lesson.
from course_documents import INFERENTIAL_REDIRECTS
import json
fragment_map = {
    'equally-likely-outcomes-logical-tests-and-proportions': 'part3-01-slide-15',
    'binomial-probabilities-exact-counts-and-cumulative-totals': 'part3-01-slide-16',
    'poisson-probabilities-arrivals-in-a-minute': 'part3-01-slide-18',
    'uniform-probabilities-delivery-times-and-diameters': 'part3-01-slide-22',
    'generate-a-simulated-dataset-the-four-r-function-families': 'part3-01-slide-31',
    'standardise-scores-compare-relative-positions': 'part3-01-slide-30',
    'normal-probabilities-thresholds-and-percentages': 'part3-01-slide-36',
}
for alias in INFERENTIAL_REDIRECTS:
    destination = '../lessons/03-inferential-statistics.html' if alias.startswith('practicals/') else '03-inferential-statistics.html'
    page = root/'_build/website'/(alias+'.html')
    page.parent.mkdir(parents=True,exist_ok=True)
    page.write_text('<!doctype html><html><head><meta charset="utf-8"><title>Inferential Statistics</title></head><body>'
        +f'<a href="{destination}">Open Inferential Statistics</a>'
        +'<script>const target='+json.dumps(destination)+';const fragments='+json.dumps(fragment_map)+';'
        +'const old=decodeURIComponent(location.hash.slice(1));'
        +'const anchor=fragments[old] || (old.startsWith("part3-") ? old : "");'
        +'location.replace(target+location.search+(anchor ? "#"+anchor : ""));</script></body></html>')
