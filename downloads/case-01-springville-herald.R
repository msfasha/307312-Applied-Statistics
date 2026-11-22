# 307312 Applied Statistics — Extended Case 1 — Springville Herald
# Run sections in order from the course root folder containing data/.
# Download the complete course ZIP for the required CSV files.
# Explanations and output interpretation are in the matching course notebook.

# --- case-import ---
source("lessons/_includes/course-tools.R")
calls <- read.csv("data/business/extended-herald-calls.csv")
marketing <- read.csv("data/business/extended-herald-marketing.csv")
subscriptions <- read.csv("data/business/extended-herald-subscriptions.csv")
stopifnot(nrow(calls) == 90, nrow(marketing) == 24, nrow(subscriptions) == 24)
knitr::kable(data.frame(file = c("SH2", "SH13", "SH16"),
  observations = c(nrow(calls), nrow(marketing), nrow(subscriptions)),
  unit = c("Day", "Month: marketing", "Month: subscription base")))

# --- Section 2 ---
call_summary <- calls %>% summarise(days = n(), mean_calls = mean(calls),
  median_calls = median(calls), sd_calls = sd(calls),
  min_calls = min(calls), max_calls = max(calls))
knitr::kable(call_summary, digits = 2)
ggplot(calls, aes(calls)) +
  geom_histogram(binwidth = 10, boundary = 0, fill = petra_ink, colour = "white") +
  labs(x = "Telephone calls per day", y = "Days")

# --- Section 3 ---
knitr::kable(data.frame(variable = c("Hours per month", "New subscriptions per month"),
  mean = sapply(marketing, mean), sd = sapply(marketing, sd),
  min = sapply(marketing, min), max = sapply(marketing, max)),
  row.names = FALSE, digits = 2)
ggplot(marketing, aes(hours, new_subscriptions)) +
  geom_point(colour = petra_ink) + geom_smooth(method = "lm", formula = y ~ x, colour = petra_ink) +
  labs(x = "Telemarketing hours per month", y = "New subscriptions per month")
model <- lm(new_subscriptions ~ hours, data = marketing)
summary(model)
confint(model)

# --- Section 4 ---
new_month <- data.frame(hours = 1200)
knitr::kable(predict(model, newdata = new_month, interval = "confidence"), digits = 1)
knitr::kable(predict(model, newdata = new_month, interval = "prediction"), digits = 1)
range(marketing$hours)
par(mfrow = c(2, 2))
plot(model)
par(mfrow = c(1, 1))

# --- Section 5 ---
subscriptions <- subscriptions %>% arrange(month)
ggplot(subscriptions, aes(month, subscriptions)) +
  geom_line(colour = petra_ink) + geom_point() +
  labs(x = "Source month number", y = "Home-delivery subscriptions")
trend <- lm(subscriptions ~ month, data = subscriptions)
future <- data.frame(month = 25:28)
knitr::kable(cbind(future, predict(trend, future, interval = "prediction")), digits = 0)
plot(subscriptions$month, residuals(trend), type = "b",
     xlab = "Source month number", ylab = "Trend residual (subscriptions)")
abline(h = 0, col = petra_ink)
acf(residuals(trend), main = "Trend residual autocorrelation")
