# Active course: 20261

**Students:** [read the published website](https://msfasha.github.io/307312-Applied-Statistics/) or [download the HTML site, RStudio project, and PDFs](https://msfasha.github.io/307312-Applied-Statistics/resources/downloads.html). Extract the student project ZIP and open **20261.Rproj** in RStudio.

**Maintainers:** open **20261.Rproj** to edit **index.qmd**. Local renders appear under **_site/**. See **../PUBLISHING.md** for publication policy; generated files are served from the **gh-pages** branch, not main.

| Location | What belongs here |
|---|---|
| `modules/` | Seven topic modules, each with an overview and numbered lessons; exercises under the relevant module |
| `data/module02/` | Checked textbook CSVs and documented supplementary illustrations |
| `data/module05/` | Survey CSV needed by the retained hypothesis-testing lesson |
| `assets/` | One shared stylesheet and only figures used by active materials |
| `resources/index.qmd` | Dataset downloads and course-resource guidance |
| `_instructor/` | Answers, teaching plans, templates, verification records, and original measurement workbook |
| `scripts/` | Data preparation, link validation, and instructor rendering |
| `_site/` | Generated student website; rebuilt from source |

Use **NN-topic.qmd** with lowercase hyphenated words for lessons. Exercises and instructor answers use the corresponding lesson number. Overviews use `index.qmd`. Keep dataset column names and documented publisher source names stable.

Module 1 has four R lessons and practice. Module 2 has four completed descriptive-statistics lessons, practice, and an integrated review. Module 3 has five probability/distribution lessons, practice, and an integrated review. Module 4 has four sampling/estimation lessons, practice, and an integrated review. Other modules clearly state whether they are planned or contain retained material.

Read `BUILD.md` before rendering. Instructor exports go to `_instructor/_output/`. Temporary Quarto state lives in `.quarto/` and can be regenerated. Syllabi are in `syllabi/`. `../docs/` and `../books/` are instructor-local collections ignored by Git; they are not included in a clone or student download. The supplied CSVs are sufficient for active lessons.
