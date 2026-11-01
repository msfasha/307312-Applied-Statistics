#!/usr/bin/env python3
"""Keep Quarto lightbox targets embedded, just like their image elements."""
from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
for page in [root/'_preview/01-introduction-to-r.html', root/'_preview/02-descriptive-statistics.html', root/'_preview/03-inferential-statistics.html']:
    if not page.exists(): continue
    content=page.read_text()
    pattern=re.compile(r'(<a\b[^>]*\bhref=")([^"]+)("[^>]*class="[^"]*lightbox[^>]*>\s*<img\b[^>]*\bsrc=")(data:image/[^\"]+)(")')
    content=pattern.sub(lambda m:m[1]+m[4]+m[3]+m[4]+m[5],content)
    content=re.sub(r'<a\b[^>]*class="[^"]*lightbox[^>]*>',
                   lambda m: m[0] if 'data-type=' in m[0] else m[0][:-1]+' data-type="image">', content)
    page.write_text(content)
