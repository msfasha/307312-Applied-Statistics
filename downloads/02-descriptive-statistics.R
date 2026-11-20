# 307312 Applied Statistics — Descriptive Statistics
# Run sections in order from the course root folder containing data/.
# Download the complete course ZIP for the required CSV files.
# Explanations and output interpretation are in the matching course notebook.

# --- r-slide-16 ---
# read.csv() imports the supplied CSV; stringsAsFactors=FALSE keeps category labels as text.
# head() previews six rows; height is in cm, weight in kg, and age in years.
# Open the course folder in Positron; paths start in that folder.
students <- read.csv("data/descriptive-statistics/students.csv", stringsAsFactors = FALSE)
head(students)

# --- r-slide-17 ---
# table() counts students in each country category; prop.table() divides by all counted students.
# Multiplying by 100 gives percentages; cumsum() is meaningful only when categories have an order.
country_counts <- table(students$country)
country_counts
100 * prop.table(country_counts)

# --- r-slide-18 ---
# cut() converts ages in years into intervals; right=FALSE includes the lower boundary, not the upper.
# table() counts each interval; these explicitly chosen bands are an added R illustration.
age_groups <- cut(students$age, breaks = c(0, 20, 25, 30, Inf), right = FALSE)
table(age_groups)

# --- r-slide-19 ---
# xtabs() counts combinations: the formula ~ major + gender creates a two-way frequency table.
# addmargins() adds row and column totals without changing the underlying counts.
major_gender <- xtabs(~ major + gender, data = students)
addmargins(major_gender)

# --- r-slide-23 ---
# barplot() draws a bar for each category count supplied by table().
# las=2 rotates country labels; ylab states that bar heights are numbers of students.
barplot(table(students$country), las = 2, col = "#356B8C", ylab = "Number of students")

# --- r-slide-24 ---
# pie() divides the circle according to the country counts computed by table().
# The denominator is all students with a recorded country category, including Other.
pie(table(students$country))

# --- r-slide-26 ---
# table() cross-classifies gender and country; barplot(beside=TRUE) places gender bars side by side.
# legend.text=TRUE labels the groups; counts, rather than percentages, determine bar heights.
barplot(table(students$gender, students$country), beside = TRUE, legend.text = TRUE,
        col = c("#356B8C", "#C47735"), ylab = "Number of students", las = 2)

# --- r-slide-added-line-chart ---
# The time-series object supplies the monthly time order; no CSV import is needed.
plot(x = AirPassengers, type = "o", pch = 16, cex = 0.4,
     col = "#595959", xlab = "Year", ylab = "Passengers (thousands)",
     main = "Monthly international airline passengers")

# --- r-slide-added-dot-plot ---
# Keep original row order; these records are not a random sample.
age_small <- head(x = students$age, n = 30)
stripchart(x = age_small, method = "stack", offset = 0.7, pch = 16,
           col = "#595959", xlab = "Age (years)",
           main = "Ages in the first 30 student records")

# --- r-slide-28 ---
# hist() groups ages into bins; breaks specifies yearly boundaries at half-year positions.
# freq=TRUE displays counts rather than probability density; recorded ages are measured in years.
hist(students$age, breaks = seq(min(students$age) - 0.5, max(students$age) + 0.5, by = 1),
     freq = TRUE, col = "#356B8C", main = "", xlab = "Age (years)")

# --- r-slide-33 ---
# plot(x,y) makes a scatterplot, with height on the horizontal axis and weight on the vertical.
# pch=16 uses filled points; no fitted line or causal relationship is assumed.
plot(students$height, students$weight, pch = 16, col = "#356B8C",
     xlab = "Height (cm)", ylab = "Weight (kg)")

# --- r-slide-42 ---
# mean() and median() summarize ages; table() counts each recorded age to identify every tied mode.
# names() returns the ages whose counts equal max(), the greatest frequency.
mean(students$age)
median(students$age)
age_counts <- table(students$age)
names(age_counts)[age_counts == max(age_counts)]

# --- r-slide-50 ---
# diff(range()) gives maximum minus minimum; mean(abs()) calculates mean absolute deviation.
# var() and sd() use the sample denominator n-1; R's mad() instead computes median absolute deviation.
age <- students$age
c(range = diff(range(age)), mean_absolute_deviation = mean(abs(age - mean(age))),
  sample_variance = var(age), sample_standard_deviation = sd(age))

# --- r-slide-55 ---
# c() creates the exact two datasets shown in the original table; sd() uses the sample denominator n-1.
# sd()/mean() expresses CV as a ratio, without multiplying by 100; these means are positive.
DS1 <- c(10, 20, 30, 40, 50)
DS2 <- c(1010, 1020, 1030, 1040, 1050)
c(DS1 = sd(DS1) / mean(DS1), DS2 = sd(DS2) / mean(DS2))

# --- r-slide-63 ---
# cov() calculates sample covariance and cor() calculates Pearson's linear correlation by default.
# use="complete.obs" omits pairs with missing values; units remain cm, kg, and years.
cov(students$height, students$weight, use = "complete.obs")
cor(students$height, students$weight, use = "complete.obs")
cov(students$height, students$age, use = "complete.obs")
cor(students$height, students$age, use = "complete.obs")

# --- r-slide-68 ---
# e1071::skewness() measures the asymmetry of the age distribution.
e1071::skewness(students$age)

# --- r-slide-72 ---
# quantile() finds percentiles; probs=0.90 requests the 90th percentile of height in cm.
quantile(students$height, probs = 0.90)

# --- r-slide-74 ---
# quantile(probs=c(0.25,0.50)) returns the first quartile and median of height in cm.
quantile(students$height, probs = c(0.25, 0.50))

# --- r-slide-76 ---
# boxplot(height~gender) compares groups; whiskers extend to the last data within 1.5 IQR of the hinges.
# subset() selects Turkish/Russian males; R's default boxplot hinges can differ from the quartiles returned by quantile().
boxplot(height ~ gender, data = students, ylab = "Height (cm)", col = "#D4D4D4")
# The source spells Russia as "Russa"; match that original label without changing the data.
males <- subset(students, gender == "Male" & country %in% c("Turkey", "Russa"))
boxplot(height ~ country, data = males, ylab = "Height (cm)", col = "#D4D4D4")

# --- r-slide-79 ---
# quantile() supplies quartiles; the 1.5-IQR fences flag values for investigation.
# sum() counts TRUE flags and does not remove observations; these age fences are measured in years.
q <- quantile(students$age, probs = c(0.25, 0.75))
iqr <- q[2] - q[1]
lower <- q[1] - 1.5 * iqr
upper <- q[2] + 1.5 * iqr
c(lower_fence = unname(lower), upper_fence = unname(upper))
sum(students$age < lower | students$age > upper)
