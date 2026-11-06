# Part 2 practical companions

Three core activities accompany the existing descriptive-statistics lesson.
They are included in the course website, individual PDF downloads and
student RStudio project. Optional coffee, Medicare, legal-advertising and Consumer
Research activities remain future work.

| Order | Notebook | Focus | Suggested time |
|---|---|---|---|
| 1 | `practical-01-categorical-business-data.qmd` | Mutual-fund categories, charts and percentage denominators | Two 40–50 minute sessions |
| 2 | `practical-02-numerical-business-data.qmd` | Cereal costs, histograms, centre, spread, quartiles, boxplots and outliers | 50–60 minutes |
| 3 | `practical-03-association-and-groups.qmd` | Fund returns, group comparisons, scatterplots and correlation | 60–75 minutes |

Open `Applied-Statistics.Rproj` in RStudio and open a notebook above. Install
`knitr`, `rmarkdown`, `dplyr` and `ggplot2` if needed. Run cells in order; starter
cells marked `eval: false` are for students to complete. Each import cell finds
the canonical `data/` folder from either the course root or notebook folder.

Click **Render** or **Preview** in RStudio, or run
`python3 scripts/preview-practicals.py` from the course root to build all three.
Output: `_build/practicals/`. Shared chart styling is in
`_includes/petra-plots.R`; document styling uses `assets/petra-brand.css`.
Render the main course with Quarto first if local links to lesson previews are
needed under `_build/website/`.

The former `practical-01-cereals.qmd` is a compatibility entry page pointing to
the extended Practical 2. The old preview helper continues to work.

Instructor material:

- `instructor/part2-practicals-source-review.md`: case map, source checks and limitations.
- `instructor/part2-practicals-answers.md`: expected results and assessment guidance.
- `instructor/cereals-pilot-notes.md`: retained notes for the original shorter pilot.

Verify executable examples and independent import paths with
`python3 scripts/check-practicals.py`. The root publishing workflow builds and stages the three approved practicals.
See `PUBLISHING.md` for deployment and student-package checks.
