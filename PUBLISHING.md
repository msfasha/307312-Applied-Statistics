# Course builds and publication

Students use <https://msfasha.github.io/307312-Applied-Statistics/>.

## One source for each part

The user’s latest instruction, 19 November 2026, is to keep the original teaching
slides and incorporate explained, executable R examples in place of spreadsheet
instructions. There are no alternative Part 3 lessons or separate practical.

- Part 1: `lessons/01-introduction-to-r.qmd`.
- Part 2: `lessons/02-descriptive-statistics.qmd`, including 20 R examples.
- Part 3: `lessons/03-inferential-statistics.qmd`, preserving the original four-part
  sequence and all 141 teaching positions, with 36 R examples. Spreadsheet
  instructions/dialogs and standalone Python implementations are replaced by R.
- Six numbered extended cases and three Superstore applications remain separate.

`scripts/course_documents.py` lists twelve canonical notebook/PDF pairs. The PDF
ZIP contains those twelve PDFs once each. The Positron ZIP contains those same
twelve runnable notebooks, grouped by course part or extended case. The Part 3
QMD in the ZIP is checked byte-for-byte against the source used for HTML and PDF.

Original PPTX/PDF reference decks remain unchanged under `sources/slides/`.
Original source errors and interpretation limits remain documented in `instructor/`;
preservation does not mean that every historical claim is validated. Non-software
Part 3 slide bodies are guarded by an instructor content manifest. The raw original
reference files are not public student downloads.

## Build and validate locally

```sh
python3 scripts/build-course.py
```

This checks the R examples, rebuilds the complete website, prints all twelve PDFs
from executed HTML, packages both student bundles and validates pages, links,
slide positions, data, source equality and exclusions. It never pushes/publishes.

- `_build/website/` is the generated site.
- `scripts/check-inferential.py` checks all 141 original Part 3 positions,
  preserved non-software text and all 36 explained R cells/results.
- `scripts/sync-descriptive-r-references.py --check` checks the 20 executable
  examples in the combined Part 2 notebook.
- `scripts/check-practicals.py` checks all twelve notebooks, pinned data,
  project-root imports and teaching results.
- The independent `practicals/` render contains compatibility entry pages only.
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

## Downloads and compatibility

Each part landing page has one resource row with its HTML/PDF; Part 3 also offers
the editable canonical QMD at `downloads/03-inferential-statistics.qmd`.

Old probability/practical HTML URLs contain only redirects to Part 3, not other
teaching versions. Their PDF URLs serve identical copies of the canonical Part 3
PDF. The old individual practical QMD download serves the current Part 3 source.
These unadvertised compatibility aliases do not enter either bundle.

The old descriptive practical URL similarly forwards to Part 2, with an identical
PDF alias. Former split R-introduction URLs/PDFs forward to/copy Part 1. Old
Superstore practical URLs open the relocated extended cases.

The advertised project is `downloads/applied-statistics-positron.zip`. The former
RStudio-named ZIP is an identical unadvertised compatibility copy. Refresh the
home-page cache query when changing the download.

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
canonical pages/PDFs, data, source downloads, compatibility URLs and both bundles.
It writes `_build/extended-review/live-verification.json`. Confirm each Part page
has one resource row and that the ZIP has one notebook per part.

## Editing in Positron

Parts 2 and 3 use native Markdown for teaching prose and source tables, so the
Visual Editor can show editable text instead of raw `<div>`/`<p>` blocks. Diagram
HTML/SVG remains where its layout requires it. Custom Petra styling appears in
the rendered preview. `scripts/native_source_markdown.py` checks this convention;
its one-time conversion report is local instructor material. Part 3 keeps the
historical body checksums and a separate guard for the native-format equivalent.
Part 1 plot setup uses boolean `echo: false` in separate hidden chunks, avoiding
the invalid `echo: !expr -1` option while retaining visible chart code.
