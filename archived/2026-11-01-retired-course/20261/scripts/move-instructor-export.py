"""Move a standalone instructor export, preserving its relative link targets."""
from pathlib import Path
from urllib.parse import urlparse, unquote, quote
import html, os, re, sys
project = Path(__file__).resolve().parents[1]
source = Path(sys.argv[1]).resolve().with_suffix('.html')
out = project / '_instructor/_output' / source.name

def rebase(match):
    value = html.unescape(match[2]); parsed = urlparse(value)
    if parsed.scheme or parsed.netloc or not parsed.path:
        return match[0]
    target = (source.parent / unquote(parsed.path)).resolve()
    if target.is_relative_to(project / 'modules') or target.is_relative_to(project / 'resources'):
        target = project / '_site' / target.relative_to(project).with_suffix('.html')
    elif target.suffix == '.qmd':
        target = out.parent / target.with_suffix('.html').name
    relative = quote(os.path.relpath(target, out.parent), safe='/')
    if parsed.query: relative += '?' + parsed.query
    if parsed.fragment: relative += '#' + parsed.fragment
    return match[1] + html.escape(relative, quote=True) + match[3]
text = re.sub(r'((?:href|src)=")(.*?)(")', rebase, source.read_text())
out.write_text(text)
source.unlink()
