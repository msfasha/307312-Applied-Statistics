"""Build a teaching-order student project independently of website source layout."""
from pathlib import Path
import posixpath
import re
import zipfile
import yaml
from urllib.parse import unquote
from course_documents import DOCUMENTS, STUDENT_PROJECT_ZIP

# Website/PDF documents remain unchanged; the Positron ZIP contains runnable work only.
RUNNABLE_DOCUMENTS = [(f, n) for f, n in DOCUMENTS
                     if f != "lessons" or n in {"01-introduction-to-r", "02-descriptive-statistics", "03-inferential-statistics"}]

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = 'https://msfasha.github.io/307312-Applied-Statistics/'

def student_path(name):
    if name.startswith('lessons/_includes/'):
        return name.replace('lessons/_includes/', 'support/', 1)
    if name.startswith('lessons/'):
        part = 'part-1-introduction-to-r' if Path(name).stem in ['01-introduction-to-r'] else ('part-2-descriptive-statistics' if Path(name).stem == '02-descriptive-statistics' else 'part-3-inferential-statistics')
        return part+'/'+Path(name).name
    return name

def project_files():
    names = {f'{folder}/{n}.qmd' for folder,n in RUNNABLE_DOCUMENTS}
    names.update(['.vscode/settings.json', 'lessons/_includes/course-tools.R'])
    for folder, notebook in RUNNABLE_DOCUMENTS:
        text = (ROOT/folder/(notebook+'.qmd')).read_text()
        for target in re.findall(r'(?:src="|!\[[^\]]*\]\()([^"\)]+)', text):
            path = posixpath.normpath(posixpath.join(folder, unquote(target)))
            if path.startswith('assets/') and (ROOT/path).is_file():
                names.add(path)
        for data in re.findall(r'data/[\w/-]+\.csv', text):
            names.add(data)
            guide = str(Path(data).parent/'README.md')
            if (ROOT/guide).exists():
                names.add(guide)
    # The combined Part 2 needs its editable diagrams and survey supplement.
    pending = [n for n in names if n.endswith('.qmd')]
    seen = set()
    while pending:
        source = pending.pop()
        if source in seen:
            continue
        seen.add(source)
        text = (ROOT/source).read_text()
        for target in re.findall(r'{{< include ([^\s]+)', text):
            included = posixpath.normpath(posixpath.join(posixpath.dirname(source), target))
            if not included.startswith('lessons/_includes/') or not (ROOT/included).is_file():
                raise RuntimeError('Unexpected student include: '+included)
            names.add(included)
            pending.append(included)
    names.update('assets/'+n for n in ['petra-theme.md', 'petra-brand.css', 'source-slides.css', 'practical-print.css'])

    return names

def rewrite(name, text, names):
    def relative(target, include=False):
        base, sep, fragment = target.partition('#')
        resolved = posixpath.normpath(posixpath.join(posixpath.dirname(name), base))
        if resolved.startswith(('pdf/', 'downloads/')):
            return PUBLIC+resolved+(sep+fragment if sep else '')
        source = resolved[:-5]+'.qmd' if resolved.endswith('.html') else resolved
        if source not in names and source.endswith('.qmd') and (ROOT/source).is_file():
            return PUBLIC+source[:-4]+'.html'+(sep+fragment if sep else '')
        if source in names:
            destination = student_path(source)
            if destination.endswith('.qmd') and not include:
                destination = destination[:-4]+'.html'
            return posixpath.relpath(destination, posixpath.dirname(student_path(name)))+(sep+fragment if sep else '')
        return target
    text = re.sub(r'(?<=\]\()([^\s)]+)', lambda m: relative(m[0]), text)
    text = re.sub(r'({{< include )([^\s]+)', lambda m: m[1]+relative(m[2], include=True), text)
    # Literal project-root paths in R source() calls and student instructions.
    for source in sorted(names, key=len, reverse=True):
        if source != student_path(source):
            text = text.replace(source, student_path(source))
    # Embedded images remain available without external lightbox image targets.
    text = text.replace('lightbox: true', 'lightbox: false')
    return text

def build_student_project(output):
    names = project_files()
    config = yaml.safe_load((ROOT/'_quarto.yml').read_text())
    config.pop('website', None)
    config['project']['type'] = 'default'
    config['project']['post-render'] = []
    config['project']['render'] = [student_path(f'{f}/{n}.qmd') for f,n in RUNNABLE_DOCUMENTS]
    config['format']['html']['css'] = ['assets/petra-brand.css', 'assets/source-slides.css', 'assets/practical-print.css']
    config['project']['resources'] = sorted(n for n in names if n.startswith('data/'))
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as z:
        for name in sorted(names):
            if Path(name).suffix in {'.qmd', '.R'}:
                z.writestr(student_path(name), rewrite(name, (ROOT/name).read_text(), names))
            else:
                z.write(ROOT/name, student_path(name))
        from r_code_files import r_code_files
        for name, code in r_code_files().items():
            z.writestr(student_path('lessons/'+name), code)
        z.writestr('_quarto.yml', yaml.safe_dump(config, sort_keys=False, allow_unicode=True))
        z.writestr('README.md', '''# 307312 Applied Statistics — start here

Extract the whole ZIP. In Positron, choose File > Open Folder and open the extracted
folder containing _quarto.yml, data/ and .vscode/. Keep that folder structure intact.
Install R, Positron and Quarto, then run once in the R console:

```r
install.packages(c("knitr", "rmarkdown", "dplyr", "ggplot2", "readr", "tidyr", "zoo", "e1071", "MASS"))
```

Open the folders in this order:

1. **part-1-introduction-to-r/** — one combined Introduction to R notebook, from basic R to dplyr and ggplot2.
2. **part-2-descriptive-statistics/** — combined Descriptive Statistics notebook: explanations, diagrams and 20 runnable R examples, including line and dot plots.
3. **part-3-inferential-statistics/** — Inferential Statistics: the teaching slides and executable R examples together, from probability through regression.
4. **extended-cases/** — optional business applications, including Superstore.

Each course part has one notebook and a plain .R script containing its code.
Run the .R scripts from the top-level folder with data/ in place.
Each course part has one notebook. The same sources generate the website, PDFs
and the notebooks in this project. Parts 2 and 3 include their teaching material
and executable R examples together; there are no separate practical notebooks.

Keep data/, assets/ and support/ in place: they contain required data, images and a
shared R helper. There are 12 runnable notebooks. Supporting editable Part 2
diagrams are under support/. Website navigation pages and unused draft notebooks are excluded.

Keep the project root as the working directory. Open the top-level course folder in Positron and select an R interpreter.
The supplied workspace runs Quarto cells in the R Console from the course root.
Run cells in order; use Preview to render the notebook with its outputs.
If a CSV cannot be found, use getwd() in the R Console to check that the working
folder contains data/. Reopen the top-level course folder if needed.
Run `quarto render` from the project root to render all material. No Python is required.
PDF/download links use the website.

Website: https://msfasha.github.io/307312-Applied-Statistics/
''')
    return output

if __name__ == '__main__':
    print(build_student_project(ROOT/'_build/website/downloads'/STUDENT_PROJECT_ZIP))
