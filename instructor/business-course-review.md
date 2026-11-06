# Business-course revision review — 6 November 2026

## Authorization and scope

The user authorized a whole-material rewrite around Superstore plus COLA and Consumer,
including commit, push and publication. Active source-slide wording preservation was
superseded for authored lessons. Original decks and publisher workbooks are unchanged.
The three former lessons and practicals are preserved in the dated archive.

## Course design

- Part 1: basic R, missing values, data frames, dplyr and ggplot2 with one retail question.
- Part 2: foundations/types, tables/charts, centre/spread, association, shape/percentiles/outliers; uses one retail dataset and progressively clearer business interpretation.
- Part 3: probability distributions, sampling/estimation, tests and regression; preserves the established four-topic sequence while replacing disconnected examples.
- Three practicals retain their URLs and scope: categorical summaries; numerical summaries; association/groups. Each has explained worked cells, executed results, charts and independent business tasks.
- Inference tasks are within Part 3. The six-document PDF and student-package contract remains intact.

## Source review

### Superstore

Official workbook obtained directly from Tableau Public on 6 November 2026.
It contains 10,194 order lines and Orders, People and Returns sheets. This version
covers 2023–2026 and includes Canada as well as the US; it is not the often-cited
9,994-line historical version. We pin US order dates in 2023–2025 (6,682 lines,
3,322 orders, 782 customer IDs). This uses complete fictional order years and avoids
combining countries/currency assumptions. Some selected orders dispatch in 2026.

Source issue: one excluded Canadian order ID has multiple customer IDs. We do not
repair it or claim the complete source workbook is universally clean. Postal codes
include Canadian alphanumeric strings in the full workbook, so preparation preserves
text instead of applying a US-only numeric coercion. The selected US frame has
consistent order attributes and no missing cells.

Return labels are derived only from Returns-sheet membership, preserving source
absence as Not listed. No refund/return accounting, return date or returned-unit
count is fabricated. Line/order totals reconcile. No extreme or negative-profit
record is removed from the main results. No causal discount claim is made.

### COLA

Reviewed the local ninth-edition PDF, printed pp. 336–339 (viewer 362–365).
Page 336 explicitly describes selecting 20 similar-volume stores and randomly
assigning ten to each display condition. Page 338 defines independent store samples
and the units as weekly cases. The publisher table has 10 observations in each
column. Every numeric observation is preserved when reshaped into long form.
Added store IDs are explicitly labelled as course identifiers, not source data.

Welch's independent two-sample analysis: mean difference end aisle minus normal
21.7 cases, approximate CI [6.568701, 36.831299], p ≈ .00784895. The source uses
pooled variance, so its p ≈ .0070 and interval differ. The course states the change
rather than silently claiming source agreement. Random assignment supports the
experimental contrast, not representative sampling of all stores or proof of net
profitability. One-week results do not establish long-term effects.

### Consumer

The selected local Modern Business Statistics collection workbook has 50 records
and income, household-size and charge columns. All 150 source numbers are preserved.
The existing Anderson Essentials index links a related Consumer Research case to
ninth-edition pp. 790–791; this is identified as a related cross-reference rather than
misstating the edition of the local workbook. This turn's external book-library mount
was unavailable during attempted page reinspection; no new page-level validation is
claimed. The reporting period is absent from the source workbook, so the course
uses card_charges, not annual_card_charges. Authentic field origins and random
selection remain unverified. Regression t/F inference is conditional on assumptions.

## Statistical checks and limits

- The uniform random selection experiment gives exact finite-frame probabilities.
- Without-replacement return counts use hypergeometric probabilities; binomial
  future-order examples are explicitly assumption-based.
- Poisson rate 3/hour and the 50-case planning benchmark are labelled illustrative
  assumptions, not source observations. No Superstore order times are fabricated.
- Approximate finite-frame t mean intervals use s/sqrt(n) × sqrt(1-n/N).
- The seeded 200-order coverage diagnostic is about 88%, not 95%, because rare large
  orders make the approximation unreliable. The lesson calls this out as a diagnostic
  counterexample, adds larger-sample comparisons, and gives the known full-frame mean
  as the descriptive answer. Do not claim validated nominal precision for n=200.
- Return proportions include a score approximation and an exact finite-frame interval
  by hypergeometric-tail inversion. The finite target and discrete conservatism are explicit.
- Sparse segment/return contingency counts use Fisher's exact test; Pearson's
  chi-square is selected only when all expected counts are at least five.
- P-values are never described as posterior probabilities of a null hypothesis.
- Confidence and prediction intervals, association and causation, SD and SE, sample
  versus frame SD, and dispatch versus delivery are distinguished.
- Shared plot styling remains Petra neutral with labelled analytical group colors.

## Release checks

See the accompanying validation record for executed checks, PDF review and live
publication evidence. The publisher now validates authored content rather than
requiring the retired 141-slide ID count. Student exports include current data only.
