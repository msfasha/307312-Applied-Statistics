# Render the lesson's ggplot examples without changing publisher or teaching CSVs.
# ggsave() writes plot images; width/height are inches and dpi controls raster resolution.
library(ggplot2)
library(dplyr)
out <- '20261/assets/module01/teaching-slides'
dir.create(out, recursive = TRUE, showWarnings = FALSE)
save_plot <- function(name, p) {
  # theme() changes display only; larger text stays readable when projected.
  # ggsave() exports a fixed-size PNG; the original data and geometry remain intact.
  p <- p + theme(text = element_text(size = 16, family = 'DejaVu Sans'))
  ggsave(file.path(out, paste0(name, '.png')), p, width = 12, height = 5.8,
         units = 'in', dpi = 150, bg = 'white')
}
# labs() clarifies the original dataset units, without altering values or mappings.
# Reuse this labelled scatterplot for appearance and layering demonstrations.
base <- ggplot(mtcars, aes(wt, mpg)) +
  labs(x = 'Vehicle weight (1,000 lb)', y = 'Miles per US gallon')
save_plot('labels', base + geom_point() + labs(title = 'Car Weight vs. Fuel Efficiency'))
save_plot('color', ggplot(mtcars, aes(wt, mpg, color = factor(cyl), shape = factor(cyl))) +
  geom_point() + labs(x = 'Vehicle weight (1,000 lb)', y = 'Miles per US gallon',
                     color = 'Cylinders', shape = 'Cylinders'))
save_plot('limits', ggplot(mtcars, aes(wt, mpg, color = factor(cyl))) + geom_point() +
  xlim(2,5) + ylim(10,35) + labs(x = 'Vehicle weight (1,000 lb)', y = 'Miles per US gallon'))
save_plot('group-lines', ggplot(mtcars, aes(wt, mpg, color = factor(cyl))) +
  geom_point() + geom_smooth(method = 'lm', se = FALSE) +
  labs(x = 'Vehicle weight (1,000 lb)', y = 'Miles per US gallon', color = 'Cylinders'))
save_plot('one-line', base + geom_point(aes(color = factor(cyl))) +
  geom_smooth(method = 'lm', se = FALSE) + labs(color = 'Cylinders'))
save_plot('wrap', base + geom_point() + facet_wrap(~ cyl))
save_plot('grid', base + geom_point() + facet_grid(vs ~ am))
save_plot('scatter', base + geom_point())
save_plot('line', base + geom_line() + geom_point())
save_plot('smooth', base + geom_smooth(method = 'lm'))
save_plot('bar', ggplot(mpg, aes(class)) + geom_bar() + labs(x = 'Vehicle class', y = 'Count'))
save_plot('histogram', ggplot(mtcars, aes(mpg)) + geom_histogram(bins = 10) +
  labs(x = 'Miles per US gallon', y = 'Count'))
save_plot('boxplot', ggplot(mpg, aes(class, hwy)) + geom_boxplot() +
  labs(x = 'Vehicle class', y = 'Highway miles per US gallon'))
save_plot('box-variants', ggplot(mtcars, aes(y = mpg)) + geom_boxplot() +
  facet_wrap(~ cyl) + labs(y = 'Miles per US gallon', title = 'Box Plot of MPG by Cylinder Count') + theme_bw())
save_plot('area', ggplot(economics, aes(date, unemploy)) + geom_area() +
  labs(x = 'Date', y = 'Unemployed persons (thousands)'))
save_plot('density', ggplot(mpg, aes(hwy)) + geom_density() +
  labs(x = 'Highway miles per US gallon', y = 'Density'))
save_plot('violin', ggplot(mpg, aes(class, hwy)) + geom_violin() +
  labs(x = 'Vehicle class', y = 'Highway miles per US gallon'))
save_plot('column', ggplot(mpg, aes(class, hwy)) + geom_col() +
  labs(x = 'Vehicle class', y = 'Stacked row hwy values (not a mean)'))
# set.seed() fixes the generated illustration for a repeatable exported figure.
# expand.grid()/runif() reproduce the lesson's artificial grid and value range.
set.seed(307312)
data <- expand.grid(Var1 = letters[1:10], Var2 = 1:10)
data$value <- runif(100, min = 0, max = 100)
save_plot('tile', ggplot(data, aes(Var1, Var2, fill = value)) + geom_tile() +
  labs(caption = 'Simulated illustration; uniform values from 0 to 100'))
save_plot('text', base + aes(label = rownames(mtcars)) + geom_text(vjust = -0.5))
save_plot('label', base + aes(label = rownames(mtcars)) + geom_label(vjust = -0.5))
# The ribbon is exactly y +/- 0.5, as in the lesson; no interval is estimated.
# set.seed() makes the random normal noise repeatable in the exported illustration.
set.seed(307313)
df <- data.frame(x = 1:100)
df$y <- sin(df$x / 10) * 2 + rnorm(100, sd = 0.5)
df$ymax <- df$y + 0.5
df$ymin <- df$y - 0.5
save_plot('ribbon', ggplot(df, aes(x = x, ymin = ymin, ymax = ymax, y = y)) +
  geom_ribbon(alpha = 0.4) + geom_line() +
  labs(caption = 'Simulated illustration; fixed +/-0.5 band, not a confidence interval'))
set.seed(307314)
save_plot('jitter', ggplot(mpg, aes(class, hwy)) + geom_jitter(width = 0.2) +
  labs(x = 'Vehicle class', y = 'Highway miles per US gallon'))
save_plot('bubble', base + aes(size = hp) + geom_point(alpha = 0.5) +
  scale_size_continuous(range = c(1,20)) + labs(size = 'Horsepower') + theme_minimal())
# Check the Restaurant dependency and source lesson calculations using the CSV.
# stopifnot() stops on a failed condition; the data file itself is not modified.
restaurants <- read.csv('20261/data/module02/restaurant_ratings.csv')
restaurants$quality_rating <- factor(restaurants$quality_rating,
  levels = c('Good','Very Good','Excellent'), ordered = TRUE)
group_summary <- restaurants |> group_by(quality_rating) |>
  summarise(n=n(),mean_price_usd=mean(meal_price_usd),median_price_usd=median(meal_price_usd),.groups='drop')
stopifnot(nrow(restaurants)==300, sum(group_summary$n)==300,
          !anyNA(restaurants), !anyDuplicated(restaurants$restaurant_id))
cat('Rendered',length(list.files(out,pattern='[.]png$')),'plots; Restaurant checks passed.\n')
