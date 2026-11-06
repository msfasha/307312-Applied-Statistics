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
