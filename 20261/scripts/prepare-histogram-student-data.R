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
