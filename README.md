# 307312 Applied Statistics — Masters Level

## Course structure

1. **Introduction to R** — retained lessons, practice, assets, and CSV dependencies.
2. **Descriptive Statistics** — `02-descriptive-statistics.qmd`, based on all 88
   original 307102 slides, using the shared Petra theme. Original text and
   graphics are retained except for the updated course identity and five
   user-authorized diagrams rebuilt in the standard Petra theme; clearly labeled R equivalents are added alongside
   the original Excel instructions.
3. **Inferential Statistics** — `03-inferential-statistics.qmd`, covering the
   141 original slides in four subsections, with 29 executable R equivalents.

Open `Applied-Statistics.Rproj` in RStudio. Render the descriptive QMD to see the
first preview, or run `quarto render` from this folder to build the local course.
Quarto and R with knitr/rmarkdown are required; Part 1 also uses dplyr and ggplot2.

Generated HTML is stored in `_preview/`. The descriptive HTML embeds its assets
for convenient sharing. The source QMD uses files in `assets/` and `data/`; keep
those folders with it when editing or rerendering. Code runs during rendering
or from the QMD in RStudio; the HTML is a rendered lesson, not an in-browser R kernel.

## Sources and preservation

Original reference decks are under `slides/` and remain unchanged.
`scripts/convert-descriptive-slides.py` rebuilds the descriptive QMD from the
original PPTX/PDF plus `scripts/descriptive-r-examples.json`. It requires Python
with Pillow and Poppler. `scripts/export-original-students.py` reproduces the
CSV from the original workbook and requires openpyxl. See `data/307102/` for
the dictionary and provenance.

`_instructor/` holds the conversion audit and source issues for later review.
The conversion preserves wording rather than silently correcting source errors.
It uses a responsive reading layout rather than the original slide coordinates.
Text remains editable; original graphics, diagrams, and formula pictures remain images.

The former course remains under `archived/2026-11-01-retired-course/`.
`books/` remains a local reference library. The active three-part course is published at
https://msfasha.github.io/307312-Applied-Statistics/. See `PUBLISHING.md` for the
source and generated-site branch workflow.

The five editable diagram replacements live under `content/diagrams/`. Formula
notation uses native MathML, so the rendered equations need no remote math service.

Part 3 uses `scripts/convert-inferential-slides.py` and
`scripts/inferential-r-examples.json`. Its six teaching CSVs reproduce exact slide
tables; data dictionaries and provenance are under `data/inferential-statistics/`.
The R distribution-fitting comparison uses the recommended MASS package.

Rebuilding Part 3 figures from the reference decks requires LibreOffice, Poppler,
and Python with Pillow; rendering the prepared Quarto lesson requires R and Quarto.
