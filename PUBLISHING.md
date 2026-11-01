# Student publishing policy

The user approved this policy on 2026-10-25. Keep one course sequence and publish
its student materials through the existing GitHub repository.

## Locations and audiences

- Editable course sources: `main`, under `20261/`.
- Generated student website and downloads: `gh-pages`, served from its root by GitHub Pages.
- Course URL: https://msfasha.github.io/307312-Applied-Statistics/
- Student downloads page: https://msfasha.github.io/307312-Applied-Statistics/resources/downloads.html
- Local generated HTML: `20261/_site/`; PDFs: `20261/_output/pdf/`.
- Local publication staging: `20261/_output/publish-site/`.

Generated outputs stay excluded from the source branch. They **must be uploaded
to gh-pages** when publishing. A successful local build or a push to main alone
does not publish the website or update student downloads. Verify the deployed URL.
GitHub's branch selection in the repository UI lets maintainers inspect gh-pages.

## Three required student downloads

1. `downloads/applied-statistics-website.zip`: rendered HTML, assets, and datasets;
   extract it and open `index.html`. Basic reading/navigation work offline; local
   browser security can limit JavaScript search. Download links point to the live site.
2. `downloads/applied-statistics-rstudio-project.zip`: a single project folder with
   `20261.Rproj`, lesson/exercise sources, CSV data, assets, Quarto configuration,
   README, and `setup.R`. Maintainer Python scripts are excluded; ordinary HTML
   rendering must not require Python or LaTeX. It must render without the
   instructor's local files. R, RStudio, Quarto, and package installation are external
   software prerequisites, not applications bundled inside this ZIP.
3. `downloads/applied-statistics-student-pdfs.zip`: student PDFs and linked assets/data.
   Extract it and open `index.pdf`; preserve folders for cross-document links.
   Also serve the same PDF tree under `pdf/` for individual viewing/downloading.

Do not include `_instructor/`, instructor answers, raw measurement workbooks,
local publisher workbooks, textbook PDFs, credentials, caches, or build logs in
student archives. `books/` and `docs/` are local-only reference collections and
must not be presented as folders supplied by a GitHub clone or student ZIP.
Preserve source attribution and the original rights of third-party materials.

## Publish an update

Reduced teaching PDFs and editable PowerPoints for Modules 1 and 2 are served under
`teaching-slides/`, with links beside the extended Quarto lessons. They are included
in all three student downloads so the links also work offline. Their maintained
authoring and R rendering scripts are under `20261/scripts/teaching-slides/`;
generated PDFs/PPTXs and their source/output hash manifest stay in
`20261/_output/teaching-slides/` and are published only to `gh-pages`.

After changing a reduced deck or one of its inputs, rebuild and visually check it
using `scripts/teaching-slides/README.md`. The packager rejects changed source or
output hashes until the checked teaching-material manifest has been refreshed.
The source manifest tracks lesson sources, teaching CSVs, styles, authoring scripts,
and figures. It does not expand the documented textbook data-match scope.

From `20261/`:

```sh
python3 scripts/publish-course.py
```

This builds all PDFs and the full HTML site, checks links and local function
documentation, creates the three downloads, validates the PDF archive against
current exports, and stages the publication. Inspect it before publishing.

Commit source changes on main, then run:

```sh
python3 scripts/publish-course.py --package-only --publish
```

`--package-only` checks that every student HTML/PDF export exists and is newer
than its QMD/Rmd source. It also checks the PDF archive byte-for-byte. It does not
prove freshness after changing shared configuration, styling, data, or rendering
scripts: use the default full build after those changes. It is appropriate directly
after the full build and source commit, when only the commit identity changed.

`--publish` uses an isolated temporary Git checkout to update gh-pages and configure
GitHub Pages to serve that branch. It does not switch the current source checkout.
It requires authenticated Git/gh access with repository administration rights.
Later source pushes do not automatically deploy; the publication command is the
explicit update step. Avoid creating a second hosting workflow without revising
this policy and verifying that the same downloads are published.

## Completion checks

- Confirm all source changes are committed, and verify source/document hashes in
  `publication-manifest.json` at the deployed site.
- Confirm Pages reports a successful build and that the live home/download page loads.
- Download all three live ZIPs; compare their SHA-256 hashes with the manifest.
- Check student archives exclude instructor/local-only material.
- Extract the student project in a separate folder and render it with the supplied
  teaching CSVs, without access to books or instructor files.
- Check individual PDF links, internal site links, ZIP integrity, and archive contents.
- Report the live URL and download links to the user. State any unverified limitation.

To prepare only the student RStudio ZIP for an isolated render check, run
`python3 scripts/publish-course.py --student-project-only` from `20261/`. This
creates `_output/applied-statistics-rstudio-project.zip` without publishing.

## Supplementary book chapters

The student-facing Book chapters page is `resources/book-chapters/index.qmd`.
Maintained supplied text and card data live under `20261/book-chapters/`, with a
separate folder for each book and edition. These user-supplied summaries are distinct
from the local-only publisher files in `books/`. Generated chapter PDFs and PPTXs
live under `_output/book-chapters/` and publish only on `gh-pages`.
Build with the bundled Python and Node runtimes using `scripts/book-chapters/build.py`
and `scripts/book-chapters/build.mjs`. The publishing and PDF packaging scripts copy
these companions into all three student downloads; the publication manifest records
their hashes. Chapter 1's unchanged original attachment remains available as text and
as a PDF preserving the wording and Markdown notation.
