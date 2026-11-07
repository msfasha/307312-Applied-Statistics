# Extended Business Cases — release validation

Local checks completed 7 November 2026 before source commit/publication.

| Check | Result |
|---|---|
| Source and output hashes | Core and extension manifests match unchanged local sources and canonical CSVs |
| Supplied ZIP comparison | All adopted numerical observations agree; helper/summary exclusions verified |
| Fresh R sessions | 48 isolated-import/worked-cell checks across twelve notebooks from root and notebook folders passed |
| Publisher-cell equivalence | All core sources plus all six extension measurement workbooks agree cell by cell with approved CSVs |
| Key numerical claims | Instructor reference calculations verify ANOVA, specification counts, batch-17 signal and other results |
| Full Quarto render | Twelve notebooks plus home page, independent practical rendering and staging passed |
| Extracted student project | Full twelve-notebook website render passed outside the maintainer workspace, with no books/instructor files |
| Final layout revisions | Springville table simplified; Springville/Potato final cells rerun from both locations in final extracted ZIP |
| Student site | All local file and fragment links, explicit data allowlist and source/packaged/published data hashes pass |
| Bundles | Exactly twelve PDFs; twelve editable notebooks plus required data/configuration/helpers; instructor/source exclusions pass |
| PDF inspection | Every page of all six new cases and first/interior/final samples of all six core PDFs inspected; final changed layouts rechecked |
| PDF functionality | All PDFs have nonempty text pages; case download links use public URLs; no local file/localhost URI links |
| Browser layout | Desktop extended-case navigation and mobile case layout visually checked, with no horizontal page overflow |

Detailed local logs, page contact sheets and release byte verification live under
`_build/extended-review/` and are excluded from source publication/student bundles.
Instructor notes, answer keys, book/workbook references and source manifests are
excluded from both public website and student packages.

The capability template in Harnswell is intentionally not executed because the
initial data signal instability. Hypothetical Oxford simulation and BLK financial
assumptions are explicitly distinguished from source observations. Source issues
remain documented rather than being described as validated textbook claims.

## Deployment check

After the source push, the authorized publisher writes the committed source
revision to `deployment.json` and pushes generated output to `gh-pages`.
`scripts/verify-live-course.py` waits for that revision, then checks live content
against the local release: home page, twelve notebook pages, twelve PDFs, both
ZIPs and every approved data resource. The resulting evidence is recorded in
`_build/extended-review/live-verification.json` after deployment completes.
