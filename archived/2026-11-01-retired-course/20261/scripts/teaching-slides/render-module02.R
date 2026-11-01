# Execute the original lesson chunks and export their tables and plot objects.
# The CSV inputs remain unchanged; assertions in the lessons run as written.
library(jsonlite)
library(ggplot2)
root <- getwd()
out <- file.path(root, '_output/.module02-teaching-build')
dir.create(file.path(out, 'plots'), recursive = TRUE, showWarnings = FALSE)
dir.create(file.path(out, 'tables'), recursive = TRUE, showWarnings = FALSE)
lessons <- sort(list.files('modules/02-data-and-descriptive-statistics',
  pattern = '^0[1-4].*[.]qmd$', full.names = TRUE))
results <- list()
example_results <- list()
for (lesson in seq_along(lessons)) {
  lines <- readLines(lessons[lesson], warn = FALSE)
  env <- new.env(parent = globalenv())
  inside <- FALSE; code <- character(); label <- ''; count <- 0; evaluate <- TRUE
  for (line in lines) {
    if (grepl('^```\\{r', line)) { inside <- TRUE; code <- character(); label <- ''; evaluate <- !grepl('eval\\s*=\\s*FALSE',line); next }
    if (inside && grepl('^```', line)) {
      count <- count + 1
      if (!nzchar(label)) label <- paste0('chunk-',count)
      if (!evaluate) { inside <- FALSE; next }
      expressions <- parse(text = code)
      plot_count <- 0
      example_output <- character()
      for (expr in expressions) {
        value <- withVisible(eval(expr, env))
        if (value$visible && inherits(value$value, 'ggplot')) {
          plot_count <- plot_count + 1
          file <- file.path(out,'plots',paste0('lesson',lesson,'-',label,'-',plot_count,'.png'))
          # ggsave() uses the exact plot object and gives its text a projection-friendly base size.
          # Units are inches; dpi controls output resolution, without changing observations or statistics.
          p <- value$value + theme(text = element_text(size = 17, family = 'DejaVu Sans'))
          ggsave(file,p,width=12,height=6.2,units='in',dpi=150,bg='white')
        }
        if (value$visible && !inherits(value$value, 'ggplot') && !inherits(value$value, 'knitr_kable')) {
          example_output <- c(example_output, capture.output(print(value$value)))
        }
        if (value$visible && inherits(value$value, 'knitr_kable')) {
          file <- file.path(out,'tables',paste0('lesson',lesson,'-',label,'.md'))
          cat(as.character(value$value),file=file,sep='\n',append=file.exists(file))
          cat('\n\n',file=file,append=TRUE)
        }
      }
      example_results[[paste0('lesson',lesson,'-',label)]] <- list(output=example_output,plots=plot_count)
      results[[length(results)+1]] <- list(lesson=lesson,label=label,expressions=length(expressions),plots=plot_count)
      inside <- FALSE
      next
    }
    if (inside) {
      if (grepl('^#\\| label:',line)) label <- trimws(sub('^#\\| label:','',line))
      if (grepl('^#\\| eval: false',line)) evaluate <- FALSE
      code <- c(code,line)
    }
  }
  # Save useful numerical objects as CSVs for editable table construction and checks.
  # Only derived summaries are exported; publisher workbooks and original CSVs are untouched.
  for (name in ls(env)) {
    value <- get(name,env)
    if (is.data.frame(value) && nrow(value)<=35 && ncol(value)<=12) {
      write.csv(value,file.path(out,'tables',paste0('lesson',lesson,'-',name,'.csv')),row.names=FALSE)
    }
  }
  if(lesson==4) {
    write.csv(addmargins(env$counts),file.path(out,'tables','lesson4-counts.csv'))
    write.csv(cbind(env$row_pct,Total=rowSums(env$row_pct)),file.path(out,'tables','lesson4-row-percentages.csv'))
    write.csv(rbind(env$column_pct,Total=colSums(env$column_pct)),file.path(out,'tables','lesson4-column-percentages.csv'))
  }
}
write_json(results,file.path(out,'executed-chunks.json'),auto_unbox=TRUE,pretty=TRUE)
write_json(example_results,file.path(out,'r-example-results.json'),auto_unbox=FALSE,pretty=TRUE)
cat('Checked',length(results),'original R chunks and rendered all visible lesson graphics.\n')
