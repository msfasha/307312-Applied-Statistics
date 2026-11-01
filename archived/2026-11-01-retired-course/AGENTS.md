# Applied Statistics project rules

These instructions apply throughout this course workspace.

## Professional judgment and continuity

- Act as a professional course-development collaborator: recommend a coherent teaching sequence using statistical correctness, learning objectives, cognitive load, and verified source material.
- Treat the user's exploratory questions as requests for explanation or evaluation, not automatic instructions to replace an established approach. Give a clear recommendation, explain tradeoffs, and respectfully disagree when appropriate.
- Follow explicit user decisions and requests. Change a recommendation when new evidence or a genuine teaching need warrants it; do not defend an earlier choice merely for consistency.
- Distinguish completed work, planned work, checked facts, and unresolved source/data issues. State limitations plainly. Never imply a reviewed example is the only option in a book.
- Preserve one course sequence and consistent terminology. Do not introduce competing tracks or restructure the course in response to a question alone.

## Textbooks and cases

- Main reference: Essentials of Modern Business Statistics with Microsoft Excel, 8th edition (2020).
- Basic Business Statistics: Concepts and Applications, 9th edition, is a supplementary reference. Its cases are candidates, not automatically adopted content.
- Use textbook examples for the active statistics lessons. Superstore is excluded from the current teaching sequence and navigation; retain older material for reference without assigning it.
- For descriptive statistics, retain the Restaurant example for classification and integrated group comparisons; use SoftDrink for categorical frequencies, Audit for distributions and numerical measures, and Electronics/Stereo for two-variable association.
- Keep recurring cases where they aid continuity, but select a suitable example for each concept. Do not force one dataset to illustrate every measurement scale or statistical method.
- Add a larger case such as Pelican Stores only after locating its data and checking alignment with the chosen edition. Do not substitute invented observations or silently change the business setting.
- See `20261/_instructor/descriptive-statistics-plan.md` for the current teaching and data decisions.

## Data provenance and presentation

- Preserve raw book files. Teaching CSVs must be reproducible from the local workbooks, with documented labels, units, and transformations.
- Follow `20261/scripts/verify-data.R` and `_instructor/data-checks/dataset-checks.csv`. A filename or edition folder is not proof of compatibility; document the scope of every match.
- Use R and Quarto for reproducible analyses. Keep student exercises and instructor answers separate.
- Follow `COURSE_STYLE.md` and the shared stylesheet. Use the approved soft palette; charts use purposeful analytical colors. Label conceptual illustrations and attribute book figures.

## Bilingual case introductions and teaching file format

- Use Arabic only for business-case introductions: introduce each business case in English, followed immediately by equivalent Arabic narration before its illustration, data preview, or analysis. Keep definitions, conceptual explanations, diagrams, summaries, and other lesson content in English unless explicitly requested otherwise. Apply this scope to future lessons too.
- Use clear Modern Standard Arabic and preserve the same business question, observational unit, quantities, units, and limitations. Do not add unsupported facts in translation.
- Mark Arabic narration with `lang="ar"` and `dir="rtl"` and the shared `case-narration` class. Keep code, variable names, filenames, and dataset values unchanged unless a separately documented translation is needed.
- Student lessons and exercises read CSV teaching files, not XLS/XLSX. Raw publisher workbooks remain unchanged as provenance sources. Maintain reproducible source-to-CSV conversions and a data dictionary; verify row counts, values, and mappings before use.

- Place summary diagrams after the concepts they summarize; explain measurement levels before showing their overview diagram.

## Workspace organization

- Active course sources belong in `20261/modules/`; use `NN-topic.qmd` with lowercase hyphenated words. Exercises and instructor answers use their corresponding lesson number. Module overview files are `index.qmd`.
- Keep instructor-only sources and original nonpublisher measurement data in `20261/_instructor/`. Render instructor answers with `20261/scripts/render-instructor.sh` into `_instructor/_output/`.
- `20261/assets/petra-brand.css` is the single maintained stylesheet. Keep used images under `assets/branding`, `assets/module01`, or `assets/module02`.
- Syllabi belong under `20261/syllabi/`; setup guidance and reference slides belong under `docs/`. Preserve publisher PDFs and raw workbooks in `books/` under their existing source names.
- Keep legacy drafts and unrelated resources outside the active course; see `docs/maintenance/cleanup-report.md` for recovery. Rebuild `_site/` from active sources; do not restore old exported pages or broad legacy redirect maps.
- Superstore lessons, exercises, and datasets have been retired from the working course. Use checked textbook CSVs for the active R practical exercises.

## Code explanations for students

Add about two concise English comment lines inside each nonempty student-facing R chunk. State its purpose and explain unfamiliar functions and consequential arguments (for example cut boundaries and right=FALSE, percentile type, or percentage denominator). Explain every unfamiliar function at its point of use, including validation helpers such as `stopifnot()` and plotting defaults such as `theme_set()`; a minimum comment count alone does not establish adequate documentation. Explain consequential argument values, units, and assumptions. Use additional short comments when needed for accuracy. Keep chunk options first, leave blank practice scaffolds blank, and preserve existing calculations when documenting code.

## Student distribution and publishing

- Follow `PUBLISHING.md`, the user-approved policy for GitHub Pages and three student downloads (HTML website, complete RStudio project, and PDF bundle).
- Editable sources stay on `main`; generated HTML/PDFs and downloadable ZIPs are published to `gh-pages` at https://msfasha.github.io/307312-Applied-Statistics/.
- A local build or a push to `main` alone is not publication. Rebuild/package/publish with `20261/scripts/publish-course.py`, then verify the live website and downloads.
- Exclude instructor answers, local textbook/publisher files, original measurement workbooks, and build caches/logs from student packages. Identify `books/` and `docs/` as local-only ignored folders.
- Preserve a self-contained student RStudio project with all required lesson sources, CSVs, assets, setup instructions, and rendering scripts. Test it separately without instructor/local-only files.
