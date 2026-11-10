#!/usr/bin/env python3
"""Render only the source-mapped probability draft; never publish it."""
from pathlib import Path
import shutil, subprocess, tempfile, zipfile, re, json
ROOT=Path(__file__).resolve().parents[1]
BUILD=ROOT/'_build/inferential-probability-draft'
PROJECT=BUILD/'project'
OUT=BUILD/'preview'
NAME='inferential-31-probability-distributions-draft'
QUARTO=shutil.which('quarto') or '/usr/lib/rstudio/resources/app/bin/quarto/bin/quarto'
ASSETS=['petra-brand.css','source-slides.css','inferential-draft.css',
    'inferential-illustrations/mass-and-density.svg',
    'inferential-illustrations/r-distribution-functions.svg',
    'inferential-statistics/part-01-slide-03-graphic-02.png',
    'inferential-statistics/part-01-slide-08-graphic-01.png',
    'inferential-statistics/part-01-slide-09-graphic-03.png']

def check_cells():
    source=(ROOT/'lessons'/f'{NAME}.qmd').read_text()
    slides=re.findall(r'\.teaching-slide #pd-(\d+)',source)
    assert slides==[f'{i:02}' for i in range(1,24)],slides
    cells=re.findall(r'```\{r\}\n(.*?)\n```',source,re.S)
    assert len(set(re.findall(r'#\| label: (.+)',source)))==len(cells)
    with tempfile.TemporaryDirectory(prefix='probability-draft-check-') as tmp:
        p=Path(tmp)
        for i,c in enumerate(cells):(p/f'{i:02}.R').write_text(c)
        code='''pdf(OUTPUT)
files <- list.files(FOLDER,pattern="[.]R$",full.names=TRUE)
for(f in files) {
 capture.output(sys.source(f,envir=new.env(parent=globalenv())))
 cat("PASS",basename(f),"\\n")
}
stopifnot(abs(dbinom(2,80,.02)-.261445383698146)<1e-8)
stopifnot(abs(pbinom(1,80,.02)-.522973503277209)<1e-8)
stopifnot(abs(ppois(2,3,lower.tail=FALSE)-.5768099189)<1e-8)
stopifnot(abs(pnorm(75,70,6,lower.tail=FALSE)-.2023283810)<1e-8)
stopifnot(abs(punif(10.1,9.8,10.2,lower.tail=FALSE)-.25)<1e-10)
stopifnot(abs((pnorm(76,70,6)-pnorm(64,70,6))-.6826894921)<1e-8)
# Independent task answers are checked here; not included in the student bundle.
stopifnot(abs((1-pbinom(1,80,.02))-.477026496722791)<1e-8)
stopifnot(abs(dpois(0,3)-.0497870684)<1e-8)
dev.off()
'''.replace('FOLDER',json.dumps(str(p))).replace('OUTPUT',json.dumps(str(p/'plots.pdf')))
        script=p/'check.r';script.write_text(code)
        result=subprocess.run(['Rscript','--vanilla',str(script)],cwd=ROOT,capture_output=True,text=True)
        (BUILD/'r-checks.log').write_text(result.stdout+result.stderr)
        if result.returncode:raise RuntimeError(result.stderr)
    return {'teaching_slides':23,'independently_executed_R_cells':len(cells),'numerical_checks':'passed'}

def main():
    (PROJECT/'lessons').mkdir(parents=True,exist_ok=True)
    (PROJECT/'assets').mkdir(exist_ok=True)
    OUT.mkdir(parents=True,exist_ok=True)
    result=check_cells()
    shutil.copy2(ROOT/'lessons'/f'{NAME}.qmd',PROJECT/'lessons'/f'{NAME}.qmd')
    for name in ASSETS:
        (PROJECT/'assets'/name).parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(ROOT/'assets'/name,PROJECT/'assets'/name)
    config=f'''project:
  type: default
  output-dir: ../preview
  execute-dir: project
  render:
    - lessons/{NAME}.qmd
'''
    (PROJECT/'_quarto.yml').write_text(config)
    subprocess.run([QUARTO,'render'],cwd=PROJECT,check=True)
    html=OUT/'probability-distributions-draft.html'
    shutil.copy2(OUT/'lessons'/f'{NAME}.html',html)
    pdf=OUT/'probability-distributions-draft.pdf'
    chrome=shutil.which('google-chrome') or shutil.which('chromium')
    if not chrome:raise RuntimeError('Chrome/Chromium is needed for PDF export.')
    with tempfile.TemporaryDirectory(prefix='probability-draft-print-') as tmp:
        subprocess.run([chrome,'--headless','--no-sandbox','--disable-dev-shm-usage',
            '--disable-gpu','--no-pdf-header-footer','--allow-file-access-from-files',
            '--virtual-time-budget=4000','--user-data-dir='+tmp,
            '--print-to-pdf='+str(pdf),html.as_uri()],check=True,capture_output=True,timeout=180)
    (PROJECT/'Probability-Draft.Rproj').write_text('Version: 1.0\nRestoreWorkspace: No\nSaveWorkspace: No\nEncoding: UTF-8\nRMarkdownRoot: Project\n')
    (PROJECT/'README.md').write_text('''# 3.1 Probability Distributions — proposed teaching draft

Open probability-distributions-draft.html or the PDF to review the section.
This preview is built independently for review. The preview builder does not publish or replace the original core slides.

The 23 teaching slides implement units P1–P9 of the agreed source map.
The probability inputs are stipulated models; this section needs no external CSV.
Observed datasets enter the later estimation/testing/regression sections.

To edit: open Probability-Draft.Rproj in RStudio, then the notebook under lessons/.
Install knitr and rmarkdown if needed. R examples use base R and knitr tables.
Keep assets/ beside lessons/. Run quarto render to rebuild the HTML.
The PDF is a snapshot printed from executed HTML; print the new HTML to refresh it.
Instructor answers and validation logs are intentionally not included.
''')
    bundle=OUT/'probability-distributions-draft.zip'
    with zipfile.ZipFile(bundle,'w',zipfile.ZIP_DEFLATED) as z:
        z.write(PROJECT/'lessons'/f'{NAME}.qmd',f'lessons/{NAME}.qmd')
        for name in ASSETS:z.write(PROJECT/'assets'/name,'assets/'+name)
        z.writestr('_quarto.yml',config.replace('../preview','preview'))
        for name in ['README.md','Probability-Draft.Rproj']:z.write(PROJECT/name,name)
        z.write(html,html.name);z.write(pdf,pdf.name)
    (BUILD/'validation.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    print('HTML:',html);print('PDF:',pdf);print('Editable package:',bundle)
if __name__=='__main__':main()
