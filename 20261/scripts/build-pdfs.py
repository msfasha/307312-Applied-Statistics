#!/usr/bin/env python3
"""Build all student PDFs, or selected project-relative QMDs, in one command."""
from pathlib import Path
import argparse
import importlib.util
import shutil
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
QUARTO = shutil.which("quarto") or "/usr/lib/rstudio/resources/app/bin/quarto/bin/quarto"


def package_outputs(output):
    """Keep download links usable and provide a clean, portable student bundle."""
    shutil.copytree(ROOT / "data", output / "data", dirs_exist_ok=True)
    (output / "README.txt").write_text(
        "Applied Statistics - student PDF edition\n\n"
        "Extract the entire ZIP, then open index.pdf in a desktop PDF reader.\n"
        "Keep the folders together so lesson and dataset links work.\n"
        "Modules marked Planned contain an overview only. Instructor answers are excluded.\n",
        encoding="utf-8",
    )
    bundle = output.parent / "applied-statistics-student-pdfs.zip"
    with zipfile.ZipFile(bundle, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(output.rglob("*")):
            relative = path.relative_to(output)
            if not path.is_file() or relative.parts[0] in {"qa", "build-logs"}:
                continue
            if relative.parts[0] in {"modules", "resources"} and path.suffix != ".pdf":
                continue
            archive.write(path, relative)
    print(f"Student bundle: {bundle}")


def prepare_diagrams():
    # Preserve the original SVGs; LaTeX reads equivalent vector PDF copies.
    python = sys.executable
    if importlib.util.find_spec("cairosvg") is None:
        bundled = Path.home() / ".cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3"
        python = str(bundled) if bundled.exists() else python
    converter = """
from pathlib import Path
import cairosvg
from PIL import Image
assets = Path('assets')
for source in assets.rglob('*.svg'):
    if 'pdf' in source.relative_to(assets).parts:
        continue
    target = assets / 'pdf/svg' / source.relative_to(assets).with_suffix('.pdf')
    target.parent.mkdir(parents=True, exist_ok=True)
    if not target.exists() or source.stat().st_mtime > target.stat().st_mtime:
        cairosvg.svg2pdf(url=str(source), write_to=str(target))
for source in assets.rglob('*.gif'):
    if 'pdf' in source.relative_to(assets).parts:
        continue
    target = assets / 'pdf/svg' / source.relative_to(assets).with_suffix('.png')
    target.parent.mkdir(parents=True, exist_ok=True)
    if not target.exists() or source.stat().st_mtime > target.stat().st_mtime:
        with Image.open(source) as image:
            image.seek(image.n_frames - 1)
            image.convert('RGB').save(target)
"""
    result = subprocess.run([python, "-c", converter], cwd=ROOT)
    if result.returncode:
        raise SystemExit("Diagram conversion needs CairoSVG: install it with python3 -m pip install cairosvg.")


def main():
    if not Path(QUARTO).exists():
        raise SystemExit("Install Quarto first, then run this command again.")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sources", nargs="*", type=Path, help="Optional project-relative lesson paths; default: all student pages")
    sources = parser.parse_args().sources
    if not sources:
        sources = [Path("index.qmd")]
        sources += sorted(p.relative_to(ROOT) for p in (ROOT / "modules").rglob("*.qmd"))
        sources += sorted(p.relative_to(ROOT) for p in (ROOT / "resources").rglob("*.qmd"))
        sources += sorted(p.relative_to(ROOT) for p in (ROOT / "resources").rglob("*.Rmd"))
    for source in sources:
        absolute = (ROOT / source).resolve()
        if not absolute.is_relative_to(ROOT) or not absolute.is_file() or source.suffix not in {".qmd", ".Rmd"}:
            raise SystemExit(f"Not a course source: {source}")
    prepare_diagrams()
    output = ROOT / "_output/pdf"
    output.mkdir(parents=True, exist_ok=True)
    for number, source in enumerate(sources, 1):
        print(f"[{number}/{len(sources)}] {source}", flush=True)
        log = output / "build-logs" / source.with_suffix(".log")
        log.parent.mkdir(parents=True, exist_ok=True)
        with log.open("w") as stream:
            result = subprocess.run(
                [QUARTO, "render", str(source), "--to", "pdf", "--profile", "pdf"],
                cwd=ROOT, stdout=stream, stderr=subprocess.STDOUT,
            )
        if result.returncode:
            print(log.read_text()[-4500:], file=sys.stderr)
            raise SystemExit(f"PDF build stopped at {source}. Details: {log}")
        if not (output / source.with_suffix(".pdf")).is_file():
            raise SystemExit(f"Expected PDF was not produced for {source}.")
    print(f"Built {len(sources)} PDFs in {output}")
    package_outputs(output)


if __name__ == "__main__":
    main()
