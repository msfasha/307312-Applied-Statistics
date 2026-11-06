# Practical datasets

## CEREALS

`cereals.csv` supports `practical-01-cereals.qmd`. It has 33 cereal product
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
