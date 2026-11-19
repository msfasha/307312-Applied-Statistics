# Course builds and publication

Students use <https://msfasha.github.io/307312-Applied-Statistics/>.

**Current instruction, 15 November 2026: push the committed updates to GitHub and publish the updated website.**
This supersedes the earlier local-only instruction.

## Active student material

`scripts/course_documents.py` is the authoritative list of fourteen notebook/PDF pairs:

- Four lesson notebooks under `lessons/`: the combined Part 1 R introduction, Part 2 descriptive slides, Part 3 inferential slides and the revised probability-distributions section.
- One companion notebook: `practicals/inferential-statistics-r-practical.qmd` (seven explained probability examples, simulation and independent tasks; later inference topics remain explicitly forthcoming).
- Three Superstore notebooks under `extended-cases/superstore/`, grouped by `index.qmd`.
- Six numbered extended cases under `extended-cases/`: Springville, Oxford, BLK, Parachute, Potato and Harnswell.

Part 2 retains 82 approved source slides after the 8 November duplicate review,
their figures, Excel instructions,
the collection/survey supplement and the authorized diagram/CV corrections.
All 20 executable R examples, their explanations and rendered results now live
in `lessons/02-descriptive-statistics.qmd`, alongside their matching topics.
The former practical HTML URL forwards to this combined notebook, preserving
example fragments; its PDF URL serves an identical copy of the combined PDF.
The canonical PDF ZIP contains only one Part 2 PDF. Run
`python3 scripts/sync-descriptive-r-references.py --check` to validate the 20
explained executable examples; there is no separate code copy to synchronize.
Downloads stay on the Part 2 landing page, which has one combined resource row.
Across all fourteen notebooks, omit repeated PDF/ZIP download rows and Part 1's
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

This command runs R checks, rebuilds HTML, exports all fourteen PDFs, rebuilds both
student bundles and validates completeness, links and exclusions. It only writes
local build files; it never pushes or publishes. The publishing command calls
this same builder before uploading the generated website.

Install the standalone Quarto CLI and ensure `quarto` is on PATH; no IDE-bundled executable is required.
The R checks verify fresh-session imports and all worked cells from the course
project root. In Positron, open the top-level course folder with File > Open Folder
and use its R Console for project-root chunk execution. All examples read fixed `data/` paths, including nested Superstore notebooks. They verify pinned hashes, source-cell
equivalence when original local workbooks are available, and key teaching results.
The combined Part 1 notebook is checked in a fresh R session and through full Quarto execution. It introduces base R first, then dplyr and ggplot2 pipelines.

Root rendering writes `_build/website/`. Its post-render steps build the independent
`practicals/` project under `_build/practicals/` and stage only approved pages and
compatibility entry pages. The root project renders Superstore and the six other
extended cases directly, with the shared Petra burgundy and gray theme.

PDFs are printed from executed HTML to preserve diagrams, tables, images,
formula notation and results. Chrome/Chromium is required; Ghostscript optionally
compresses images at 180 dpi while retaining vector text. All fourteen PDFs go
under `_build/website/pdf/`, with both ZIPs under `_build/website/downloads/`.
Check PDF text and representative rendered pages. Extract the student Positron ZIP
into a fresh directory and render the complete project to verify independence
from maintainer files. Keep `assets/petra-theme.md` synchronized with the portable
master `../petra_theme/petra_theme.md` when changing the shared theme.

## Student resources and exclusions

The PDF bundle includes all fourteen approved documents. The Positron ZIP contains twelve runnable notebooks (one combined R introduction, one combined descriptive lesson, one inference practical and nine extended cases), plus required data, introductory images, a shared R helper, theme assets,
project configuration and setup instructions. The PDF ZIP contains exactly one PDF per
approved notebook. The home page links all fourteen PDFs and both bundles.

Only explicitly listed `data/` resources in `_quarto.yml` enter the website and
student project: original descriptive/inferential teaching CSVs and guides,
canonical business CSVs and guide, and the supplied historical R-introduction
Superstore CSV and guide. The Positron ZIP takes only the data used by its twelve notebooks
and the corresponding guides from this allowlist. The 2014–2017 R-introduction dataset is distinct from
the pinned US 2023–2025 business Superstore extract. Keep the only editable data
under root `data/`; read fixed paths from the project root in interactive Positron Console cells.

Exclude books, instructor notes/answers, provenance manifests, archives, original
student measurement workbooks, publisher workbooks, source decks and build caches.
The website retains original instructional images and approved editable diagrams.
The Positron ZIP includes the images and editable fragments needed by its runnable notebooks, including the combined descriptive material.
The Superstore workbook and publisher workbooks stay unchanged and local-only.
Do not infer random sampling, causal discount effects or refund accounting.

The extension source reviews and answer keys remain under `instructor/`.
`scripts/prepare-extended-data.py` regenerates approved extension CSVs only when
intentionally requested; it must not silently change source measurements.
Historical slide converters write `_build/reference-conversions/` and must not
overwrite authored lessons or overwrite the combined Part 2 notebook.

## Authorized publication

After explicit authorization, commit and push sources on `main`, then run:

```sh
python3 scripts/publish-course.py
python3 scripts/verify-live-course.py
```

The publisher rebuilds HTML, all fourteen PDFs and both ZIPs, validates slide IDs,
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

The home page has a Course material heading with three plain part links, followed by Other Downloads with both bundles and Extended scenarios. The navbar Course link opens the home page; course/index.qmd remains a compatible entry page. Part landing pages collect their own HTML/PDF and practical resources, ending with only a Home link to the main page. Part 3 links the original slides, the revised probability section, and the developing inferential R practical with online/PDF/Quarto downloads. NAVIGATION_PAGES in scripts/course_documents.py tracks the website landing pages for validation. These do not add PDFs to the fourteen-document contract.

## Part 3 probability and developing practical — 8 November 2026

The user authorized building and publishing the reviewed probability section and
its course-long practical. Keep the original 141-slide lesson available; the
new probability section is a separate 23-slide notebook. It adds an explicit
d/p/q/r function-family slide and reproducible rnorm() simulation.

The practical currently covers probability only and identifies later sections
as forthcoming. Part 3 offers an individual editable Quarto download under
`downloads/inferential-statistics-r-practical.qmd`. This is the sole approved
public .qmd exception; preserve the exclusions for all other source files.
The PDF bundle includes all fourteen approved PDFs. The Positron bundle contains only the twelve runnable R notebooks and required support files. The live verifier checks the individual notebook
byte-for-byte as well as the pages, PDFs, data and bundles.

## Student ZIP organization — 8 November 2026

The website source folders are not the student project layout. `scripts/student_project.py`
packages the twelve runnable notebooks into `part-1-introduction-to-r/`,
`part-2-descriptive-statistics/`, `part-3-inferential-statistics/` and `extended-cases/`.
Part 1 contains the combined R introduction; Part 2 contains the combined descriptive lesson and R examples; Part 3 contains its developing R practical.
`support/` contains only the required shared R helper; data and image paths retain their root folders. Links, include paths and
R helper paths are rewritten in the ZIP only. The descriptive lesson is now the canonical Part 2 notebook; the old practical HTML/PDF URLs remain compatibility aliases. The ZIP uses one root Quarto project with project-root execution, no nested
practical project or Python render helpers, and no website navigation pages, non-runnable inferential slide sources or obsolete compatibility notebooks. The combined Part 2 includes its required editable diagrams and survey fragment under support/.
Links to omitted teaching lessons open the published website. The README identifies the developing probability companion.
Validate a fresh extraction with a complete `quarto render` before release.


## Combined release — 8 November 2026

Publish the runnable-only Positron ZIP and the approved descriptive ending cleanup together.
The five repeated/empty outlier slides (77, 80, 83, 84, 85) are removed, with distinct
screening explanations consolidated on slide 82; source IDs and practical links remain.
Rebuild all fourteen PDFs and both ZIPs. Keep the existing download URL; the home-page
Positron link adds `?v=20261108-clean` to refresh previously cached downloads.
Unpublished inference-review files remain outside this release.

## Descriptive chart additions — 14 November 2026

Two added teaching slides supplement the 82 retained source slides: line charts
after source slide 26 and dot plots before source slide 28. The companion has
20 examples; 7a and 7b preserve the numbering and anchors of all 18 originals.
The line chart uses R's built-in AirPassengers monthly series (1949–1960, thousands);
the dot plot uses the first 30 student ages in unchanged file order, without
claiming random selection. Original source decks remain unchanged.
`scripts/render-descriptive-chart-additions.py` reproduces the SVG slide charts
from the combined notebook's R cells; the local builder runs it before rendering.
`scripts/sync-descriptive-r-references.py` now validates all 20 executable example panels in the combined notebook.

## Combined R introduction — 15 November 2026

The user approved replacing the four introductory R notebooks with the concise
combined `lessons/01-introduction-to-r.qmd`, including two dplyr-to-ggplot2
pipelines. Base R covers programming foundations; dplyr is the main table
manipulation approach; conventional plots precede the ggplot2 introduction.
Prior notebooks are preserved under `archived/2026-11-15-four-part-r-introduction/`.

There are now fourteen canonical notebook/PDF pairs and twelve runnable student
notebooks. Part 1 links only the combined notebook and its PDF. The old three
lesson URLs remain compatibility entry pages, and their old individual PDF URLs
serve identical copies of the combined introduction PDF. Compatibility PDFs
are excluded from the fourteen-document PDF ZIP. `R_INTRODUCTION_ALIASES` in
`scripts/course_documents.py` controls these URLs; build and live verification
check the aliases as well as the canonical resources. Original reference decks
and all Parts 2–3, practicals and extended-case teaching content remain unchanged.

No standalone public Part 1 QMD download is added. The runnable combined
introduction is included in the student Positron workspace. The separate Word
review draft and all instructor drafts remain local-only. This change is
authorized for commit, source push, website publication and live verification.

## Positron folder workspace — 15 November 2026

The user replaced the RStudio workflow with Positron. Open the top-level folder
containing `_quarto.yml` and `data/` through File > Open Folder. The old root
R project file is archived under `archived/2026-11-15-before-positron/`; it is
not shipped in the student project. `.vscode/settings.json` is tracked and
included explicitly in the student ZIP, but excluded from website resources.
Its `quarto.inlineOutput.enabled: false` setting sends interactive Quarto cells
to the R Console, which uses the opened course root. This preserves fixed
`data/...` imports: Positron's per-document inline kernels otherwise start
in the notebook folder. Do not silently enable inline kernels while keeping
root-relative imports. Quarto renders still execute at the project root.

The visible project download is `downloads/applied-statistics-positron.zip`.
The previous `applied-statistics-rstudio.zip` URL serves an identical Positron ZIP
for compatibility only; no active page advertises it. Both URLs are validated
and checked live. The student project retains twelve runnable notebooks; all
fourteen PDFs and the PDF bundle are refreshed. No statistical teaching content
is changed beyond setup instructions and the matching R code comments.
The shared Petra theme remains active.

Workspace behaviour references: [Positron folder workspaces](https://positron.posit.co/rstudio-rproj-file.html)
and [Quarto inline-output working directories](https://positron.posit.co/quarto-inline-output.html#working-directory).

## R introduction content review — 15 November 2026

The combined introduction now includes classical data-frame functions, a fully
explained dplyr pipeline with nested/intermediate/piped equivalence, both original
pipe/layer diagrams, and a more developed Grammar of Graphics explanation.
Keep `pipe_operator.png` and `clipboard-834917176.png` unchanged and include both
in the student ZIP; validation checks their exact bytes against the source assets.

Numerical boxplots/scatter plots use all 32 models in the built-in `mtcars` data
from the original ggplot material, not clipped Superstore Sales/Profit axes. The
notebook explains historical provenance, units, recorded group sizes, medians,
mapping versus setting, and a boxplot/point layer that shows every observation.
The business pipelines still use the unchanged historical Superstore CSV.
No additional CSV or package is required. The R checker verifies the stated
car-data facts and equivalence of the three pipeline forms. Preserve all other
course material and the fourteen-PDF/twelve-notebook download contract.


## Combined Part 2 — 19 November 2026

The user requested combining the two Part 2 resources into one. Preserve every
non-R source-slide passage, approved diagram, Excel example and survey addition.
Move the complete 20 practical sections into their matching lesson positions,
including all original R code/comments, explanations, captions and executed
results. The combined source is `lessons/02-descriptive-statistics.qmd`.

There are fourteen canonical HTML/PDF pairs and twelve runnable student
notebooks. `practicals/descriptive-statistics-r-practical.html` forwards to the
combined lesson with its query/fragment; all former example anchors are retained.
`pdf/descriptive-statistics-r-practical.pdf` is an identical compatibility copy
of `pdf/02-descriptive-statistics.pdf`, excluded from the PDF ZIP. The Part 2
landing page presents one resource. The student ZIP includes the combined source
and its required images, editable diagrams and survey supplement.

The separate unapproved inference redesign/expansion remains local. Build a
release from the committed source, preserving the previously approved Part 3
material rather than deploying unrelated uncommitted review changes.
