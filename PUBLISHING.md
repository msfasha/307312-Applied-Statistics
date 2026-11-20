# Course builds and publication

Students use <https://msfasha.github.io/307312-Applied-Statistics/>.

## One source for each part

The user authorized a four-part course on 20 November 2026. Quarto is the
canonical editable source; HTML and PDF are display versions of the same material.

- Part 1: `lessons/01-introduction-to-r.qmd`.
- Part 2: `lessons/02-descriptive-statistics.qmd`, including 20 R examples.
- Part 3: `lessons/03-probability-foundations.qmd`: events, random variables and distributions.
- Part 4: `lessons/04-statistical-inference-and-estimation.qmd`: inference, sampling distributions, SE, CLT, point/interval estimation, hypothesis testing and regression.
- Six numbered extended cases and three Superstore applications remain separate.

Parts 3–4 retain every one of the 141 historical teaching positions once and all
36 explained R examples. The authorized reordered sequence lives in the instructor
manifest; sampling distributions, SE and CLT precede confidence intervals.

`scripts/course_documents.py` lists thirteen canonical notebook/PDF pairs. Both
bundles contain each document once. All thirteen notebooks are runnable; the Part
3 and Part 4 Quarto copies in the student ZIP must match their canonical sources
byte-for-byte. The four core plain `.R` downloads are exported reproducibly from
the notebooks; the old combined inference file is not regenerated.

Original PPTX/PDF reference decks remain unchanged under `sources/slides/`.
Original source errors and interpretation limits remain documented in `instructor/`;
preservation does not mean that every historical claim is validated. Non-software
Parts 3–4 slide bodies are guarded by an instructor content manifest. The raw original
reference files are not public student downloads.

## Build and validate locally

```sh
python3 scripts/build-course.py
```

This checks the R examples, rebuilds the complete website, prints all thirteen PDFs
from executed HTML, packages both student bundles and validates pages, links,
slide positions, data, source equality and exclusions. It never pushes/publishes.

- `_build/website/` is the generated site.
- `scripts/check-inferential.py` checks all 141 historical positions across Parts 3–4,
  preserved non-software text and all 36 explained R cells/results.
- `scripts/sync-descriptive-r-references.py --check` checks the 20 executable
  examples in the combined Part 2 notebook.
- `scripts/check-course.py` checks all thirteen notebooks, pinned data,
  project-root imports and teaching results.
- Validate a fresh extraction of the Positron ZIP by running `quarto render`.

R, Quarto, Chrome/Chromium and the documented R packages are required. MASS is
used by the original distribution-fitting example. PDFs preserve the HTML
figures, diagrams, formulas and calculated results; inspect representative pages.

## Student folder workflow

Open the extracted top-level folder containing `_quarto.yml`, `data/` and
`.vscode/` in Positron with File > Open Folder. Keep the R Console at this root.
`quarto.inlineOutput.enabled` is false, so interactive chunks use that Console
and fixed `data/...` CSV paths. Do not introduce notebook-relative data imports.
There is no RStudio project-file requirement.

The shared Petra theme is `assets/petra-theme.md`, synchronized with
`../petra_theme/petra_theme.md`. Use the shared burgundy headings, neutral teaching
surfaces, centred figures and consistent meaningful analytical colours.

## Downloads

Each part landing page has one resource row with its HTML/PDF; each part also offers
a plain `.R` script exported from its executable notebook cells.

The student project is `downloads/applied-statistics-positron.zip`; the PDF bundle
is `downloads/applied-statistics-pdfs.zip`. Only the thirteen canonical PDFs and
current download names are generated. Superseded entry pages, redirects and
duplicate downloads have been removed. Old external bookmarks may no longer work.
Refresh the home-page cache query when changing the download.

## Data and exclusions

Publish only the explicit CSV/guide allowlist in `_quarto.yml`: the historical R
introduction data, supplied descriptive teaching data, six original inferential
teaching CSVs, and approved business/extended-case data. Keep the historical
2014–2017 tutorial Superstore separate from the pinned US 2023–2025 business data.

Student packages include required images, the editable Part 2 fragments, the
shared R helper, theme specification and Positron settings. Exclude books,
publisher workbooks, original measurement workbooks, source decks, instructor
notes/solutions/provenance, archives, unused drafts and build caches. Original
source workbooks remain unchanged and local-only. No additional raw observations,
collection dates or causal assignments may be invented.

## Commit, publish and verify

The user explicitly requested consolidation and updating the website and student
downloads. Commit and push the scoped source changes to `main`, then run:

```sh
python3 scripts/publish-course.py
python3 scripts/verify-live-course.py
```

The publisher calls the local builder, records the source revision, and pushes a
normal generated-site commit to `gh-pages`; it never force-pushes. `--skip-render`
is only for a fully completed, checked HTML build and still refreshes downloads.
Use a full build after structural changes. A source push alone is not publication.

The live verifier checks the deployed source revision and actual bytes of all
canonical pages/PDFs, data, source downloads and both bundles.
It writes `_build/extended-review/live-verification.json`. Confirm each Part page
has one resource row and that the ZIP has one notebook per part.

## Editing in Positron

Parts 2–4 use native Markdown for teaching prose and source tables, so the
Visual Editor can show editable text instead of raw `<div>`/`<p>` blocks. Diagram
HTML/SVG remains where its layout requires it. Custom Petra styling appears in
the rendered preview. `scripts/native_source_markdown.py` checks this convention;
its one-time conversion report is local instructor material. Parts 3–4 keep the
historical body checksums and a separate guard for the native-format equivalent.
Part 1 plot setup uses boolean `echo: false` in separate hidden chunks, avoiding
the invalid `echo: !expr -1` option while retaining visible chart code.
