# 307312 Applied Statistics — Masters Level

Students: [open the course website](https://msfasha.github.io/307312-Applied-Statistics/).
For a compact working copy, download the student RStudio project from that website.

## Start here

Open `Applied-Statistics.Rproj` in RStudio. The three teaching notebooks are in
**lessons/**, in teaching order. **practicals/** contains the separate CEREALS
pilot, which has not yet been adopted into the published course.

| Folder | What belongs here |
|---|---|
| **lessons/** | The three active lessons; `_includes/` holds their shared diagrams and survey section |
| **practicals/** | Draft practical R activities, starting with CEREALS |
| **data/** | CSVs and data guides; grouped as descriptive-statistics, inferential-statistics, and practicals |
| **assets/** | Images and shared Petra styling used by the lessons |
| **sources/slides/** | Untouched original PPTX/PDF reference decks, with a guide to their contents |
| **instructor/** | Source reviews, conversion audits, teaching notes and practical answers |
| **books/** | Local textbook/reference collection; never published |
| **archived/** | Retired material; excluded from the active course |
| **scripts/** | Conversion, preview, packaging and publication tools |
| **_build/** | Generated output: `website/`, `practicals/`, and conversion `cache/`; not editable course sources |

The root contains only the course home page (`index.qmd`), RStudio/Quarto
configuration, project instructions, licence and this guide. All dataset files
belong under **data/**; there are no root-level dataset files.

## Lessons

1. `lessons/01-introduction-to-r.qmd` — essential R, dplyr and ggplot2.
2. `lessons/02-descriptive-statistics.qmd` — descriptive statistics.
3. `lessons/03-inferential-statistics.qmd` — probability, estimation, tests and regression.

Data import cells locate the shared **course-level `data/`** folder whether R is working from the course root or from the notebook folder. Keep the complete
folder structure when moving or downloading the project.

## Local previews

Run `quarto render` from the project root for the course website. Output is
`_build/website/index.html`. Quarto and R with knitr, rmarkdown, dplyr, ggplot2 and
MASS are required. On this workstation Quarto is also bundled with RStudio.

For the standalone pilot, run `python3 scripts/preview-cereals-pilot.py`.
Its output is `_build/practicals/practical-01-cereals.html`; its editable source
stays in `practicals/`. This preview is separate from the published course.

See [PUBLISHING.md](PUBLISHING.md) for the required PDF/ZIP builds and publication.
A local render does not publish anything.

## Historical material and source accuracy

The original 307102 slides are provenance for the current 307312 course, not a
second active course. Original slide text and images are preserved except for
previously authorized identity and diagram changes. Source issues are documented
in `instructor/`; preservation does not validate every source claim.

`archived/2026-11-01-retired-course/` holds the previous course;
`archived/2026-11-01-r-introduction-expanded/` holds the expanded R lessons.
`archived/2026-11-04-unused-support/` holds unused textbook CSVs and old R images
removed from the active folders during reorganization. Nothing there is adopted
automatically. Original publisher files and original student measurements remain
local-only. Instructor notes tracked on a public source branch are publicly
visible there even though excluded from the student website and ZIPs.
