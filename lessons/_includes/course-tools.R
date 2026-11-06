# Shared course functions. No hidden imports or working-directory changes.
suppressPackageStartupMessages(library(dplyr))
suppressPackageStartupMessages(library(ggplot2))
petra_ink <- '#4B4B4B'
petra_accent <- '#D4D4D4'
petra_categories <- c(Furniture = '#3B6B8A', 'Office Supplies' = '#777777', Technology = '#B56A3A')
petra_display <- c(Normal = '#777777', 'End aisle' = '#3B6B8A')
theme_set(theme_minimal(base_size = 12) +
  theme(panel.grid.minor = element_blank(),
        plot.title = element_text(colour = '#262626', face = 'bold'),
        axis.title = element_text(colour = '#303030'), legend.position = 'bottom',
        plot.margin = margin(10, 24, 10, 10)))
make_orders <- function(lines) {
  # Refuse to silently take the first value of inconsistent order attributes.
  attributes <- c('customer_id','order_date','ship_date','ship_mode','region','segment','return_status')
  agreement <- lines %>% group_by(order_id) %>%
    summarise(across(all_of(attributes), n_distinct), .groups = 'drop')
  stopifnot(all(as.matrix(agreement[attributes]) == 1))
  lines %>% group_by(order_id) %>%
    summarise(across(all_of(attributes), first),
      sales = sum(sales), profit = sum(profit), quantity = sum(quantity),
      line_count = n(), .groups = 'drop') %>%
    mutate(order_date = as.Date(order_date), ship_date = as.Date(ship_date),
      ship_days = as.numeric(ship_date - order_date),
      loss_order = profit < 0, listed_return = return_status == 'Listed return',
      margin_pct = 100 * profit / sales)
}
