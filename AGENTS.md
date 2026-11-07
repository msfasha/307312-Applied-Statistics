# Applied Statistics project rules

## Current direction — user decision, 1 November 2026

- The previous course is retired in full under `archived/2026-11-01-retired-course/`.
- Build a fresh, simple PowerPoint-style course based on the user's original
  307102 Descriptive Statistics for Business slides.
- `sources/slides/307102-descriptive-statistics-original.pptx` and its PDF companion are
  unchanged reference copies from the neighboring 307102 course.
- Preserve the original slides' teaching sequence and simple format as the basis
  for future work. Do not carry over the retired Quarto structure, textbook
  sequence, case selections, styling, or publishing requirements automatically.
- The Sharpe book has been evaluated as a possible reference; its cases have not
  been adopted for the new course.
- Keep statistical statements accurate. Flag substantive source errors before
  changing the teaching approach. Do not invent case data or claim unverified
  publisher resources are available.
- Keep original reference decks and publisher files unchanged. Put revised decks
  in separate files and preserve source attribution.
- Keep `books/` local-only. Do not publish original student measurement files or
  instructor materials. The current publishing workflow is documented in `PUBLISHING.md`.
- Treat archived instructions and course plans as historical records, not the
  active course specification. Do not restore retired content automatically.

## Accepted structure and conversion — 1 November 2026

- Part 1: Introduction to R, `lessons/01-introduction-to-r.qmd`, condensed from the four expanded R lessons.
- Part 2: Descriptive Statistics, `lessons/02-descriptive-statistics.qmd`.
- Part 3: Inferential Statistics, `lessons/03-inferential-statistics.qmd`, authorized and developed from the four original 307102 inferential decks.
- Use Quarto with the shared Petra theme to give the lessons a slide-like sense.
- Preserve the original slide text and images exactly; do not silently correct or rewrite them.
- Convert existing code examples into executable Quarto cells. Original Excel instructions remain unchanged unless the user explicitly authorizes adaptation.
- Record statistical source issues separately under `instructor/`.
- `assets/petra-brand.css` is the active shared stylesheet; the archived copy is historical.
- `_build/website/` contains generated local previews, not a published website.

## Course identity and diagrams — 1 November 2026

- The active course is **307312 Applied Statistics — Masters Level**. The 307102
  identifier is source provenance only, not the current course title.
- The user authorized replacing the inconsistent statistical process, data-types,
  measurement-level, scale-comparison, and variance/SD diagrams with a standard
  Petra theme. Editable replacements live under `lessons/_includes/diagrams/`, with shared
  styles in `assets/source-slides.css`; the converter includes them reproducibly.
- Preserve other original material and executable R cells. The untouched source
  PPTX/PDF remain the reference for the historical diagrams.

## Part 3 sources and conversion

- The four original inferential decks contain 37, 26, 57, and 21 slides (141 total).
- Keep their sequence: probability distributions, estimation, hypothesis testing, regression.
- `scripts/convert-inferential-slides.py` reproducibly converts the source decks and exports selected native slide tables as CSV.
- Added R equivalents are labeled; original Python listings are preserved as source examples.
- Source errors and interpretation issues are documented separately in `instructor/inferential-source-review.md`. Do not describe uncorrected source claims as validated.

## Publication authorization — 1 November 2026

- The user explicitly requested committing, pushing, and publishing the restarted
  course after Part 3 is complete. Use the root `PUBLISHING.md` and
  `scripts/publish-course.py`, and verify the live website.

## Condensed Part 1 — 1 November 2026

- The user authorized skimming and combining the R introduction into one Quarto notebook beside Parts 2 and 3 in `lessons/`.
- Retain setup, basic R objects/data frames/missing values, essential dplyr, and introductory ggplot2.
- Use the same original student CSV as Part 2 for continuity.
- The expanded R lessons and exercises are preserved under `archived/2026-11-01-r-introduction-expanded/`; do not render or navigate to them in the active course.

## Required student downloads

- Publish a PDF for each of the three lesson notebooks on every deployment.
- Use `scripts/build-student-downloads.py` through the publisher to preserve HTML diagrams and executed results.
- The home page links each PDF plus the complete student RStudio project and PDF bundle.
- Follow `PUBLISHING.md`; a source push alone is not publication. Verify live downloads.

## Workspace organization — 4 November 2026

- User authorized reorganizing the workspace. Active notebooks live in `lessons/`;
  their shared fragments live in `lessons/_includes/`. Keep the root uncluttered.
- Separate pilot activities live in `practicals/`; they are not adopted into the
  published course automatically. All working CSVs belong under `data/`.
- Original decks live in `sources/slides/`; instructor material in `instructor/`.
- Generated website, pilot previews, and slide caches belong under `_build/`.
- Unused textbook data and R images were preserved under
  `archived/2026-11-04-unused-support/`. Empty placeholder folders were removed.
- Keep R execution relative to the project root. Update converters, packaging,
  links, and publishing validation together when moving course files.

## Data paths — 4 November 2026

- Keep the only editable datasets under the course root `data/`.
- R import cells must work both from the course root and from the notebook
  folder (`lessons/` or `practicals/`), including individually executed cells.
- Locate `data_dir` inside every import cell, then use `file.path(data_dir, ...)`.
  Do not rely on YAML working-directory settings for interactive RStudio cells.
- Preserve this convention in the converter R-example JSON sources as well.

## Student-facing case language — 4 November 2026

- Present cases directly through their business context, question and task.
- Keep authoring commentary such as “teaching scenario” or “newly written
  teaching activities” in instructor notes, not student-facing material.
- Retain accurate source attribution, dates, units and substantive data limits.

## Part 2 core practicals — 6 November 2026

- User authorized stages 1–3: source/data review and three separate Part 2
  practical notebooks, followed by commit and push.
- Practical 1 is categorical business data (FUNDS2002); Practical 2 is numerical
  business data (CEREALS); Practical 3 is association/group comparisons
  (FUNDS2002). Editable notebooks live under `practicals/`.
- `practicals/practical-01-cereals.qmd` is now an entry page linking to Practical 2;
  the former shorter pilot is retained in Git history.
- Use the shared Petra chart styling in `practicals/_includes/petra-plots.R`.
- Keep answers and source issues in `instructor/part2-practicals-*.md`; keep
  working CSVs and manifests in `data/practicals/`.
- `scripts/preview-practicals.py` builds the independent practical project;
  `scripts/check-practicals.py` verifies worked R cells, data and both import
  locations. Preserve the existing lesson content and source decks.
- Public adoption/navigation and download integration remain stage 5. The four
  optional extension cases remain future work; do not adopt them automatically.

## Publication of core practicals — 6 November 2026

- The user authorized making all three core practicals available online.
- The home page links their HTML pages and individual PDFs. Both student bundles
  include the approved practicals; preserve instructor/source-file exclusions.
- Root Quarto rendering builds/stages the independent practical project through
  `scripts/preview-practicals.py` and `scripts/stage-practicals.py`.
- `scripts/build-student-downloads.py` exports all six notebooks as PDFs and
  includes the practical CSVs, shared R styling and required scripts in the
  RStudio ZIP. Verify the extracted project and live downloads on deployment.
- Future optional extension cases are still not adopted automatically.

## Practical readability — 6 November 2026

- The user prefers short, slide-like bullet points over continuous explanatory
  paragraphs throughout the three practicals. Separate the observational unit,
  source, period, interpretation and limitations into distinct points.
- Present learning outcomes and multi-part prompts as scannable lists. Preserve
  statistical meaning, source attribution, code cells, tables and task scope.
- Apply this preference to future practicals; preserve original source-slide
  wording in the main lessons unless separately authorized.

## Burgundy and gray teaching theme — 6 November 2026

- The user approved the muted burgundy preview for all authored course headings,
  superseding the previous grayscale and pale pink heading palettes. Use
  `assets/petra-theme.md`; synchronize it with `../petra_theme/petra_theme.md`.
- Use `#763D52` for H2–H4 heading bands with white text and `#542638` for the
  document title panel. Keep diagrams, table fills and note surfaces neutral
  gray with dark labels. Keep heading and content color tokens separate.
  Follow the shared CSS, not per-notebook overrides.
- Our generated charts use neutral defaults; meaningful analytical group and
  ordered-category colors remain appropriate. Preserve labels and consistent mappings.
- Keep source-slide images and R plots centered. Small instructional images use
  at least half the content width; retain aspect ratio and cover artwork sizing.
- Original reference decks, source images and logos retain their colors and attribution.
- Refresh HTML, all six PDFs and both student bundles on publication. Include the
  tracked theme specification in the student RStudio project.

## Superstore business-course revision — 6 November 2026

- The user explicitly authorized new content throughout the material, followed by commit, push and publication. This supersedes preservation of source-slide wording in the active authored lessons; untouched PPTX/PDF reference decks remain unchanged.
- Active Part 1 and Part 2 and all three descriptive practicals use Tableau Superstore. Pin the official 6 November 2026 download and the US orders placed in 2023–2025: 6,682 lines, 3,322 orders, 782 customer IDs. Do not substitute old tutorial versions or silently relabel dates.
- Part 3 preserves probability → estimation → hypothesis testing → regression, with Superstore finite-frame sampling, randomized COLA store displays and observational Consumer credit-card regression. Its independent inference tasks are inside the lesson.
- Only data/business/ enters active publication and student ZIPs. Previous students/funds/cereals/slide extracts remain historical and excluded. Source workbooks remain local-only in books/.
- Current shared R functions and plot style: lessons/_includes/course-tools.R. The practical plot helper is a compatibility wrapper. Preserve per-cell data_dir lookup from both working locations.
- Pre-revision notebooks are preserved under archived/2026-11-06-before-superstore/. Historical slide converters export under _build/reference-conversions/ and must not overwrite authored active lessons.
- Preserve the six-document download contract (three lessons and three descriptive practicals), existing URLs, all PDF exports and both student ZIPs. Follow PUBLISHING.md and verify the extracted project and live downloads.
- Superstore is fictitious. Return status means membership in the source Returns sheet. Treat lines, orders and customers separately; do not infer refund accounting or causal discount effects.
- The COLA source describes random assignment, not random selection of all supermarkets. Use independent groups, report cases/week and distinguish the course Welch analysis from the book's pooled analysis.
- Consumer source reporting periods are not established by the workbook; do not add annual labels. Regression inference remains conditional on model/sampling assumptions.
- The nominal t interval on 200 Superstore orders undercovers in the seeded simulation; retain this diagnostic and coverage comparison rather than claiming validated 95% precision.

## Extended Business Cases — 7 November 2026

- User authorized preparing, committing, pushing and publishing six standalone extended cases from the supplied `Six_Business_Statistics_Quarto_Cases.zip`.
- Keep each case together under `extended-cases/`, linked from the home page and relevant lessons: Springville Herald, Oxford Cereal, BLK Retail Display, Perfect Parachute, Mountain States Potato, Harnswell Quality.
- Preserve the existing core lessons/practicals. Springville has descriptive, regression and optional forecasting sections inside one notebook. BLK is a follow-up to the core COLA example. ANOVA, forecasting and process control include introductions and optional/extension labels.
- Apply the shared Petra theme, brief bullet points, explained executable R, independent briefing tasks and per-import `data_dir` lookup from root or notebook folder. Instructor solutions and source issues remain in `instructor/`.
- Publish all twelve notebook PDFs and include all twelve notebooks in both appropriate student bundles. This extends the six-document minimum; preserve all existing URLs. The approved document list is `scripts/course_documents.py`.
- Only canonical CSVs under `data/business/` enter publication and student ZIPs. BLK reuses `cola.csv`. Reproduce extension exports with `scripts/prepare-extended-data.py`; preserve publisher workbooks unchanged and local-only.
- Oxford has one row of reported summary inputs, not raw box weights; simulations and BLK commercial assumptions must be explicit hypotheticals.
- Harnswell workbook contains 56 above-specification rollers; book narrative says 55. Retain measurements and report the discrepancy. Do not claim capability from unstable initial charts or delete batch 17 automatically.
- `Parachute2.xls` does have raw loom observations on its `Data` sheet, contrary to the supplied draft's summary-only claim. The adopted case analyses the separate one-way dataset only.
- Potato has repeated measurements over 20 days without timestamps/day IDs; regression inference remains conditional. Preserve unestablished unit/period limits, source attribution and the distinction between below 12% and not above 12%.

## Restore original core; retain practicals and six cases — 7 November 2026

- Latest user clarification supersedes the Superstore rewrite of the core lessons:
  use the original slide-based descriptive and inferential lessons from `70bf7ee`.
  Preserve their original text, figures, teaching sequence, Excel instructions,
  collection/survey addition and labeled R equivalents. Keep the burgundy theme.
- Practical R applications stay separate from these core slides. Retain the
  three current practicals and all six recently approved extended business cases.
  Do not replace the core slides with a business narrative or case examples.
- The active publication includes the original lesson teaching CSVs under
  `data/descriptive-statistics/` and `data/inferential-statistics/`, in addition
  to the approved business CSVs. Only explicitly allowed CSVs/guides enter bundles;
  original workbooks and instructor/source provenance remain local-only.
- Preserve all twelve notebook/PDF URLs and both student bundles. The publisher
  checks all 88 descriptive slides and 141 inferential slides before deployment.
- Future practical/case work must preserve the core lessons unless the user
  explicitly authorizes a change to the original slide material.
- A safety copy of the pre-restoration revision is on Git branch
  `codex/backup-before-original-course-restore-20261107`.

## Reviewable median and mean-AD diagrams — 7 November 2026

- The user authorized replacing only the median graphics on slide 39 and the
  mean absolute deviation graphics on slide 46 with original editable diagrams.
- Replacements live in `lessons/_includes/diagrams/39-median.qmd` and
  `46-mean-absolute-deviation.qmd`. Preserve surrounding slide text and all other
  slides, practicals and six business cases. Original images/PPTX/PDF stay untouched.
- Use burgundy to identify the median positions/mean reference line, gray for
  other values and distances, and readable formulas. MAD here means mean absolute
  deviation; distinguish R's `mad()` (median absolute deviation).
- Keep this as a separate reversible commit; the user will review the result
  and may request restoration of the previous graphics.

## Targeted CV/figure review — 7 November 2026

- User requested smaller CV formulas and covariance graphics, a MAD-style
  squared-deviation diagram (slide 47), a larger three-panel skewness image
  (slide 66), and a moderately larger outlier/boxplot illustration (slide 82).
- CV review found source errors: sample CVs for the stated datasets are
  0.5270462767 and 0.0153508624; finance examples give 0.0372684564 and
  0.1326530612 using the stated summaries. Applied corrections are documented
  in `instructor/descriptive-source-review.md`; retain original reference files.
- The user explicitly removed the final Practice Datasets/QR-code slide because
  it belongs to another course. Source slide 88 must not appear in active HTML
  or PDFs; publisher guards 87 retained descriptive slides and 141 inference slides.
- Keep these edits scoped; retain the current Superstore R practicals, all six
  business cases and the approved burgundy theme.

## Replacement Part 1 — 7 November 2026

- User replaced the condensed R introduction with the four supplied 307307 notebooks, numbered 1–4, using shared Petra styles. Originals remain unchanged in the neighboring course.
- Active files: lessons/01-introduction-to-r.qmd, r-02-basic-concepts.qmd, r-03-dplyr.qmd, r-04-ggplot2.qmd. The previous introduction is archived under archived/2026-11-07-replaced-part1/.
- Preserve supplied examples and images; the historical tutorial Superstore CSV is under data/r-introduction/ with original dates and is separate from the practical dataset. Both bundles and PDF exports now cover fifteen notebooks.
- User instructed local commit only, with no push or publication for this change.
