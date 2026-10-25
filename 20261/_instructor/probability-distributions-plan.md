# Module 3: probability and distributions

## Sequence and scope

Developed 2026-10-24: five lessons, matching practices, separate instructor guides, and an integrated review. Teach events before conditioning, conditioning before distributions, a discrete PMF before named count models, and area before normal quantiles. Module 4 was planned at that point and was developed on 2026-10-25; see `sampling-estimation-plan.md`.

1. Probability rules: uniformly select one Restaurant record. Define A = Very Good and B = USD 20 to <30. Counts 150, 118, joint 64; disjoint regions 64, 86, 54, 96. Complements, inclusive union, exactly one, and pair counting. This is an original course adaptation using the main book's checked Restaurant aggregates.
2. Conditional probability: retain A/B, then two suppliers for Bayes. Separate finite-experiment dependence from inferential testing, and independence from mutual exclusion. Include the without-replacement mechanism.
3. Discrete random variables: DiCarlo PMF, CDF, expectation, variance, and distinction between empirical distribution and future model.
4. Binomial and Poisson: Martin purchases, arrivals over fixed exposure, correct integer tail boundaries, and seeded artificial simulation.
5. Continuous distributions: uniform flight times, normal Grear lifetimes, density versus area, SD versus variance, z-scores, tails, and quantiles. Preserve the book's miles and minutes.
6. Integrated review: method choice, assumptions, calculations, interpretation, and unavailable-data limits.

Detailed permutations, bivariate financial distributions, hypergeometric calculations, and exponential models are deferred extensions. This is selected coverage of Chapters 4–6, not every textbook topic. Do not imply the reviewed examples are the only choices in the book.

## Source checks

Main reference: Anderson et al. (2020), Essentials of Modern Business Statistics with Microsoft Excel, 8th edition. Local PDF: `books/1-Modern Business Statistics-Organized-Data/8th e-Essentials of Modern Business Statistics with Microsoft Excel.pdf` (relative to repository root). Printed p maps to PDF page p+32 for the pages below. The source pages were read from text and visually inspected, including settings, units, values, and assumptions.

| Input | Checked printed source | Verification scope |
|---|---|---|
| Restaurant | Tables 2.9–2.10, pp.65–66; existing verify-data.R | Existing first-ten-row and all-twelve-cell checks; not all 300 individual records |
| Supplier priors 0.65/0.35 and bad-part rates 0.02/0.05 | p.201, text and Table 4.6; posterior calculations pp.203–204 | All stated shares/rates; no inspection records or underlying sample sizes |
| DiCarlo counts 54,117,72,42,12,3 at x=0:5 | p.222; Table 5.4 p.223; Tables 5.5–5.6 pp.227–228 | All six published frequencies and PMF cells; expected value 1.50 and variance 1.25 |
| Martin n=3, p=0.30; independent customer decisions | p.244 | Stated inputs and binomial assumptions; no individual customer records |
| Hospital arrivals mean 10 per 15 minutes; 2 per 3 minutes | p.253; process discussion p.252 | Stated rates, units, and assumptions; no timestamps or real operational forecast |
| Uniform flight bounds 120–140 minutes, Chicago to New York | pp.275–277 | Bounds, units, route, equal-length interval assumption, 128–136 event |
| Grear mean 36,500 miles, SD 5,000 miles; tail at 40,000 and lower 10% guarantee cutoff | pp.286–288, R-equivalent precision also pp.290 | Model inputs, setting, questions; no raw road-test data and no independently checked fit |

## Data and reproducibility

Do not create a new observation CSV for an aggregate table or a parameter list. Restaurant lessons read the existing teaching CSV, reproducible from preserved Restaurant.xls through scripts/verify-data.R. Raw publisher workbooks remain unchanged.

DiCarlo's six frequencies are entered as a published aggregate table, explicitly not reconstructed daily observations. The other new examples enter explicitly cited probability/model parameters directly in R. Those statements are not claims of workbook compatibility. No new source workbook was adopted, and no synthetic raw observations stand in for missing book files. The seeded binomial simulation is explicitly artificial and demonstrates model implications rather than validating real-world fit.

Student-facing nonempty R chunks include purpose and function/argument comments. English–Arabic narration applies only to business-case introductions. All charts are original calculated R plots; no new raster assets or unattributed book figures are needed.

## Verification

Render student sources through the Quarto project, check local navigation links, and render all instructor guides through scripts/render-instructor.sh. PDF exports use scripts/build-pdfs.py. Numerical assertions in the lessons check the verified Restaurant counts, supplier totals, DiCarlo PMF/moments, binomial mass calculation, and equivalence of standardized/direct normal tails.
