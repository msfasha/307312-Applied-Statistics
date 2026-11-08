# Inferential Statistics: proposed teaching skeleton

Working design for discussion. This is a topic-level plan, not a new lesson,
fixed slide count, or adoption of the earlier review edition.

## Main title and organising principle

**Part 3: Inferential Statistics — Using Samples to Make Business Decisions**

Retain the familiar four main sections:

1. Probability distributions.
2. Sampling, estimation and confidence intervals.
3. Hypothesis testing.
4. Linear regression.

The original slides supply the topic backbone. Berenson, Levine and Krehbiel,
*Basic Business Statistics: Concepts and Applications*, ninth edition, supplies
selected cases and a reference for the methods. The scope is selected material
from Chapters 5–14, with a short collinearity introduction from Chapter 15.

Within a worked topic, use: question → variable/design → concept → worked result
→ interpretation. Include a short R example when it helps students calculate,
visualise or check that result. Avoid making R syntax the organising principle.

There are 39 core teaching units below, including a six-slide power block, plus the optional two-way ANOVA extension and four separate optional subject sections. A unit may
need more than one slide. The final count should follow readable content rather
than the original 141-slide count.

## 3.1 Probability Distributions

**Purpose:** understand the models behind probability calculations before using
those models for inference. Book alignment: selected Chapter 5 and Chapter 6.

| ID | Main topic / proposed subtitle | What the slides will do | Example and R placement |
|---|---|---|---|
| P1 | Why inferential statistics? / Population, sample, parameter and statistic | Explain what we want to learn and why a sample creates uncertainty. Separate random sampling from random assignment. | Introduce mean product strength and display comparisons briefly; no code needed. |
| P2 | Random variables and probability models / Counts, measurements, mass and density | Define the response and units. Distinguish a discrete probability from a continuous density and interval area. State that a chosen model needs justification. | Calls, defects and measured force. A simple plot may support explanation; no fitting package. |
| P3 | Discrete uniform distribution / Equally likely outcomes | Show individual and combined event probabilities. | Retain the fair die. One short R calculation, optionally demonstrated rather than a separate exercise. |
| P4 | Binomial distribution / Defects in a fixed number of trials | Explain fixed n, two outcomes, constant probability and independence. Distinguish exactly, fewer than and more than. | Retain 80 cars and 2% assumed defect probability. R: dbinom/pbinom and a probability plot. |
| P5 | Poisson distribution / Events in a defined interval | Explain the rate and time unit, exact counts and complement probabilities. Discuss when the model is unsuitable. | Book bank arrivals: three per minute, pp. 183–184. R: dpois/ppois. Stipulated model, not observed bank data. |
| P6 | Continuous uniform distribution / Equal-length intervals | Calculate interval probabilities and the midpoint mean. Explain why the mean is not a peak. | Retain delivery times and widget diameters. A density diagram and one calculation; R need not be another full worked section. |
| P7 | Normal distribution / Centre, spread and the empirical rule | Explain mean/SD, normal shape and approximate 68–95–99.7 percentages. State that not all business variables are normal. | Retain the exam-score illustration with corrected calculations and an explicit normal-model assumption. |
| P8 | Standard scores / Comparing relative positions | Explain standardisation and distinguish a relative score from a normal probability. | Retain Khalid's two exam scores. A brief R check is enough. |
| P9 | Normal probabilities / Left tail, right tail and intervals | Translate a question into a shaded region, z-score and probability. Connect table, Excel and R answers with consistent thresholds. | Retain mean 70, SD 6 and score above 75. R: pnorm; explain rounding and percentages. |

**Optional enrichment:** choosing plausible distributions from data. Keep automatic
fitting outside the required introductory sequence; it does not prove a true
family or replace a process-based model choice.

## 3.2 Sampling, Estimation and Confidence Intervals

**Purpose:** make the sampling basis visible before confidence-interval
calculations. Book alignment: Chapter 7 and selected Chapter 8.

| ID | Main topic / proposed subtitle | What the slides will do | Example and R placement |
|---|---|---|---|
| E1 | Sampling variation / One population, different samples | Show that sample statistics change even when the population stays fixed. Define a sampling distribution. | A clearly labeled simulated population and repeated samples. R produces one reusable visual. |
| E2 | Standard error and the CLT / Individual variation versus variation of means | Separate SD from SE. Explain sample size, independence and the approximate normality of means. | Compare simulated sample means for small and larger n. Simulation is an illustration, not proof. |
| E3 | Point estimation / Estimating mean product strength | Define the population mean and calculate its point estimate from observations. | Introduce FORCE: 30 insulator breaking forces in pounds, Example 8.3, p. 262. R imports the CSV and summarises it. |
| E4 | Confidence intervals / Estimate, uncertainty and repeated-sampling coverage | Explain margin of error, confidence level, tail areas and correct interpretation before the formula is used mechanically. | Continue the strength question. Add a coverage diagram or labeled simulation; not another unrelated case. |
| E5 | Known population SD / A normal confidence interval | Explain the special known-sigma setting and how the normal critical value is used. | Book cereal-fill summary illustration, p. 255: known SD 15 g, n=25, mean 362.3 g. No raw box weights invented. |
| E6 | Unknown population SD / A t confidence interval | Introduce t and degrees of freedom, inspect measurements, calculate and interpret the mean interval. Compare confidence levels on the same data. | Return to FORCE. R: summary, Q-Q plot and t.test confidence interval. Match Excel and hand calculations to the same settings. |
| E7 | Estimating a proportion / Uncertainty in a customer percentage | Add the missing link between a sample percentage and an interval for a population proportion. Explain conditions and the chosen interval method. | Retain 140 satisfied out of 200. Use the same counts again in hypothesis testing. R must implement or clearly label the method actually taught. |
| E8 | Precision and sample size / Planning the information we need | Explain the effects of n, variability and confidence level on precision. Introduce a manageable planning calculation and design limitations. | Hypothetical planning inputs linked to strength measurement, clearly labeled as planning assumptions. R calculates a rounded-up sample size. Distinguish margin-of-error planning here from the power-based test planning in H4a. |

## 3.3 Hypothesis Testing

**Purpose:** turn a question into a defensible comparison, then interpret the
result in its business context. Book alignment: selected Chapters 9–12. Retain
paired before independent tests and categorical tests before ANOVA from our flow.

| ID | Main topic / proposed subtitle | What the slides will do | Example and R placement |
|---|---|---|---|
| H1 | Claims and hypotheses / What is the parameter and the question? | Define null, alternative and direction. Separate a benchmark claim from observed estimates. | Start with the existing delivery-time question. No numerical output yet. |
| H2 | Evidence and decisions / Test statistic, p-value, alpha and errors | Build the testing process once. Explain rejection/failure to reject, Type I/II errors, power and effect size without treating p-values as hypothesis probabilities. | One visual using the delivery question. Avoid numerous disconnected mini-scenarios. |
| H3 | One-sample mean test / Does average delivery time differ from three days? | Work through a two-sided t test, including a non-significant result and its limits. | Retain original n=40, mean 3.4 days and sample variance summaries. Label summary-only inputs; do not fabricate 40 records. R calculates from those summaries. |
| H4 | Directional mean test / Is average strength above a benchmark? | Explain one-sided hypotheses, boundary calculation and choosing direction before looking at results. | Reuse FORCE with the book's 1,500-pound benchmark, Exercise 9.103, p. 329. R: one-sided t.test. Explain that average strength is not an individual guarantee. |
| H4a | Power and study planning / Detecting a specified meaningful effect | Six-slide core block: effect size in business units, Type II error, power, alpha/sample-size/variability trade-offs, power curves and prospective sample-size planning. | Use the book's section 9.8 cereal model (368 g benchmark, true mean 360 g, known SD 15 g). R visualises power and plans n; distinguish planning assumptions from observed results. |
| H5 | Paired comparisons / Two software packages, the same projects | Explain pairing, signed differences and assumptions on those differences. Calculate a paired test and discuss whether the saving matters. | COMPTIME, ten matched projects, pp. 356–359. R: differences, graph and paired t.test. |
| H6 | Independent comparisons / Sales under two display conditions | Explain independent experimental units and the equal-variance pooled method as a specified model. Show the difference and interval. | COLA, 20 stores randomly assigned to two displays, pp. 336–341. R: group plot and pooled test; brief Welch sensitivity check. |
| H7 | Welch's test / Comparing means without equal population variances | Explain the standard error, differing observed spreads and why Welch is useful. Report direction, magnitude and uncertainty. | TRAINING, 42 randomly assigned employees, Exercise 10.13, p. 346. R: group summaries and Welch test. Follow the source two-sided 5% question. |
| H8 | One population proportion / Does satisfaction differ from the claimed rate? | Connect the earlier proportion estimate/interval to testing a benchmark. Explain the null-based standard error. | Reuse 140/200 against 75%. R: score/z calculation with continuity-correction settings stated. |
| H9 | Two population proportions / Do guests report different return intentions? | Compare two independent percentages and distinguish percentage points from relative percentages. | Book hotel counts: 163/227 versus 154/262, pp. 449–450. Aggregate counts only; acknowledge voluntary survey response. R: two-proportion test. |
| H10 | Chi-square independence / Is preference associated with age group? | Build observed and expected tables, the statistic and association interpretation. | Retain the original 3×2 beverage-preference table of 200 customers. R: chisq.test, expected counts and within-group percentages. |
| H11 | One-way ANOVA / Comparing sales across three locations | Introduce between/within variation, assumptions, omnibus inference and appropriate pairwise follow-up. | LOCATE, 18 stores across three aisle locations, Exercise 11.13, pp. 402–403. R: aov and a limited Tukey interpretation. Keep the full Parachute case separate. |
| H12 | Choosing the method / A decision guide from question and design | Consolidate numerical/binary/categorical outcomes, group count, pairing and assumptions. End with brief independent questions. | Use questions drawn from the examples already taught. Students choose a method and justify it before running code. |

**Optional extension after H11:** two-way ANOVA, main effects and interaction.
Use COMPUTERS2 only if we want a worked 2×2 dataset. Its historical browser and
computer labels must remain explicit. This extension should not interrupt the
main one-way-to-test-selection progression.

## 3.4 Linear Regression

**Purpose:** develop one simple model carefully before adding predictors. Book
alignment: selected Chapters 13–14 and a short collinearity concept from Chapter 15.

| ID | Main topic / proposed subtitle | What the slides will do | Example and R placement |
|---|---|---|---|
| R1 | Regression questions / Response, predictor and association | Explain what regression estimates and what it does not establish. Define the business prediction question and units. | RENT, 25 apartments in one neighbourhood, Exercise 13.7, p. 493. |
| R2 | The regression line / Predicted values and residuals | Introduce intercept, slope and least squares using a scatterplot and vertical residuals. | Use the same apartments. R supplies the scatterplot; a small numerical illustration can explain the arithmetic. |
| R3 | Fit the rental model / Interpreting the equation in dollars and square feet | Fit the line and interpret a meaningful change such as another 100 square feet. Explain intercept limits. | R: lm. Include the corresponding Excel input/output orientation. |
| R4 | Model checks / Mean pattern, spread, normality and independence | Introduce assumptions before relying on coefficient tests and intervals. Inspect residuals and discuss design limitations. | Same rental model. R: residual-versus-fitted and Q-Q plots. No claim that passing a diagnostic proves assumptions. |
| R5 | Model fit / R-squared and residual standard error | Explain represented sample variation, error units and limits of in-sample fit. Correct Multiple R and residual-SE interpretations. | Same rental output. Keep a compact, annotated table rather than several unconnected screenshots. |
| R6 | Inference for the slope / Coefficient uncertainty and model evidence | Explain coefficient SE, t test, confidence interval and relationship to the simple-model F test. | Same rental output. R: coefficients, confint and regression ANOVA. No smallest-p-value predictor ranking. |
| R7 | Prediction / Average rent versus one apartment | Distinguish a confidence interval for the mean response from an individual prediction interval. Explain extrapolation and validation. | Predict at 1,200 square feet, within the observed range. R: predict with confidence/prediction intervals. |
| R8 | Multiple regression / Price and promotion together | Explain partial slopes, holding another predictor fixed, model fit and conditional interpretation. | OMNI, 34 stores, pp. 542–548. R: lm with two predictors and one compact diagnostic sequence. Preserve cents versus dollars. |
| R9 | Limits and responsible use / Collinearity, influential values and conclusions | Explain why an apparently strong model can mislead. Briefly introduce VIF and influence, then end with an interpretation checklist. | Continue OMNI rather than introduce a third compulsory regression dataset. Distinguish association, prediction and causality. |

## Additional optional slide sections

The user approved adding these to the design as separate optional material:

| Section | Purpose | Proposed slides | Main book/data anchor |
|---|---|---|---|
| Optional A: Time-Series Forecasting and Index Numbers | Introduce time ordering, trend, seasonality, smoothing, autoregression, forecast evaluation and base-100 comparisons. | 10 | Chapter 16; verified WALMART quarterly revenues and GASOLINE annual prices; existing Springville case as further practice. |
| Optional B: Decision Analysis | Connect payoff tables, decision trees, uncertainty criteria, information value and utility to a transparent decision. | 9 | Chapter 17; verified source product-introduction payoff table; other inputs individually checked before use. |
| Optional C: Quality and Productivity Management | Explain variation, DMAIC, control charts, specifications and capability after stability. | 11 | Chapter 18; existing Harnswell measurements and source cautions. |
| Optional D: Nonparametric Methods | Match independent, paired and blocked designs to Wilcoxon rank-sum, signed-rank, Kruskal–Wallis and Friedman methods; interpret assumptions and rank-based hypotheses. | 8 | Sections 10.4–10.5 and 11.4–11.5; reuse COLA, COMPTIME and LOCATE, plus REAPPR3 for repeated appraisals. |

See [the detailed power and optional-section plan](inferential-power-and-optional-sections.md)
for every proposed slide's title, purpose, example and R placement. These counts
are planning estimates, not a commitment to squeeze content into unreadable slides.

## R and data design across the part

- R follows the explanation; it does not replace the explanation.
- Each major method gets a short worked R example and an interpretation task.
- Keep imports simple and project-root relative, following the current course convention.
- Each worked example identifies the observational unit, variables, units, design,
  question and limits before the output appears.
- Use seven principal raw-data files: FORCE, COMPTIME, COLA, TRAINING, LOCATE,
  RENT and OMNI. Reuse FORCE across estimation/testing, and RENT across the full
  simple-regression sequence.
- Keep the existing satisfaction and beverage counts, book hotel aggregate counts,
  and existing delivery summaries. Identify their different levels of detail.
- Die, car-defect, uniform, normal-score and bank-arrival exercises use stipulated
  probability models; they do not require a fabricated observation dataset.
- Label simulations and hypothetical planning assumptions explicitly.
- Detailed code can sit immediately after the worked explanation or in a linked
  executable companion when it is too long for a comfortable teaching slide.
  The core slide should still show the question, method and interpretation.
- Do not add video to this design.

## Source map completed

The [unit-by-unit source map](inferential-source-map.md) identifies the book
section/page, selected example, available data, planned R activity and source
treatment for every unit and optional slide. Its 84 rows cover the 39 core units
(with H4a expanded into six power slides), four optional modules and two small
optional enrichments. Nonparametric Methods is Optional D.

## Decisions intentionally left open

- Final slide count and exact grouping of explanation/example/output panels.
- Whether longer R code remains in the lesson or moves to a dedicated inferential
  R companion, following the descriptive-statistics arrangement.
- Whether the two-way ANOVA extension receives teaching time or remains optional.
- Detailed visual layouts, wording, code and calculations: write these after the
  topic design is agreed, then verify them against the data and source assumptions.
