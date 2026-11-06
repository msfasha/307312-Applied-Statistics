# Practical datasets

## CEREALS

`cereals.csv` supports `practical-02-numerical-business-data.qmd`. It has 33 cereal product
entries and five fields. All rows, source order, labels and numerical values
are retained from the publisher's CEREALS.xls, sheet `Data`. Only column names
were simplified for R. No observations were simulated or added.

| CSV field | Original column | Interpretation |
|---|---|---|
| product | Product | Original product label |
| cost_per_ounce | Cost (per ounce) | Historical dollars per ounce as reported |
| calories | Calories | Reported calories; serving basis unspecified |
| fiber_g | Fiber (grams) | Reported fibre, grams; serving basis unspecified |
| sugar_g | Sugar (grams) | Reported sugar, grams; serving basis unspecified |

Book source: Berenson, Levine and Krehbiel, *Basic Business Statistics:
Concepts and Applications*, ninth edition, exercise 3.68, pp. 127–128.
The book attributes these data to Consumers Union of U.S., Inc.,
*Consumer Reports*, October 1999, pp. 33–34. That underlying attribution
has not been independently checked against the magazine.

These records do not represent current prices or an established probability
sample of all cereals. The file does not specify a common serving mass for
the nutrition fields. Product labels are preserved as supplied, including
capitalisation and spelling. Zero sugar is an observed value, not a missing
value code. There are no missing cells in this extract.

`cereals-provenance.json` records the source workbook path and SHA-256,
column mapping, conversion, value checks and CSV hash. Original publisher
files were not modified. This is a pilot dataset; it has not been added to
the published student download bundles.

## FUNDS2002

`funds2002.csv` supports categorical analysis in Practical 1 and descriptive
association/group comparisons in Practical 3. It contains 259 historical fund
entries and 13 variables. One row is one listed fund entry; the file does not
contain investor records or repeated annual observations for each fund.

| Course field | Publisher field | Meaning and units |
|---|---|---|
| fund | Fund | Original fund label |
| type | Type | Large-, mid- or small-cap stocks |
| objective | Objective | Growth or Value |
| assets_million_dollars | Assets | Millions of dollars, as reported |
| sales_charge | Fees | Sales charge recorded as Yes/No; not all operating expenses |
| expense_ratio_pct | Expense ratio | Expenses as a percentage of average net assets |
| return_2001_pct | Return 2001 | Twelve-month return in 2001, percent |
| return_3yr_pct | 3Yr-Return | Annualized return 1999–2001, percent |
| return_5yr_pct | 5-Yr-Return | Annualized return 1997–2001, percent |
| turnover | Turnover | Trading activity: very low, low, average, high, very high |
| risk | Risk | Risk-of-loss classification in the same five ordered levels |
| best_quarter_pct | Best Quarter | Best quarterly performance during 1997–2001, percent |
| worst_quarter_pct | Worst Quarter | Worst quarterly performance during 1997–2001, percent |

Source: Berenson, Levine and Krehbiel, *Basic Business Statistics: Concepts and
Applications*, ninth edition. Printed p. 40 defines the five-year period;
p. 75 (TP2.1) and pp. 130–131 (team projects) define variables and comparisons.
PDF viewer pages in the local copy are printed pages plus 26. These page
references are specific to this edition, not the international edition.

All records, fund labels, source order and numerical text values are preserved.
Only headers and surrounding whitespace in `Type` were changed. No observations
were simulated, added or excluded; there are no missing cells. Original
classification labels are retained even where a fund name might suggest a
different objective. Do not infer a correction from its name.

`scripts/prepare-practical-funds.py` reproduces the CSV from the local publisher
text file and verifies each exported cell. `funds2002-provenance.json` records
hashes, mapping and transformations. The publisher workbook was also checked
against the text records during the case review.

The publisher collection is verified as ninth-edition companion material.
Original data-collection and probability-selection methods are not established;
do not claim a representative random sample or current market coverage. Sales
charges are not expense ratios. Differences in returns are percentage-point
differences. The 2001, three-year and five-year return windows overlap. Cross-fund
SD measures differences across funds, not individual-fund volatility through time.

The canonical datasets remain here; generated preview downloads are copies under
`_build/practicals/`. These practicals have not entered the public student bundles.
