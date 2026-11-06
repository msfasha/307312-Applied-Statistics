# Module 2 teaching datasets (CSV)

Use these UTF-8 CSV files in R/Quarto. Rows contain observations; the first row contains variable names. Files have comma separators, a dot decimal separator, and no exported row-number column. Raw publisher Excel files are retained unchanged in the books folder; students do not need them to run the lessons.

| CSV | Observations | One row represents | Original workbook |
|---|---:|---|---|
| restaurant_ratings.csv | 300 | One restaurant | Restaurant.xls |
| audit_times.csv | 20 | One audit | Audit.xls |
| electronics_sales.csv | 10 | One week | Stereo.xls |
| soft_drinks.csv | 50 | One recorded soft-drink purchase | SoftDrink.xls |

## Variables and units

- **restaurant_ratings.csv**
  - `restaurant_id`: identifier, not a measured quantity. Read or convert to character when classifying variables.
  - `quality_rating`: ordered categories Good < Very Good < Excellent. CSV cannot retain an R factor's ordering; recreate the ordered factor after import.
  - `meal_price_usd`: meal price in US dollars.
- **audit_times.csv**
  - `audit_days`: audit duration, recorded in whole days. Distinguish the recording precision from the underlying elapsed duration.
- **electronics_sales.csv**
  - `week`: observation sequence, 1 to 10.
  - `commercials`: count of advertising commercials that week.
  - `sales_hundreds_usd`: weekly sales in hundreds of US dollars; 50 means USD 5,000.
- **soft_drinks.csv**
  - `brand_original`: original workbook label.
  - `brand_book_label`: documented matching label for the 8th-edition example: Coke Classic → Coca-Cola and Pepsi-Cola → Pepsi; other labels unchanged. These two columns describe the same response, not two independent observations.

## Reading the files

From the `20261` course project:

```r
restaurants <- read.csv("data/module02/restaurant_ratings.csv")
restaurants$restaurant_id <- as.character(restaurants$restaurant_id)
restaurants$quality_rating <- factor(restaurants$quality_rating,
  levels = c("Good", "Very Good", "Excellent"), ordered = TRUE)
audit <- read.csv("data/module02/audit_times.csv")
electronics <- read.csv("data/module02/electronics_sales.csv")
soft_drinks <- read.csv("data/module02/soft_drinks.csv")
```

If downloaded separately, adjust the path to the CSV location.

## Provenance and verification limits

Original workbooks are maintained only in the instructor's local, Git-ignored `books/` collection, not in the student download or GitHub clone. Source paths below document provenance and are not student dependencies.

Source workbooks are in the instructor's local course's `books/1-Modern Business Statistics-Organized-Data/7th-Data - Modern Business Statistics with Microsoft Excel Anderson Sweeney Williams/Chapter 02 Descriptive/` folder. That folder's older edition label is preserved. The selected data were checked against the main 8th-edition PDF:

- Audit: all 20 printed values match (Table 2.4, p.47).
- Restaurant: first 10 printed records and all 12 crosstab cells match (Tables 2.9–2.10, pp.65–66). The remaining individual records are not printed for comparison.
- Electronics: all 10 printed observations match (Table 2.14, p.76); the original workbook is named Stereo.xls.
- SoftDrink: category totals match after the explicit label mapping (Table 2.2, p.38). Observation order is not asserted to match the book.

`20261/scripts/verify-data.R` reproduces these CSVs and source checks. Results are recorded in `20261/_instructor/data-checks/dataset-checks.csv`. These are historical teaching data, not descriptions of today's market.

## Supplementary numerical-measure illustrations

`measure_limitations_examples.csv` contains 32 illustrative observations adapted from the instructor's slides and an explicitly labeled original A/B comparison. See `measure-limitations-source-notes.md` for values, units, and provenance. These are separate from the four checked textbook datasets and their ZIP bundle.
