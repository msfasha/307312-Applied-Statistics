# Power and optional business-statistics sections

Added to the proposed design at the user's request. These are slide-by-slide
plans, not completed slide files or changes to the adopted course. The four core
sections retain their order. Power becomes a core teaching block; the four
additional subject areas remain separately marked optional.

## Core addition: Power and Study Planning

**Place:** section 3.3, after the first one-sample two-sided/directional tests and
before paired comparisons. Reuse the established testing concepts and connect
back to sample-size planning in estimation.

**Main title:** Power and Study Planning.
**Subtitle:** Detecting a meaningful effect with an appropriate sample.
**Reference:** ninth-edition section 9.8, *The Power of a Test*, supplied locally
as `Data-9th e/browse/CDROM_Topics/section9_8.pdf`, printed CD9-1 onward. This is
actual available supplement content, not an assumed publisher download.

| Slide | Title / subtitle | Purpose and planned content | Example / R |
|---|---|---|---|
| PW1 | Why might a test miss an effect? / Type II error and power | Revisit failure to reject. Define power as P(reject H0 given a specified alternative) and beta as its complement. Power is a property of a test/design at an assumed effect, not the probability that the alternative is true. | Revisit a small-sample/non-significant result without calculating retrospective observed power. |
| PW2 | Specify the effect worth detecting / Business units before standardised effects | Distinguish the null value, a scientifically/business-relevant alternative and observed sample difference. Explain why power depends on the specified effect. | Book cereal example: null boundary 368 g, alternative true mean 360 g, stipulated known SD 15 g. The 8 g difference is the source scenario, not an independently approved commercial tolerance. |
| PW3 | Visualise power / One rejection rule, two sampling distributions | Plot the mean distribution at the null boundary and at the specified alternative. Identify alpha, beta and power using the same critical cutoff. | Book lower-tail z test; n=25 and alpha=.05. R draws model distributions and shaded regions. No raw box weights are invented. |
| PW4 | What changes power? / Effect, sample size, alpha, variability and direction | Larger effect, larger n, higher alpha and lower SD improve power for a fixed suitable test. Explain the false-positive trade-off and why one-sided direction must be chosen in advance. | Compare a small table and power curves for n=10,25,50 and alpha=.05/.01. R calculates model probabilities. |
| PW5 | Plan sample size for a target power / Detecting the stated effect | Choose effect, SD, alpha, direction and target power before collecting observations. Round n up. Distinguish a precision-based CI plan from a power-based test plan. Allow for clustering, missingness, cost and uncertainty in planning SD where applicable. | In the source normal known-SD model, target 80% power for the 8 g reduction. R solves the normal planning formula and checks the resulting power. |
| PW6 | Interpret the plan / Assumptions and an independent task | Summarise what a power calculation can and cannot promise. Give a changed-effect or changed-alpha planning task. Explain why observed p-values and retrospective observed power are not a useful replacement for effect estimates and intervals. | Students vary one input, predict the consequence, then verify it in R. Brief optional pointer to power.t.test for future unknown-SD planning; do not use a t procedure while labeling the result as the book's z calculation. |

### Checked illustrative values

The book's model tests H0: mu >= 368 against Ha: mu < 368, with known SD 15 g,
independent normal sample means and true alternative mean 360 g. The cutoff is
368 + qnorm(alpha) * 15 / sqrt(n). Values below use unrounded critical values.

| n | Power at alpha=.05 | Power at alpha=.01 |
|---|---|---|
| 10 | 0.51663 | 0.26115 |
| 25 | 0.84657 | 0.63319 |
| 50 | 0.98326 | 0.92576 |

For target 80% power, the known-SD lower-tail normal planning formula gives
22 boxes at alpha=.05, versus 36 at alpha=.01, rounded up. These are conditional
planning results, not a recommendation that those sample sizes suit every
production process. Actual achieved power is at least the target under the stated
model after rounding; it need not equal exactly 80%.

## Optional A: Time-Series Forecasting and Index Numbers

**Purpose:** extend regression to observations whose time order matters and
introduce consistent comparisons across periods. **Book:** selected Chapter 16.
**Suggested length:** 10 slides, with longer R walkthroughs kept separate if needed.

**Main example:** original `WALMART.XLS`, Data sheet: 36 fiscal-quarter revenues,
1994–2002, in millions of dollars, verified against Table 16.4, p. 671. Preserve
fiscal-quarter meaning; the book notes that its fourth fiscal quarter ends in
January. These are historical instructional data, not current company results.

**Index example:** original `GASOLINE.XLS`, Data sheet: 23 annual gasoline prices,
1980–2002, and the 1980-base index. Table 16.5, p. 679. Calendar years and nominal
prices must remain as supplied. The existing 24-month Springville series can be
cross-referenced for practice, but is short for assessing annual seasonality.

| Slide | Title / subtitle | What it will do | R / example |
|---|---|---|---|
| TS1 | Forecasting questions / What must be predicted, and how far ahead? | Define frequency, horizon, target and available information. Distinguish a forecast from an explanation of historical association. | Introduce quarterly revenue and chronological ordering. |
| TS2 | Reading a time series / Trend, seasonality, cycles and irregular variation | Plot observations in order and distinguish recurring seasonal patterns from longer movement. | Walmart line plot and quarterly views. |
| TS3 | A baseline forecast / Naive and seasonal-naive benchmarks | Explain why a more complicated method must outperform a relevant simple benchmark. | Last observation and same-quarter-last-year baselines. |
| TS4 | Smoothing / Moving averages and exponential smoothing | Explain smoothing for seeing patterns and simple forecasting. Describe lag and sensitivity to the smoothing parameter. | R rolling mean and simple exponential smoothing; do not use future observations to form a past forecast. |
| TS5 | Modelling trend / Regression on time | Connect to the core regression lesson. Explain trend extrapolation and why changing conditions can invalidate it. | A simple time-trend model. |
| TS6 | Modelling seasonality / Quarter effects and seasonal decomposition | Show how quarter indicators or an appropriate decomposition represent seasonal differences. Discuss additive versus multiplicative scale without implying every series suits either model. | Walmart quarter indicators; source fiscal labels retained. |
| TS7 | Evaluating forecasts / Chronological validation | Hold out the most recent quarters, compare methods at the same horizon, and introduce MAE/RMSE. Fit preprocessing only on training periods. | An eight-quarter holdout gives a manageable illustration; explain the limited evaluation sample. |
| TS8 | Autoregressive models / Using information from the recent past | Introduce lag, autocorrelation and AR(1). Address trend/seasonality before assuming a stationary AR process; distinguish a serial-dependence model from ordinary independent errors. | A lag/ACF demonstration and a modest AR illustration on appropriately transformed data. All model fitting uses training data. |
| TS9 | Forecast uncertainty / An interval is not a guarantee | Distinguish point forecasts and prediction intervals. Explain conditional model uncertainty, shocks and residual checks. | Compare forecasts and intervals without claiming coverage has been validated by one short holdout. |
| TS10 | Index numbers / Base 100, rebasing and nominal versus real values | Calculate a simple price index and rebase it. Explain index-point versus percentage change and the idea of weighted aggregate indexes. Explain that deflation needs a suitable price index. | Gasoline index: 1980=100, then rebase to 1995. R verifies the book's historical example; no claim that a gasoline index is a general inflation measure. |

Scope is an introduction, not complete Chapter 16 coverage. Holt–Winters, detailed
AR model selection and weighted-index derivations can be further enrichment.

## Optional B: Decision Analysis

**Purpose:** turn uncertain outcomes and explicit preferences into a transparent
choice. **Book:** Chapter 17, payoff tables/trees, decision criteria, sample
information and utility. **Suggested length:** 9 slides.

Use the book's television-model introduction example (Example 17.1, beginning
p. 696) as the main payoff case. A payoff table and event probabilities are
specified decision inputs, not necessarily an observation dataset. Table 17.1 at p. 697 has been checked: market +45/-36 and do not market -3/-3,
in millions of dollars. Preserve the source payoff accounting; do not subtract
the prior cost a second time. Verify any additional input before slide authoring; no verified
local guest/customer-level dataset is claimed for this example. Clearly label
any simplified or changed inputs as hypothetical course adaptations.

| Slide | Title / subtitle | What it will do | R / example |
|---|---|---|---|
| DA1 | Decisions under uncertainty / Choices, states and consequences | Define actions, states of nature, payoffs and the decision-maker's objective. Separate controllable decisions from uncertain events. | Book product-introduction context. |
| DA2 | Payoff tables / Making consequences explicit | Build the action-by-state table, identify units and distinguish profits from costs. | Verified source payoff table. |
| DA3 | Decisions without agreed probabilities / Optimism, caution and regret | Introduce maximax, maximin and minimax regret for profit tables as a clearly labeled course extension. These rules are not presented as verified content of the ninth edition’s section 17.2, which develops EMV, EOL and return-to-risk criteria. Explain their different preferences. | R calculates criteria from the same payoff matrix; do not present equal probabilities as ignorance-free fact. |
| DA4 | Expected monetary value / Combining payoffs with probabilities | Calculate expected values using stated probabilities. Explain long-run averaging and why expected payoff is not a guaranteed outcome. | Matrix calculations in R. |
| DA5 | Decision trees / Decisions, chance and rollback | Draw the same problem as a tree. Explain event order, conditional probabilities and rollback. | One small tree consistent with the payoff table. |
| DA6 | Value of perfect information / An upper bound on information value | Compare expected value with and without perfect information. Account for the information cost before claiming a gain. | R calculates EVPI with matched payoff/probability inputs. |
| DA7 | Sample information / Updating probabilities | Explain how imperfect market information changes decisions. Add a short conditional-probability/Bayes refresher because it is not assumed in the core skeleton. | Use the verified book signal model: prior success .40, P(favorable given success)=.80 and P(favorable given failure)=.30 (p. 154); compute both report branches. Distinguish EVSI from EVPI and subtract a separately stated research cost. |
| DA8 | Utility and risk preferences / Why largest expected profit may not win | Explain utility, expected utility, risk aversion and certainty equivalents conceptually. Distinguish utility of expected payoff from expected utility. | An explicitly specified illustrative utility function and sensitivity check. No real person's utility is inferred. |
| DA9 | Sensitivity and a recommendation / What would change our decision? | Vary probabilities, payoffs and information costs. Write a conditional recommendation with the key switching assumptions. | A concise R sensitivity table and an independent decision question. |

## Optional C: Quality and Productivity Management

**Purpose:** distinguish common process variation, special signals and capability
against specifications. **Book:** selected Chapter 18. **Suggested length:** 11 slides.

Use the existing Harnswell roller-diameter case as the numerical anchor, with
cross-references to the separate extended notebook. Canonical measurements:
`data/business/extended-harnswell.csv`, 150 rollers arranged in 30 batches of five.
Verify and retain the grouping/order and original physical units when authoring.
The initial chart signals batch 17; this is not a verified stable baseline.
The workbook has 56 above-specification measurements; the book narrative says
55. Preserve all observations and disclose this discrepancy.

| Slide | Title / subtitle | What it will do | R / example |
|---|---|---|---|
| QM1 | Quality and productivity / Consistency, defects and customer requirements | Connect process variation to waste, rework, service and cost. Define the measured characteristic and the decision. | Harnswell roller diameters. |
| QM2 | Common and special causes / Responding to variation appropriately | Distinguish routine process variation from unusual changes. Explain why adjusting after every fluctuation can make a process worse. | A short conceptual illustration; no fabricated operating history presented as actual. |
| QM3 | Six Sigma and improvement / DMAIC | Introduce Define, Measure, Analyse, Improve and Control. Connect statistical tools to each step; avoid treating a tool or a single chart as certification of Six Sigma quality. | Apply the stages briefly to the roller problem. |
| QM4 | Control charts / Observations in process order | Explain centre line, control limits and signaling rules. Distinguish monitoring from a one-off mean test. | R plot with batch order preserved. |
| QM5 | Control limits versus specifications / Process behaviour versus requirements | Explain why estimated statistical limits and external engineering specifications answer different questions. A stable process can still be unacceptable. | Roller limits/specifications displayed with clear labels. |
| QM6 | Charts for measurements / X-bar and R charts | Explain rational subgroups, within-subgroup variation, appropriate constants and why the variation chart matters. | Harnswell five-observation batches; R chart calculations. |
| QM7 | Charts for counts and proportions / p and c charts | Distinguish fraction nonconforming from number of defects. Explain sample-size/opportunity conditions and when other chart forms are needed. | A separate clearly labeled illustrative count example; do not treat the diameter sample as defect counts without definition. |
| QM8 | Reading signals / Investigation before intervention | Explain prespecified rules and false signals. Investigate process context without claiming a chart identifies the cause. | Retain batch 17 and discuss its signal. Any exclusion is a labeled sensitivity exercise, not automatic cleaning. |
| QM9 | Establishing a monitoring baseline / Retrospective and prospective use | Distinguish investigating a historical baseline from monitoring a future process. Re-estimate limits only with a justified process history and record the decision. | Discuss evidence required before adopting a stable baseline. |
| QM10 | Process capability / Cp and Cpk after stability | Introduce spread versus specifications and centring. Explain the assumptions behind a capability claim and the difference from observed nonconformance. | Supply formulas and a clearly hypothetical stable-process calculation; do not declare capability from the unstable initial Harnswell charts. |
| QM11 | An improvement recommendation / What evidence is still needed? | Combine stability, specifications, observed defects, practical action and verification after change. | Brief report referencing Harnswell; distinguish the source discrepancy (56 versus 55) from process improvement evidence. |

## Optional D: Nonparametric Methods

**Purpose:** choose rank-based methods from the study design and interpret their
actual hypotheses. **Book:** sections 10.4 (p. 361), 10.5 (p. 367), 11.4
(p. 424) and 11.5 (p. 428). **Suggested length:** 8 slides.

Reuse COLA, COMPTIME and LOCATE so students can compare questions and assumptions
without learning a new context for each method. Add REAPPR3 for a genuinely
blocked design: 12 houses assessed by each of three agents, in thousands of
dollars. The publisher workbook's Data sheet has 12 rows and three valuation
columns plus house ID. Exercise 11.50, p. 432, explicitly uses the Friedman test;
Exercise 11.25, p. 411, describes its randomized-block comparison.

| Slide | Title / subtitle | What it will do | R / example |
|---|---|---|---|
| NP1 | Why consider nonparametric methods? / Questions and assumptions | Introduce rank-based inference when its hypotheses and design fit the question. Explain that nonparametric is not assumption-free, and skewness alone does not automatically require replacing a mean test. | Compare the core designs; no automatic decision based on a normality-test p-value. |
| NP2 | Working with ranks / Ordering observations and handling ties | Explain pooled ranks, signed absolute ranks, within-block ranks, ties and zero differences. Show which information ranking keeps and loses. | Small subsets of the existing data, explicitly identified as an illustration rather than a separate random sample. |
| NP3 | Two independent groups / Wilcoxon rank-sum or Mann–Whitney | Compare distributions using independent groups. A simple median/location-shift interpretation needs additional shape assumptions. | COLA; section 10.4 and book worked comparison, pp. 361–365. R: wilcox.test with paired=FALSE and tie/approximation settings stated. |
| NP4 | Paired observations / Wilcoxon signed-rank | Preserve pairing and inspect the difference distribution. Explain the symmetry assumption for a location interpretation and treatment of zeros/ties. | COMPTIME; section 10.5, pp. 367–371, revisits the software example. R: wilcox.test with paired=TRUE. |
| NP5 | Three or more independent groups / Kruskal–Wallis | Extend independent rank comparisons to multiple groups. An omnibus result does not identify every differing pair; median interpretations require suitable common-shape/location conditions. | LOCATE; Exercise 11.43, p. 428, compared with Exercise 11.13. R: kruskal.test. |
| NP6 | Repeated or blocked observations / Friedman | Rank methods within each block. Explain why measurements on the same house are related and different houses supply separate blocks. | REAPPR3, Exercise 11.50, p. 432; 12 houses × 3 agents. R: friedman.test. Do not call the appraisers independent samples or infer training effectiveness from agreement alone. |
| NP7 | What does the result mean? / Estimates, assumptions and sensitivity | Compare rank-based and mean-based questions, not merely their p-values. Explain that different decisions can reflect different hypotheses as well as uncertainty; never select the method giving significance. | Side-by-side interpretation on COLA or COMPTIME. State exact versus approximate calculation and tie corrections. |
| NP8 | Choosing a method / Match outcome, design and question | Consolidate independent/paired and two/multiple-group choices. Give an independent method-selection and interpretation task. | A decision table and a short R activity; answer in business context. |

No raw observations are changed to remove ties or make an exact-test calculation
possible. Do not describe all four tests as general tests of means or medians.
Post-hoc observed power is not used to choose between methods.

## Delivery boundaries

- The power block is part of the proposed inferential core.
- Optional A, B, C and D are separately named slide sections. They do not become
  required core content automatically.
- Each optional section has an introduction, one main example, short worked R
  checkpoints and an independent interpretation task.
- Preserve existing optional case notebooks; link to them instead of silently
  replacing or duplicating their complete analyses.
- Original books and workbooks remain unchanged and local-only. New exports,
  if needed, belong under root data/ with units, source and period documented.
- The current task updates the design only. The existing lesson, earlier review
  notebook, source decks, public navigation and student bundles are unchanged.
