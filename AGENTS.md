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
