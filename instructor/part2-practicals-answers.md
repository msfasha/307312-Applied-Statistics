# Part 2 practical answers and assessment guidance

Instructor material, 6 November 2026. Use alongside the three practical notebooks.
Do not include this file in student previews or assessed distributions.
Calculations use the canonical course CSVs, R sample SD and type-7 quantiles.

## Practical 1 Categorical business data

| Check | Expected result |
|---|---|
| Shape | 259 entries, 13 columns; no missing values after ordered-factor conversion |
| Objectives | Growth 158 (61.0039%); Value 101 (38.9961%) |
| Type task A | Large cap 171 (66.0232%); mid cap 46 (17.7606%); small cap 42 (16.2162%) |
| Risk, in order | 6, 76, 82, 80, 15 |
| Risk at most Average | 164/259 = 63.3205%; Average alone 82/259 = 31.6602% |
| Turnover, in order | 27, 66, 102, 50, 14 |
| Turnover at most Low, task B | 93/259 = 35.9073% |
| Sales charge | No 164; Yes 95 |
| High risk and Yes | 35/259 = 13.5135% overall; 35/80 = 43.75% within High risk; 35/95 = 36.8421% within Yes |

Task C counts and the within-type percentage carrying a charge:

| Type | No | Yes | Yes within type |
|---|---:|---:|---:|
| Large cap | 105 | 66 | 38.5965% |
| Mid cap | 30 | 16 | 34.7826% |
| Small cap | 29 | 13 | 30.9524% |

Task D:

| Type | Growth | Value | Growth within type | Value within type |
|---|---:|---:|---:|---:|
| Large cap | 100 | 71 | 58.4795% | 41.5205% |
| Mid cap | 29 | 17 | 63.0435% | 36.9565% |
| Small cap | 29 | 13 | 69.0476% | 30.9524% |

A row question is “Among small-cap entries, what share have a Growth objective?”
A column question is “Among Growth entries, what share are small cap?”
The latter is 29/158 = 18.3544%, not 29/42.

Interpretation workshop: (1) supported for this list; (2) confuses Average with
Average-or-lower; (3) wrong denominator, 13.5% of all entries; (4) sales charges
are not all expenses; (5) no causal conclusion from the descriptive table.

Example solution code for the independent tasks:

```r
data_dir <- if (dir.exists("data")) "data" else file.path("..", "data")
funds <- read.csv(file.path(data_dir, "practicals/funds2002.csv"))
levels_in_order <- c("very low", "low", "average", "high", "very high")
funds$turnover <- factor(funds$turnover, levels = levels_in_order, ordered = TRUE)
100 * prop.table(table(funds$type))
t <- table(funds$turnover)
data.frame(Frequency = as.vector(t), Cumulative_percentage = 100 * cumsum(t) / sum(t))
charges <- table(funds$type, funds$sales_charge)
100 * prop.table(charges, 1)
100 * prop.table(table(funds$type, funds$objective), 1)
```

The independent briefing should specify the population being described as the
supplied list, identify denominators, use within-type percentages when comparing
composition, and distinguish trading activity from numerical return.

## Practical 2 Numerical business data

All cost values are historical dollars per ounce. See the separate source review
for the book's cents/dollars inconsistency.

| Measure | Full list | Cost at most $0.15 subset |
|---|---:|---:|
| n | 33 | 14 |
| Mean | 0.1706060606 | 0.1271428571 |
| Median | 0.17 | 0.125 |
| Sample SD | 0.0469001195 | 0.0185756546 |
| IQR | 0.07 | 0.035 |

Full-list minimum 0.10, maximum 0.27, range 0.17. Q1 0.13 and Q3 0.20 give
1.5-IQR fences 0.025 and 0.305; no products are flagged. The median is 0.17.
The subset's lower location and smaller spread follow selection on the measured
cost variable. They do not show an intervention, temporal price reduction or
superior product quality. Similar mean and median do not prove symmetry or
normality. Nutrition comparisons require a common measurement basis.

```r
data_dir <- if (dir.exists("data")) "data" else file.path("..", "data")
cereals <- read.csv(file.path(data_dir, "practicals/cereals.csv"))
low <- subset(cereals, cost_per_ounce <= 0.15)
summarize_cost <- function(x) c(n = length(x), mean = mean(x), median = median(x),
                               sd = sd(x), IQR = IQR(x))
rbind(All = summarize_cost(cereals$cost_per_ounce),
      Shortlist = summarize_cost(low$cost_per_ounce))
```

Changing histogram bin width changes the display but none of these statistics.
A histogram shows clustering and potential shape; a boxplot provides a compact
location/spread comparison and flags points according to its convention.

## Practical 3 Association and group comparisons

Five-year annualized returns (percent); SD is in percentage points:

| Objective | n | Mean | Median | SD | Q1 | Q3 |
|---|---:|---:|---:|---:|---:|---:|
| Growth | 158 | 10.148734 | 10.1 | 4.772583 | 7.8 | 12.3 |
| Value | 101 | 11.694059 | 11.7 | 4.007064 | 8.8 | 14.2 |

Value minus Growth mean = 1.545325 percentage points. For the 2001-only task,
means are -18.903165% (Growth) and 0.759406% (Value): the gap is about 19.662571
percentage points. The direction remains, but the magnitudes concern different
return windows, and the five-year figure is annualized rather than a sum.

Expense ratio versus five-year annualized return: 259 complete pairs,
overall r = 0.1416481; Growth r = 0.1069141; Value r = 0.2445624. All three are
positive in these records, with a stronger linear association within Value.
Neither correlation nor its difference across objectives is a causal effect.
No arbitrary universal cutoff is required; credit descriptions grounded in the
scatterplot and coefficients.

Independent risk comparison, in the correct order:

| Risk | n | Median return (%) | IQR (pp) |
|---|---:|---:|---:|
| Very low | 6 | 12.20 | 2.375 |
| Low | 76 | 11.75 | 5.350 |
| Average | 82 | 10.55 | 3.700 |
| High | 80 | 9.40 | 5.400 |
| Very high | 15 | 6.50 | 7.900 |

The smallest groups require particular caution. The historical classification
is not a randomly assigned treatment, and a risk-return relationship here is
not a universal law or forecast.

```r
data_dir <- if (dir.exists("data")) "data" else file.path("..", "data")
funds <- read.csv(file.path(data_dir, "practicals/funds2002.csv"))
library(dplyr)
funds$risk <- factor(funds$risk,
  levels = c("very low", "low", "average", "high", "very high"), ordered = TRUE)
funds |> group_by(objective) |>
  summarise(n = n(), r = cor(expense_ratio_pct, return_5yr_pct),
            mean_2001 = mean(return_2001_pct), .groups = "drop")
funds |> group_by(risk) |>
  summarise(n = n(), median_pct = median(return_5yr_pct),
            IQR_pp = IQR(return_5yr_pct), .groups = "drop")
```

Claims: (1) supported descriptively; (2) distributions overlap; (3) cross-fund
variation is not within-fund volatility; (4) association is not a response to
an intervention; (5) the windows overlap, so not independent-period evidence.

Useful additional information includes selection design, expense-ratio history,
return calculation conventions, asset weights, fund holdings or performance in
nonoverlapping periods. Accept other defensible information needs.

## Assessment guidance

Use the same suggested ten-point scale for each independent briefing:

- 3 points for appropriate methods, displays and grouping.
- 3 points for correct calculations, units and denominators.
- 3 points for findings that answer the business question and acknowledge limits.
- 1 point for a reproducible notebook and clear communication.

A numerically correct output with a causal, population-wide or unit error loses
interpretation credit. Do not grade students on mimicking a single wording or
on the appearance of a preferred shape label for a small dataset. These are
suggested practice rubrics, not changes to official course assessment weights.
