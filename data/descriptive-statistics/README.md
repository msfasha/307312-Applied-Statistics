# Original 307102 student example

`students.csv` contains all 8,239 rows from the `students` worksheet in the
original 307102 practical workbook. No observations are invented or corrected.
Only the six columns needed by this preview are exported; names and IDs are omitted.

| Column | Meaning | Unit / labels |
|---|---|---|
| gender | Recorded gender category | Original labels |
| age | Recorded age | years |
| height | Recorded height | cm |
| weight | Recorded weight | kg |
| country | Recorded country category | Original labels, including Other |
| major | Recorded field of study | Original labels |

Units follow the teaching context. The original data-collection provenance has
not been established; these must not be presented as verified records of actual
university students. Category labels, all numeric values, and row order are unchanged.

`scripts/export-original-students.py` reproduces the CSV and verifies every
selected cell after round-trip import. `provenance.json` records the source path,
worksheet, checksum, selected columns, and verification scope. The original
workbook stays unchanged in the neighboring 307102 course folder.

The original country label `Russa` is preserved. R examples use that exact label
when selecting Russian students.
