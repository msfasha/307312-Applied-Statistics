# Build and verify

Open `20261.Rproj` in RStudio. Run these commands from this folder.

```sh
quarto render
quarto preview
```

The student site is generated in `_site/`. Render the entire project after renaming sources or changing navigation. The build checks internal file links with `scripts/validate-course.py`. Source calculations execute on rebuild rather than relying on old frozen results.

Required R packages: `knitr`, `rmarkdown`, `ggplot2`, `dplyr`, `tidyr`, `readr`, and `stringr`. Data verification also uses `readxl`. Use the system R environment; the former broad package lock snapshot is preserved in the external recovery archive, not presented as a tested current environment.

```sh
python3 scripts/audit-code-documentation.py
Rscript scripts/verify-data.R
Rscript scripts/prepare-histogram-student-data.R
bash scripts/render-instructor.sh
```

Instructor HTML exports are kept in `_instructor/_output/`, apart from editable answers. They are not part of the student website.

Quarto is installed locally at `/usr/lib/rstudio/resources/app/bin/quarto/bin/quarto` if it is not on PATH. The instructor rendering script uses that path as a fallback.

Do not edit `_site/` directly or copy old HTML exports into it. `.quarto/` is generated working state. Export personal reports to `_output/`, never to the input CSV folders.

## Build all student PDFs

From this `20261` folder, run:

```sh
python3 scripts/build-pdfs.py
```

This creates one A4 PDF for each student page (lessons, exercises, overviews, and resources) in `_output/pdf/`, retaining the module folders and lesson numbers. It rebuilds from the QMD sources, including the R calculations, rather than printing old HTML files. Instructor answers are excluded. The normal HTML website stays in `_site/`.

The command also copies the teaching data into the PDF folder and creates `_output/applied-statistics-student-pdfs.zip`, including PDFs, linked figures, and datasets. Extract the entire ZIP and open `index.pdf` in a desktop PDF reader; keep its folder structure intact. Build logs and visual-review images are excluded from the ZIP. A selected-lesson build refreshes the bundle using the PDFs currently present; use the full command for a complete fresh export.

To rebuild just one lesson:

```sh
python3 scripts/build-pdfs.py modules/02-data-and-descriptive-statistics/01-data-types-and-toolbox.qmd
```

The print profile is `_quarto-pdf.yml`; print styling is in `assets/pdf/petra-print.tex` and `scripts/pdf-layout.lua`. It uses dark, muted Petra headings, neutral body text, visible teaching code, and an Arabic font for case narration. Hidden setup chunks remain hidden. PDF links to other lessons use their PDF filenames; keep the exported folders together. Interactive HTML controls are replaced by static print content.

First-time setup on another computer: install Quarto and the R packages listed above, run `quarto install tinytex --no-prompt`, and install the fonts DejaVu Sans, DejaVu Sans Mono, and Noto Naskh Arabic. SVG diagrams require CairoSVG (`python3 -m pip install cairosvg` and its platform Cairo dependency). The script also recognizes the bundled Codex Python runtime when available. Generated vector diagram copies live under `assets/pdf/svg/`; do not edit these copies. Build logs are in `_output/pdf/build-logs/`.

The documentation audit parses actual R function calls and requires each to be explained in comments within its chunk or script. It also checks the student comment minimum. This is a coverage check: review unfamiliar arguments, units, and statistical assumptions for meaning. Existing deliberately unfinished practice templates are reported separately.
