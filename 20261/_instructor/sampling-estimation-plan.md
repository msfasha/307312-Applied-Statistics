# Module 4: sampling and estimation

Developed 2026-10-25. Four lessons, four matching practices, an integrated review, and five separate instructor guides. Follow Module 3 with sampling designs and variability, sampling distributions/SE, mean confidence intervals, then proportion intervals and sample-size planning. Module 5 expansion follows.

## Checked sources

Main reference: Anderson et al. (2020), Essentials of Modern Business Statistics with Microsoft Excel, 8th edition. Local PDF is preserved under books/1-Modern Business Statistics-Organized-Data/. Printed page p corresponds to PDF page p+32. Text extraction and page images checked for the following inputs; these are selected examples, not an exhaustive inventory of Chapters 7–8.

| Case | Printed page | Checked scope |
|---|---|---|
| EAI | 308, 316 | N=2500 employees, annual mean salary $71800, population SD $4000, 1500 training completers (p=.60); sample n=30, mean=$71814, training count=19. Published summaries only; no individual-record/workbook compatibility claim. |
| EAI SE and theory | 323–324 | Finite correction sqrt((N-n)/(N-1)) with population variance denominator N; textbook 5% convention, approximate SE=730.3, CLT and distinction between population and sampling shape. |
| Lloyd's | 357 | n=100 customers, sample mean spending $82/trip, population SD treated as known at $20, normal population assumption. No transaction verification. |
| Household balances | 367–368 | n=70 U.S. households, rounded mean=$9312, rounded sample SD=$4007, df=69, 95% t interval approximately $8357–$10267. Table 8.3 observations not adopted or independently matched. |
| Women golfers | 378, 380–381 | 396 satisfied of 900; normal interval .4076–.4724, planning E=.025, p*=.44 or .50, completed n=1515 or 1537. Counts do not verify design or observation order. |

## Data and adaptations

No new observation CSV is needed: these examples use stated book summaries/parameters directly in R. Raw publisher files remain unchanged; no artificial observations substitute for unavailable records. EAI ID sampling demonstrates selection only. Independent normal salary simulation using EAI parameters is explicitly artificial, not a reconstruction of the finite population. Lloyd's coverage demonstration fixes an artificial mean of $82; that is not a claim that its actual population mean equals the sample mean. The $2 and $1 Lloyd's planning margins are original course extensions, not additional book observations.

## Teaching decisions

Explain target/frame/unit and bias before SE, then interval coverage before t. Unknown population SD uses t even above n=30. State the normal-model exactness conditions and approximate robustness limits. Use a cautious count threshold of ten for proportion normal approximations; teach the book's Wald calculation with explicit limitations and explain why default prop.test() differs. Sample-size formulas assume simple sampling, use completed responses, and round up. Complex-design and small-count methods remain extensions. Arabic narration is limited to case introductions.

## Verification

Run publisher checks, render the full student site with its link validator, render separate instructor guides, and build student PDFs. Record actual outcomes in data-checks/module04-verification.json. Code documentation is checked by function/argument meaning, not solely the number of comment lines. Instructor and student answers stay separate.
