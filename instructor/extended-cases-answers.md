# Extended Business Cases — instructor answers and marking

Instructor-only. Reference calculations: `Rscript --vanilla instructor/extended-cases-answer-key.R`.
Use `extended-cases-source-review.md` for attribution, source discrepancies and
interpretation limits. Student code should be assessed on its question and
assumptions, not whether a preferred p-value or management recommendation appears.

## 1. Springville Herald

- Daily calls: n=90, mean 51.8444, median 49, SD 17.4291, Q1=40.25,
  Q3=66, IQR=25.75, range 11–94. No 1.5-IQR outliers under base R's boxplot rule.
- Marketing: fitted new subscriptions = -413.8204 + 4.407951 × hours;
  R²≈0.86173; observed hours 704–1498.
- At 1200 hours: fitted 4875.72; mean-response 95% interval
  [4689.30, 5062.14]; individual prediction interval [4005.69, 5745.75].
- At 2000 hours: fitted 8402.08; confidence interval [7687.85, 9116.32];
  prediction interval [7291.98, 9512.19]. This extrapolates beyond observed hours.
- Subscription trend: fitted base = 75095.275 + 1234.451 × month;
  months 25–28 about 105957, 107191, 108425, 109660. Initial-to-final increase
  31048 (41.2176%). Residual lag-one ACF≈0.502; the nominal interval assumptions
  are questionable. Do not grade these as validated production forecasts.
- Missing seasonal/campaign/staffing information and unclear temporal mapping
  limit inference. Distinguish stocks, flows and unrelated source rows.

## 2. Oxford Cereal

- Reported scenario: SE=3 g, Z=1.5, two-sided p=0.1336144;
  mean interval [366.6201, 378.3799] g. Insufficient evidence at 5%.
- Hypothetical 375 g mean: Z=2.3333, p=0.0196307,
  interval [369.1201, 380.8799] g; reject at 5% under the stated model.
- n=100 with sigma=15 gives SE=1.5 g, half the SE at n=25.
- No raw-data histogram, individual defect rate, sample SD or single-row t test
  can be supported. A label weight is not by itself a fully specified individual
  compliance rule. Require collection design, individual weights, timestamps,
  calibration and a defined compliance standard for further investigation.

## 3. BLK Retail Display

- Normal mean 50.3, end-aisle mean 72.0; difference 21.7 cases/store/week.
- Welch: t≈3.0446, df≈15.723, p≈0.00784895,
  CI [6.568701, 36.831299]. Pooled: df=18, p≈0.006975,
  CI [6.7257, 36.6743]. Same sample t statistic here because group sizes match.
- Wilcoxon with continuity correction: W=83, p≈0.01395. General rank/distribution
  comparison; a location-shift interpretation needs additional shape assumptions.
- Hypothetical margins 4/6/8, cost 80: estimated weekly net contributions
  $6.80/$50.20/$93.60; corresponding conditional intervals
  [-53.73,67.33], [-40.59,140.99], [-27.45,214.65].
- Break-even cases 20, 13.3333 and 10. All three intervals cross zero;
  favourable point estimates do not remove financial uncertainty.
- Random assignment is not representative store sampling. Cannibalization,
  margin/cost uncertainty, implementation and future-week effects are unmeasured.

## 4. Perfect Parachute

- Means 19.52, 24.26, 22.84, 21.16; grand mean 21.945.
- Classical ANOVA: between SS=63.2855, within SS=97.504,
  df=3,16; F≈3.461629, p≈0.0413656.
- Largest mean contrast, supplier 2 minus 1: 4.74;
  Tukey 95% interval [0.273143,9.206857], adjusted p≈0.0356281.
  Other Tukey intervals include zero.
- Welch ANOVA F≈3.3206, denominator df≈8.7743, p≈0.07206.
  Sensitivity to method warrants caution; no guarantee about individual minimum
  strength or universal supplier superiority follows from these small groups.
- Request price, engineering requirements, quality consistency and documented
  assignment/testing/loom conditions; do not invent a minimum strength threshold.

## 5. Mountain States Potato

- Mean solids 11.09259%; 49/54=90.7407% below 12;
  50/54=92.5926% at or below 12.
- Pressure correlation≈0.93572; Varidriv/drum speed≈-0.93526.
- Full coefficients: intercept -13.50253; pH 2.94422;
  lower pressure -0.15421; upper pressure -0.10619;
  cake thickness 1.50329; Varidriv 1.79546; drum speed 0.14897.
- Full adjusted R²≈0.4232, AIC≈166.3018; illustrated reduced model
  adjusted R²≈0.2239, AIC≈179.6696. The full model has lower AIC here.
- Largest Cook distances: rows 35≈0.44593 and 28≈0.44230;
  request a source/process check. Retain the full-data result and explicitly
  label any deletion sensitivity analysis; high influence is not proof of error.
- Repeated process records over 20 days and missing timestamps limit error-model
  assessment. AIC/VIF/p-values do not establish process causation or future validity.
- Require feasible controlled trials, day/time IDs and subsequent validation.

## 6. Harnswell Quality

- Diameter counts at .5072/.5073/.5074/.5075/.5076/.5077:
  1/4/18/71/49/7. Above specification 56 (37.3333%), within 94 (62.6667%), below 0.
  Retain and disclose the book narrative's different count of 55.
- Initial grand mean .5075226667; average range .0001833333.
  X-bar LCL=.5074168833, UCL=.5076284500;
  R LCL=0, UCL=.0003875667. Batch 17 mean .5074 is below X-bar LCL;
  its individual minimum .5072 remains within the inclusive specification.
- Excluding batch 17 (retrospective sensitivity only): grand mean .5075268966,
  Rbar=.0001793103; X-bar limits [.5074234345,.5076303586];
  R upper=.0003790621. Does not validate future stability or causal correction.
- Initial diagnostic Cp≈.63436, Cpk≈-.09586, but the process is unstable;
  these are not reliable capability claims and are not printed as student results.
  Cpk is negative because the fitted mean exceeds the upper specification.
- The control chart concerns subgroup statistics; individual engineering limits
  are different. No annual defect forecast follows from the sample proportion.

## Suggested marking: 10 points per assigned case

| Criterion | Points |
|---|---:|
| Correct data, observational unit and method | 2 |
| Reproducible calculations and readable tables/charts | 3 |
| Effect sizes, units and uncertainty interpreted correctly | 2 |
| Business recommendation linked to evidence | 2 |
| Substantive limitation and defensible follow-up | 1 |

Use the relevant sections only when assigning part of Springville. Do not reward
raw software output without interpretation. Alternative defensible conclusions
are acceptable when assumptions, uncertainty and practical constraints are explicit.
