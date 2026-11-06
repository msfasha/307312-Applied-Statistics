# Part 2 practical source review

Reviewed 6 November 2026. Stages 1–3 produce three local practical companions;
they do not adopt the optional extension cases or publish the practicals.
Existing lesson text and source decks are unchanged by this work.

## Case map

| Practical | Learning objectives | Data | Book basis |
|---|---|---|---|
| 1 Categorical business data | Nominal/ordinal variables; frequencies; cumulative percentages; categorical charts; joint and conditional percentages | FUNDS2002, 259 rows and 13 variables | Ninth-edition chapter 2, including p. 40 and variable dictionary p. 75 |
| 2 Numerical business data | Histogram; centre/spread; quartiles; boxplot; outlier investigation; descriptive reporting | CEREALS, 33 rows and 5 variables | Exercise 3.68, pp. 127–128 |
| 3 Association and groups | Comparative distributions; percentage-point differences; scatterplots; Pearson correlation; limits of causal interpretation | FUNDS2002 reused | Five-year comparison p. 40; definitions p. 75 and team projects pp. 130–131 |

The main conceptual sequence remains the original Part 2. Practicals provide
applications after the corresponding methods. Each has one business question,
explained R, interpretation and an independent briefing. Guidance decreases
across the three. No inferential test or population conclusion is added here.

## Edition and source evidence

Source PDF: `books/2-Basic business statistics  concepts and applications/9th-Basic business statistics concepts and applications (Berenson, Mark L, Levine, David M. etc.).pdf`.
The local publisher CD identifies the ninth edition. In this PDF, body-page
viewer numbers equal printed pages plus 26. The international-edition page
references in the supplied practical/report are not automatically transferable.
The selected pages and their text were reviewed; pp. 75, 127 and 128 were also
visually inspected. The supplied draft is a source for activity design, not an
instruction to reorganize the course around the textbook.

Book statements verified:

- Printed p. 40: 259 funds, including 158 Growth and 101 Value; five-year annualized
  returns cover 1 January 1997 through 31 December 2001.
- Printed p. 75: Fees means sales charges; assets are in millions of dollars;
  risk and turnover have five ordered categories; the three-year period is
  1999–2001 and quarterly extremes refer to 1997–2001.
- Printed p. 130: expense ratio is a percentage of average net assets.
- Printed p. 127, exercise 3.68: cereal cost is **dollars per ounce**; the source
  citation is Consumer Reports, October 1999, pp. 33–34. A common serving mass
  for nutrition fields is not established by the local file.

## Data checks and transformations

FUNDS2002 publisher XLS (`Data` sheet) and tab-separated text were compared cell
by cell: all 3,367 observation cells agree numerically/textually after surrounding
text whitespace is ignored. Headers and 259-row/13-column shape also agree.
The supplied practical's TXT matches both local publisher TXT copies by parsed
records. `scripts/prepare-practical-funds.py` produces the course CSV and its
SHA-256 manifest reproducibly. Numeric strings and fund labels are retained;
only headers and surrounding `Type` whitespace change. There are no missing
cells or duplicate fund labels. All classifications are retained, even if a
fund's name suggests a different objective.

CEREALS: all 165 observation cells were rechecked against the publisher workbook.
The existing CSV, values, labels and provenance manifest are unchanged. It has
33 records and no missing cells. Its original source workbook hash and current
CSV hash are recorded in `data/practicals/cereals-provenance.json`.

## Source issues and interpretation limits

1. **Cereal unit inconsistency in book:** exercise 3.68 begins with dollars per
   ounce on p. 127 but part (f) says cents on p. 128. The practical follows the
   explicit starting definition and unchanged 0.10–0.27 values, in dollars per
   ounce. No 100-fold conversion is silently applied. Nutritional rankings are
   avoided because serving equivalence is unverified.
2. **Fund origins:** publisher-file provenance is established; underlying
   collection method and probability-selection design are not. Do not call the
   list a random or representative sample, or its observations independently
   authenticated company data. Historical performance is not a forecast.
3. **Charge semantics:** `Fees` is renamed `sales_charge` to preserve the book's
   definition. No-charge funds may still have operating expenses. The expense
   ratio is a separate numerical variable, not a cost-free/paid indicator.
4. **Return periods:** returns are percentages, annualized where specified;
   differences are percentage points. The 2001, three-year and five-year windows
   overlap, so correlations between them are not independent-period persistence
   evidence. No net/gross-return convention is inferred beyond the source.
5. **Spread and design:** SD across fund returns is not individual-fund time-series
   volatility. Common markets/holdings may induce dependence. Groups are not
   randomized; neither expense correlations nor group differences identify causes.
6. **Summaries:** each fund receives equal weight; these are not asset-weighted
   portfolio returns. Boxplot hinges can differ from explicitly calculated type-7
   quartiles; outlier flags are not deletion rules.
7. **Ordered categories:** cumulative percentages use the stated risk/turnover
   ordering; no equal numerical spacing or nominal cumulative interpretation is
   imposed. Capitalization types are compared as categories without averaging.

These checks establish the chosen definitions and reproducible calculations,
not validation of every source claim or every book exercise.

## Teaching and release boundaries

Use Petra document styling and the shared `practicals/_includes/petra-plots.R`
palette. Keep the working CSVs under root `data/practicals/`; each import cell
must run from either root or `practicals/`. Instructor answers remain separate
and are excluded from preview downloads. Student starter chunks do not execute
until completed. `scripts/check-practicals.py` checks worked code, key results,
file hashes and isolated imports; Quarto builds the student HTML separately.

The old cereals notebook path remains an entry page. Its previous shorter
activity is preserved in Git commit `a49dd2f`; the extended editable source is
Practical 2. No duplicate editable CSV is introduced. Preview copies live under
`_build/`. No optional coffee, Medicare, legal-advertising or Consumer Research
activity is adopted. Integration into navigation, PDFs and public student ZIPs
belongs to the later publishing stage.

## Validation completed

- All worked R cells execute from both the course root and notebook directory.
  Each of the three import cells also executes in isolation from both locations:
  12 fresh-session execution checks in total.
- Canonical CSV hashes, fund source-cell equivalence and key counts, summaries,
  subgroup correlations and student-task results passed the maintainer checker.
- All three practicals render with no R warnings/errors; local CSV, data-note,
  lesson and cross-practical links resolve. No selected instructor answer section
  is embedded in the student HTML.
- Browser previews and all 12 charts were visually reviewed for Petra colors,
  legible labels, legends and layout.
- The three existing course lessons render successfully. The main website build
  excludes the practical notebooks, their data, books, source decks and instructor
  material. No publication was performed for this stages 1–3 work.
