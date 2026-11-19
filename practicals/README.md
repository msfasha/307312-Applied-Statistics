# Compatibility entry pages

The core R examples are part of the course notebooks:

- Part 2: `lessons/02-descriptive-statistics.qmd`.
- Part 3: `lessons/03-inferential-statistics.qmd`.

This folder only retains small entry pages for older links. The three Superstore
applications live under `extended-cases/superstore/`, with their working CSVs
under `data/business/`. They remain separate business applications, not a second
version of a course part.

`python3 scripts/preview-practicals.py` renders these compatibility pages; the
root build stages them. Use the course root for all interactive R and Quarto
execution. Shared R functions/styles are in `lessons/_includes/course-tools.R`.
