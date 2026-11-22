# 307312 Applied Statistics — Extended Case 2 — Oxford Cereal
# Run sections in order from the course root folder containing data/.
# Download the complete course ZIP for the required CSV files.
# Explanations and output interpretation are in the matching course notebook.

# --- case-import ---
source("lessons/_includes/course-tools.R")
oxford <- read.csv("data/business/extended-oxford-summary.csv")
knitr::kable(oxford)
n <- oxford$n[1]
xbar <- oxford$sample_mean_g[1]
sigma <- oxford$population_sd_g[1]
mu0 <- oxford$target_mean_g[1]
alpha <- oxford$alpha[1]
stopifnot(n == 25, sigma == 15, mu0 == 368, xbar == 372.5)

# --- Section 2 ---
se <- sigma / sqrt(n)
knitr::kable(data.frame(sample_size = n, sample_mean_g = xbar,
  difference_from_target_g = xbar - mu0, process_sd_g = sigma,
  standard_error_g = se), digits = 2)

# --- Section 3 ---
set.seed(42001)
sim_means <- replicate(10000, mean(rnorm(n, mean = mu0, sd = sigma)))
ggplot(data.frame(sample_mean = sim_means), aes(sample_mean)) +
  geom_histogram(bins = 35, fill = petra_accent, colour = "white") +
  geom_vline(xintercept = xbar, colour = petra_ink, linewidth = 1) +
  labs(x = "Mean of 25 simulated boxes (g)", y = "Simulated samples")

# --- Section 4 ---
z <- (xbar - mu0) / se
p_value <- 2 * pnorm(-abs(z))
ci <- xbar + c(-1, 1) * qnorm(1 - alpha / 2) * se
knitr::kable(data.frame(z = z, p_value = p_value,
  lower_mean_g = ci[1], upper_mean_g = ci[2], reject = p_value < alpha), digits = 4)

# --- Section 5 ---
# Run manually once if the packages are not installed:
# # Independent task: change the summary inputs and label the scenario hypothetical.
# # Use (sample_mean - target) / (known_sd / sqrt(sample_size)).
