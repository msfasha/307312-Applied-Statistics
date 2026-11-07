#!/usr/bin/env python3
"""Print the rendered HTML lessons and package only active student resources."""
from pathlib import Path
import shutil, subprocess, tempfile, zipfile, re
from urllib.parse import urljoin, urlsplit
from html import unescape, escape
ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/'_build/website'
from course_documents import LESSONS as PARTS, PRACTICALS, EXTENDED, DOCUMENTS
chrome=shutil.which('google-chrome') or shutil.which('chromium')
if not chrome: raise RuntimeError('Google Chrome or Chromium is required to export the lesson PDFs.')
(SITE/'pdf').mkdir(exist_ok=True)
for folder, part in DOCUMENTS:
    output=SITE/'pdf'/(part+'.pdf')
    page = SITE/folder/(part+'.html')
    public_page = 'https://msfasha.github.io/307312-Applied-Statistics/'+folder+'/'+part+'.html'
    def public_link(match):
        href = unescape(match[2])
        if href.startswith('#') or urlsplit(href).scheme or href.startswith('//'):
            return match[0]
        return match[1]+escape(urljoin(public_page, href), quote=True)+match[3]
    # Keep local CSS/images for printing, but make PDF navigation work for students.
    printable = re.sub(r'(<a\b[^>]*\bhref=")([^"]*)(")', public_link, page.read_text())
    with tempfile.NamedTemporaryFile(mode='w', suffix='.html', dir=page.parent,
                                     prefix='.print-', delete=False) as stream:
        stream.write(printable)
        print_page = Path(stream.name)
    try:
        with tempfile.TemporaryDirectory(prefix='307312-print-') as profile:
            subprocess.run([chrome,'--headless','--no-sandbox','--disable-dev-shm-usage',
                '--disable-gpu','--no-pdf-header-footer','--allow-file-access-from-files',
                '--run-all-compositor-stages-before-draw','--virtual-time-budget=5000',
                '--user-data-dir='+profile,'--print-to-pdf='+str(output),
                print_page.as_uri()],check=True,capture_output=True,timeout=180)
    finally:
        print_page.unlink(missing_ok=True)
    # Keep downloads compact; text remains vector, screenshots use 180 dpi.
    if shutil.which('gs'):
        compact=output.with_suffix('.compact.pdf')
        subprocess.run(['gs','-sDEVICE=pdfwrite','-dCompatibilityLevel=1.7',
            '-dNOPAUSE','-dBATCH','-dQUIET','-dDetectDuplicateImages=true',
            '-dCompressFonts=true','-dDownsampleColorImages=true',
            '-dColorImageResolution=180','-dDownsampleGrayImages=true',
            '-dGrayImageResolution=180','-dAutoRotatePages=/None',
            '-sOutputFile='+str(compact),str(output)],check=True,capture_output=True,timeout=180)
        compact.replace(output)
    # Chrome can append an empty page from trailing layout space. Remove it only
    # when both text extraction and Ghostscript ink coverage establish emptiness.
    if all(shutil.which(t) for t in ['gs', 'pdfinfo', 'pdftotext']):
        while True:
            info = subprocess.check_output(['pdfinfo', str(output)], text=True)
            pages = int(next(line.split(':', 1)[1] for line in info.splitlines() if line.startswith('Pages:')))
            if pages <= 1:
                break
            text = subprocess.check_output(['pdftotext', '-f', str(pages), '-l', str(pages), str(output), '-'], text=True)
            coverage = subprocess.check_output(['gs', '-q', '-dNOPAUSE', '-dBATCH', '-sDEVICE=inkcov',
                '-o', '-', '-dFirstPage='+str(pages), '-dLastPage='+str(pages), str(output)], text=True)
            lines = [line.split() for line in coverage.splitlines() if 'CMYK' in line]
            blank = not text.strip() and len(lines) == 1 and all(float(v) == 0 for v in lines[0][:4])
            if not blank:
                break
            trimmed = output.with_suffix('.trimmed.pdf')
            subprocess.run(['gs', '-q', '-dNOPAUSE', '-dBATCH', '-sDEVICE=pdfwrite',
                '-dFirstPage=1', '-dLastPage='+str(pages-1), '-sOutputFile='+str(trimmed), str(output)], check=True)
            trimmed.replace(output)
    if not output.exists() or output.stat().st_size<10000 or output.read_bytes()[:5]!=b'%PDF-':
        raise RuntimeError('PDF export failed: '+part)
    print('Created',output.name,flush=True)
(SITE/'downloads').mkdir(exist_ok=True)
with zipfile.ZipFile(SITE/'downloads/applied-statistics-pdfs.zip','w',zipfile.ZIP_DEFLATED) as z:
    for _, part in DOCUMENTS:z.write(SITE/'pdf'/(part+'.pdf'),part+'.pdf')
with zipfile.ZipFile(SITE/'downloads/applied-statistics-rstudio.zip','w',zipfile.ZIP_DEFLATED) as z:
    # No instructor files, archives, original slides, books, or build caches.
    names=['assets/petra-theme.md','assets/practical-print.css','assets/petra-brand.css','assets/source-slides.css','Applied-Statistics.Rproj','_quarto.yml','index.qmd']+['lessons/'+p+'.qmd' for p in PARTS]+['practicals/'+p+'.qmd' for p in PRACTICALS]+['practicals/_quarto.yml','practicals/practical-01-cereals.qmd','practicals/_includes/petra-plots.R','lessons/_includes/course-tools.R','scripts/finalize-preview.py','scripts/finalize-practical-preview.py','scripts/preview-practicals.py']
    names += ['extended-cases/'+p+'.qmd' for p in EXTENDED]
    for folder in ['data/business', 'data/descriptive-statistics', 'data/inferential-statistics',
                   'assets/descriptive-statistics', 'assets/inferential-statistics', 'lessons/_includes']:
        names.extend(str(p.relative_to(ROOT)) for p in (ROOT/folder).rglob('*') if p.is_file() and p.suffix.lower() in ['.png','.jpg','.jpeg','.svg','.css','.qmd','.csv','.json','.md','.R'])
    # Resources must be restricted to the same explicit teaching files as the site.
    import re
    allowed=set(re.findall(r'^    - (data/[^\n]+)',(ROOT/'_quarto.yml').read_text(),re.M))
    names=[n for n in names if not n.startswith('data/') or n in allowed]
    for name in sorted(set(names)):
        if name.endswith('.qmd'):
            text=(ROOT/name).read_text()
            text=text.replace('](../pdf/','](https://msfasha.github.io/307312-Applied-Statistics/pdf/')
            text=text.replace('](../downloads/','](https://msfasha.github.io/307312-Applied-Statistics/downloads/')
            text=text.replace('](pdf/','](https://msfasha.github.io/307312-Applied-Statistics/pdf/')
            text=text.replace('](downloads/','](https://msfasha.github.io/307312-Applied-Statistics/downloads/')
            z.writestr(name,text)
        else:z.write(ROOT/name,name)
    # The packaged project stages practicals after a website render, just like the publisher.
    z.write(ROOT/'scripts/stage-practicals.py', 'scripts/stage-practicals.py')
    z.writestr('README.md','''# 307312 Applied Statistics - student project

1. Install R, RStudio, and Quarto.
2. Extract this whole ZIP to a folder and open Applied-Statistics.Rproj.
3. Run this once in the R console:
   install.packages(c("knitr", "rmarkdown", "dplyr", "ggplot2"))
4. Open lessons/01-introduction-to-r.qmd, then Parts 2 and 3. Run code chunks in order.
5. Open practicals/practical-01-categorical-business-data.qmd, then Practicals 2 and 3.
6. Choose Render to view a notebook. Run `quarto render practicals` for practicals.
7. Run `quarto render` to build the lesson website.
8. Choose optional activities in extended-cases/. Each case lists prerequisites.
   Run `quarto render extended-cases/case-02-oxford-cereal.qmd` for one case.

Parts 2 and 3 preserve the original slide-based lessons, including Excel instructions
and labeled R examples. Their original teaching CSVs and diagrams are included.
The separate R practicals use Superstore (US, 2023–2025).
The extended cases add historical ninth-edition business cases and summary inputs.
All twelve notebooks are included; choose the extended cases assigned by your instructor.
See data/business/README.md for provenance, units and limitations.
The six extended cases provide separate business applications of course concepts.
Python 3 is needed for the small HTML post-render step.
PDF and ZIP download links point to the published website; local rendering creates HTML.
Keep the complete folder structure. Import cells locate the shared data/ folder
from either the course root or the notebook folder. All teaching data is CSV.
Website: https://msfasha.github.io/307312-Applied-Statistics/
''')
print('Created student RStudio project and PDF bundle.',flush=True)
