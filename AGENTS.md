# Applied Statistics project rules

## Current direction — user decision, 1 November 2026

- The previous course is retired in full under `archived/2026-11-01-retired-course/`.
- Build a fresh, simple PowerPoint-style course based on the user's original
  307102 Descriptive Statistics for Business slides.
- `slides/307102-descriptive-statistics-original.pptx` and its PDF companion are
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

- Part 1: Introduction to R, restored from the archive with its assets and CSV dependencies.
- Part 2: Descriptive Statistics, `02-descriptive-statistics.qmd`.
- Part 3: Inferential Statistics, `03-inferential-statistics.qmd`, authorized and developed from the four original 307102 inferential decks.
- Use Quarto with the shared Petra theme to give the lessons a slide-like sense.
- Preserve the original slide text and images exactly; do not silently correct or rewrite them.
- Convert existing code examples into executable Quarto cells. Original Excel instructions remain unchanged unless the user explicitly authorizes adaptation.
- Record statistical source issues separately under `_instructor/`.
- `assets/petra-brand.css` is the active shared stylesheet; the archived copy is historical.
- `_preview/` contains generated local previews, not a published website.

## Course identity and diagrams — 1 November 2026

- The active course is **307312 Applied Statistics — Masters Level**. The 307102
  identifier is source provenance only, not the current course title.
- The user authorized replacing the inconsistent statistical process, data-types,
  measurement-level, scale-comparison, and variance/SD diagrams with a standard
  Petra theme. Editable replacements live under `content/diagrams/`, with shared
  styles in `assets/source-slides.css`; the converter includes them reproducibly.
- Preserve other original material and executable R cells. The untouched source
  PPTX/PDF remain the reference for the historical diagrams.

## Part 3 sources and conversion

- The four original inferential decks contain 37, 26, 57, and 21 slides (141 total).
- Keep their sequence: probability distributions, estimation, hypothesis testing, regression.
- `scripts/convert-inferential-slides.py` reproducibly converts the source decks and exports selected native slide tables as CSV.
- Added R equivalents are labeled; original Python listings are preserved as source examples.
- Source errors and interpretation issues are documented separately in `_instructor/inferential-source-review.md`. Do not describe uncorrected source claims as validated.

## Publication authorization — 1 November 2026

- The user explicitly requested committing, pushing, and publishing the restarted
  course after Part 3 is complete. Use the root `PUBLISHING.md` and
  `scripts/publish-course.py`, and verify the live website.
