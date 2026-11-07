# Course builds and publication

Students use <https://msfasha.github.io/307312-Applied-Statistics/>.

**Current instruction, 7 November 2026: push the committed updates to GitHub and publish the updated website.**
This supersedes the earlier local-only instruction.

## Active student material

`scripts/course_documents.py` is the authoritative list of sixteen notebook/PDF pairs:

- Six lesson notebooks under `lessons/`: the four supplied Part 1 R notebooks, Part 2 descriptive slides and Part 3 inferential slides.
- One companion notebook, `practicals/descriptive-statistics-r-practical.qmd`, containing all eighteen Part 2 R examples in slide order, with original code/comments and explanatory introductions.
- Three Superstore notebooks under `extended-cases/superstore/`, grouped by `index.qmd`.
- Six numbered extended cases under `extended-cases/`: Springville, Oxford, BLK, Parachute, Potato and Harnswell.

Part 2 retains all 87 approved source slides, their figures, Excel instructions,
the collection/survey supplement and the authorized diagram/CV corrections.
Its executable R cells live in the companion practical. Each of the 18 matching
slides also shows a **Try this in R** code reference and one direct link to the
corresponding practical section. The practical remains the code source: run
`python3 scripts/sync-descriptive-r-references.py` after editing its R examples.
The local builder checks that the slide references match. These references appear
in the lesson HTML and PDF without a separate PowerPoint copy. Downloads stay on
the Part 2 landing page rather than a repeated link row in the practical.
Across all sixteen notebooks, omit repeated PDF/ZIP download rows and Part 1's
repeated four-lesson menu. Keep individual downloads on the part/scenario landing
pages and identify bundled data files by path in notebooks. Preserve source
citations and links that connect a specific teaching example to its explanation.
Part 3 retains all 141
source slides and its labeled R equivalents. Original PPTX/PDF files remain unchanged.
The publisher checks all retained slide IDs and rejects reintroduction of slide 88.

The Superstore move preserves its three existing PDF names. Old HTML URLs under
`practicals/` remain compatibility entry pages, pointing to the relocated notebooks.
The former cereals entry page points to the new descriptive practical.
The home page and navbar distinguish the core practical from extended cases.

## Local verification

```sh
python3 scripts/build-course.py
```

This command runs R checks, rebuilds HTML, exports all sixteen PDFs, rebuilds both
student bundles and validates completeness, links and exclusions. It only writes
local build files; it never pushes or publishes. The publishing command calls
this same builder before uploading the generated website.

Use the configured RStudio Quarto executable if `quarto` is not on PATH.
The R checks verify fresh-session imports and all worked cells from both the
course root and each notebook folder. Nested Superstore imports also locate
`data/` from `extended-cases/superstore/`. They verify pinned hashes, source-cell
equivalence when original local workbooks are available, and key teaching results.
The four supplied Part 1 notebooks contain expected-error demonstrations and
are verified through full Quarto execution.

Root rendering writes `_build/website/`. Its post-render steps build the independent
`practicals/` project under `_build/practicals/` and stage only approved pages and
compatibility entry pages. The root project renders Superstore and the six other
extended cases directly, with the shared Petra burgundy and gray theme.

PDFs are printed from executed HTML to preserve diagrams, tables, images,
formula notation and results. Chrome/Chromium is required; Ghostscript optionally
compresses images at 180 dpi while retaining vector text. All sixteen PDFs go
under `_build/website/pdf/`, with both ZIPs under `_build/website/downloads/`.
Check PDF text and representative rendered pages. Extract the student RStudio ZIP
into a fresh directory and render the complete project to verify independence
from maintainer files. Keep `assets/petra-theme.md` synchronized with the portable
master `../petra_theme/petra_theme.md` when changing the shared theme.

## Student resources and exclusions

Both bundles include all sixteen approved documents. The RStudio ZIP contains
editable notebooks, required shared fragments, theme assets, project configuration,
build helpers and setup instructions. The PDF ZIP contains exactly one PDF per
approved notebook. The home page links all sixteen PDFs and both bundles.

Only explicitly listed `data/` resources in `_quarto.yml` enter the website and
student project: original descriptive/inferential teaching CSVs and guides,
canonical business CSVs and guide, and the supplied historical R-introduction
Superstore CSV and guide. The 2014–2017 R-introduction dataset is distinct from
the pinned US 2023–2025 business Superstore extract. Keep the only editable data
under root `data/`; preserve per-import path lookup for interactive RStudio cells.

Exclude books, instructor notes/answers, provenance manifests, archives, original
student measurement workbooks, publisher workbooks, source decks and build caches.
Original instructional image assets and approved editable diagrams remain included.
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

The publisher rebuilds HTML, all sixteen PDFs and both ZIPs, validates slide IDs,
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

The home page presents Course and Extended scenarios. course/index.qmd links the three part landing pages, which collect their own HTML/PDF and practical resources. Part 3 practical is coming soon, without a placeholder download. NAVIGATION_PAGES in scripts/course_documents.py tracks the landing pages for packaging and validation. These do not add PDFs to the sixteen-document contract.
