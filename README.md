# 307312 Applied Statistics — Masters Level

[Open the student course](https://msfasha.github.io/307312-Applied-Statistics/).
The course was revised on 6 November 2026 around understandable retail and consumer questions.

## Course sequence

1. **Introduction to R:** import Superstore, prepare a category summary and explain a chart.
2. **Descriptive Statistics:** product mix, order sizes, tables, charts, numerical measures and profitability.
3. **Inferential Statistics:** probability and sampling with Superstore, randomized COLA display comparisons, and Consumer regression.

Three published practicals develop Superstore categorical analysis, order-size summaries,
and discount/profit comparisons. Part 3 contains worked inference plus independent
sampling, display-decision and modelling briefings. All six notebooks have PDF downloads.

## Work locally

Extract the full student project ZIP from the website and open `Applied-Statistics.Rproj`.
Install `knitr`, `rmarkdown`, `dplyr` and `ggplot2`. Install Quarto to render notebooks.
Import cells run both from the project root and from `lessons/` or `practicals/`.

- `lessons/`: the three active notebooks; `_includes/course-tools.R` holds shared aggregation and chart styling.
- `practicals/`: three active Superstore practicals and a compatibility entry page.
- `data/business/`: the only datasets used by the current course, plus the student dictionary.
- `assets/`: shared Petra burgundy/gray CSS and the tracked theme specification.
- `instructor/`: source reviews, provenance, validation and answer keys; excluded from student exports.
- `sources/slides/`: unchanged original 307102 reference decks.
- `books/`: unchanged local reference books/workbooks; ignored by Git and never published.
- `scripts/`: validation, rendering and publication tools.
- `_build/`: generated output; not editable sources.
- `archived/`: historical course versions; not active render targets.

## Data and interpretation

Superstore is Tableau's fictitious sample company. We pin its US orders placed in
2023–2025: 6,682 lines, 3,322 orders and 782 customer IDs. COLA has 20 store-week
observations in two randomized conditions. Consumer has 50 household records.
Read [the data guide](data/business/README.md) for units, selections and limits.
Do not substitute a different Superstore version without explicitly reviewing results.

Old students, funds, cereals and inferential slide extracts remain for historical
provenance under data/ and Git. They are not used, staged or packaged for students.
The pre-revision notebooks are preserved under
`archived/2026-11-06-before-superstore/`. Original decks remain unchanged.
Historical slide converters now write only under `_build/reference-conversions/`;
they do not overwrite the authored active notebooks.

## Verify and publish

- `python3 scripts/check-practicals.py`: all six notebooks, isolated imports, source-cell checks and teaching results.
- `quarto render`: full site and independently rendered practicals.
- `python3 scripts/publish-course.py`: fresh HTML, six PDFs, both ZIPs, validation and normal push to gh-pages.
- See [PUBLISHING.md](PUBLISHING.md) for publication and live verification requirements.

The source branch can contain instructor notes; exclusion from the student website
and ZIP does not make the public Git repository private. Keep original instructor
resources and private measurements local-only.

## Shared teaching theme

Use [assets/petra-theme.md](assets/petra-theme.md), synchronized with the portable
`../petra_theme/petra_theme.md`. Keep burgundy heading bands, neutral content surfaces,
centred charts and labelled analytical group colors. No notebook-specific theme overrides.
