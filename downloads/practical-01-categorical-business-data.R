# 307312 Applied Statistics — Practical 1 — Superstore product mix
# Run sections in order from the course root folder containing data/.
# Download the complete course ZIP for the required CSV files.
# Explanations and output interpretation are in the matching course notebook.

# --- categorical-import ---
source("lessons/_includes/course-tools.R")
lines <- read.csv("data/business/superstore-lines.csv",
                  stringsAsFactors = FALSE, colClasses = c(postal_code = "character"))
orders <- make_orders(lines)
c(lines = nrow(lines), orders = nrow(orders), customers = n_distinct(lines$customer_id))
colSums(is.na(lines))

# --- Section 2 ---
knitr::kable(head(lines[c("order_id", "category", "sub_category", "segment", "region")]))

# --- Section 3 ---
category_mix <- lines %>% count(category, name = "line_count") %>%
  mutate(line_pct = 100 * line_count / sum(line_count))
knitr::kable(category_mix, digits = 1)

ggplot(category_mix, aes(reorder(category, line_count), line_count)) +
  geom_col(fill = petra_ink) + coord_flip() +
  labs(x = NULL, y = "Product lines")

# --- Section 4 ---
category_sales <- lines %>% group_by(category) %>%
  summarise(total_sales = sum(sales), total_units = sum(quantity), .groups = "drop") %>%
  mutate(sales_pct = 100 * total_sales / sum(total_sales))
knitr::kable(category_sales, digits = 1)

# --- Section 5 ---
counts <- xtabs(~ segment + category, data = lines)
row_percent <- 100 * prop.table(counts, margin = 1)
knitr::kable(counts)
knitr::kable(row_percent, digits = 1)

# --- Section 6 ---
plot_mix <- lines %>% count(segment, category) %>%
  group_by(segment) %>% mutate(percent = 100 * n / sum(n)) %>% ungroup()
ggplot(plot_mix, aes(segment, percent, fill = category)) +
  geom_col() + scale_fill_manual(values = petra_categories) +
  labs(x = NULL, y = "Product lines within segment (%)", fill = "Category")

# --- Section 7 ---
shipping <- orders %>% count(ship_days, name = "order_count") %>%
  arrange(ship_days) %>%
  mutate(percent = 100 * order_count / sum(order_count), cumulative_pct = cumsum(percent))
knitr::kable(shipping, digits = 1)
ggplot(shipping, aes(ship_days, cumulative_pct)) +
  geom_step(colour = petra_ink) + geom_point(colour = petra_ink) +
  labs(x = "Days from order to dispatch", y = "Orders dispatched within this duration (%)")

# --- Section 8 ---
return_mix <- orders %>% count(return_status, name = "order_count") %>%
  mutate(percent = 100 * order_count / sum(order_count))
knitr::kable(return_mix, digits = 2)

# --- Section 9 ---
# Run manually once if the packages are not installed:
# # Use orders for these questions.
# # Start with count(region), then xtabs(~ region + ship_mode, data = orders).
# # For a group proportion: mean(ship_days <= 4) within each region.
