# 307312 Applied Statistics — Extended Case 6 — Harnswell Quality
# Run sections in order from the course root folder containing data/.
# Download the complete course ZIP for the required CSV files.
# Explanations and output interpretation are in the matching course notebook.

# --- case-import ---
source("lessons/_includes/course-tools.R")
rollers <- read.csv("data/business/extended-harnswell.csv")
stopifnot(nrow(rollers) == 150, all(table(rollers$batch) == 5))
LSL <- .5072
USL <- .5075
knitr::kable(head(rollers), digits = 4)

# --- Section 2 ---
knitr::kable(rollers %>% summarise(n = n(), mean = mean(diameter),
  sd = sd(diameter), min = min(diameter), max = max(diameter)), digits = 6)
compliance <- rollers %>% mutate(status = case_when(
  diameter < LSL ~ "Below specification",
  diameter > USL ~ "Above specification",
  TRUE ~ "Within specification")) %>%
  count(status) %>% mutate(percent = 100 * n / sum(n))
knitr::kable(compliance, digits = 2)
ggplot(rollers, aes(diameter)) +
  geom_histogram(binwidth = .0001, boundary = .50715,
                 fill = petra_accent, colour = "white") +
  geom_vline(xintercept = c(LSL, USL), colour = petra_ink, linetype = "dashed") +
  scale_x_continuous(labels = function(x) sprintf("%.4f", x)) +
  labs(x = "Roller diameter (inches)", y = "Rollers")

# --- Section 3 ---
subgroups <- rollers %>% group_by(batch) %>%
  summarise(xbar = mean(diameter), R = max(diameter) - min(diameter),
    n = n(), .groups = "drop") %>% arrange(batch)
stopifnot(all(subgroups$n == 5))
xbarbar <- mean(subgroups$xbar)
Rbar <- mean(subgroups$R)
xlimits <- xbarbar + c(-1, 1) * .577 * Rbar
rlimits <- c(0, 2.114 * Rbar)
knitr::kable(data.frame(chart = c("X-bar", "R"),
  centre = c(xbarbar, Rbar), lower = c(xlimits[1], rlimits[1]),
  upper = c(xlimits[2], rlimits[2])), digits = 7)

# --- Section 4 ---
ggplot(subgroups, aes(batch, R)) + geom_line() + geom_point() +
  geom_hline(yintercept = Rbar, colour = petra_ink) +
  geom_hline(yintercept = rlimits, linetype = "dashed") +
  scale_y_continuous(labels = function(x) sprintf("%.5f", x)) +
  labs(x = "Source batch number", y = "Within-batch range (inches)")
ggplot(subgroups, aes(batch, xbar)) + geom_line() + geom_point() +
  geom_hline(yintercept = xbarbar, colour = petra_ink) +
  geom_hline(yintercept = xlimits, linetype = "dashed") +
  scale_y_continuous(labels = function(x) sprintf("%.5f", x)) +
  labs(x = "Source batch number", y = "Mean diameter (inches)")
flags <- subgroups %>% mutate(xbar_out = xbar < xlimits[1] | xbar > xlimits[2],
  R_out = R < rlimits[1] | R > rlimits[2]) %>% filter(xbar_out | R_out)
knitr::kable(flags, digits = 6)

# --- Section 5 ---
# Run manually once if the packages are not installed:
# # stable_subgroups must come from a justified, documented process phase.
# mu <- mean(stable_subgroups$xbar)
# sigma_within <- mean(stable_subgroups$R) / 2.326
# Cp <- (USL - LSL) / (6 * sigma_within)
# Cpk <- min((USL - mu) / (3 * sigma_within),
#            (mu - LSL) / (3 * sigma_within))
