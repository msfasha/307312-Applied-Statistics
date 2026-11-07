# Original core restoration — 7 November 2026

- Original reference PPTX/PDF files under `sources/slides/` were never changed.
- In chat **Review practical dataset options**, commit `491f030` (6 November,
  23:02 Asia/Amman) replaced the core lessons with Superstore/COLA/Consumer content.
- Commit `3e2011e` added six business cases afterwards; it did not cause the
  earlier core replacement.
- The user explicitly requested the original slides back, then clarified that
  R practicals and all six business cases must remain alongside those slides.
- Restore only Parts 2 and 3 byte-for-byte from `70bf7ee`, retaining the current
  burgundy theme. Keep practicals and extended cases separate from core theory.
- Restore required original lesson CSVs/assets/fragments to packaging and update
  case prerequisite links to the original slide headings.
- The pre-restoration revision is preserved on
  `codex/backup-before-original-course-restore-20261107` at `3e2011e`.
- Check all 88 descriptive and 141 inferential slide IDs before publication;
  preserve twelve notebooks/PDFs and both bundles. Do not force-push history.

The original MASS distribution-fitting example can produce intermediate `NaNs
produced` optimization warnings. Preserve its source and the original warning
policy; run restored Part 3 with warnings permitted, while all newer notebooks
retain warnings-as-errors checks. Successful execution is not validation of
uncorrected source claims; retain `inferential-source-review.md`.
