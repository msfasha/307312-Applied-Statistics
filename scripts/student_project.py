"""Build a teaching-order student project independently of website source layout."""
from pathlib import Path
import posixpath
import re
import zipfile
import yaml
from urllib.parse import unquote
from course_documents import DOCUMENTS

# Website/PDF documents remain unchanged; the RStudio ZIP contains runnable work only.
RSTUDIO_DOCUMENTS = [(f, n) for f, n in DOCUMENTS
                     if f != "lessons" or n in {"01-introduction-to-r", "r-02-basic-concepts", "r-03-dplyr", "r-04-ggplot2"}]

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = 'https://msfasha.github.io/307312-Applied-Statistics/'

def student_path(name):
    if name.startswith('lessons/_includes/'):
        return name.replace('lessons/_includes/', 'support/', 1)
    if name.startswith('lessons/'):
        part = 'part-1-introduction-to-r' if Path(name).stem in ['01-introduction-to-r', 'r-02-basic-concepts', 'r-03-dplyr', 'r-04-ggplot2'] else ('part-2-descriptive-statistics' if Path(name).stem == '02-descriptive-statistics' else 'part-3-inferential-statistics')
        return part+'/'+Path(name).name
    if name.startswith('practicals/'):
        part = 'part-2-descriptive-statistics' if 'descriptive-statistics-r-practical' in name else 'part-3-inferential-statistics'
        return part+'/'+Path(name).name
    return name

def project_files():
    names = {f'{folder}/{n}.qmd' for folder,n in RSTUDIO_DOCUMENTS}
    names.update(['Applied-Statistics.Rproj', 'lessons/_includes/course-tools.R'])
    for folder, notebook in RSTUDIO_DOCUMENTS:
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
    names.update('assets/'+n for n in ['petra-theme.md', 'petra-brand.css', 'source-slides.css', 'practical-print.css'])

    return names

def rewrite(name, text, names):
    def relative(target):
        base, sep, fragment = target.partition('#')
        resolved = posixpath.normpath(posixpath.join(posixpath.dirname(name), base))
        if resolved.startswith(('pdf/', 'downloads/')):
            return PUBLIC+resolved+(sep+fragment if sep else '')
        source = resolved[:-5]+'.qmd' if resolved.endswith('.html') else resolved
        if source not in names and source.endswith('.qmd') and (ROOT/source).is_file():
            return PUBLIC+source[:-4]+'.html'+(sep+fragment if sep else '')
        if source in names:
            destination = student_path(source)
            if destination.endswith('.qmd'):
                destination = destination[:-4]+'.html'
            return posixpath.relpath(destination, posixpath.dirname(student_path(name)))+(sep+fragment if sep else '')
        return target
    text = re.sub(r'(?<=\]\()([^\s)]+)', lambda m: relative(m[0]), text)
    text = re.sub(r'({{< include )([^\s]+)', lambda m: m[1]+relative(m[2]), text)
    # Literal project-root paths in R source() calls and student instructions.
    for source in sorted(names, key=len, reverse=True):
        if source != student_path(source):
            text = text.replace(source, student_path(source))
    text = text.replace('this notebook under `practicals/`', 'this notebook under `part-3-inferential-statistics/`')
    if name.startswith('practicals/'):
        text = re.sub(r'```\{r\}\n#\| label: render-project-root\n#\| include: false\nknitr::opts_knit\$set\(root.dir = normalizePath\("\.\."\)\)\n```', '', text)
    # Embedded images remain available without external lightbox image targets.
    text = text.replace('lightbox: true', 'lightbox: false')
    return text

def build_student_project(output):
    names = project_files()
    config = yaml.safe_load((ROOT/'_quarto.yml').read_text())
    config.pop('website', None)
    config['project']['type'] = 'default'
    config['project']['post-render'] = []
    config['project']['render'] = [student_path(f'{f}/{n}.qmd') for f,n in RSTUDIO_DOCUMENTS]
    config['format']['html']['css'] = ['assets/petra-brand.css', 'assets/source-slides.css', 'assets/practical-print.css']
    config['project']['resources'] = sorted(n for n in names if n.startswith('data/'))
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as z:
        for name in sorted(names):
            if Path(name).suffix in {'.qmd', '.R'}:
                z.writestr(student_path(name), rewrite(name, (ROOT/name).read_text(), names))
            else:
                z.write(ROOT/name, student_path(name))
        z.writestr('_quarto.yml', yaml.safe_dump(config, sort_keys=False, allow_unicode=True))
        z.writestr('README.md', '''# 307312 Applied Statistics — start here

Extract the whole ZIP and open Applied-Statistics.Rproj in RStudio.
Install R, RStudio and Quarto, then run once in the R console:

```r
install.packages(c("knitr", "rmarkdown", "dplyr", "ggplot2", "readr", "tidyr", "zoo", "e1071"))
```

Open the folders in this order:

1. **part-1-introduction-to-r/** — four R notebooks, in order: 01, r-02, r-03, r-04.
2. **part-2-descriptive-statistics/** — runnable descriptive R practical (20 examples, including line and dot plots).
3. **part-3-inferential-statistics/** — developing inference R practical (probability available; estimation, testing and regression forthcoming).
4. **extended-cases/** — optional business applications, including Superstore.

Teaching slides and the revised probability lesson are available on the course website
and as PDFs. Links to those lessons open the website; their sources are not in this ZIP.

Keep data/, assets/ and support/ in place: they contain required data, images and a
shared R helper. There are 15 runnable notebooks. Website navigation pages, slide-lesson
sources, obsolete redirects and unpublished review notebooks are excluded.

Keep the project root as the working directory. In RStudio, set Tools > Global Options >
R Markdown > Evaluate chunks in directory to Project. Run chunks in order, or use Render.
Run `quarto render` from the project root to render all material. No Python is required.
PDF/download links use the website.

Website: https://msfasha.github.io/307312-Applied-Statistics/
''')
    return output

if __name__ == '__main__':
    print(build_student_project(ROOT/'_build/website/downloads/applied-statistics-rstudio.zip'))
