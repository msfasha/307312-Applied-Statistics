# Publishing the three-part course

Students use https://msfasha.github.io/307312-Applied-Statistics/.
The home page must offer three lessons, a PDF for **each** lesson, a complete
student RStudio project ZIP, and an all-PDF ZIP.

The three lesson notebooks sit together under `lessons/`:

1. `lessons/01-introduction-to-r.qmd`
2. `lessons/02-descriptive-statistics.qmd`
3. `lessons/03-inferential-statistics.qmd`

## Build and publish

Commit and push the editable sources on `main`, then run:

```sh
python3 scripts/publish-course.py
```

The publisher renders all lessons with executable R cells, renders the three approved Part 2 practicals, prints all six
rendered notebooks to PDF, builds both student ZIPs, validates the required
outputs and exclusions, and pushes a normal commit to `gh-pages`. PDFs are
printed from HTML to preserve the original HTML diagrams, tables, images,
formula notation, and executed R results. Chrome or Chromium is required for
printing. Ghostscript, when installed, compresses images at 180 dpi while retaining vector text; Quarto, R, Python 3, and the lesson R packages are required to build.

`--skip-render` is only for an already completed, verified full HTML build.
It **always regenerates all six PDFs and both ZIPs** from that build.
For a local download build without publication, run
`python3 scripts/build-student-downloads.py` after rendering the full site.

## Required published downloads

- `pdf/01-introduction-to-r.pdf`
- `pdf/02-descriptive-statistics.pdf`
- `pdf/03-inferential-statistics.pdf`
- `downloads/applied-statistics-pdfs.zip`
- `downloads/applied-statistics-rstudio.zip`

The student project contains the three editable lessons and three practical notebooks, project and website
configuration, required assets/CSV data, and setup instructions. It excludes
instructor answers, archives, books, original measurement workbooks, source
PowerPoint decks, and build caches/logs. Test it after extraction separately
from the maintainer workspace.

The RStudio ZIP also includes `assets/petra-theme.md`, the tracked specification
for the Petra burgundy and gray theme. Keep it synchronized with the portable master
`../petra_theme/petra_theme.md` when changing the shared palette or layout rules.

## Source and student website

`main` is the maintainer workspace, with support scripts and historical sources.
`gh-pages` contains only the generated active student website from `_build/website/`.
Books and local reference documents remain ignored. Never copy instructor files,
archives, publisher books, raw measurement workbooks, caches, or logs to the site.

A local build or push to `main` alone is **not publication**. Check the live home
page, all three lessons, all three practicals, all six PDF downloads, both ZIPs, and the source commit
in `deployment.json`. Check PDF text and sample rendered pages, and confirm that
executable R results appear. The publisher preserves branch history and never
force pushes. The existing user authorization covers this course publication.

Rendered lesson pages live under `lessons/` on the website. Root-level legacy
lesson URLs redirect to those pages. The three approved practicals are rendered independently under
`_build/practicals/` and staged as self-contained HTML under website `practicals/`
by `scripts/stage-practicals.py`. Only the approved pages, the compatibility
entry page, cereals/funds CSVs and their student data guide enter the site.
Instructor answers, provenance manifests for these practicals, books, original
publisher workbooks and future draft activities stay out of public downloads.

## Approved Part 2 practical downloads

- `pdf/practical-01-categorical-business-data.pdf`
- `pdf/practical-02-numerical-business-data.pdf`
- `pdf/practical-03-association-and-groups.pdf`

The home page links all three HTML practicals and their PDFs. The all-PDF ZIP
contains six PDFs. The RStudio ZIP includes all six editable notebooks, the
shared practical plot helper, practical configuration and post-render scripts.
A full website render also renders and stages the approved practicals.
`--skip-render` reuses lesson HTML but refreshes practical HTML before packaging.
