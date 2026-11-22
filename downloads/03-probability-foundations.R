# 307312 Applied Statistics — Probability foundations
# Run sections in order from the course root folder containing data/.
# Download the complete course ZIP for the required CSV files.
# Explanations and output interpretation are in the matching course notebook.

# --- inferential-1-15 ---
# rep() assigns equal mass to the six fair-die outcomes; sum() adds the selected probabilities.
# %in% selects even outcomes; the second selection includes both endpoints 2 and 5.
outcomes <- 1:6
probability <- rep(1/6, 6)
c(three = probability[3], even = sum(probability[outcomes %in% c(2,4,6)]),
  between_2_and_5 = sum(probability[outcomes >= 2 & outcomes <= 5]))

# --- inferential-1-16 ---
# dbinom() gives exact counts; pbinom() gives cumulative probabilities for 80 independent cars.
# less than 2 means X<=1; lower.tail=FALSE computes P(X>2), using the stated defect probability 0.02.
c(exactly_2 = dbinom(2, size=80, prob=0.02), less_than_2 = pbinom(1,80,0.02),
  more_than_2 = pbinom(2,80,0.02,lower.tail=FALSE), no_defects = dbinom(0,80,0.02))

# --- inferential-1-17 ---
# Compare success probabilities at n = 10, then increase n to 100.
# Save the current plotting layout so it can be restored afterwards.
old_par <- par(mfrow = c(2, 2), mar = c(4, 4, 3, 1))
trial_counts <- c(10, 10, 10, 100)
success_probs <- c(0.2, 0.5, 0.8, 0.5)
for (i in 1:4) {
  n <- trial_counts[i]
  p <- success_probs[i]
  x <- 0:n
  probabilities <- dbinom(x = x, size = n, prob = p)
  plot(x = x, y = probabilities, type = "h", lwd = 3,
       col = "#595959", xlab = "Number of successes",
       ylab = "Probability", main = paste("n =", n, "; p =", p))
  if (n == 10 && p == 0.5) {
    # Highlight the question: exactly two heads in ten fair tosses.
    segments(x0 = 2, y0 = 0, x1 = 2,
             y1 = dbinom(x = 2, size = n, prob = p),
             col = "#763D52", lwd = 4)
  }
}
par(old_par)
dbinom(x = 2, size = 10, prob = 0.5)

# --- inferential-1-18 ---
# ppois() uses the stated one-hour mean lambda=1000 under a homogeneous Poisson model.
# lower.tail=FALSE gives P(X>1100), so exactly 1100 calls does not exceed capacity.
ppois(1100, lambda=1000, lower.tail=FALSE)

# --- inferential-1-19 ---
# Compare a small expected count with the calculator example, lambda = 20.
old_par <- par(mfrow = c(1, 2), mar = c(4, 4, 3, 1))
lambda_values <- c(2, 20)
for (lambda in lambda_values) {
  # Display counts through the 99.9th percentile; a small right tail is omitted.
  x <- 0:qpois(p = 0.999, lambda = lambda)
  probabilities <- dpois(x = x, lambda = lambda)
  plot(x = x, y = probabilities, type = "h", lwd = 3,
       col = "#595959", xlab = "Number of events",
       ylab = "Probability", main = paste("Poisson: lambda =", lambda))
  if (lambda == 20) {
    segments(x0 = 15, y0 = 0, x1 = 15,
             y1 = dpois(x = 15, lambda = lambda),
             col = "#763D52", lwd = 4)
  }
}
par(old_par)
dpois(x = 15, lambda = 20)

# --- inferential-1-22 ---
# Exact interval probabilities from the two stated continuous uniform models.
c(arrival_before_9 = punif(q = 9, min = 8, max = 12),
  diameter_above_10_1 = punif(q = 10.1, min = 9.8, max = 10.2,
                             lower.tail = FALSE))
# Plot density heights; shaded areas represent the required probabilities.
old_par <- par(mfrow = c(1, 2), mar = c(4, 4, 3, 1))
plot(x = c(8, 12), y = c(0, 0.30), type = "n",
     xlab = "Arrival hour", ylab = "Density", main = "Arrive before 9 AM")
rect(xleft = 8, ybottom = 0, xright = 9, ytop = 1 / (12 - 8),
     col = "#D8D8D8", border = NA)
segments(x0 = 8, y0 = 0.25, x1 = 12, y1 = 0.25,
         col = "#763D52", lwd = 3)
plot(x = c(9.8, 10.2), y = c(0, 3), type = "n",
     xlab = "Diameter (mm)", ylab = "Density", main = "Diameter above 10.1 mm")
rect(xleft = 10.1, ybottom = 0, xright = 10.2, ytop = 1 / (10.2 - 9.8),
     col = "#D8D8D8", border = NA)
segments(x0 = 9.8, y0 = 2.5, x1 = 10.2, y1 = 2.5,
         col = "#763D52", lwd = 3)
par(old_par)

# --- inferential-1-28 ---
# c() collects the two approximate expected counts, using the original 95% empirical-rule approximation.
# These are normal-model approximations for 280 students, not observed counts.
c(between_58_and_90 = 280*0.95, above_90 = 280*0.025)

# --- inferential-1-30 ---
# Standardization subtracts the stated course mean and divides by that course's SD.
# Both exam scores are 90; a larger z-score means a higher position relative to the course mean.
c(Python = (90-70)/10, Database = (90-80)/10)

# --- inferential-1-31 ---
# set.seed() makes rnorm() reproducible; the 2,000 simulated values use the source mean 25 and SD 8.
# MASS::fitdistr() fits three candidate families by maximum likelihood; this is a limited R comparison.
set.seed(307312)
y <- rnorm(2000, mean=25, sd=8)
# lapply() passes each family name to the anonymous function and collects its fitted model.
fits <- lapply(c("normal","logistic","cauchy"), function(family) MASS::fitdistr(y, family))
# AIC() trades fit against parameter count; lower AIC only compares these candidates, not all distributions.
# sapply() applies AIC to each fitted object; names label the results for interpretation.
aic <- sapply(fits, AIC)
names(aic) <- c("normal","logistic","cauchy")
aic

# --- inferential-1-36 ---
# pnorm() integrates the stated normal model: mean 70, SD 6, and a score threshold of 75.
# lower.tail=FALSE gives P(score>75) directly, without rounding the z-score to a table entry.
pnorm(75, mean=70, sd=6, lower.tail=FALSE)

# --- inferential-1-37 ---
# The question on this slide asks for a score above 90.
p_above_90 <- pnorm(q=90, mean=70, sd=6, lower.tail=FALSE)
c(probability=p_above_90, percentage=100*p_above_90)
