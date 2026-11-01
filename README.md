# 307312 Applied Statistics — Masters Level

**Students: [open the course website](https://msfasha.github.io/307312-Applied-Statistics/).**
Read the lessons online or download each part as PDF, all PDFs together, or the
student RStudio project from the home page.

## The active course: three notebooks

| Part | Editable source | Content |
|---|---|---|
| 1 | `01-introduction-to-r.qmd` | Essential R, dplyr, and ggplot2 |
| 2 | `02-descriptive-statistics.qmd` | Descriptive statistics, original slides plus R equivalents |
| 3 | `03-inferential-statistics.qmd` | Probability, estimation, tests, and regression plus R equivalents |

All three sit together at the root. There is no separate active module folder.
Open `Applied-Statistics.Rproj` in RStudio to edit or execute the notebooks.
The website and PDFs show executed results; use RStudio to run or change code.

## What the other files are for

This GitHub repository is the **maintainer workspace**. For a compact student
folder, use the **student RStudio project download** on the course website.

| Item | Purpose |
|---|---|
| `index.qmd` | Student home page and downloads |
| `assets/`, `content/`, `data/` | Styling, diagrams, pictures, and teaching CSVs required by the lessons |
| `scripts/` | Reproducible conversion, PDF export, packaging, and publication |
| `slides/` | Unchanged original reference decks; not assigned separately |
| `_instructor/` | Conversion audits and source issues; excluded from student downloads |
| `archived/` | Retired course and expanded R notes; excluded from student downloads |
| `_quarto.yml` | Website configuration |
| `PUBLISHING.md` | Required build, PDF, packaging, and live verification instructions |
| `AGENTS.md` | Course development instructions |

Instructor and archived files on this public source branch are publicly visible
on GitHub, although excluded from the student website and packages.

## Building and maintaining

Run `quarto render` to build the HTML lessons in `_preview/`. Quarto and R with
knitr/rmarkdown, dplyr, ggplot2, and MASS are required. See `PUBLISHING.md` to
create the PDFs and downloads and publish the website.

The condensed Part 1 replaces the expanded notes retained in
`archived/2026-11-01-r-introduction-expanded/`. The former full course is retained
in `archived/2026-11-01-retired-course/`. Books and local documents stay ignored.

Parts 2 and 3 preserve original slide text and images, apart from authorized
course identity updates and five standardized diagrams. Clearly labeled R
examples supplement the original examples. Source errors are recorded separately
under `_instructor/`; preserving the text does not validate every original claim.
The converters and their R-example files under `scripts/` reproduce the lessons.
The CSV dictionaries and provenance records are under `data/`.
