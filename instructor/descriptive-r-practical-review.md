# Descriptive R practical reorganization — 7 November 2026

- All 18 original `r-slide-*` cells were extracted verbatim from the active descriptive lesson. Full cell text, labels, code and comments were compared against a pre-edit snapshot and match exactly.
- Source slides: 16, 17, 18, 19, 23, 24, 26, 28, 33, 42, 50, 55, 63, 68, 72, 74, 76 and 79. The order is unchanged.
- Added context covers purpose, observational unit, units, interpretation, sample formulas, Excel percentile conventions, country-label spelling and the distinction between mean and median absolute deviation.
- The student CSV and source-data limitations are unchanged. Code uses base R; notebook rendering uses knitr/rmarkdown.
- All other descriptive lesson material remains unchanged apart from a link to the companion practical; original Excel instructions remain in the slide lesson.
- The three Superstore analyses moved to extended-cases/superstore/; path resolution and relative links changed for the deeper folder. A pre-existing inaccurate final link description claiming Part 3 taught COLA/Consumer was changed to the actual original Part 3 topics.
- Original slide decks/PDFs, the inferential lesson, datasets and six numbered extended cases were not modified.
- Local commit only; no push or publication is authorized for this revision.

## Local checks

- 44 fresh-session execution checks passed, including isolated import cells and complete worked examples from the root and notebook directories. Pinned datasets, local workbook cells and key reference calculations passed the existing checks.
- Full maintainer Quarto render succeeded. Student-site navigation, all sixteen PDFs, both bundles and data exclusions passed validation.
- The practical PDF has thirteen A4 pages. All pages were visually reviewed in a contact sheet, with representative pages inspected at larger size.
- All non-R descriptive slide content was compared against the preceding committed lesson and is identical, apart from the added companion-practical link.
- A freshly extracted final student ZIP rendered all sixteen notebooks successfully. Page, CSV and fragment navigation passed independently; no source QMDs leaked into the generated student site.
