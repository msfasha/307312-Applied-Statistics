# Numerical-measure teaching comparisons

These are illustrative numbers, separate from the checked textbook datasets.

Source: instructor-provided `Part 1 Descriptive Statistics.pptx`, located at `/mnt/mywork/active/3_education/university_courses/307102-Descriptive-Statistics-for-Business/Part 1 - Descriptive Statistics/Part 1 Descriptive Statistics.pptx`.

- Slide 38: dollar values 1, 2, 3, 3, 3, 1, 100. The slide specifies dollar amounts but no business setting. CSV unit USD follows the course's dollar convention.
- Slides 44–45: S1 = 100,200,300; S2 = 200,200,200; S3 = 0,600,0; S4 = -600,600,600; S5 = -2000,2500,100. No units specified, so the course labels them arbitrary units.
- Slides 46–47 motivate absolute and squared deviations. The course clarifies that absolute contributions grow linearly, and that SD remains sensitive to extremes.
- Original course illustration, inspired by the range limitation: A = 0,5,5,5,10; B = 0,0,5,10,10. These values do not appear in the source slides.

`measure_limitations_examples.csv` preserves each listed value, with example, series, observation number, value, unit, and origin columns. It contains 32 rows: 7 dollar amounts, 15 equal-mean values, and 10 equal-range values. Observation numbers identify order within each series, not people or businesses. No values are missing.

All lesson summaries and the dot plot are calculated in R. No source deck or textbook data was modified. This supplementary CSV is downloaded separately from the four-file textbook bundle.
