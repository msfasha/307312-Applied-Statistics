# 307312 Applied Statistics — Extended Case 4 — Perfect Parachute
# Run sections in order from the course root folder containing data/.
# Download the complete course ZIP for the required CSV files.
# Explanations and output interpretation are in the matching course notebook.

# --- case-import ---
source("lessons/_includes/course-tools.R")
parachutes <- read.csv("data/business/extended-parachute.csv")
parachutes$supplier <- factor(parachutes$supplier)
stopifnot(nrow(parachutes) == 20, all(table(parachutes$supplier) == 5))
supplier_summary <- parachutes %>% group_by(supplier) %>%
  summarise(n = n(), mean_strength = mean(strength), sd_strength = sd(strength),
    min_strength = min(strength), max_strength = max(strength), .groups = "drop")
knitr::kable(supplier_summary, digits = 2)

# --- Section 2 ---
ggplot(parachutes, aes(supplier, strength)) +
  geom_boxplot(fill = petra_accent, width = .45, outlier.shape = NA) +
  geom_point(position = position_jitter(width = .06, height = 0, seed = 307312)) +
  labs(x = "Fibre supplier", y = "Tensile strength (source scale)")

# --- Section 3 ---
fit <- aov(strength ~ supplier, data = parachutes)
summary(fit)

# --- Section 4 ---
TukeyHSD(fit)

# --- Section 5 ---
par(mfrow = c(1, 2))
plot(fit, which = 1)
plot(fit, which = 2)
par(mfrow = c(1, 1))
fligner.test(strength ~ supplier, data = parachutes)

# --- Section 6 ---
oneway.test(strength ~ supplier, data = parachutes, var.equal = FALSE)
