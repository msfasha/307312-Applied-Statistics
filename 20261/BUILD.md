# Build and verify

Open `20261.Rproj` in RStudio. Run these commands from this folder.

```sh
quarto render
quarto preview
```

The student site is generated in `_site/`. Render the entire project after renaming sources or changing navigation. The build checks internal file links with `scripts/validate-course.py`. Source calculations execute on rebuild rather than relying on old frozen results.

Required R packages: `knitr`, `rmarkdown`, `ggplot2`, `dplyr`, `tidyr`, `readr`, and `stringr`. Data verification also uses `readxl`. Use the system R environment; the former broad package lock snapshot is preserved in the external recovery archive, not presented as a tested current environment.

```sh
Rscript scripts/verify-data.R
Rscript scripts/prepare-histogram-student-data.R
bash scripts/render-instructor.sh
```

Instructor HTML exports are kept in `_instructor/_output/`, apart from editable answers. They are not part of the student website.

Quarto is installed locally at `/usr/lib/rstudio/resources/app/bin/quarto/bin/quarto` if it is not on PATH. The instructor rendering script uses that path as a fallback.

Do not edit `_site/` directly or copy old HTML exports into it. `.quarto/` is generated working state. Export personal reports to `_output/`, never to the input CSV folders.
