# 307312 Applied Statistics — Extended Case 5 — Mountain States Potato
# Run sections in order from the course root folder containing data/.
# Download the complete course ZIP for the required CSV files.
# Explanations and output interpretation are in the matching course notebook.

# --- case-import ---
source("lessons/_includes/course-tools.R")
potato <- read.csv("data/business/extended-potato.csv")
stopifnot(nrow(potato) == 54, ncol(potato) == 7, !anyNA(potato))
knitr::kable(head(potato))

# --- Section 2 ---
knitr::kable(data.frame(variable = names(potato),
  mean = sapply(potato, mean), sd = sapply(potato, sd),
  min = sapply(potato, min), max = sapply(potato, max)),
  row.names = FALSE, digits = 3)
knitr::kable(data.frame(measurements = nrow(potato),
  below_12_pct = 100 * mean(potato$solids < 12),
  at_or_below_12_pct = 100 * mean(potato$solids <= 12)), digits = 2)
ggplot(potato, aes(solids)) +
  geom_histogram(binwidth = .5, fill = petra_accent, colour = "white") +
  geom_vline(xintercept = 12, colour = petra_ink, linewidth = 1) +
  labs(x = "Filter-cake solids (%)", y = "Process measurements")

# --- Section 3 ---
knitr::kable(cor(potato), digits = 2)
ggplot(potato, aes(ph, solids)) + geom_point(colour = petra_ink) +
  geom_smooth(method = "lm", formula = y ~ x, colour = petra_ink) +
  labs(x = "pH", y = "Filter-cake solids (%)")

# --- Section 4 ---
full <- lm(solids ~ ph + lower_pressure + upper_pressure +
  cake_thickness + varidriv_speed + drum_speed, data = potato)
summary(full)
confint(full)

# --- Section 5 ---
par(mfrow = c(2, 2))
plot(full)
par(mfrow = c(1, 1))
influence <- data.frame(source_row = seq_len(nrow(potato)),
  cooks_distance = cooks.distance(full), leverage = hatvalues(full))
knitr::kable(head(influence[order(-influence$cooks_distance), ], 5), digits = 3)

# --- Section 6 ---
predictor_names <- names(potato)[names(potato) != "solids"]
vif <- sapply(predictor_names, function(variable) {
  others <- setdiff(predictor_names, variable)
  1 / (1 - summary(lm(reformulate(others, variable), data = potato))$r.squared)
})
knitr::kable(data.frame(predictor = names(vif), VIF = as.numeric(vif)), digits = 2)

# --- Section 7 ---
reduced <- lm(solids ~ ph + cake_thickness + drum_speed, data = potato)
knitr::kable(AIC(full, reduced), digits = 2)
summary(reduced)
