# 307312 Applied Statistics — Practical 3 — Superstore discounts and profit
# Run sections in order from the course root folder containing data/.
# Download the complete course ZIP for the required CSV files.
# Explanations and output interpretation are in the matching course notebook.

# --- association-import ---
source("lessons/_includes/course-tools.R")
lines <- read.csv("data/business/superstore-lines.csv",
                  stringsAsFactors = FALSE, colClasses = c(postal_code = "character"))
orders <- make_orders(lines)
lines <- lines %>% mutate(
  line_margin_pct = 100 * profit / sales,
  loss_line = profit < 0,
  discount_band = cut(discount, breaks = c(-Inf, 0, .2, Inf),
    labels = c("None", "Above 0 to 20%", "Above 20%"), ordered_result = TRUE))
stopifnot(!anyNA(lines$discount_band), all(lines$sales > 0))

# --- Section 2 ---
category_results <- lines %>% group_by(category) %>%
  summarise(line_count = n(), total_sales = sum(sales), total_profit = sum(profit),
            median_line_profit = median(profit), loss_line_pct = 100 * mean(loss_line),
            .groups = "drop") %>%
  mutate(overall_margin_pct = 100 * total_profit / total_sales)
knitr::kable(category_results, digits = 2)
ggplot(category_results, aes(category, overall_margin_pct)) +
  geom_col(fill = petra_ink) +
  labs(x = NULL, y = "Total profit / total sales (%)")

# --- Section 3 ---
margin_comparison <- lines %>% group_by(category) %>%
  summarise(equal_line_mean_margin_pct = mean(line_margin_pct),
            sales_weighted_margin_pct = 100 * sum(profit) / sum(sales), .groups = "drop")
knitr::kable(margin_comparison, digits = 2)

# --- Section 4 ---
discount_results <- lines %>% group_by(discount_band) %>%
  summarise(line_count = n(), total_sales = sum(sales), total_profit = sum(profit),
            median_line_profit = median(profit), loss_line_pct = 100 * mean(loss_line),
            .groups = "drop") %>%
  mutate(overall_margin_pct = 100 * total_profit / total_sales)
knitr::kable(discount_results, digits = 2)
ggplot(lines, aes(discount_band, line_margin_pct)) +
  geom_hline(yintercept = 0, colour = "#A3A3A3") +
  geom_boxplot(fill = petra_accent, outlier.alpha = .25) +
  labs(x = "Recorded line discount", y = "Line profit / line sales (%)")

# --- Section 5 ---
within_category <- lines %>% group_by(category, discount_band) %>%
  summarise(line_count = n(), margin_pct = 100 * sum(profit) / sum(sales),
            .groups = "drop")
knitr::kable(within_category, digits = 2)
ggplot(within_category, aes(discount_band, margin_pct)) +
  geom_col(fill = petra_ink) + facet_wrap(~ category) +
  scale_x_discrete(labels = c("None" = "0%", "Above 0 to 20%" = "(0,20%]",
                               "Above 20%" = ">20%")) +
  labs(x = "Discount band", y = "Group overall margin (%)")

# --- Section 6 ---
ggplot(orders, aes(sales, profit)) +
  geom_hline(yintercept = 0, colour = "#A3A3A3") +
  geom_point(alpha = .35, colour = petra_ink) +
  labs(x = "Order sales ($)", y = "Order profit ($)")

correlations <- orders %>% group_by(segment) %>%
  summarise(orders = n(), pearson_r = cor(sales, profit),
            spearman_r = cor(sales, profit, method = "spearman"), .groups = "drop")
knitr::kable(correlations, digits = 3)

# --- Section 7 ---
# Run manually once if the packages are not installed:
# # Use lines for product/discount questions and orders for basket questions.
# # A group loss percentage is 100 * mean(profit < 0).
# # Calculate rates before overwriting any column with a group total.
