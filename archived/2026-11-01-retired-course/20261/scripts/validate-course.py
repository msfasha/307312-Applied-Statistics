"""Check local file targets in the freshly rendered student site."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote

site = Path(__file__).resolve().parents[1] / "_site"

class Targets(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in {"href", "src"} and value:
                u = urlparse(value)
                if not u.scheme and not u.netloc and u.path:
                    self.links.append(unquote(u.path))

missing = []
pages = [p for p in site.rglob("*.html")
         if not any(part == "site_libs" or part.endswith("_files") for part in p.relative_to(site).parts)]
for page in pages:
    parser = Targets()
    parser.feed(page.read_text())
    for link in parser.links:
        target = site / link.lstrip("/") if link.startswith("/") else page.parent / link
        if not target.exists():
            missing.append(f"{page.relative_to(site)} -> {link}")
if missing:
    raise SystemExit("Broken local targets:\n" + "\n".join(sorted(set(missing))))
print(f"Checked local file links in {len(pages)} course pages.")
