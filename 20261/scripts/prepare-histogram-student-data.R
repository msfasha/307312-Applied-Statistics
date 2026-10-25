# library(): loads a package so its functions can be used in this session.
# grep(): finds text matching a regular expression; value=TRUE returns matching text rather than positions.
# commandArgs(): reads arguments passed to R; trailingOnly=TRUE keeps arguments intended for the script.
# length(): counts elements in a vector or list.
# stop(): ends execution and displays an error message.
# normalizePath(): resolves a path into a canonical absolute path.
# file.path(): joins path components with the platform-appropriate separator.
# dirname(): returns the directory portion of a file path.
# sub(): replaces the first pattern match in each text value; patterns normally use regular expressions.
# read_excel(): reads a publisher workbook for provenance checks; sheet selects its worksheet.
# stopifnot(): stops execution if any supplied condition is FALSE; successful checks produce no output.
# all(): returns TRUE only when every supplied logical value is TRUE.
# c(): combines values into a vector, converting them to a common type when needed.
# names(): reads or assigns names to vector elements or table columns.
# nrow(): returns the number of rows in a table or matrix.
# as.data.frame(): converts an object to a rectangular data frame.
# is.numeric(): checks whether an object has a numeric storage type.
# anyNA(): returns TRUE if any value is missing; !anyNA(...) requires no missing values.
# is.finite(): marks values that are neither infinite nor missing/NaN.
# identical(): requires exact equality of values, types, and attributes.
# range(): returns the minimum and maximum as a two-element vector.
# write.csv(): exports comma-separated data; row.names=FALSE avoids adding an unwanted index column.
# cat(): prints combined values directly; \n in its strings starts a new output line.
# unname(): removes names or dimension names without changing the underlying values.
# md5sum(): computes a file checksum to detect byte-level differences; it does not establish textbook compatibility.
# read.csv(): reads a comma-separated file into a data frame; its first row supplies column names by default.
# isTRUE(): returns TRUE only for a single nonmissing logical TRUE.
# all.equal(): compares objects allowing numerical tolerance; isTRUE() converts its result to a single TRUE/FALSE.
# as.numeric(): converts values to numbers; for a factor this gives internal codes rather than printed labels.
# Export only the two measurements used in the authorized histogram comparison.
library(readxl)
script_arg <- grep("^--file=", commandArgs(), value = TRUE)
if (!length(script_arg)) stop("Run this script with Rscript")
project <- normalizePath(file.path(dirname(sub("^--file=", "", script_arg[1])), ".."))
source <- file.path(project, "_instructor", "source-data", "student-measurements.xlsx")
d <- read_excel(source, sheet = "students")
stopifnot(all(c("age", "height") %in% names(d)), nrow(d) == 8239)
out <- as.data.frame(d[c("age", "height")])
stopifnot(is.numeric(out$age), is.numeric(out$height), !anyNA(out),
          all(is.finite(out$age)), all(is.finite(out$height)),
          identical(range(out$age), c(18,64)), identical(range(out$height),c(135,206)))
write.csv(out, file.path(project, "data", "module02", "student_age_height.csv"), row.names = FALSE)
cat("Exported",nrow(out),"records; age and height only. Source MD5:",unname(tools::md5sum(source)),"\n")

roundtrip <- read.csv(file.path(project, "data", "module02", "student_age_height.csv"))
stopifnot(identical(names(roundtrip), c("age", "height")),
          nrow(roundtrip) == nrow(out),
          isTRUE(all.equal(as.numeric(out$age), as.numeric(roundtrip$age), tolerance = 0)),
          isTRUE(all.equal(as.numeric(out$height), as.numeric(roundtrip$height), tolerance = 0)))
