# Applied Statistics (307312)

## For students

**[Read the course website](https://msfasha.github.io/307312-Applied-Statistics/)**

**[Open student downloads](https://msfasha.github.io/307312-Applied-Statistics/resources/downloads.html)** for:

- An HTML website ZIP for offline browser reading.
- A complete student RStudio project ZIP with lessons, exercises, CSV datasets,
  required assets, configuration, and setup instructions. Extract it and open `20261.Rproj`.
- A PDF bundle for offline reading, printing, and annotation. Extract it and open `index.pdf`.

For practical work, download the student RStudio project rather than cloning this
maintainer repository. Install R, RStudio, and Quarto, run the included `setup.R`
once, then open a lesson or exercise and click Render. HTML rendering needs no
Python or LaTeX. The website and supplied PDFs need none of these installations. Keep source attribution and third-party rights notices.

## For maintainers

`main` contains editable sources. **[`gh-pages`](https://github.com/msfasha/307312-Applied-Statistics/tree/gh-pages)**
contains the generated HTML, individual PDFs under `pdf/`, and ZIPs under `downloads/`.
Generated files are not committed to main. A source push alone does not update the site.
See [PUBLISHING.md](PUBLISHING.md) for the approved policy, publishing command,
student package contents, and completion checks.

| Location | Purpose |
|---|---|
| `20261/` | Active Quarto course and RStudio project |
| `20261/modules/` | Numbered lessons and student exercises |
| `20261/data/` | Ready-to-use teaching CSVs and provenance notes |
| `20261/_instructor/` | Instructor sources, answers, and verification records |
| `20261/syllabi/` | Available syllabus files |
| `COURSE_STYLE.md` | Shared course design rules |
| `AGENTS.md` | Instructions for future collaborators and agents |

The instructor's **`books/` and `docs/` folders are local-only and ignored by Git**.
A GitHub download or clone does not contain them. `books/` preserves textbook PDFs
and raw publisher workbooks for provenance; students use supplied CSVs and do not
need these original files to run the lessons.

Modules 1–4 include developed lessons and practice. Modules 5–7 indicate their
retained/planned status. See `20261/README.md` and `20261/BUILD.md` for source
organization and build instructions.
