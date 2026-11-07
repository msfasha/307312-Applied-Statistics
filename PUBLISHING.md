# Publishing the course and extended cases

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

The publisher renders all lessons with executable R cells, renders the three approved Part 2 practicals and six extended cases, prints all twelve
rendered notebooks to PDF, builds both student ZIPs, validates the required
outputs and exclusions, and pushes a normal commit to `gh-pages`. PDFs are
printed from HTML to preserve the original HTML diagrams, tables, images,
formula notation, and executed R results. Chrome or Chromium is required for
printing. Ghostscript, when installed, compresses images at 180 dpi while retaining vector text; Quarto, R, Python 3, and the lesson R packages are required to build.

`--skip-render` is only for an already completed, verified full HTML build.
It **always regenerates all twelve PDFs and both ZIPs** from that build.
For a local download build without publication, run
`python3 scripts/build-student-downloads.py` after rendering the full site.

## Required published downloads

- `pdf/01-introduction-to-r.pdf`
- `pdf/02-descriptive-statistics.pdf`
- `pdf/03-inferential-statistics.pdf`
- `downloads/applied-statistics-pdfs.zip`
- `downloads/applied-statistics-rstudio.zip`

The student project contains the three editable lessons, three practical notebooks and six extended-case notebooks, project and website
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
page, all three lessons, all three practicals, all six extended cases, all twelve PDF downloads, both ZIPs, and the source commit
in `deployment.json`. Check PDF text and sample rendered pages, and confirm that
executable R results appear. The publisher preserves branch history and never
force pushes. The existing user authorization covers this course publication.

Rendered lesson pages live under `lessons/` on the website. Root-level legacy
lesson URLs redirect to those pages. The three approved practicals are rendered independently under
`_build/practicals/` and staged as self-contained HTML under website `practicals/`
by `scripts/stage-practicals.py`. Only the approved pages, the compatibility
entry page, approved lesson/business CSVs and their student data guide enter the site.
Instructor answers, provenance manifests for these practicals, books, original
publisher workbooks and future draft activities stay out of public downloads.

## Approved Part 2 practical downloads

- `pdf/practical-01-categorical-business-data.pdf`
- `pdf/practical-02-numerical-business-data.pdf`
- `pdf/practical-03-association-and-groups.pdf`

The home page links all three HTML practicals and their PDFs. The all-PDF ZIP
contains twelve PDFs. The RStudio ZIP includes all twelve editable notebooks, the
shared practical plot helper, practical configuration and post-render scripts.
A full website render also renders and stages the approved practicals.
`--skip-render` reuses lesson HTML but refreshes practical HTML before packaging.

## Original core restored; applications kept separate — 7 November 2026

Parts 2 and 3 restore the original slide-based lessons from `70bf7ee`: all 87 retained
descriptive slides (source slide 88 was removed at the user’s request) plus the approved collection/survey section, and all 141
inferential slides. Preserve the original sequence, Excel examples, source
figures and labeled R equivalents. The publisher checks these slide IDs.
The three R practicals and all six extended cases remain separate applications.
Do not replace the core lessons while updating practical examples.

The website and student project include only explicitly listed resources in
`_quarto.yml`: approved `data/business/` CSVs, the previously approved de-identified
`data/descriptive-statistics/students.csv`, the six printed-slide inference CSVs,
and their student guides. Do not publish original measurement workbooks or source
provenance JSONs. Include original instructional assets and all required shared
lesson fragments alongside the current business/practical helpers in the ZIP.
The restored original R examples use MASS, which is a recommended R package.

Before committing, run python3 scripts/check-practicals.py. It checks all twelve
notebooks, fresh-session imports from both locations, full source-cell equivalence
when publisher workbooks are available, provenance hashes and key teaching results.
After building downloads, extract the RStudio ZIP into a new directory and run all
twelve notebooks there; the extraction must not depend on maintainer files or books/.
Inspect representative PDF pages and verify all live pages, twelve PDFs, both ZIPs,
and deployment.json against the committed source revision.

## Extended Business Cases — 7 November 2026

The user authorized six standalone extension notebooks under `extended-cases/`.
The root Quarto project renders these with the shared course theme and normal
website navigation. Lesson links point to the complete cases or Springville
sections; the core teaching sequence remains intact.

`scripts/course_documents.py` lists the twelve approved notebooks used for PDF
exports and release checks. Preserve the original six PDF URLs and add:

- `pdf/case-01-springville-herald.pdf`
- `pdf/case-02-oxford-cereal.pdf`
- `pdf/case-03-retail-display.pdf`
- `pdf/case-04-perfect-parachute.pdf`
- `pdf/case-05-mountain-states-potato.pdf`
- `pdf/case-06-harnswell-quality.pdf`

The home page and navbar link Extended Business Cases; each case has its own PDF
and student-project link. Both bundles now cover twelve documents. The RStudio
ZIP includes the six editable case notebooks and seven canonical extension CSVs
explicitly allowed in `_quarto.yml`, under `data/business/`, alongside the restored core lesson CSVs. COLA is reused
rather than duplicated. Do not copy the supplied ZIP, unfiltered Parachute summary
rows, SH2 chart helpers or publisher workbooks into student outputs.

Run `scripts/prepare-extended-data.py` only when intentionally regenerating the
extension CSVs from local publisher workbooks. Check source/output hashes and
source-cell equivalence. `instructor/extended-cases-source-review.md`, the
provenance manifest and answer keys stay out of publication and student bundles.

A release must pass fresh-session imports/worked cells from both locations for
all twelve notebooks, full site navigation including fragments, twelve-PDF ZIP
contents, and a separately extracted student project's full render. Inspect all
six new PDFs and representative core PDFs; verify live case pages, twelve PDF
URLs, both ZIPs and `deployment.json` against the committed revision.

After publishing, run `python3 scripts/verify-live-course.py`. It waits for the
committed revision to reach GitHub Pages, then compares deployed bytes against
the local release for all twelve notebook pages, twelve PDFs, both ZIPs and all
approved data. Its release report is `_build/extended-review/live-verification.json`.
PDF navigation is exported with public course URLs rather than local build paths.
