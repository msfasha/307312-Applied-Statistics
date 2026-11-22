# 307312 Applied Statistics — Practical 2 — Superstore order size
# Run sections in order from the course root folder containing data/.
# Download the complete course ZIP for the required CSV files.
# Explanations and output interpretation are in the matching course notebook.

# --- numerical-import ---
source("lessons/_includes/course-tools.R")
lines <- read.csv("data/business/superstore-lines.csv",
                  stringsAsFactors = FALSE, colClasses = c(postal_code = "character"))
orders <- make_orders(lines)
stopifnot(nrow(orders) == n_distinct(lines$order_id),
          isTRUE(all.equal(sum(orders$sales), sum(lines$sales))))
knitr::kable(head(orders[c("order_id", "sales", "profit", "quantity", "line_count")] ), digits = 2)

# --- Section 2 ---
ggplot(orders, aes(sales)) +
  geom_histogram(bins = 35, fill = petra_ink, colour = "white") +
  labs(x = "Order sales (USD)", y = "Orders")

# --- Section 3 ---
ggplot(orders, aes(sales)) +
  geom_histogram(bins = 25, fill = petra_ink, colour = "white") +
  scale_x_log10() + labs(x = "Order sales ($; log10 axis)", y = "Orders")

# --- Section 4 ---
x <- orders$sales
summary_table <- data.frame(
  statistic = c("Orders", "Mean (USD)", "Median (USD)", "Sample SD (USD)",
                "Minimum (USD)", "Q1 (USD)", "Q3 (USD)", "Maximum (USD)", "IQR (USD)"),
  value = c(length(x), mean(x), median(x), sd(x), min(x),
            quantile(x, .25, type = 7), quantile(x, .75, type = 7), max(x), IQR(x)))
knitr::kable(summary_table, digits = 2)

# --- Section 5 ---
c(total_sales = sum(x), mean_times_orders = mean(x) * length(x),
  median_times_orders = median(x) * length(x))

# --- Section 6 ---
c(range_dollars = diff(range(x)),
  mean_absolute_deviation = mean(abs(x - mean(x))),
  coefficient_of_variation_pct = 100 * sd(x) / mean(x))

# --- Section 7 ---
knitr::kable(data.frame(percentile = c("50th", "75th", "90th", "95th", "99th"),
  order_sales = as.numeric(quantile(x, c(.5, .75, .9, .95, .99), type = 7))), digits = 2)

# --- Section 8 ---
ggplot(orders, aes(x = "All orders", y = sales)) +
  geom_boxplot(fill = petra_accent, outlier.alpha = .3) +
  labs(x = NULL, y = "Order sales (USD)")

quartiles <- quantile(x, c(.25, .75), type = 7)
lower_fence <- quartiles[1] - 1.5 * IQR(x)
upper_fence <- quartiles[2] + 1.5 * IQR(x)
flagged <- orders %>% filter(sales < lower_fence | sales > upper_fence)
c(lower_fence = lower_fence, upper_fence = upper_fence, flagged_orders = nrow(flagged))

# --- Section 9 ---
knitr::kable(orders %>% arrange(desc(sales)) %>%
  select(order_id, sales, profit, line_count, quantity) %>% head(5), digits = 2)

# --- Section 10 ---
central_orders <- orders %>% filter(sales >= lower_fence, sales <= upper_fence)
knitr::kable(data.frame(
  scope = c("Full frame — primary result", "Within IQR fences — sensitivity only"),
  n = c(nrow(orders), nrow(central_orders)),
  mean_sales = c(mean(orders$sales), mean(central_orders$sales)),
  median_sales = c(median(orders$sales), median(central_orders$sales))), digits = 2)

# --- Section 11 ---
# Run manually once if the packages are not installed:
# # group_by(region) %>% summarise(...) builds the regional table.
# # arrange(desc(sales)) ranks order records.
# # An explicit rule is to take ceiling(0.10 * nrow(orders)) highest-ranked orders.
