# Inferential source review — 1 November 2026

Part 3 follows the four original 307102 decks (37 + 26 + 57 + 21 = 141 slides).
Current course covers identify 307312 Applied Statistics — Masters Level.
Original text is retained; these observations are not silent edits to the source.

## Probability distributions (3.1)

- Slide 28 substitutes 58 where the second z-score calculation should use 90;
  its final z=+2 and empirical-rule counts correspond to 90.
- Slide 31's Python distribution-fitting example is preserved as an original
  code listing. The executable R counterpart compares only normal, logistic,
  and Cauchy fits. Lowest AIC is relative to those candidates and does not prove
  the true family. No claim about current distfit package capabilities is verified.
- Slide 37's question says score >90, but its worked Excel calculation uses >75.
  The R cell shows both thresholds. A probability near 0.2023 means 20.23%, not
  0.2023%. Table rounding explains small differences for the >75 calculation.
- Normal and Poisson approximations require the relevant distributional assumptions;
  neither salaries nor profits should automatically be assumed normal.

## Estimation (3.2)

- Slide 12's CLT wording confuses the number of repeated samples with the size
  of each sample. Approximate normality of a mean depends on sample size and
  population/dependence conditions; merely drawing more samples does not ensure it.
- Slide 16 is a simulation illustration, not an empirical proof. R uses a fixed
  seed and the same stated normal-population settings; its output will differ
  from the original unseeded Python realization.
- Slides 17 and 19 alternate between known population SD and estimated sample SD.
  The R examples explicitly distinguish z and t calculations.
- Slide 21's n>30 rule is a heuristic. Unknown population SD does not become known
  at that threshold; a t procedure remains appropriate under its assumptions.
- Confidence levels describe long-run coverage, not a probability assigned to
  the fixed parameter after a particular frequentist interval is computed.

## Hypothesis testing (3.3)

- Slides 13 and 20 repeat the simplistic z-versus-t sample-size threshold.
- Slide 21's wording asks to conclude equality; a non-significant test does not
  establish equality. The R cell reports the two-sided test against mu=3.
- Slides 27–28 describe voluntary tutorial participation. A paired difference is
  not, by itself, proof that the tutorial caused improvement. The R equivalent
  uses the stated directional improvement alternative, which can differ from a
  two-sided Excel p-value.
- Salary narrative says Euro, while printed tables use dollar signs. CSVs retain
  the printed amounts without assigning a resolved currency. The source
  collection provenance is not established.
- Slide 31's 1% upper-tail test is retained through Welch's test with an explicitly
  greater alternative and 99% confidence.
- Proportion-test cells use the counts visible in source slides 36 and 38;
  continuity correction is disabled to match the source's approximate z tests.
- Slide 47's chi-square result is approximately 8.42857 (df=2). The small example
  ANOVA and regression datasets are teaching examples, not verified business data.

## Regression (3.4)

- The simple-regression coefficients and R-squared calculated from the printed
  table agree with the source to its displayed rounding.
- Excel Multiple R is nonnegative; it does not generally indicate direction as
  slide 10 suggests. In simple regression, slope/correlation determine direction.
- The residual standard error is not the mean absolute prediction error.
- Source location values 1,2,3 represent categories. The R multiple regression
  treats them as a factor rather than imposing equal-spaced numerical effects.
  Its coefficient structure may therefore differ from the Excel model.
- Small p-values do not establish causal effects or identify the best predictor
  without considering design, units, collinearity, model fit and uncertainty.
- Normality of errors is different from normality of predictors. Diagnostic plots
  can reveal problems but do not prove assumptions.

## Conversion and data checks

Original source files remain unchanged in sources/slides/. Existing PDF exports remain historical companions, without assuming positional
compatibility. Embedded pictures are extracted directly, preserving source crop
and rotation. Composite figure crops come from fresh LibreOffice renders of the
actual PPTX, kept in the ignored instructor render cache. A tiny hidden ink
compatibility object is excluded rather than cropping neighboring text. Native text and tables are read
from PPTX. Source covers are updated to the current identity; text in composite
source diagrams remains inside images. Conversion audits account separately for
native and graphic text runs, including AlternateContent fallbacks.

Six CSVs are generated from the exact native slide tables, with round-trip
cell checks after removing printed dollar symbols/thousands separators. No new
observations are invented. Formula-only examples use source summary statistics.
