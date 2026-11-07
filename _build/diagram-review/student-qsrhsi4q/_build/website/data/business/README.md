# Business datasets for 307312 Applied Statistics

## Superstore: a fixed retail case

- Source: Tableau Public, [Sample Data](https://public.tableau.com/app/resources/sample-data).
- Direct original workbook: https://public.tableau.com/app/sample-data/sample_-_superstore.xls
- Downloaded: **6 November 2026**. The original is preserved locally under `books/tableau/` and is not published.
- Tableau describes Superstore as a **fictitious company**. It is not independently audited business evidence.
- The downloaded workbook has **10,194 order lines**, with order dates in 2023–2026, plus People and Returns sheets. It differs from older 9,994-row versions used by many tutorials.
- Course selection: **United States**, order dates from **1 January 2023 through 31 December 2025**, inclusive. Canada and 2026 orders are excluded, not relabelled or imputed.
- The fixed extract contains **6,682 product lines**, **3,322 orders** and **782 customer IDs**. Some selected orders ship in January 2026; selection is by order date.
- File: `superstore-lines.csv`. No records are silently removed for high sales or negative profit.
- Currency: recorded dollar amounts in the US sample. No currency conversion or inference about real accounting practices is performed.
- Original worksheet headers are renamed to lower-case course variables; dates become ISO dates. Postal codes retain source text.
- `return_status` is added by checking whether Order ID occurs on the source Returns sheet. It is **Listed return** or **Not listed**. No line-level refund, unit-return quantity or return date is inferred.
- The People sheet is not used. No fictional manager performance inference is added.

| Variables | Meaning and cautions |
|---|---|
| `row_id` | Original line identifier; unique in the extract |
| `order_id` | Order identifier; repeats across product lines |
| `order_date`, `ship_date` | ISO calendar dates; ship date is dispatch, not delivery |
| `ship_mode` | Service label: First Class, Same Day, Second Class, Standard Class |
| `customer_id`, `customer_name` | Fictional customer labels; customers may place repeated orders |
| `segment` | Consumer, Corporate, Home Office |
| `country`, `city`, `state`, `postal_code`, `region` | Recorded geographic labels; postal codes are text |
| `product_id`, `product_name`, `category`, `sub_category` | Product labels and classification |
| `sales`, `profit` | Recorded line dollar amounts; profit can be negative |
| `quantity` | Number of units on the line |
| `discount` | Fractional discount: 0.20 means 20% |
| `return_status` | Membership in the source Returns list; absence is not independent evidence of non-return |

### Order-level analysis

`make_orders()` in `lessons/_includes/course-tools.R` verifies that customer, date,
shipping, region, segment and return fields agree within each order. It then sums
line sales, profit and quantity. Derived fields:

- `line_count`: number of product lines in an order.
- `ship_days`: calendar days from order to dispatch, not transit time.
- `loss_order`: whether total recorded order profit is negative.
- `listed_return`: whether the order is on the Returns list.
- `margin_pct`: 100 × order profit / order sales.

For a category or other group, overall margin is **sum(profit) / sum(sales)**,
not an unweighted average of line percentages. Sales are not assumed to be
undiscounted list prices. Returns are not used to adjust recorded profit.

### Inference limits

The course extract is a complete fixed teaching frame. We deliberately sample
orders from it to demonstrate sampling uncertainty. This supports conclusions
about that frame under the stated sampling design, not about real retail markets.
Models of independent future orders require additional assumptions because
customers, products and time periods repeat. Discount correlations do not prove
causal effects. Historical associations are not forecasts.

## COLA: a randomized display comparison

- File: `cola.csv`; 20 stores, ten per condition.
- Source: publisher `COLA.XLS`, Data sheet, *Basic Business Statistics: Concepts and Applications*, ninth edition, Berenson, Levine and Krehbiel.
- Book context: printed pp. **336–339** (PDF viewer pp. 362–365 in the local copy).
- Twenty stores with similar storewide sales volume were selected. The case describes random assignment of ten stores to normal shelving and ten to end-aisle displays, followed by one week of observation.
- `display`: Normal or End aisle.
- `weekly_cases`: cases of cola sold during that week; not individual cans, dollars or multiple weeks from each store.
- `store_id`: course-added labels N1–N10 and E1–E10, not original store identifiers or matched pairs.
- All 20 numerical observations are preserved; the source's two columns are reshaped into long form.
- Independent-group Welch t analysis is the course default. The book's pooled-variance test assumes equal variances and gives a slightly different interval/p-value.
- Random assignment supports the within-experiment comparison. Random selection of stores from all supermarkets is not established. The textbook scenario is not independently verified field research.
- Profit per case, display cost and displaced sales are absent. Extended Case 3 uses explicitly hypothetical margins and costs for sensitivity analysis; these are not source observations.

## Consumer: income, household size and card charges

- File: `consumer.csv`; 50 records, three variables.
- Source: `Consumer.xls`, first sheet, local *Modern Business Statistics with Microsoft Excel* Anderson/Sweeney/Williams data collection, Chapter 15 Multiple Regression.
- `income_thousands`: recorded household income in thousands of dollars.
- `household_size`: recorded number of household members.
- `card_charges`: recorded credit-card charges, dollars.
- The workbook alone does not establish the income/charge reporting period. The course does not add “annual” to the variable names.
- Related case: Consumer Research, Inc., indexed against *Essentials of Statistics for Business and Economics*, ninth edition, printed pp. 790–791. This is a cross-reference, not a claim that the local collection is that edition. The current CSV is exported directly from the identified local workbook.
- No rows or numerical values are changed. Source headers are renamed for R.
- Authenticity and probability sampling are not independently established. Treat regression inference as conditional on a suitable model and target population, not as causal evidence or verified lending forecasts.

## Extended Business Cases: ninth-edition publisher data

- Source: Berenson, Levine and Krehbiel, *Basic Business Statistics: Concepts and Applications*, ninth edition, and its local publisher workbook collection.
- These are historical case data, not independently authenticated contemporary business measurements.
- All numerical observations are preserved. Headers are standardized for R; the transformations below exclude workbook chart helpers or summary rows.
- Calendar dates and units not established by the source are not invented.
- Student notebooks stay together under `extended-cases/`; source workbooks and instructor solutions are excluded from downloads.

| File | Records and observational unit | Variables and limits |
|---|---|---|
| `extended-herald-calls.csv` | 90 days, SH2 | `day`: source day number; `calls`: telephone calls that day. `Bins` and `Midpoints` chart helpers excluded. |
| `extended-herald-marketing.csv` | 24 months, SH13 | `hours`: telemarketing hours per month; `new_subscriptions`: new monthly subscriptions. No calendar/month identifier; do not join to SH16 by row. |
| `extended-herald-subscriptions.csv` | 24 months, SH16 | `month`: source month index 1–24; `subscriptions`: total home-delivery subscription base, a stock rather than a monthly inflow. |
| `extended-oxford-summary.csv` | One reported case summary, not raw boxes | `n=25`, `sample_mean_g=372.5`, assumed known `population_sd_g=15`, `target_mean_g=368`, `alpha=0.05`. Transcribed from printed p. 302; the separate CEREALS nutrition file is unrelated. |
| `extended-parachute.csv` | 20 tested parachutes; five per supplier | `supplier`: Supplier 1–4; `strength`: original tensile-strength scale, physical force unit unspecified. Only the first five measurement rows in each source supplier column; summary rows excluded. |
| `extended-potato.csv` | 54 process measurements, collected several times daily over 20 days | `solids`: percentage solids; `ph`: acidity; `lower_pressure`, `upper_pressure`: vacuum-line pressures; `cake_thickness`: drum cake thickness; `varidriv_speed`: control setting; `drum_speed`: measured drum speed. Pressure/thickness/speed units and timestamps are unestablished. Temporal dependence may affect regression inference. |
| `extended-harnswell.csv` | 150 rollers; five per source batch, 30 batches | `batch`: source `Day` identifier retained as a subgroup; `diameter`: inches. Engineering limits 0.5072–0.5075 inclusive. Preserve subgroup membership and source order. |

### Case sources and substantive limits

- Springville: Chapters 2, 13 (pp. 536–537) and 16 (pp. 689–690). The files describe different units and are not linked records.
- Oxford: Chapters 7 (p. 232) and 9 (pp. 296–303; reported numerical inputs p. 302). Simulated weights/means are clearly labelled hypothetical. No raw box weights are reconstructed.
- Perfect Parachute: Chapter 11, pp. 388 and 393–399. The one-way case does not combine its 20 measurements with the separate supplier-by-loom experiment.
- Mountain States Potato: Chapter 15, p. 623, and dictionary p. 790. The business goal is solids above 12%; below 12 and at-or-below 12 are different counts. Observational regression does not identify causal setting changes.
- Harnswell: Chapter 18, pp. 752–754. The workbook has **56** above-specification measurements (37.33%), whereas the narrative says **55** (36.67%). We retain workbook values. Initial chart limits flag batch 17; capability should not be claimed for an unstable process. Specification compliance is not process stability.
- BLK uses the existing `cola.csv`, with the same measurements as Part 3. Fixed assumed margins/costs in its independent task are not publisher financial data.

## Reproduction and preservation

- Editable teaching CSVs live only here under the course-root `data/` folder.
- Source workbooks remain unchanged and local-only under `books/`.
- `scripts/prepare-business-data.py` verifies pinned source hashes, runs the R exporter and verifies the CSV hashes. It requires the local source workbooks and maintainer package `readxl`.
- Local-only provenance hashes and source checks are recorded in `instructor/business-data-provenance.json`; these are excluded from student downloads.
- Students need only the CSVs and ordinary R packages listed in the project README.
- `scripts/prepare-extended-data.py` recreates the seven extension CSVs from local publisher workbooks and the documented Oxford inputs, recording source/output hashes under `instructor/extended-cases-provenance.json`.
