# Descriptive statistics: teaching decisions and source data

## Current decision

Use the main 8th-edition textbook throughout Module 2. Keep the Restaurant example as a recurring context, supported by simpler textbook examples where they explain a particular tool better. Do not use Superstore in the active sequence. The second book is supplementary; its running case is not currently adopted.

The restaurant setting connects variable meaning, ordered quality ratings, prices, grouped summaries, and comparisons. It does not cover all measurement levels: interval scales require a separate clearly defined example such as Celsius temperature. Introducing a short second example is preferable to inventing a variable in the Restaurant dataset.

## Example sequence

| Teaching purpose | Textbook example | Local workbook | Prepared teaching CSV | Verification scope |
|---|---|---|---|---|
| Categorical frequencies, proportions, bar charts | Soft drinks | SoftDrink.xls | data/module02/soft_drinks.csv | 50 records; category totals match after documented label mapping; ordering not asserted |
| Distribution, grouped tables, histograms, center, spread, quartiles, boxplots | Audit duration | Audit.xls | data/module02/audit_times.csv | All 20 printed observations match |
| Variable meaning, ordinal categories, crosstabs, price comparisons | Restaurants | Restaurant.xls | data/module02/restaurant_ratings.csv | 300 records; first 10 printed rows and all 12 crosstab cells match; remaining individual rows not printed |
| Scatterplots and descriptive association | Electronics advertising and sales | Stereo.xls | data/module02/electronics_sales.csv | All 10 printed rows match; sales measured in hundreds of USD |

The introductory lesson currently loads the Restaurant, Audit, and Electronics CSVs. SoftDrink is prepared and checked and is analyzed in Lesson 2; it is not analyzed in the introductory page.

Raw workbook directory, relative to the course root:

`books/1-Modern Business Statistics-Organized-Data/7th-Data - Modern Business Statistics with Microsoft Excel Anderson Sweeney Williams/Chapter 02 Descriptive/`

The local raw-data folder retains an older edition label. We use these selected files because their stated checks against the 8th-edition PDF passed, not because we assume that folder matches every 8th-edition example. Preserve that distinction in explanations.

The source-to-CSV preparation and checks are in `20261/scripts/verify-data.R`; results are in `20261/_instructor/data-checks/dataset-checks.csv`. Never describe aggregate checks as full row-level verification.

## Development sequence

1. Completed: introductory data types, measurement levels, toolbox overview, examples, practice, and instructor answers.
2. Completed: Lesson 2 and practice on categorical tables/charts using SoftDrink, followed by grouped distributions, histograms, and cumulative frequencies using Audit; instructor answers are separate.
3. Completed: Lesson 3, practice, and separate instructor answers on center, variability, type-6 quartiles, IQR fences, boxplots, CV, z-scores, and Restaurant group comparisons.
4. Completed: Lesson 4, practice, and separate instructor answers on Restaurant crosstabs and conditional percentages, Electronics scatterplots/covariance/correlation, units, and interpretation limits.
5. Completed: integrated review across all four checked textbook datasets, with a separate instructor guide.
6. Optional future extension: consider a larger case report only after confirming the required data. Pelican Stores is a promising book case, but its matching local workbook has not been located and verified.

The planned descriptive-statistics module is complete with Lessons 1–4, practice, and an integrated review. A larger new case and exhaustive coverage of every Chapter 2–3 topic are optional extensions, not requirements for this sequence. Module 3 now develops probability and distributions in five lessons with practice and a review; see `probability-distributions-plan.md`.

## Language and teaching data format

Business-case introductions appear in English followed immediately by equivalent Arabic narration with right-to-left layout. Module 2's Restaurant, Audit, Electronics, and SoftDrink introductions follow this pattern. All four selected Module 2 datasets are provided as CSV with a data guide and downloadable ZIP; original XLS files remain provenance sources.

## Histogram interpretation expansion

Lesson 2 now teaches Shape–Center–Spread–Unusual features, tail direction, modality, and sensitivity to bin width. Constructed model-quantile plots are explicitly labeled artificial. At the user's request, the local students worksheet supplies an additional age/height comparison, using a two-column CSV without identifiers; source metadata limits and the export script are documented separately. This is an authorized supplementary teaching example; the main worked sequence remains textbook-based. Lesson 2 practice and instructor answers include interpretation questions.
