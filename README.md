# 307312 Applied Statistics

[Open the student course](https://msfasha.github.io/307312-Applied-Statistics/).
The core descriptive and inferential lessons preserve the original slides.
R practicals and six extended business cases apply the concepts separately.

## Course sequence

1. **Introduction to R:** one concise notebook covering Positron setup, base R foundations, dplyr and ggplot2 pipelines.
2. **Descriptive Statistics:** the original slide sequence (82 retained source slides plus the approved line-chart and dot-plot additions), original examples, diagrams, Excel instructions, labeled R equivalents and the approved survey section.
3. **Inferential Statistics:** all 141 original slides in order: probability distributions, estimation, hypothesis testing and regression, with original Excel/Python source examples and labeled R equivalents.

The descriptive R practical and developing inference R practical accompany the core
lessons. Three Superstore applications and six standalone business cases remain
under Extended scenarios. All fifteen approved documents have PDF downloads.

## Work locally

Extract the full student project ZIP from the website and open the extracted folder in Positron using File > Open Folder.
Install `knitr`, `rmarkdown`, `dplyr`, `ggplot2` and `e1071`; MASS is used by the original inference examples. Install Quarto to render notebooks.
Keep the R Console working directory at the project root. The supplied workspace
settings send Quarto cells to that Console; use Preview for rendered results. CSV paths start with `data/`; no path-finding code is needed.

- `.vscode/settings.json`: portable Positron workspace settings, included in the student ZIP.
- `lessons/`: combined R introduction, original core slides and the separate probability section; `_includes/course-tools.R` holds shared aggregation and chart styling.
- `practicals/`: descriptive and developing inferential R companions, plus old URL entry pages.
- `data/r-introduction/`: unchanged historical 2014–2017 Superstore tutorial data.
- `data/business/`: pinned business practical and extended-case data.
- `data/descriptive-statistics/` and `data/inferential-statistics/`: original lesson teaching CSVs.
- `extended-cases/`: six standalone business cases and the three Superstore applications.
- `assets/`: shared Petra burgundy/gray CSS and the tracked theme specification.
- `instructor/`: source reviews, provenance, validation and answer keys; excluded from student exports.
- `sources/slides/`: unchanged original reference decks.
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

The original descriptive lesson uses the previously approved de-identified student
teaching CSV, and the inferential lesson uses observations printed in its source
slides. Include these required CSVs in the website and Positron workspace. Original
workbooks and instructor/source provenance stay excluded. Funds/cereals remain historical.
The pre-revision notebooks are preserved under
`archived/2026-11-06-before-superstore/`. Original decks remain unchanged.
Historical slide converters now write only under `_build/reference-conversions/`;
they do not overwrite the authored active notebooks.

## Verify and publish

- `python3 scripts/check-practicals.py`: worked R cells, isolated imports, source-cell checks and teaching results.
- `quarto render`: full site and independently rendered practicals.
- `python3 scripts/publish-course.py`: fresh HTML, fifteen PDFs, both ZIPs, validation and normal push to gh-pages.
- See [PUBLISHING.md](PUBLISHING.md) for publication and live verification requirements.

The source branch can contain instructor notes; exclusion from the student website
and ZIP does not make the public Git repository private. Keep original instructor
resources and private measurements local-only.

## Shared teaching theme

Use [assets/petra-theme.md](assets/petra-theme.md), synchronized with the portable
`../petra_theme/petra_theme.md`. Keep burgundy heading bands, neutral content surfaces,
centred charts and labelled analytical group colors. No notebook-specific theme overrides.

## Recovery — 7 November 2026

Commit `491f030` replaced the original core lessons during the Superstore rebuild.
The user requested the original slides back while retaining the R practicals and
all six extended cases. Parts 2 and 3 are restored byte-for-byte from `70bf7ee`.
Core lessons must not be rewritten as part of future practical/case changes.
The pre-restoration revision remains on `codex/backup-before-original-course-restore-20261107`.
