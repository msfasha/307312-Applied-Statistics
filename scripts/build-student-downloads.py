#!/usr/bin/env python3
"""Print the rendered HTML lessons and package only active student resources."""
from pathlib import Path
import shutil, subprocess, tempfile, zipfile, re
from urllib.parse import urljoin, urlsplit
from html import unescape, escape
ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/'_build/website'
from course_documents import LESSONS as PARTS, PRACTICALS, EXTENDED, SUPERSTORE, DOCUMENTS, NAVIGATION_PAGES
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
# Explicitly approved editable Part 3 practical, also included in the full project.
shutil.copy2(ROOT/'practicals/inferential-statistics-r-practical.qmd',
             SITE/'downloads/inferential-statistics-r-practical.qmd')
with zipfile.ZipFile(SITE/'downloads/applied-statistics-pdfs.zip','w',zipfile.ZIP_DEFLATED) as z:
    for _, part in DOCUMENTS:z.write(SITE/'pdf'/(part+'.pdf'),part+'.pdf')
from student_project import build_student_project
build_student_project(SITE/'downloads/applied-statistics-rstudio.zip')
print('Created student RStudio project and PDF bundle.',flush=True)
