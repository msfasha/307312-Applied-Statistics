# Course builds and publication

Students use <https://msfasha.github.io/307312-Applied-Statistics/>.

**Current instruction, 7 November 2026: push the committed updates to GitHub and publish the updated website.**
This supersedes the earlier local-only instruction.

## Active student material

`scripts/course_documents.py` is the authoritative list of eighteen notebook/PDF pairs:

- Seven lesson notebooks under `lessons/`: the four supplied Part 1 R notebooks, Part 2 descriptive slides, Part 3 inferential slides and the revised probability-distributions section.
- Two companion notebooks: `practicals/descriptive-statistics-r-practical.qmd` (the eighteen Part 2 R examples) and `practicals/inferential-statistics-r-practical.qmd` (seven explained probability examples, simulation and independent tasks; later inference topics remain explicitly forthcoming).
- Three Superstore notebooks under `extended-cases/superstore/`, grouped by `index.qmd`.
- Six numbered extended cases under `extended-cases/`: Springville, Oxford, BLK, Parachute, Potato and Harnswell.

Part 2 retains 82 approved source slides after the 8 November duplicate review,
their figures, Excel instructions,
the collection/survey supplement and the authorized diagram/CV corrections.
Its executable R cells live in the companion practical. Each of the 18 matching
slides also shows a **Try this in R** code reference and one direct link to the
corresponding practical section. The practical remains the code source: run
`python3 scripts/sync-descriptive-r-references.py` after editing its R examples.
The local builder checks that the slide references match. These references appear
in the lesson HTML and PDF without a separate PowerPoint copy. Downloads stay on
the Part 2 landing page rather than a repeated link row in the practical.
Across all eighteen notebooks, omit repeated PDF/ZIP download rows and Part 1's
repeated four-lesson menu. Keep individual downloads on the part/scenario landing
pages and identify bundled data files by path in notebooks. Preserve source
citations and links that connect a specific teaching example to its explanation.
Part 3 retains all 141
source slides and its labeled R equivalents. Original PPTX/PDF files remain unchanged.
The publisher checks all 82 retained descriptive slide IDs and rejects reintroduction
of removed slides 77, 80, 83, 84, 85 and 88.

The Superstore move preserves its three existing PDF names. Old HTML URLs under
`practicals/` remain compatibility entry pages, pointing to the relocated notebooks.
The former cereals entry page points to the new descriptive practical.
The home page and navbar distinguish the core practical from extended cases.

## Local verification

```sh
python3 scripts/build-course.py
```

This command runs R checks, rebuilds HTML, exports all eighteen PDFs, rebuilds both
student bundles and validates completeness, links and exclusions. It only writes
local build files; it never pushes or publishes. The publishing command calls
this same builder before uploading the generated website.

Use the configured RStudio Quarto executable if `quarto` is not on PATH.
The R checks verify fresh-session imports and all worked cells from the course
project root. Open `Applied-Statistics.Rproj` and use project-root chunk execution
in RStudio. All examples read fixed `data/` paths, including nested Superstore notebooks. They verify pinned hashes, source-cell
equivalence when original local workbooks are available, and key teaching results.
The four supplied Part 1 notebooks contain expected-error demonstrations and
are verified through full Quarto execution.

Root rendering writes `_build/website/`. Its post-render steps build the independent
`practicals/` project under `_build/practicals/` and stage only approved pages and
compatibility entry pages. The root project renders Superstore and the six other
extended cases directly, with the shared Petra burgundy and gray theme.

PDFs are printed from executed HTML to preserve diagrams, tables, images,
formula notation and results. Chrome/Chromium is required; Ghostscript optionally
compresses images at 180 dpi while retaining vector text. All eighteen PDFs go
under `_build/website/pdf/`, with both ZIPs under `_build/website/downloads/`.
Check PDF text and representative rendered pages. Extract the student RStudio ZIP
into a fresh directory and render the complete project to verify independence
from maintainer files. Keep `assets/petra-theme.md` synchronized with the portable
master `../petra_theme/petra_theme.md` when changing the shared theme.

## Student resources and exclusions

The PDF bundle includes all eighteen approved documents. The RStudio ZIP contains fifteen runnable notebooks (four R introductions, two practicals and nine extended cases), plus required data, introductory images, a shared R helper, theme assets,
project configuration and setup instructions. The PDF ZIP contains exactly one PDF per
approved notebook. The home page links all eighteen PDFs and both bundles.

Only explicitly listed `data/` resources in `_quarto.yml` enter the website and
student project: original descriptive/inferential teaching CSVs and guides,
canonical business CSVs and guide, and the supplied historical R-introduction
Superstore CSV and guide. The RStudio ZIP takes only the data used by its fifteen notebooks
and the corresponding guides from this allowlist. The 2014–2017 R-introduction dataset is distinct from
the pinned US 2023–2025 business Superstore extract. Keep the only editable data
under root `data/`; read fixed paths from the project root in interactive RStudio cells.

Exclude books, instructor notes/answers, provenance manifests, archives, original
student measurement workbooks, publisher workbooks, source decks and build caches.
The website retains original instructional images and approved editable diagrams.
The RStudio ZIP includes only images needed by its runnable notebooks.
The Superstore workbook and publisher workbooks stay unchanged and local-only.
Do not infer random sampling, causal discount effects or refund accounting.

The extension source reviews and answer keys remain under `instructor/`.
`scripts/prepare-extended-data.py` regenerates approved extension CSVs only when
intentionally requested; it must not silently change source measurements.
Historical slide converters write `_build/reference-conversions/` and must not
overwrite authored lessons or reinsert Part 2 R cells into the active slide lesson.

## Authorized publication

After explicit authorization, commit and push sources on `main`, then run:

```sh
python3 scripts/publish-course.py
python3 scripts/verify-live-course.py
```

The publisher rebuilds HTML, all eighteen PDFs and both ZIPs, validates slide IDs,
navigation, bundle contents and exclusions, and pushes a normal commit to `gh-pages`.
It preserves branch history and never force pushes. `--skip-render` is only for a
completed, verified HTML build; it refreshes the independent practical pages and
always rebuilds all PDFs and both ZIPs. After structural moves, prefer a full build.

`main` is the maintainer workspace; `gh-pages` contains only generated student
website files. A source push or local render alone is not publication. Verify
`deployment.json`, every approved page/PDF/CSV and both bundles against the
committed source revision. The live verifier compares actual bytes and writes
`_build/extended-review/live-verification.json`. PDF navigation uses public URLs.
The user explicitly authorized the current push and website update.

## Simplified interface

The home page has a Course material heading with three plain part links, followed by Other Downloads with both bundles and Extended scenarios. The navbar Course link opens the home page; course/index.qmd remains a compatible entry page. Part landing pages collect their own HTML/PDF and practical resources, ending with only a Home link to the main page. Part 3 links the original slides, the revised probability section, and the developing inferential R practical with online/PDF/Quarto downloads. NAVIGATION_PAGES in scripts/course_documents.py tracks the website landing pages for validation. These do not add PDFs to the eighteen-document contract.

## Part 3 probability and developing practical — 8 November 2026

The user authorized building and publishing the reviewed probability section and
its course-long practical. Keep the original 141-slide lesson available; the
new probability section is a separate 23-slide notebook. It adds an explicit
d/p/q/r function-family slide and reproducible rnorm() simulation.

The practical currently covers probability only and identifies later sections
as forthcoming. Part 3 offers an individual editable Quarto download under
`downloads/inferential-statistics-r-practical.qmd`. This is the sole approved
public .qmd exception; preserve the exclusions for all other source files.
The PDF bundle includes all eighteen approved PDFs. The RStudio bundle contains only the fifteen runnable R notebooks and required support files. The live verifier checks the individual notebook
byte-for-byte as well as the pages, PDFs, data and bundles.

## Student ZIP organization — 8 November 2026

The website source folders are not the student project layout. `scripts/student_project.py`
packages the fifteen runnable notebooks into `part-1-introduction-to-r/`,
`part-2-descriptive-statistics/`, `part-3-inferential-statistics/` and `extended-cases/`.
Part 1 contains its four R introductions; Parts 2 and 3 each contain their R practical.
`support/` contains only the required shared R helper; data and image paths retain their root folders. Links, include paths and
R helper paths are rewritten in the ZIP only. Website URLs and canonical sources stay
unchanged. The ZIP uses one root Quarto project with project-root execution, no nested
practical project or Python render helpers, and no website navigation pages, slide-lesson sources or obsolete compatibility notebooks.
Links to omitted teaching lessons open the published website. The README identifies the developing probability companion.
Validate a fresh extraction with a complete `quarto render` before release.


## Combined release — 8 November 2026

Publish the runnable-only RStudio ZIP and the approved descriptive ending cleanup together.
The five repeated/empty outlier slides (77, 80, 83, 84, 85) are removed, with distinct
screening explanations consolidated on slide 82; source IDs and practical links remain.
Rebuild all eighteen PDFs and both ZIPs. Keep the existing download URL; the home-page
RStudio link adds `?v=20261108-clean` to refresh previously cached downloads.
Unpublished inference-review files remain outside this release.
