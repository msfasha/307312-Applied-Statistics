# Publishing the restarted course

The user authorized committing, pushing, and publishing the restarted course on
1 November 2026. This replaces the retired course's publishing workflow.

- `main` holds editable Quarto sources, assets, teaching CSVs, original reference
  slides, build scripts, and archived sources. Books, local reference documents,
  source measurement workbooks, and generated caches remain local and ignored.
- `gh-pages` holds only the generated active course from `_preview/`.
- The active site has three parts: Introduction to R, Descriptive Statistics, and
  Inferential Statistics. Old site exports and old downloads are retired.
- Never copy instructor files, archives, raw measurement workbooks, publisher
  books, build caches, or logs into the generated student website.
- Commit and push the editable sources on `main`, then run
  `python3 scripts/publish-course.py`. It builds the active course, validates its
  required pages and exclusions, and pushes a normal commit to `gh-pages`.
- `--skip-render` reuses an already completed, verified full build.
- The publisher preserves branch history and does not force push. The generated
  `deployment.json` identifies the exact source commit used for the website.
- A push to `main` alone is not publication. Verify the live home page, all three
  parts, the source commit in deployment.json, and an executable-example output.

Live website: https://msfasha.github.io/307312-Applied-Statistics/
