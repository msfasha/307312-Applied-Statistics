# Inferential examples: ninth-edition book review

Reviewed 7 November 2026. Decision support only: no active lesson, source deck,
student dataset, download, navigation or publication was changed by this review.

## Decision

Preserve probability distributions → estimation → hypothesis testing → regression.
Keep the successful short introductory examples. Correct mathematical and
interpretation errors wherever the current example is retained. Replace selected
worked examples where the book supplies a clearer design and usable observations.

Recommended first set: FORCE for the unknown-SD confidence interval; COMPTIME
for the paired test; COLA for the pooled independent test; TRAINING for Welch;
OMNI for multiple regression. RENT is a worthwhile but lower-priority improvement
to simple regression. These are proposals for discussion, not adopted changes.

## Evidence and scope

- Book: Berenson, Levine and Krehbiel, *Basic Business Statistics: Concepts and
  Applications*, ninth edition, local scanned PDF.
- Book path: `books/2-Basic business statistics  concepts and applications/9th-Basic business statistics concepts and applications (Berenson, Mark L, Levine, David M. etc.).pdf`.
- Printed pages and PDF viewer pages differ: PDF page = printed page + 26.
- Dataset source: `books/2-Basic business statistics  concepts and applications/Data-9th e/browse/Data_Files/Excel/`.
- Read the earlier local ninth-edition inventory, then independently reread the
  relevant book sections/exercises, imported 21 candidate workbooks and recomputed
  selected tests and regression models in R. This is a targeted review of the
  chapter's example needs, not a new validation of every file on the CD.
- Visually checked the source COMPTIME, RENT and OMNI tables. Examined RENT and
  OMNI residual plots and COMPTIME difference Q-Q plot.
- Generated inspection files and numerical checks are local previews under
  `_build/inferential-example-review/`. All original files were read only.
- Official publisher inclusion establishes edition provenance, not proof that
  observations are authentic field records. Do not advertise invented companies
  or instructional experiments as independently verified real businesses.

## Recommended replacements

| Current section and slides | Book candidate and exact reference | Available observations | Decision and teaching value |
|---|---|---|---|
| 3.2, 24–25: student-weight t interval; surrounding 17–21 distinguish z and t | Example 8.3, electric-insulator breaking force, printed p. 262 / PDF p. 288; `FORCE.xls`, `Data` sheet | 30 force measurements in pounds | Replace the worked unknown-SD interval. Clear manufacturing context and fully worked source. Keep a separately labeled known-population-SD demonstration; never manufacture a known sigma from these 30 measurements. |
| 3.3, 27–28: voluntary tutorial before/after scores | Financial-software benchmark, Table 10.5, printed pp. 356–359 / PDF pp. 382–385; `COMPTIME.xls`, `Data` | Ten projects, each run with the current and new package; seconds | Replace. Each project supplies its own matched comparison. Define difference as current minus new, test whether mean difference is positive, and discuss statistical versus commercially meaningful speed improvement. |
| 3.3, 29–30: male/female graduate salaries, pooled t | BLK retail displays, printed pp. 336–341 / PDF pp. 362–367; Table 10.1 at p. 338; `COLA.XLS`, `Data` | 20 stores, ten per display condition; cases sold in one week | Replace. Source explicitly describes random assignment to displays. Stores were selected for similar sales volume; do not claim a random sample of all supermarkets. Adjacent worksheet rows are not pairs. The book's pooled procedure illustrates the existing equal-variance slot; show the assumption explicitly. |
| 3.3, 31–32: political/social-science graduate salaries, Welch | Exercise 10.13, assembly training, printed p. 346 / PDF p. 372; `training.xls`, `Data` | 42 newly hired employees randomly assigned, 21 per training method; assembly seconds | Replace. Meaningful business outcome, independent groups and noticeably different sample spreads. Source compares both pooled and unequal-variance calculations. Coding: 0 team-based, 1 computer-assisted individual-based. |
| 3.4, 14: four housing predictors on ten observations | OmniPower, printed pp. 542–548 / PDF pp. 568–574; Table 14.1 at p. 543; `OMNI.xls`, `Data` | 34 stores; monthly bars sold, price in cents, monthly promotion budget in dollars | Highest-priority regression replacement. Two numerical predictors explain the multiple-regression idea with 31 residual degrees of freedom. Retain categorical predictors as a brief separate concept if desired. |
| 3.4, 8–13 and housing diagnostics: ten-house price/size example | Exercise 13.7, printed p. 493 / PDF p. 519, continued in exercises 13.18 (p. 498), 13.26 (p. 503), 13.41 (p. 514), 13.55 (p. 520); `rent.xls`, `Data` | 25 apartments in one residential neighbourhood; monthly dollars and square feet | Recommended second priority. Preserves the familiar property-and-size context while supplying more observations and a source exercise sequence. Use the same data through scatterplot, equation, output interpretation and diagnostics. A sample from one neighbourhood does not represent an entire city or current rental market. |

### Confidence-interval continuity

FORCE should replace a worked example rather than expand the lesson into a case
study. Use point estimate → sample SD → standard error → t critical value → margin
of error → interval → interpretation. The book's interval is 95%; a 90% version
would be a clearly labeled course adaptation. Avoid comparing the current
50-student z interval and 20-student t interval as if the changed critical value
alone explained their different widths: n, mean and SD also change.

For a book-based known-SD illustration, the cereal-fill example on printed
pp. 255–258 (PDF pp. 281–284) supplies hypothetical repeated samples of 25 boxes
with stipulated population SD 15 g. It is a model/summary demonstration, not a
raw-data workbook. Its purpose is long-run coverage. Oxford's later hypothesis
test uses different summary inputs; do not merge those samples.

### Preserve the Welch teaching slot deliberately

The current salary exercise uses an upper-tail alternative and alpha 0.01. The
TRAINING source exercise uses a two-sided alternative at alpha 0.05. Replacing
it does not require changing the section order or the test method, but it does
require an explicit decision about the question and significance level.

Preferred: teach the book's two-sided question at 5%, retaining the directional
test already taught with manufacturing output. If retaining the current 1%
upper-tail format, label it as an adaptation: is mean team-based assembly time
greater than individual-based time? With the specified coding, one-sided Welch
p is about 0.02025, so there is insufficient evidence at 1%. Choose direction and
alpha before examining results; never select them to obtain significance.

## Other examples: retain, consolidate or reserve

| Topic/current example | Book alternative | Review decision |
|---|---|---|
| Fair die and coin tosses | Saxon tagged order forms, binomial section pp. 173–177; four orders with stipulated tagging probability 0.10 in the introductory calculation | Retain a brief die/coin warm-up. The car-defect example is already a clear business binomial exercise; no strong reason to replace it. The Saxon probabilities are model inputs, not an observed dataset. |
| Poisson call-centre capacity plus context-free mean-20 calculation | Bank customer arrivals, pp. 183–184 / PDF pp. 209–210; mean three arrivals/minute, find P(X=2) and P(X>2) | Good optional consolidation. Small numbers support a transparent hand calculation and complement rule. No raw arrival workbook is supplied by this example. Keep the call-centre example if preferred, but do not infer staffing adequacy from hourly volume alone. |
| Continuous-uniform delivery and widget examples | Uniform random-number illustration, p. 219 / PDF p. 245 | Retain the existing examples. They are more concrete. Remove the claim that a uniform arrival time makes 10 a.m. especially busy. |
| Exam empirical rule and z-table examples | Website download-time normal model, pp. 200–205; stipulated mean seven seconds, SD two seconds | Existing exam examples are intuitive; correct them in place. Website model is an optional business alternative, not a demonstrated distribution of recorded web timings. |
| CLT and standard-error simulation | Book sampling-distribution discussion, Chapter 7 | Retain executable simulation, but call it an illustration. A nonnormal simulated population would better demonstrate the CLT; retain clear labels for simulation. Repetitions improve Monte Carlo accuracy, not the normality of an individual sample mean. |
| One-sample delivery and production tests | BANK1, Exercise 9.100, p. 328 / PDF p. 354: 15 lunch-hour waits, test mean below five minutes; FORCE, Exercise 9.103, p. 329: mean above 1,500 pounds | Keep the current delivery and production examples after correction. BANK1 is a useful optional lower-tail exercise and gives a non-significant result at 5% despite a sample mean below the target. FORCE can provide continuity from the CI if wanted; it need not replace production automatically. |
| Customer satisfaction: 140/200 against 75% | Other book one-proportion exercises exist, but many use stipulated samples or reported counts | Keep. This is already clear and business-relevant. Explain sampling, a binary response and failure to reject. A new book example is not inherently better. |
| Two treatments: 65/100 versus 50/100 | T.C. Resort, pp. 448–450 / PDF pp. 474–476: 163/227 versus 154/262 likely to return | Optional business replacement. Available as aggregate counts in the book; no verified guest-level workbook identified in this review. It changes the original one-sided efficacy question to a two-sided comparison, and voluntary checkout responses limit generalization. |
| Beverage preference by age chi-square | T.C. Resort reasons for nonreturn, Table 12.9, p. 467 / PDF p. 493; 4×3 table of 187 respondents | Keep current simpler 3×2 table. The larger table adds work and conditions on guests already unlikely to return; it is not clearly better as a first example. |
| Three teaching methods one-way ANOVA | LOCATE, Exercise 11.13, pp. 402–403 / PDF pp. 428–429: 18 stores assigned to three aisle locations; `LOCATE.xls` | Optional business replacement preserving three groups. One-month pet-toy sales in thousands of dollars. Use aisle location alone for the source one-way exercise; the `Data` sheet also has a Height column, which must not become a second adopted factor without its own source justification. |
| Same one-way ANOVA | Perfect Parachute, Chapter 11 and `Parachute.xls` | Already adopted as a separate extended case. Link to that case for practice rather than duplicating the full analysis in core slides. Preserve the one-way/factorial dataset distinction. |
| Teaching method × gender, eight observations | Exercise 11.71 Part II, p. 436 / PDF p. 462; `COMPUTERS2.XLS`, first sheet | Stronger 2×2 replication: 32 downloads, eight per browser/computer combination. Historical Netscape/Internet Explorer and MAC/Dell setting. Reserve as an optional extension: do not silently rename it as current technology or claim the measurements represent today's performance. |

## Independent numerical checks

Values below were recomputed from original worksheet observations, not copied
from the book's output. These calculations support suitability; they do not prove
sampling assumptions or authentic field provenance.

| Candidate | Recomputed result | Teaching implication |
|---|---|---|
| FORCE | n=30, mean 1,723.4 lb, s=89.5508 lb; 95% t CI [1,689.961, 1,756.839] lb; 90% version [1,695.62, 1,751.18] | Raw observations support a transparent worked interval. Do not call mean strength a minimum strength guarantee. |
| COMPTIME | Mean current−new = 0.084 s; paired t=3.1490, df=9, upper-tail p=0.005878; two-sided 95% CI [0.023657, 0.144343] s | Illustrates pairing and effect size. Only ten pairs; two larger positive differences are visible in the Q-Q plot. Inspect differences and describe benchmark conditions; do not claim demonstrated speed gains for every possible workload. |
| COLA | Normal mean=50.3, end-aisle mean=72.0 cases/week; difference=21.7. Two-sided pooled p=0.006975; Welch p=0.007849 | Book pooled calculation reproduces; robustness comparison can be brief. Pooled and Welch are different assumptions applied to the same independent design. |
| TRAINING | Team mean=19.8905 s, SD=4.5767; individual mean=17.5571 s, SD=1.9333; 21 each. Two-sided Welch p=0.04051; 95% difference CI [0.10850, 4.55817] s. Pooled p=0.03747 | Source design is randomized. Different sample spreads make the Welch example meaningful; do not treat a variance pretest as a mandatory gate. |
| RENT | fitted rent=177.1208 + 1.065144×size; R²=0.72260; residual SE=$194.5954; residual df=23 | Clear dollars-per-square-foot slope and residual-SE units. Plots show substantial scatter and large residuals; a non-significant normality test would not validate assumptions. No held-out prediction validation was performed. |
| OMNI | fitted monthly sales=5,837.5208 − 53.21734×price(cents) + 3.613058×promotion(dollars); R²=0.75773; adjusted R²=0.74210; residual df=31 | Interpretable partial slopes. A one-cent price increase corresponds to about 53 fewer fitted monthly bars, holding promotion fixed. Price has only three tested levels and promotion three levels; extrapolation is not justified. |
| LOCATE | One-way F(2,15)=14.10455, p≈0.000358; group means 6.0667, 2.0667, 3.7333 thousand dollars | F test identifies some difference. Tukey comparisons do not establish every pair differs; avoid using ANOVA alone to declare a unique best policy. |
| BANK1 | mean=4.28667 min; lower-tail t=-1.6867, df=14, p=0.05691 | Good illustration of insufficient evidence at 5%. Neither this result nor a CI for the mean guarantees that an individual waits under five minutes. |

OMNI residual plots include sizable errors and are not proof of a perfect model.
The source describes a test-market study but the reviewed introduction does not
establish random assignment of price/promotion. Use model-conditional association
and prediction language unless stronger design evidence is established. Keep
34 stores: do not fabricate the two missing observations at the 99-cent/$600
combination to create a balanced 36-row design.

## Candidates examined but not preferred

- **TEABAGS:** 50 raw weights, mean 5.5014 g, SD 0.1058302 g; 99% t interval
  [5.46129, 5.54151] g; two-sided p=0.9259 against 5.5 g. Useful CI/test continuity,
  but Exercise 8.70 (p. 283) says one hour and Exercise 9.60 (p. 316) says an
  eight-hour shift. Values are stored in sorted order, not verified time order.
  FORCE is the cleaner primary CI source. Failure to reject the nominal mean is
  not proof of label compliance or process capability.
- **BANK1 versus BANK2:** fifteen observations each, but commercial-branch lunch
  hour and residential-branch Friday evening mix branch and time. Good confounding
  discussion, weaker replacement for a first independent experimental comparison.
- **SH10:** fifteen early and fifteen late calls. Source p. 378 explicitly gives
  an independent random-assignment design, followed by a hypothetical paired
  redesign. Excellent design-discussion extension; do not switch between them
  without explicitly changing the design. Longer calls are not themselves verified
  additional subscription sales.
- **SH8:** 46 willingness-to-pay amounts come only from non-subscribers willing
  to consider a discounted trial. Do not call these a random sample of all
  households. Keep outside the first CI demonstration.
- **PERFORM:** employee performance before/after motivational training has the
  same uncontrolled before/after causal limitation as the current tutorial case.
  Replacing one with the other would not solve the problem.
- **TEXTBOOK:** 15 matched title prices, including tax/shipping, Exercise 10.36,
  p. 360; source refers to spring 2001. A good backup paired example with an
  explicit random sample of titles. Historical prices cannot support current
  claims about Amazon or local bookstores. COMPTIME offers a more compact
  worked derivation in the book.
- **WARECOST:** 24 consecutive months of distribution costs, sales and orders;
  worthwhile operations example, but temporal dependence needs attention. In this
  fit the largest Cook's distance is about 0.56. OMNI is the simpler first multiple
  regression choice; high R² alone is not grounds to prefer WARECOST.
- **ADVERTISE:** 22 cities, radio and newspaper expenditure. Viable marketing
  alternative, but OMNI has more observations and the book's main worked sequence.
- **SITE:** fourteen stores with size and annual sales. Book software appendix
  references it, and it is usable, but the small increase from ten observations
  does not justify changing the existing housing context as strongly as RENT does.
- **INVOICE:** 30 daily processing counts and hours; clear operations regression
  but daily ordering and dependence should be considered. Optional alternative to
  RENT rather than an additional compulsory context.
- **PEN:** 30 respondents, five advertisements, summed ratings. The source
  one-way exercise does not by itself justify turning the Gender column into an
  experimental treatment. More levels and rating interpretation add complexity.

## Corrections required regardless of replacement decisions

These are findings for a later scoped edit, not edits already made.

1. Probability 28: substitute 90, not 58, in the upper z-score calculation.
2. Probability 37: choose one score threshold consistently (question says 90,
   solution uses 75); distinguish probability 0.2023 from percentage 20.23%.
3. Uniform arrival graphic: a midpoint mean does not make that time a peak.
4. Continuous distributions: probabilities are integrals over intervals; individual
   densities need not be at most one and point probabilities are zero. The
   discrete mass-function checklist must not be applied unchanged to densities.
5. CLT: distinguish sample size from number of simulation repetitions. A simulation
   is not a proof; dependence and tail behaviour matter.
6. Known population SD versus estimated SD must stay explicit. Sample size above
   30 does not turn an estimated SD into a known population quantity.
7. Estimation 25: fix `3.24 ~ 2` and make the chosen SD rounding, margin and
   endpoints agree; with s=8.3946 the margin is approximately 3.2457.
8. Confidence level is long-run coverage under assumptions, not a post-data
   probability assigned to a fixed parameter.
9. Delivery test: ask for evidence of a difference, not proof of equality.
10. Paired tutorial timing and causal wording need correction if retained.
11. Salary currencies and provenance remain unresolved if retained.
12. In one-way ANOVA, between-group variation is not interaction. A significant
    omnibus test does not identify all differing pairs or the best method.
13. In regression, Multiple R is nonnegative; direction comes from slope or signed
    correlation in a simple model. A small p-value does not establish a good model
    or identify the best predictor.
14. Residual SE estimates error SD; it is not mean absolute prediction error or
    demonstrated out-of-sample accuracy. Preserve response units.
15. Regression 12: `9.3499E-5` is 0.000093499, not 0.00000934.
16. Treat location categories as factors. Do not silently compare the resulting
    R model to an Excel model that uses numerical location codes.
17. A funnel pattern is evidence of nonconstant error variance, not necessarily
    nonlinearity of the conditional mean. Normal errors do not require normal
    predictors. Diagnostics reveal concerns but cannot prove assumptions.

## Implementation boundary for the later discussion

- Make correction-only edits and approved example replacements separately
  reviewable. Keep source decks/PDF unchanged and preserve attribution.
- Preserve original section order, Excel teaching steps where applicable, and
  executable labeled R equivalents. A new dataset requires regenerated outputs,
  figures and Excel instructions matching those observations, not old screenshots.
- Do not replace core slides with the full standalone practicals or extended cases.
- Only after example choices are agreed should a scoped lesson edit, approved CSV
  exports, publication allowlist, student-project packaging and PDF checks follow.
- This review creates no permission to push or publish. The user's latest course
  instruction restricts the Part 1 replacement to a local commit; no publication
  was attempted here.
