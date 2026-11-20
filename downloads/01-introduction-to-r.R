# 307312 Applied Statistics — Introduction To R
# Run sections in order from the course root folder containing data/.
# Download the complete course ZIP for the required CSV files.
# Explanations and output interpretation are in the matching course notebook.

# --- Section 1 ---
knitr::opts_chunk$set(message = FALSE, dpi = 200)

# --- Section 2 ---
print("Hello, World!")

# --- Section 3 ---
age <- 25          # Store a number
name <- "Alice"    # Store text
is_registered <- TRUE
age

# --- Section 4 ---
typeof(age)
class(age)
typeof(25L)
typeof(name)
typeof(is_registered)

# --- Section 5 ---
round(x = 12.345, digits = 2)

# --- Section 6 ---
ages <- c(20, 22, 25, 28, 30)
length(ages)

# --- Section 7 ---
1:5
seq(from = 2, to = 10, by = 2)
rep(x = 0, times = 3)

# --- Section 8 ---
ages[3]           # Third value: 25
ages[2:4]         # Positions 2, 3 and 4: 22, 25, 28
ages[c(1, 5)]     # First and fifth values: 20, 30

# --- Section 9 ---
ages >= 25
ages[ages >= 25]

# --- Section 10 ---
ages[(ages >= 22) & (ages <= 28)]

# --- Section 11 ---
score <- 65
if (score >= 50) {
  print("Pass")
} else {
  print("Below the pass mark")
}

# --- Section 12 ---
for (number in 1:3) {
  print(number^2)
}

# --- Section 13 ---
people <- data.frame(
  name = c("Alice", "Bob", "Eva"),
  age = c(25, 30, 22)
)
people

# --- Section 14 ---
car_data <- mtcars

# --- Section 15 ---
class(car_data)
dim(car_data)
nrow(car_data)
ncol(car_data)
names(car_data)

# --- Section 16 ---
car_data[1:3, c("mpg", "wt", "cyl")]
class(car_data["mpg"])
class(car_data[["mpg"]])

# --- Section 17 ---
head(x = car_data[c("mpg", "wt", "cyl")], n = 3)
tail(x = car_data[c("mpg", "wt", "cyl")], n = 2)

# --- Section 18 ---
str(object = car_data[c("mpg", "wt", "cyl")])
summary(object = car_data[c("mpg", "wt")])

# --- Section 19 ---
car_data$weight_kg <- car_data$wt * 453.59237
head(x = car_data[c("wt", "weight_kg")], n = 3)

# --- Section 20 ---
efficient_cars <- car_data[
  car_data$mpg >= 25, c("mpg", "weight_kg", "cyl")
]
efficient_cars

# --- Section 21 ---
efficient_cars[order(efficient_cars$weight_kg), ]

# --- Section 22 ---
superstore <- read.csv(file = "data/r-introduction/superstore.csv")
head(x = superstore[c("Category", "Sales", "Profit")], n = 3)

# --- Section 23 ---
values <- c(10, NA, 20)
is.na(values)
mean(x = values, na.rm = TRUE)

# --- Section 24 ---
# Run manually once if the packages are not installed:
# install.packages(pkgs = c("dplyr", "ggplot2"))

# --- Section 25 ---
library(dplyr)

# --- Section 26 ---
sales_columns <- select(superstore, Category, Sales, Profit)
technology <- filter(sales_columns, Category == "Technology")
largest_first <- arrange(technology, desc(Sales))
head(x = largest_first, n = 3)

# --- Section 27 ---
sales_units <- mutate(largest_first, Sales_thousands = Sales / 1000)
head(x = sales_units, n = 3)

# --- Section 28 ---
labelled_sales <- rename(sales_columns, Sales_USD = Sales)
head(x = labelled_sales, n = 3)

# --- Section 29 ---
# Nested calls: read the innermost operation first
nested_technology <- select(
  filter(superstore, Category == "Technology"), Category, Sales, Profit
)

# Intermediate table: store each step
technology <- filter(superstore, Category == "Technology")
step_technology <- select(technology, Category, Sales, Profit)

# Pipeline: read the operations from top to bottom
piped_technology <- superstore %>%
  filter(Category == "Technology") %>%
  select(Category, Sales, Profit)

identical(x = nested_technology, y = piped_technology)
identical(x = step_technology, y = piped_technology)
head(x = piped_technology, n = 3)

# --- Section 30 ---
multi_unit_totals <- superstore %>%
  filter(Quantity >= 2) %>%
  mutate(Sales_thousands = Sales / 1000) %>%
  group_by(Category) %>%
  summarise(lines = n(),
            sales_thousands = sum(Sales_thousands),
            .groups = "drop") %>%
  arrange(desc(sales_thousands))
multi_unit_totals

# --- Section 31 ---
par(mar = c(4.2, 4.7, 2.5, 0.8), mgp = c(2.8, 0.7, 0), las = 1, cex = 0.9)

# --- Section 32 ---
hist(x = car_data$mpg, breaks = 6,
     main = "Fuel economy of 32 car models",
     xlab = "Miles per US gallon", col = "gray75")

# --- Section 33 ---
par(mar = c(4.2, 4.7, 2.5, 0.8), mgp = c(2.8, 0.7, 0), las = 1, cex = 0.9)

# --- Section 34 ---
category_counts <- table(superstore$Category)
barplot(height = category_counts, main = "Order lines by category",
        ylab = "Number of order lines", col = "gray75")

# --- Section 35 ---
car_data$cylinders <- factor(x = car_data$cyl)

# --- Section 36 ---
par(mar = c(4.2, 4.7, 2.5, 0.8), mgp = c(2.8, 0.7, 0), las = 1, cex = 0.9)

# --- Section 37 ---
boxplot(mpg ~ cylinders, data = car_data,
        main = "Fuel economy by cylinder group",
        xlab = "Recorded cylinder group", ylab = "Miles per US gallon",
        col = "gray80")

# --- Section 38 ---
par(mar = c(4.2, 4.7, 2.5, 0.8), mgp = c(2.8, 0.7, 0), las = 1, cex = 0.9)

# --- Section 39 ---
plot(x = car_data$weight_kg, y = car_data$mpg,
     main = "Vehicle weight and fuel economy",
     xlab = "Vehicle weight in kilograms", ylab = "Miles per US gallon",
     pch = 16, cex = 1, col = "gray35")

# --- Section 40 ---
library(ggplot2)

# --- Section 41 ---
p <- ggplot(data = car_data,
            mapping = aes(x = weight_kg, y = mpg))

# --- Section 42 ---
p <- p + geom_point(size = 2, colour = "gray35")

# --- Section 43 ---
p +
  labs(title = "Vehicle weight and fuel economy",
       x = "Vehicle weight in kilograms", y = "Miles per US gallon") +
  theme_minimal()

# --- Section 44 ---
ggplot(data = car_data,
       mapping = aes(x = weight_kg, y = mpg,
                     colour = cylinders, shape = cylinders)) +
  geom_point(size = 2.5) +
  labs(title = "Weight and fuel economy by cylinder group",
       x = "Vehicle weight in kilograms", y = "Miles per US gallon",
       colour = "Cylinders", shape = "Cylinders") +
  theme_minimal()

# --- Section 45 ---
ggplot(data = car_data, mapping = aes(x = cylinders, y = mpg)) +
  geom_boxplot(fill = "gray85", outlier.shape = NA) +
  geom_point(position = position_jitter(width = 0.12, height = 0, seed = 312),
             size = 1.6, colour = "gray30") +
  labs(title = "Fuel economy by group with all 32 observations",
       x = "Recorded cylinder group", y = "Miles per US gallon") +
  theme_minimal()

# --- Section 46 ---
superstore %>%
  filter(Category == "Technology") %>%
  ggplot(mapping = aes(x = Quantity)) +
  geom_histogram(binwidth = 1, boundary = 0.5,
                 fill = "gray75", colour = "white") +
  labs(title = "Quantity on Technology order lines",
       x = "Quantity", y = "Number of order lines") +
  theme_minimal()

# --- Section 47 ---
superstore %>%
  group_by(Category) %>%
  summarise(sales_thousands = sum(Sales) / 1000, .groups = "drop") %>%
  ggplot(mapping = aes(x = Category, y = sales_thousands)) +
  geom_col(fill = "gray65") +
  labs(title = "Total sales by category",
       x = "Product category", y = "Sales in US$ thousands") +
  theme_minimal()
