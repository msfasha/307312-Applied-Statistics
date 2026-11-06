# CEREALS pilot — instructor notes

Historical notes for the shorter pilot. The current expanded activity is
`practicals/practical-02-numerical-business-data.qmd`; see
`instructor/part2-practicals-answers.md` for current tasks and answers.
The former notebook path is retained as an entry page.

This is one practical activity for review before developing the proposed
descriptive and inferential companions. The existing three course lessons,
teaching content is unchanged. The notebook in `practicals/`
is not in the active project render list or the student ZIP allowlist.

## Purpose and boundaries

- Aim for 30–40 minutes: business question, import/inspection, histogram,
  centre, spread, interpretation, short independent task.
- Focus on historical cost per ounce. Source nutrition fields do not establish
  equal serving sizes, so avoid unsupported nutrition rankings.
- All 33 observations and source labels were preserved. CSV values were
  compared cell by cell with CEREALS.xls, sheet Data.
- Do not call the 33 products a random sample of all cereals. The sample-SD
  convention is computational, not evidence of a probability sample.
- The buyer scenario and exercises are adaptations, not claims that an actual
  shop made this decision. Costs are historical, not updated or inflation-adjusted.

## Expected calculations

All cost quantities below are dollars per ounce.

| Quantity | Full list | Cost <= 0.15 subset |
|---|---:|---:|
| Entries | 33 | 14 |
| Mean | 0.1706060606 | 0.1271428571 |
| Median | 0.17 | 0.125 |
| Sample SD | 0.0469001195 | 0.0185756546 |
| Minimum | 0.10 | 0.10 |
| Maximum | 0.27 | 0.15 |

Full-list Q1 = 0.13, Q3 = 0.20 and IQR = 0.07 using R's default type-7
quantiles. Mean/median agreement alone does not prove symmetry or normality.
Do not force a strong skewness claim from this small, cent-rounded dataset.

## Student-task solution

```r
# Find the shared data folder from either the course root or this notebook folder.
data_dir <- if (dir.exists("data")) "data" else file.path("..", "data")
cereals <- read.csv(file.path(data_dir, "practicals/cereals.csv"), stringsAsFactors = FALSE)
lower_cost <- subset(cereals, cost_per_ounce <= 0.15)
data.frame(
  group = c("All products", "Lower-cost shortlist"),
  n = c(nrow(cereals), nrow(lower_cost)),
  mean = c(mean(cereals$cost_per_ounce), mean(lower_cost$cost_per_ounce)),
  median = c(median(cereals$cost_per_ounce), median(lower_cost$cost_per_ounce)),
  sample_sd = c(sd(cereals$cost_per_ounce), sd(lower_cost$cost_per_ounce))
)
```

The threshold selects 14 products. Mean/median are lower and SD is smaller
than in the complete list. This is a selected subset, not evidence that an
intervention reduced prices or that lower-cost products are superior.
Changing histogram bins alters the display, not the observations or their
mean/median/SD. Award credit for explaining the selection and the limits of
the decision, not just copying numbers.

## Preview

Build the local preview from the project root:

```sh
python3 scripts/preview-cereals-pilot.py
```

If Quarto is available only through RStudio on this workstation, its executable
is `/usr/lib/rstudio/resources/app/bin/quarto/bin/quarto`.
The generated HTML is `_build/practicals/practical-01-cereals.html`.
The helper renders the independent project in `practicals/`, uses the notebook folder as the R working directory, and copies its two data downloads into the preview.
It does not render or modify the active course lessons. For editing and
ordinary standalone rendering, the notebook can also be opened directly in
RStudio; that render writes its HTML to `_build/practicals/` as well.
Publishing or adding this practical to course navigation is a later adoption
step, not part of the pilot build.
