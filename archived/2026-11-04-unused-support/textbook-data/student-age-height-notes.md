# Student age and height: supplementary histogram example

This is a user-authorized local teaching example, separate from the main textbook datasets. It is used to discuss histogram shape. Do not identify it as a verified University of Petra survey or assume it describes a real target population.

## Source and preparation

- Source, relative to `20261`: `_instructor/source-data/student-measurements.xlsx`.
- Worksheet: `students` (the other worksheet contains a small country summary and is not used).
- Source workbook MD5: `7e094ba7ee5c900290e64b17b0d15bdf`.
- Export: `data/module02/student_age_height.csv`, reproduced by `scripts/prepare-histogram-student-data.R`.
- 8,239 rows, preserving source order and the values in the `age` and `height` columns only. No names, identifiers, or other columns are exported. The two measurements have no missing or nonfinite values in the local file.
- Recorded ranges: age 18–64; height 135–206. No clipping, removal of extremes, or imputation was performed.

## Metadata limits

The local workbook does not provide a verified population definition, collection method, real-versus-simulated status, or explicit units for these columns. Use the axis wording **recorded units**. Do not assert years or centimeters from numerical plausibility alone. Confirm documentation before using this file for claims about a student population, unit-specific recommendations, or inferential analysis.

## Lesson figures

Age uses two-unit bins from 18 to 66; height uses three-unit bins from 132 to 210. Each plotted variable includes all 8,239 records. Each panel has its own horizontal and vertical scales. Different bin widths and scales mean counts per bin and visual widths cannot be directly compared as if the variables used the same measurement scale.

This CSV is downloadable separately. The main four-dataset textbook ZIP remains unchanged.
