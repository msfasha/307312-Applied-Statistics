library(readxl)

script_arg <- grep("^--file=", commandArgs(), value = TRUE)
if (length(script_arg)) {
  project <- normalizePath(file.path(dirname(sub("^--file=", "", script_arg[1])), ".."))
} else {
  project <- normalizePath(getwd())
  while (!file.exists(file.path(project, "20261.Rproj")) && dirname(project) != project) {
    if (file.exists(file.path(project, "20261", "20261.Rproj"))) {
      project <- file.path(project, "20261")
      break
    }
    project <- dirname(project)
  }
}
if (!file.exists(file.path(project, "20261.Rproj"))) stop("Cannot locate the 20261 course project")
root <- normalizePath(file.path(project, ".."))
out <- file.path(project, "data", "module02")
checks_out <- file.path(project, "_instructor", "data-checks")
source_dir <- file.path(root, "books", "1-Modern Business Statistics-Organized-Data",
  "7th-Data - Modern Business Statistics with Microsoft Excel Anderson Sweeney Williams")
if (!dir.exists(source_dir)) stop("Original workbook folder is missing")
dir.create(out, recursive = TRUE, showWarnings = FALSE)
dir.create(checks_out, recursive = TRUE, showWarnings = FALSE)
read_source <- function(chapter, name) as.data.frame(read_excel(file.path(source_dir, chapter, name)))

files <- sort(list.files(source_dir, pattern = "\\.xls$", recursive = TRUE, full.names = TRUE, ignore.case = TRUE))
inventory <- data.frame(file = substring(files, nchar(source_dir) + 2),
  filename = basename(files), md5 = unname(tools::md5sum(files)))
write.csv(inventory, file.path(checks_out, "inventory.csv"), row.names = FALSE)

soft <- read_source("Chapter 02 Descriptive", "SoftDrink.xls")
soft <- data.frame(brand_original = soft[[1]], stringsAsFactors = FALSE)
soft$brand_book_label <- soft$brand_original
soft$brand_book_label[soft$brand_original == "Coke Classic"] <- "Coca-Cola"
soft$brand_book_label[soft$brand_original == "Pepsi-Cola"] <- "Pepsi"
brand_levels <- c("Coca-Cola", "Diet Coke", "Dr. Pepper", "Pepsi", "Sprite")
stopifnot(nrow(soft) == 50, !anyNA(soft), all(soft$brand_book_label %in% brand_levels),
  identical(as.integer(table(factor(soft$brand_book_label, levels = brand_levels))), c(19L,8L,5L,13L,5L)))
write.csv(soft, file.path(out, "soft_drinks.csv"), row.names = FALSE)

audit <- read_source("Chapter 02 Descriptive", "Audit.xls")
audit <- data.frame(audit_days = audit[[1]])
audit_book <- c(12,15,20,22,14,14,15,27,21,18,19,18,22,33,16,18,17,23,28,13)
stopifnot(identical(audit$audit_days, audit_book))
write.csv(audit, file.path(out, "audit_times.csv"), row.names = FALSE)

restaurants <- read_source("Chapter 02 Descriptive", "Restaurant.xls")
names(restaurants) <- c("restaurant_id", "quality_rating", "meal_price_usd")
quality <- c("Good", "Very Good", "Excellent")
price_group <- cut(restaurants$meal_price_usd, breaks = c(10,20,30,40,50), right = FALSE)
cross <- table(factor(restaurants$quality_rating, levels = quality), price_group)
book_cross <- matrix(c(42,40,2,0,34,64,46,6,2,14,28,22), nrow = 3, byrow = TRUE)
stopifnot(nrow(restaurants) == 300, !anyNA(restaurants), !anyNA(price_group),
  all(cross == book_cross),
  identical(restaurants$restaurant_id[1:10], as.numeric(1:10)),
  identical(restaurants$quality_rating[1:10], c("Good","Very Good","Good","Excellent","Very Good","Good","Very Good","Very Good","Very Good","Good")),
  identical(restaurants$meal_price_usd[1:10], c(18,22,28,38,33,28,19,11,23,13)))
write.csv(restaurants, file.path(out, "restaurant_ratings.csv"), row.names = FALSE)

electronics <- read_source("Chapter 02 Descriptive", "Stereo.xls")
names(electronics) <- c("week", "commercials", "sales_hundreds_usd")
stopifnot(nrow(electronics) == 10,
  identical(electronics$week, as.numeric(1:10)),
  identical(electronics$commercials, c(2,5,1,3,4,1,5,3,4,2)),
  identical(electronics$sales_hundreds_usd, c(50,57,41,54,54,38,63,48,59,46)))
write.csv(electronics, file.path(out, "electronics_sales.csv"), row.names = FALSE)

butler <- read_source("Chapter 15 Multiple Regression", "Butler.xls")
stopifnot(nrow(butler) == 10, ncol(butler) == 3,
  identical(butler[[1]], as.numeric(1:10)),
  identical(butler[[2]], c(100,50,100,100,50,80,75,65,90,90)),
  identical(butler[[3]], c(9.3,4.8,8.9,6.5,4.2,6.2,7.4,6.0,7.6,6.1)))

checks <- data.frame(
  workbook = c("SoftDrink.xls", "Audit.xls", "Restaurant.xls", "Stereo.xls", "Butler.xls"),
  rows = c(50,20,300,10,10),
  book_reference = c("Table 2.2; printed p.38", "Table 2.4; printed p.47", "Tables 2.9 and 2.10; printed pp.65-66", "Table 2.14; printed p.76", "Tables 15.1 and 15.2; printed pp.689-690"),
  status = c("Verified totals after documented label mapping", "All observations match", "Displayed rows and all crosstab cells match", "All observations match; filename differs", "Partial match: deliveries predictor absent"),
  limitation = c("Observation order not verified; retain original labels", "Historical teaching sample; not current operations data", "Remaining individual rows not printed; aggregate verification only", "Sales are in hundreds of US dollars; association is not causation", "Use for simple regression only; incomplete for Table 15.2"))
write.csv(checks, file.path(checks_out, "dataset-checks.csv"), row.names = FALSE)
cat("Checked", nrow(inventory), "Excel files;", length(unique(tolower(inventory$filename))), "distinct filenames.\n")
print(checks[c("workbook", "rows", "status")], row.names = FALSE)
