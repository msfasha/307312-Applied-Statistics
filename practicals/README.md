# Practical R activities — drafts

`practical-01-cereals.qmd` is the first descriptive statistics pilot: inspect 33
historical cereal records, plot costs, compare mean and median, measure spread,
and write a business interpretation. Data: `data/practicals/`. Answers:
`instructor/cereals-pilot-notes.md`.

Open the root RStudio project first. Build with
`python3 scripts/preview-cereals-pilot.py` from the project root. Output:
`_build/practicals/practical-01-cereals.html`. The pilot is separate from the
active website and student packages pending review.

## Preview in RStudio

Open `Applied-Statistics.Rproj`, then `practicals/practical-01-cereals.qmd`,
and click **Render** or **Preview**. This folder has its own Quarto configuration,
so the draft does not inherit the published website settings. Data import cells work from either the course root or the notebook folder,
matching both RStudio cell execution and Quarto Preview.

Keep the editable data at **`data/practicals/` in the course root**. Do not move
the course data folder into `practicals/`. Markup links are relative to the
notebook; R imports locate `data/` from the course root or `../data/` from the notebook folder. Both reference the same files.
The preview build creates download copies automatically under `_build/practicals/`.
