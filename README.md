# 307312 Applied Statistics

[Open the student course](https://msfasha.github.io/307312-Applied-Statistics/).

## Course material

1. **Introduction to R:** one notebook covering Positron setup, base R, data frames, dplyr and ggplot2.
2. **Descriptive Statistics:** the original teaching sequence, approved figures/survey additions and 20 executable R examples together.
3. **Probability foundations:** experiments, outcomes, events, random variables and probability distributions, with explained R examples.
4. **Statistical inference and estimation:** populations and samples, sampling distributions, standard error, CLT, estimation, hypothesis testing and regression.

Quarto is the editable teaching source for each part. HTML and PDF are display
versions built from that same source. The course has thirteen canonical documents:
four parts and nine extended applications. Both bundles contain each document once.
Each part page offers a plain `.R` script; the complete course ZIP includes all
four scripts, the thirteen runnable Quarto notebooks and their required data.
Parts 3–4 include all 141 retained teaching positions and the same 36 R examples,
reordered so sampling distributions, SE and CLT precede confidence intervals.

## Work locally

Extract the complete Positron ZIP and open its top-level folder with File > Open
Folder. Keep the R Console at the folder containing `_quarto.yml` and `data/`.
Shared `.vscode/settings.json` sends interactive chunks to that Console.
Install R, Quarto and the R packages listed in the student README; MASS supports
the source distribution-fitting example. Run cells in order, then preview.

- `lessons/`: the four course notebooks and shared Part 2 fragments/R helper.
- `extended-cases/`: the nine separate business applications.
- `data/`: canonical CSVs and guides; only the configured allowlist is published.
- `assets/`: required teaching images and the shared Petra burgundy/gray theme.
- `instructor/`: source reviews, checks and solutions; excluded from student exports.
- `sources/slides/`: untouched original PPTX/PDF references.
- `books/`: unchanged local-only source books/workbooks, ignored by Git.
- `scripts/`: active build, check, packaging, reference conversion and publishing tools.
- `archived/`: historical editable material, outside the active course.
- `_build/`: generated outputs, not editable sources.

Historical reference converters write under `_build/reference-conversions/` and
must not overwrite the active authored notebooks. Retired material is historical,
not an instruction to restore it. Superseded entry pages and duplicate downloads
have been removed; use the current course links.

## Data and interpretation

The R introduction uses its original 2014–2017 tutorial Superstore data. Business
applications use the pinned fictitious US 2023–2025 Superstore extract (6,682
lines, 3,322 orders and 782 customer IDs). Their definitions are separate.

Part 2 uses the supplied de-identified student teaching CSV; its original
collection provenance is not established. Part 3 uses the original printed
teaching data. Keep source units, dates and design limits. Original workbooks,
private measurements and instructor resources remain local-only.

Source issues are documented under `instructor/`; retaining historical wording
does not validate every source interpretation. R implementations explain their
assumptions and distinguish an estimate, a probability and a causal conclusion.

## Build and publish

- `python3 scripts/build-course.py`: check and build all thirteen documents, PDFs and both bundles locally.
- `python3 scripts/publish-course.py`: build and deploy the current committed source.
- `python3 scripts/verify-live-course.py`: verify the release and actual download bytes.
- See [PUBLISHING.md](PUBLISHING.md) for the workflow, exclusions and download policy.

The public source repository can contain course-authored instructor notes; this
does not make it a private store for publisher or personal material.
