# library(): loads a package so its functions can be used in this session.
# grep(): finds text matching a regular expression; value=TRUE returns matching text rather than positions.
# commandArgs(): reads arguments passed to R; trailingOnly=TRUE keeps arguments intended for the script.
# length(): counts elements in a vector or list.
# normalizePath(): resolves a path into a canonical absolute path.
# file.path(): joins path components with the platform-appropriate separator.
# dirname(): returns the directory portion of a file path.
# sub(): replaces the first pattern match in each text value; patterns normally use regular expressions.
# getwd(): returns the current working-directory path.
# file.exists(): checks whether each specified file path exists.
# stop(): ends execution and displays an error message.
# dir.exists(): checks whether a specified directory exists.
# dir.create(): creates an output folder; recursive=TRUE creates missing parents and showWarnings=FALSE silences existing-folder warnings.
# as.data.frame(): converts an object to a rectangular data frame.
# read_excel(): reads a publisher workbook for provenance checks; sheet selects its worksheet.
# sort(): sorts values; decreasing=TRUE reverses the default ascending order.
# list.files(): lists directory entries; pattern filters names and recursive=TRUE searches subdirectories.
# data.frame(): builds a table whose named columns have compatible lengths.
# substring(): extracts characters between the supplied first and last positions.
# nchar(): counts the characters in each text value by default.
# basename(): returns the final filename portion of a path.
# unname(): removes names or dimension names without changing the underlying values.
# md5sum(): computes a file checksum to detect byte-level differences; it does not establish textbook compatibility.
# write.csv(): exports comma-separated data; row.names=FALSE avoids adding an unwanted index column.
# read_source(): is a locally defined helper reading a preserved source workbook for reproducible verification.
# c(): combines values into a vector, converting them to a common type when needed.
# stopifnot(): stops execution if any supplied condition is FALSE; successful checks produce no output.
# nrow(): returns the number of rows in a table or matrix.
# anyNA(): returns TRUE if any value is missing; !anyNA(...) requires no missing values.
# all(): returns TRUE only when every supplied logical value is TRUE.
# identical(): requires exact equality of values, types, and attributes.
# as.integer(): converts to integers by truncating numeric fractional parts; it does not round to nearest.
# table(): counts observations for each category or combination of categories.
# factor(): stores categorical values; levels fixes their permitted order and labels can rename their display.
# names(): reads or assigns names to vector elements or table columns.
# cut(): groups numeric values into intervals; breaks sets edges and right=FALSE makes [left,right) intervals.
# matrix(): arranges values in rows and columns; byrow=TRUE fills rows rather than the default columns.
# as.numeric(): converts values to numbers; for a factor this gives internal codes rather than printed labels.
# ncol(): returns the number of columns in a table or matrix.
# cat(): prints combined values directly; \n in its strings starts a new output line.
# unique(): keeps distinct values or rows in first-occurrence order.
# tolower(): converts text to lowercase for consistent matching.
# print(): displays the supplied value or object.
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
