# Inferential teaching data

All files reproduce observations printed in the original inferential-statistics slides. Original
collection provenance is not established. They are teaching examples, not verified
records from the named businesses or university.

| CSV | Source section / slide | Rows | Variables and units |
|---|---|---:|---|
| paired_scores.csv | Hypothesis testing / 27 | 30 | observation number, score1 and score2 (0–100 points) |
| graduate_salaries.csv | Hypothesis testing / 29 | 30 | observation number, male and female annual salaries; narrative Euro / table dollar-symbol conflict unresolved |
| female_major_salaries.csv | Hypothesis testing / 31 | 30 | observation number, Political Science and Social Science female annual salaries; currency unresolved |
| teaching_methods.csv | Hypothesis testing / 53 | 15 | student number, teaching group A/B/C, test score |
| teaching_gender.csv | Hypothesis testing / 56 | 8 | gender, teaching method, exam score |
| houses.csv | Regression / 14 | 10 | house ID, price (thousands of dollars), size (square feet), bedrooms (count), age (years), location (category code) |

`scripts/convert-inferential-slides.py` regenerates these files from the source
PowerPoint tables. Header labels are simplified, dollar symbols and thousands
separators are removed, and all remaining cell values and row order are retained.
Each export is checked cell by cell after CSV re-import. `provenance.json` records
the source section, slide, table index, row count, and transformation scope.

Proportion and beverage-count examples use the explicit counts printed in the
slides. Summary-data t tests and confidence intervals use printed summary values,
without manufacturing underlying observations. Simulations are labeled as such.
