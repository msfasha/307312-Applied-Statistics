# Inferential statistics: unit-by-unit source map

This maps the proposed skeleton to the actual ninth-edition book, original slide material, available data and planned R activities. It is a writing specification, not adoption or publication of a new course.

## Reading the map

- Printed page references refer to the local ninth edition. PDF viewer page = printed page + 26. CD9 references use the separately supplied power supplement.
- An exact book case, a book-supported method applied to a retained example, and an authored course addition are distinguished explicitly.
- “Raw” means available individual measurements, not independent verification of authentic field provenance. Reported counts, summaries, probability models and simulations are not interchangeable.
- R activities are planned implementations. Book spreadsheet instructions are references; statistical results and current R code must be checked during authoring.
- Coverage: 39 core teaching units. H4a expands into six power slides PW1–PW6, giving 44 core mapping rows. Four optional modules contain 38 planned slides; two small optional enrichments give 84 total mapping rows.

## Core: probability distributions

| ID / teaching unit | Book section / printed page | Selected example and available data | Planned R activity | Source treatment |
|---|---|---|---|---|
| P1 — Why inferential statistics? | §1.1 p. 2; §1.2 p. 4; §1.7 pp. 11–16; COLA study p. 336 | Original probability slides 3–6; FORCE and COLA as introductory questions. | No compulsory code. | Retain original orientation; book supports sampling and study-design distinctions. |
| P2 — Random variables and probability models | §1.8 p. 17; §5.1 pp. 166–168; §6.1 pp. 196–199 | Original probability slides 7–13: counts and measurements. No raw observations required. | One probability-mass/density diagram if needed. | Retain and correct original explanation; mass/density distinction explicit. |
| P3 — Discrete uniform distribution | §5.1 pp. 166–168 supplies discrete-distribution principles, not a claim of this exact die exercise. | Original slides 14–15: fair six-sided die; model probabilities. | rep(), sum(), event selection. | Retained course example; not represented as a book exercise. |
| P4 — Binomial distribution | §5.3 pp. 173–179; book’s tagged-order illustration pp. 174–177 is a reference alternative. | Original slides 16–17: 80 cars, p=.02; coin tosses as short illustration. Stipulated model. | dbinom(), pbinom(), probability plot. | Retain the clear original business example; book supplies method. |
| P5 — Poisson distribution | §5.5 pp. 183–186; bank-arrival calculation p. 184. | Book mean three arrivals/minute; exactly two and more than two. No observed arrival dataset. | dpois(), ppois(); define the time unit. | Adopt book example; replace/consolidate original Poisson calculations. |
| P6 — Continuous uniform distribution | §6.3 pp. 218–221. | Original slides 21–22: deliveries 8–12 and diameters 9.8–10.2 mm. Model assumptions. | punif(); a density diagram. | Retain original examples, correct midpoint/peak interpretation. |
| P7 — Normal distribution and empirical rule | §6.1 pp. 196–211; normality assessment §6.2 pp. 212–218; empirical rule also p. 108. | Original slides 23–26 and 28: 280 students, mean 74, SD 8, approximate counts. | dnorm() plot; compare rounded empirical-rule and exact pnorm() counts. | Retain and correct original example; explicitly assume approximate normality. |
| P8 — Standard scores | §6.1 standardisation p. 199 onward. | Original slides 27,29–30: Khalid’s score of 90 in two courses. | Direct standardisation in R. | Retain original comparison; no claim it is a book case. |
| P9 — Normal probabilities | §6.1 pp. 199–211; software Appendix 6 pp. 226–229. | Original slides 32–37: score above 75, mean 70, SD 6. Consistent threshold throughout. | pnorm(); table/Excel comparison with rounding explained. | Retain and correct original example and probability/percentage wording. |

## Core: sampling and estimation

| ID / teaching unit | Book section / printed page | Selected example and available data | Planned R activity | Source treatment |
|---|---|---|---|---|
| E1 — Sampling variation | §7.1 pp. 232–242. | A course-authored simulated population; distinguish it from book observations. | set.seed(), repeated sampling and histogram of means. | Book concept; new explicitly labeled simulation. |
| E2 — Standard error and CLT | §7.1 pp. 232–242. | Same simulated population, with two sample sizes; individual SD versus SD of means. | replicate(); compare sample size, sampling spread and estimated SE. | Book concept; new simulation, not a proof. |
| E3 — Point estimation: product strength | §8.2, Example 8.3, p. 262, Table 8.2. | FORCE: 30 insulator breaking-force observations, pounds. CSV insulator-force.csv. | read.csv(); length(), mean(), sd(). | Adopt verified book data and context. |
| E4 — Confidence-interval reasoning | §8.1 pp. 255–258; §8.2 pp. 259–264. | Continue strength question; coverage visual is a labeled model illustration. | Repeated-interval simulation or static coverage diagram. | Book interpretation; course-authored visual, no invented production observations. |
| E5 — Known-SD normal interval | §8.1 p. 255 and following coverage examples. | Cereal summary/model: n=25, mean 362.3 g, known sigma=15 g. No raw box data. | qnorm(); SE and endpoints; Excel CONFIDENCE.NORM. | Adopt book summary example, keep known-SD assumption explicit. |
| E6 — Unknown-SD t interval | §8.2 pp. 259–264; Example 8.3 p. 262. | Reuse FORCE, 30 measured strengths. | t.test() confidence interval, qqnorm(); same-data 90/95/99% comparison. | Adopt book worked example; outputs recomputed from observations. |
| E7 — Confidence interval for a proportion | §8.3 pp. 265–267. | Retain source satisfaction counts: 140 of 200. Aggregate counts, provenance limited. | Compute the book’s large-sample normal interval explicitly; label a Wilson comparison separately if included. | Book method applied to existing course counts; do not silently equate different interval methods. |
| E8 — Precision-based sample-size planning | §8.4 pp. 268–273. | Strength-planning scenario with explicitly hypothetical planning SD 90 lb and chosen margin. | qnorm(), ceiling(); change one planning input at a time. | Book planning method; hypothetical course inputs, not another sample. |

## Core: hypothesis testing and power

| ID / teaching unit | Book section / printed page | Selected example and available data | Planned R activity | Source treatment |
|---|---|---|---|---|
| H1 — Claims and hypotheses | §9.1 pp. 296–300. | Original hypothesis slides 3,6–7: logistics mean benchmark three days. | No compulsory code. | Retain original business question and correct hypothesis wording. |
| H2 — Evidence, decisions and errors | §9.1 pp. 296–300; §9.3 pp. 306–309; §9.7 pp. 324–326. | Original slides 9–18, explained through one ongoing question. | Null-distribution/rejection-region plot only where useful. | Book-supported concepts; original explanations corrected. |
| H3 — One-sample two-sided delivery test | §9.4 pp. 310–316. | Original slides 21–22: n=40, mean=3.4 days, sample variance=1.887179487 days squared. Summary inputs only. | Summary t statistic and pt(); two-sided interval. | Retain original summary example; no fabricated delivery records. |
| H4 — One-sided strength test | §9.3 pp. 306–309; §9.4 p. 310 onward; Exercise 9.103 p. 329. | Reuse FORCE; benchmark 1,500 lb, upper-tail mean test. | t.test(force, mu=1500, alternative="greater"). | Adopt book exercise; reuse earlier dataset. |
| PW1 — Why might a test miss an effect? | §9.8 CD supplement, CD9-1 onward; §9.1 errors. | Link to H3; define beta and power at a specified alternative, not retrospective observed power. | No numerical calculation required. | Book power concept, core addition; parent unit H4a. |
| PW2 — Specify the effect worth detecting | §9.8, cereal example CD9-1 onward. | Null boundary 368 g, assumed true mean 360 g, known sigma 15 g. Source scenario, not independently approved tolerance. | Set named model inputs; no raw sample invented. | Adopt book model; parent H4a. |
| PW3 — Visualising power | §9.8, Figures 9.27–9.28 and cereal calculation. | Same lower-tail normal mean model; n=25, alpha=.05. | dnorm(), qnorm(), pnorm(); two sampling curves and a common cutoff. | Book model, newly drawn teaching visual; parent H4a. |
| PW4 — What changes power? | §9.8 introductory explanation and operating-characteristic/power discussion. | Vary n, alpha, effect and SD in the same stipulated cereal model. | Grid of power probabilities and curves. | Book-supported comparison with labeled course-chosen scenarios; parent H4a. |
| PW5 — Planning n for a target power | §9.8 supplies power model; §8.4 supplies sample-size planning principles. | Target .80 power, 8 g reduction, sigma 15 g; illustrative alpha .05/.01. | Invert the known-SD normal power expression and round up; verify power at integer n. | Course-derived planning calculation using book assumptions; not attributed to an unverified numbered book example; parent H4a. |
| PW6 — Interpreting a power plan | §9.8; §9.7 pitfalls. | Change one input; explain design assumptions, cost and false-positive trade-offs. | Small independent planning task; optional power.t.test introduction clearly distinguished from known-sigma model. | Course synthesis; parent H4a. |
| H5 — Paired software comparison | §10.3 pp. 354–359; Table 10.5 p. 356. | COMPTIME: ten matched financial projects; current/new seconds. CSV software-times.csv. | Differences, plot, paired t.test; one-sided test and separately labeled interval. | Adopt book worked example and data. |
| H6 — Independent display comparison | §10.1 pp. 336–346; Table 10.1 p. 338. | COLA: 20 stores, ten per randomized display; cases sold in one week. CSV cola-displays.csv. | Group summaries/plot, pooled t.test; Welch sensitivity comparison. | Adopt book independent-groups example; selected stores are not a random sample of all stores. |
| H7 — Welch comparison: training | §10.1; Exercise 10.13 p. 346 explicitly compares pooled and nonpooled methods. | TRAINING: 42 employees, 21 assigned per method; assembly seconds. CSV assembly-training.csv. | Group spread plot; t.test(var.equal=FALSE), two-sided at 5%. | Adopt book exercise and direction/alpha; differs from old one-sided salary example. |
| H8 — One population proportion | §9.5 pp. 317–319. | Reuse 140/200 against .75, original slide 36. | Null-based z; prop.test(correct=FALSE), with method/continuity setting explained. | Book method applied to retained aggregate course example. |
| H9 — Two independent proportions | §12.1 pp. 448–452; worked hotel counts pp. 449–450. | Beachcomber 163/227; Windsurfer 154/262 likely to return. CSV hotel-return-counts.csv. | prop.test(correct=FALSE); pooled null SE and difference in percentage points. | Adopt book aggregate example; voluntary checkout responses limit inference. |
| H10 — Chi-square independence | §12.4 pp. 466–471. | Original slides 44–49 beverage preference by age; six cells, 200 respondents. CSV beverage-preferences.csv. | chisq.test(), expected counts and row percentages. | Retain simpler original table; book supplies method, not these exact counts. |
| H11 — One-way ANOVA | §11.1 pp. 388–402; Exercise 11.13 pp. 402–403. | LOCATE: 18 independent assigned stores, three aisle locations, monthly sales in $000. CSV aisle-location.csv. | aov(), residual checks and TukeyHSD with appropriate assumptions. | Adopt book case; omit unexplained Height variable from this one-way exercise. |
| H12 — Choosing a method | Chapters 9–12 and their summary diagrams. | Questions drawn from completed examples; no new observed dataset. | Students choose a method and justify it before code. | Course synthesis, not a claim of a numbered book exercise. |

## Core: regression

| ID / teaching unit | Book section / printed page | Selected example and available data | Planned R activity | Source treatment |
|---|---|---|---|---|
| R1 — Regression question and variables | §13.1 pp. 484–486; Exercise 13.7 p. 493. | RENT: 25 apartments, monthly dollars and square feet; one neighbourhood. CSV apartment-rent.csv. | Inspect variables and scatterplot. | Adopt book context and data, historical period not invented. |
| R2 — Line, residuals and least squares | §13.2 pp. 487–493; §13.10 pp. 523–528 for optional arithmetic. | Same RENT data; use identified observations to illustrate residuals. | Plot line and vertical deviations; no new statistical sample. | Book method applied consistently to RENT. |
| R3 — Fit and interpret rental model | §13.2; Exercise 13.7 p. 493; Appendix 13 pp. 538–540 supports software orientation. | Same RENT; interpreting a 100-square-foot change. | lm(); coefficients and fitted line; matching Excel setup. | Book exercise, new R implementation. |
| R4 — Assumptions and residual checks | §13.4 p. 498; §13.5 pp. 499–503; §13.6 pp. 503–508. | RENT; Exercise 13.21 p. 498 and Exercise 13.33 p. 503 revisit the case. | Residual-versus-fitted and Q-Q plots; independence assessed from design, not invented row chronology. | Book-supported diagnostics; no claim a plot proves assumptions. |
| R5 — Fit statistics | §13.3 pp. 494–497; RENT Exercise 13.18 p. 498. | Same RENT; R-squared and residual SE in dollars. | summary(lm()); compact annotated output. | Book concepts; correct original Multiple R/MAE confusion. |
| R6 — Slope inference and regression ANOVA | §13.7 pp. 509–515; RENT Exercise 13.41 p. 514. | Same RENT; slope units, SE, test and interval. | summary(), confint(), anova(). | Adopt book progression on the same dataset. |
| R7 — Mean response and individual prediction | §13.8 pp. 516–519; pitfalls §13.9 p. 520; RENT follow-up Exercise 13.55 p. 520 (source target 1,000 square feet). | RENT at 1,200 square feet, within its observed range; the selected prediction target is a course choice. | predict(interval="confidence") versus predict(interval="prediction"). | Book method; explicitly distinguish chosen course input from exact source exercise request. |
| R8 — Multiple regression: price and promotion | §14.1 pp. 542–549; Table 14.1 p. 543; §14.2 p. 550; §§14.3–14.4 pp. 552–556. | OMNI: 34 stores; monthly bars, price cents, promotion dollars. CSV omnipower.csv. | lm() with two predictors, partial slopes, output and residual checks. | Adopt book main worked case; causal assignment not established by reviewed text. |
| R9 — Collinearity, influence and conclusions | §15.3 pp. 602–604; §15.4 pp. 605–606; §13.9 p. 520; §15.6 p. 618. | Continue OMNI; no additional compulsory dataset. | VIF interpretation and cooks.distance(); sensitivity without automatic deletion. | Selected advanced concepts adapted to existing model, not full Chapter 15 coverage. |

## Optional A: time series and index numbers

| ID / teaching unit | Book section / printed page | Selected example and available data | Planned R activity | Source treatment |
|---|---|---|---|---|
| TS1 — Forecasting question and horizon | §16.1 p. 630; §16.8 p. 670. | WALMART: 36 fiscal quarters, 1994–2002; revenue $millions. Data sheet verified. | Time-series construction with verified fiscal-quarter labels. | Adopt book historical data; CSV export still to prepare. |
| TS2 — Trend and seasonality | §16.2 pp. 631–632; §16.8 pp. 670–677; Table 16.4 p. 671. | Same WALMART; fiscal fourth quarter ends in January. | Time plot, quarter comparisons. | Book concepts and case; preserve fiscal periods. |
| TS3 — Baseline forecasts | §16.1 and §16.7 p. 666 support forecast purpose/comparison; specific naive benchmarks are course additions. | Same WALMART; last-value and seasonal-naive baselines. | Training-only naive and seasonal-naive forecasts. | Authored benchmarking addition; not a claimed book exercise. |
| TS4 — Moving averages and exponential smoothing | §16.3 pp. 633–638. | WALMART as a method illustration; simple smoothing alone does not address all seasonality/trend. | Trailing mean and simple exponential smoothing; avoid look-ahead. | Book methods transferred to selected series; limitations explicit. |
| TS5 — Trend regression | §16.4 pp. 639–651. | Same WALMART; historical quarterly trend. | lm(revenue ~ time), training data only. | Book method, adapted data application. |
| TS6 — Seasonal modelling | §16.8 pp. 670–677; WALMART worked case p. 671 onward. | Same WALMART; quarter labels and scale retained. | Quarter indicator model; optional decomposition with scale/assumptions stated. | Book case, newly implemented in R. |
| TS7 — Chronological evaluation | §16.7 pp. 666–669 and §16.10 pp. 685 onward; explicit holdout protocol is a course addition. | Last eight WALMART quarters held out; earlier 28 used for fitting. | Same-horizon errors, MAE/RMSE; no random split or fitting on holdout. | Authored evaluation design using book data; limited test sample. |
| TS8 — Autoregressive illustration | §16.6 pp. 655–665. | WALMART or its appropriately detrended/differenced form; no raw-trend stationary AR claim. | Lag plot, ACF, modest AR(1) fit with training-only transformations. | Book method illustration; specific R specification to be checked during authoring. |
| TS9 — Forecast uncertainty | §16.4 and §16.6; §16.10 pitfalls p. 685. | Same series; point forecasts, conditional prediction intervals and shocks. | Compare intervals and holdout outcomes without claiming validated nominal coverage. | Book-supported discussion with a course validation exercise. |
| TS10 — Index numbers and rebasing | §16.9 pp. 678–684; Table 16.5 p. 679. | GASOLINE: 23 annual prices 1980–2002, 1980-base index. Workbook Data verified. | price/base*100; rebase to 1995; distinguish index points and percentage change. | Adopt book historical index example; CSV export to prepare. |

## Optional B: decision analysis

| ID / teaching unit | Book section / printed page | Selected example and available data | Planned R activity | Source treatment |
|---|---|---|---|---|
| DA1 — Actions, states and consequences | §17.1 pp. 696–699; Example 17.1 p. 697. | Television market/do-not-market, success/failure. Source payoff table, not field observations. | Define payoff matrix labels; no required code. | Book decision model. |
| DA2 — Payoff table | §17.1, Example 17.1 and Table 17.1 p. 697. | Market payoffs +45/-36; do-not-market -3/-3, $millions, as printed. | matrix() with named actions and states; retain source accounting. | Source values checked; do not subtract the prior $3m a second time. |
| DA3 — Criteria without agreed probabilities | No verified matching section for maximax/maximin/minimax in this edition; §17.2 p. 700 instead develops EMV/EOL/return-to-risk. | Reuse the TV payoff table; decision rules are a labeled course extension. | Row maxima/minima and regret matrix, with profit/cost convention. | Authored extension, not misattributed to the book. |
| DA4 — Expected monetary value | §17.2, Example 17.4 and Table 17.5 p. 701. | TV prior success probability .40, failure .60; source payoffs retained. | Probability-weighted payoffs; compare actions. | Book worked example; probabilities are specified model inputs. |
| DA5 — Decision tree and rollback | §17.1, Example 17.2 and Figure 17.1 p. 697; §17.2 expected-value criterion. | Same TV actions and outcomes. | One consistent tree and rollback arithmetic; R checks expected values. | Book representation plus course teaching graphic. |
| DA6 — Perfect information value | §17.2 expected opportunity loss/perfect-information discussion pp. 702–704. | Same verified TV payoff matrix and prior probabilities. | Expected best statewise payoff minus best prior EMV; subtract information cost separately. | Book method applied to ongoing case; preserve $millions. |
| DA7 — Imperfect information and updating | §4.3 pp. 154–157; §17.3 Example 17.7 pp. 708–709. | Prior success .40; P(favorable\|success)=.80, P(favorable\|failure)=.30, source p. 154. Favorable posterior .64; full binary signal model verified. | Bayes update for both report outcomes; ex-ante EVSI; compare with EVPI and subtract a separately stated research cost. | Book inputs verified; ex-ante EVSI is an explicit course extension from those inputs, not confused with a conditional EMV. |
| DA8 — Utility and risk preference | §17.4 pp. 713–714. | Book fair-coin small-versus-large stakes; an additional utility function must be labeled hypothetical. | Expected utility under specified illustrative function; compare with utility of expected payoff. | Book concepts and example; no inferred real person’s utility. |
| DA9 — Sensitivity and decision recommendation | §17.2 and §17.3; question/threshold grid is a course synthesis. | Reuse verified TV inputs; vary one input explicitly as a scenario. | Probability/payoff switching thresholds and information-cost sensitivity. | Authored task, not newly observed business data. |

## Optional C: quality and productivity

| ID / teaching unit | Book section / printed page | Selected example and available data | Planned R activity | Source treatment |
|---|---|---|---|---|
| QM1 — Quality and customer requirements | §18.1 pp. 720–722; Harnswell case pp. 752–754. | Existing Harnswell CSV: 150 roller diameters, 30 batches of five. | Read data and identify unit, subgroup and specification. | Book case and already prepared data; source discrepancy retained. |
| QM2 — Common and special causes | §18.3 p. 724; §18.5 pp. 731–732. | Harnswell plus explicitly conceptual examples; do not invent actual process history. | Simple ordered plot if needed. | Book concepts; no random cause assigned to batch 17. |
| QM3 — Six Sigma and DMAIC | §18.2 pp. 723–724. | Apply Define/Measure/Analyse/Improve/Control to the roller question. | No obligatory code; statistical tools placed in improvement cycle. | Book topic; no certification or 3.4-defects claim without stated convention. |
| QM4 — Control-chart structure | §18.3 p. 724; §18.7 pp. 736–742. | Same Harnswell batch order. | Centre line, limits and prespecified signaling rule. | Book methods, existing case. |
| QM5 — Control limits versus specifications | §18.7 and §18.8 pp. 743–748. | Harnswell specifications from source case; chart limits estimated from data. | Label the two types of limits separately. | Book concepts; avoid confusing process behaviour and requirements. |
| QM6 — X-bar and R charts | §18.7 pp. 736–742; Harnswell pp. 752–754. | 30 subgroups of five, not 25 of six. Existing extended-harnswell.csv. | Subgroup means/ranges and verified n=5 chart constants. | Book design and canonical data checked; stability not assumed. |
| QM7 — p and c charts | §18.4 pp. 725–730; §18.6 pp. 733–735. | COLASPC: 22 days, cans filled and unacceptable cans, source p. 730, workbook verified. c-chart input example may be explicitly hypothetical. | p-chart limits account for daily denominators; c chart needs constant opportunity. | Book raw data available for p; illustrative c counts require clear hypothetical label. |
| QM8 — Signals and investigation | §18.3 and §18.7; Harnswell case pp. 752–754. | Retain batch 17 and all measurements. | Plot signals; investigate context; optional labeled sensitivity. | Book case reviewed; chart is not a causal diagnosis. |
| QM9 — Retrospective baseline and future monitoring | §18.3 and §18.7 support chart use; explicit baseline/monitoring workflow is a course elaboration. | Same Harnswell; initial process signals mean no stable baseline has yet been established. | No automatic removal/re-estimation; document any justified monitoring phase. | Methodological elaboration; no invented stable history. |
| QM10 — Capability after stability | §18.8 pp. 743–748. | Use formulas plus an explicitly hypothetical stable process; not an unconditional Harnswell capability claim. | Cp/Cpk calculation with a clearly identified within-process sigma estimate and assumptions. | Book formulas; hypothetical inputs until a justified stable phase exists. |
| QM11 — Quality-improvement recommendation | Chapter 18 summary and Harnswell pp. 752–754. | Actual workbook has 56 above-spec measurements; narrative says 55. Preserve discrepancy and data. | Brief evidence-based report and proposed follow-up measurement. | Course synthesis; no automatic exclusion or claimed process improvement. |

## Optional D: nonparametric methods

| ID / teaching unit | Book section / printed page | Selected example and available data | Planned R activity | Source treatment |
|---|---|---|---|---|
| NP1 — Why nonparametric methods? | §10.4 p. 361; §10.5 p. 367; §11.4 p. 424; §11.5 p. 428. | Core independent, paired and multiple-group designs. | No automatic switch based only on normality-test p. | Book concepts with explicit modern interpretation cautions. |
| NP2 — Ranks, ties and zeros | §10.4 pp. 361–365; §10.5 pp. 367–371; §11.5 p. 428 onward. | Identified small subsets from existing data, not a new random sample. | rank(ties.method="average"); signed absolute ranks and within-block ranks. | Book methods; exact/asymptotic settings and conventions stated. |
| NP3 — Independent Wilcoxon rank-sum | §10.4 pp. 361–365; COLA worked example. | Reuse COLA independent store groups. | wilcox.test(paired=FALSE); account for ties and state approximation/continuity settings. | Book case; distribution/location claim, not a generic mean test or unconditional median test. |
| NP4 — Paired Wilcoxon signed-rank | §10.5 pp. 367–371; COMPTIME explicitly revisited p. 368. | Same ten software pairs, including a zero difference and ties. | wilcox.test(paired=TRUE); explicit symmetry and tie/zero treatment. | Book case; no deletion of valid observations merely to avoid ties. |
| NP5 — Kruskal–Wallis independent groups | §11.4 pp. 424–428; Exercise 11.43 p. 428. | Reuse LOCATE 18 stores across three aisle locations. | kruskal.test; compare interpretations with one-way mean ANOVA. | Book exercise; omnibus rank/distribution result, not automatic pairwise median claims. |
| NP6 — Friedman blocked comparison | §11.5 pp. 428–432; Exercise 11.50 p. 432; design Exercise 11.25 p. 411. | REAPPR3: 12 houses each appraised by three agents, values in $000. Data sheet verified. | friedman.test on house-by-agent matrix; houses are blocks. | Book exercise and local data verified; CSV export still to prepare. |
| NP7 — Interpretation and sensitivity | §10.4–10.5 and §11.4–11.5; side-by-side teaching comparison is course synthesis. | Reuse COLA or COMPTIME, not a new context. | Compare effect descriptions and assumptions rather than choosing the smaller p-value. | Course interpretation exercise; median/location interpretation requires added conditions. |
| NP8 — Choosing a rank-based method | Same four book sections and their design distinctions. | Independent/paired; two groups/multiple groups; meaningful response scale. | Short method-selection and interpretation task. | Course synthesis; nonparametric does not mean assumption-free. |

## Other optional enrichments

| ID / teaching unit | Book section / printed page | Selected example and available data | Planned R activity | Source treatment |
|---|---|---|---|---|
| OX1 — Two-way ANOVA extension | §11.3 pp. 412–423; Exercise 11.71 Part II p. 436. | COMPUTERS2: 32 historical downloads, 2 browsers × 2 computers, eight per cell. CSV historical-downloads.csv. | aov(response ~ browser*computer); interaction plot. | Optional existing extension; historical labels and independence limits retained. |
| OX2 — Distribution fitting enrichment | §6.2 p. 212 supplies model-assessment context, not the automatic fitter demonstration. | Explicit simulated normal observations, not measured business data. | Optional candidate-model AIC comparison; identify the limited candidate set. | Authored enrichment; not attributed to a verified book procedure. |

## Raw-data availability catalogue

Original workbook directory: `books/2-Basic business statistics  concepts and applications/Data-9th e/browse/Data_Files/Excel`. Source hashes and exact case-sensitive paths are retained in the JSON companion. Existing CSVs remain review-only unless already separately approved for a published extended case. This map exports no new data.

| Dataset | Publisher workbook / sheet | Observations and units | Prepared CSV / preparation status |
|---|---|---|---|
| FORCE | FORCE.xls / Data | 30 insulators; pounds | data/inferential-review/insulator-force.csv |
| COMPTIME | COMPTIME.xls / Data | 10 matched projects; seconds | data/inferential-review/software-times.csv |
| COLA | COLA.XLS / Data | 20 independent stores; cases/week | data/inferential-review/cola-displays.csv |
| TRAINING | training.xls / Data | 42 employees; assembly seconds | data/inferential-review/assembly-training.csv |
| RENT | rent.xls / Data | 25 apartments; monthly dollars and square feet | data/inferential-review/apartment-rent.csv |
| OMNI | OMNI.xls / Data | 34 stores; monthly bars, cents and promotion dollars | data/inferential-review/omnipower.csv |
| LOCATE | LOCATE.xls / Data | 18 stores; one-month sales in $000 | data/inferential-review/aisle-location.csv |
| WALMART | WALMART.XLS / Data | 36 fiscal quarters, 1994–2002; revenue $millions | Not exported for proposed optional section yet |
| GASOLINE | GASOLINE.XLS / Data | 23 annual prices/index rows, 1980–2002 | Not exported for proposed optional section yet |
| COLASPC | COLASPC.xls / Data | 22 days; total and unacceptable cans | Not exported for proposed optional section yet |
| REAPPR3 | reappr3.xls / Data | 12 houses × 3 agents; appraisals in $000 | Not exported for proposed optional section yet |
| COMPUTERS2 | COMPUTERS2.XLS / first sheet | 32 downloads; 2×2×8; seconds | data/inferential-review/historical-downloads.csv |
| HARNSWELL | HARNSWELL.xls / Data | 150 diameters; 30 batches × 5 | data/business/extended-harnswell.csv |

## Non-raw inputs and their status

| Input | Exact source / current availability | How to present it |
|---|---|---|
| Delivery summaries | Original hypothesis slides 21–22: n=40, mean=3.4, variance=1.887179487 | Summary calculation; do not invent delivery records. |
| Customer satisfaction | Original slide 36: 140 satisfied of 200 | Aggregate counts, source sampling provenance not established. |
| Beverage preferences | Original slide 44; existing review CSV of six counts | Original aggregated survey illustration, not newly verified field data. |
| Hotel return intentions | Book pp. 449–450: 163/227 and 154/262; existing review CSV | Book-reported aggregate responses; voluntary-response limitation. |
| Known-SD cereal interval | Book p. 255: n=25, mean=362.3 g, sigma=15 g | Stipulated known-SD summary, not an invented raw sample. |
| Power model | Actual local section9_8.pdf: null boundary 368 g, alternative 360 g, sigma=15 g | Alternative mean is a model/planning condition; no measured sample required. |
| TV payoff matrix | Table 17.1 p. 697: market +45/-36, do not market -3/-3 ($millions) | Preserve source accounting and distinguish assumed probabilities from sample frequencies. |
| Simulations and planning tasks | Authored fixed-seed demonstrations / explicitly selected planning inputs | Label simulation, hypothetical scenario or course adaptation. |

## Remaining work before actual slide authoring

1. Prepare only the four new optional-data exports WALMART, GASOLINE, COLASPC and REAPPR3 under root data/, with units, source references, complete-row checks and provenance. Source workbooks are already available and inspected.
2. Decision-analysis input transcription is now verified: prior success .40, favorable-report probabilities .80/.30, and payoffs +45/-36 versus -3/-3. The authoring step should derive both posterior branches and ex-ante EVSI, with a separately stated information cost. Do not use only the favorable branch.
3. Mark additions honestly: naive forecasting benchmarks, explicit chronological holdout design and probability-free decision criteria are course additions, not verified named exercises from this edition.
4. Use a stated proportion-interval method and match the R result to it. A Wilson interval and the book’s normal approximation are different methods.
5. During writing, check all calculations, plot assumptions, labels, code settings and ties/zeros. Do not treat nonparametric methods as assumption-free tests of medians.
6. Develop one coherent section at a time against this map. The next production section is 3.1 Probability Distributions; do not automatically rebuild the whole lesson or publish it.

## Preservation

Only design documents and this source map were created or updated by this task. Original decks, book and publisher workbooks, adopted lessons, the previous review notebook, public navigation and student bundles were not changed. No commit, push or publication was performed.
