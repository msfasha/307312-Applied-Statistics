# 307312 Applied Statistics — Extended Case 3 — BLK Retail Display
# Run sections in order from the course root folder containing data/.
# Download the complete course ZIP for the required CSV files.
# Explanations and output interpretation are in the matching course notebook.

# --- case-import ---
source("lessons/_includes/course-tools.R")
cola <- read.csv("data/business/cola.csv")
cola$display <- factor(cola$display, levels = c("Normal", "End aisle"))
normal <- cola$weekly_cases[cola$display == "Normal"]
end <- cola$weekly_cases[cola$display == "End aisle"]
stopifnot(length(normal) == 10, length(end) == 10)
knitr::kable(cola %>% group_by(display) %>%
  summarise(stores = n(), mean_cases = mean(weekly_cases),
    sd_cases = sd(weekly_cases), .groups = "drop"), digits = 2)

# --- Section 2 ---
ggplot(cola, aes(display, weekly_cases)) +
  geom_boxplot(fill = petra_accent, width = .45, outlier.shape = NA) +
  geom_point(position = position_jitter(width = .07, height = 0, seed = 307312),
             colour = petra_ink) +
  labs(x = "Display", y = "Cases sold per store per week")
welch <- t.test(end, normal, var.equal = FALSE)
knitr::kable(data.frame(difference = mean(end) - mean(normal),
  lower_95 = welch$conf.int[1], upper_95 = welch$conf.int[2],
  p_value = welch$p.value), digits = 4)

# --- Section 3 ---
par(mfrow = c(1, 2))
qqnorm(normal, main = "Normal shelf: Q-Q plot"); qqline(normal)
qqnorm(end, main = "End aisle: Q-Q plot"); qqline(end)
par(mfrow = c(1, 1))

# --- Section 4 ---
# Run manually once if the packages are not installed:
# margin_per_case <- c(4, 6, 8)
# display_cost <- 80
# # For each assumed margin, calculate:
# # estimated net contribution = estimated case difference * margin - cost
# # corresponding interval endpoints = Welch endpoints * margin - cost
# # break-even additional cases = cost / margin
