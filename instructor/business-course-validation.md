# Prepublication validation — business-course revision, 6 November 2026

- Original reference decks and source workbooks were not modified.
- Pinned-source reproduction succeeds: source SHA-256 values and regenerated CSV hashes match the approved manifest.
- All 21 Superstore source columns were compared across all selected rows; COLA's 20 numbers and Consumer's 150 numbers match source workbooks. Return-list membership was checked separately.
- All six notebooks passed 24 fresh-session checks: isolated import plus all worked cells, from both the root and notebook folder. Warnings were treated as errors.
- Numerical checks cover line/order/customer counts, losses, return-list counts, aggregation reconciliation, order summaries, COLA's effect/interval/p-value and Consumer coefficients/fit.
- The full Quarto website renders all three lessons and three practicals. All generated R charts were inspected: 24 charts, with centred plots, neutral defaults, consistent group colors and text alternatives.
- Representative HTML title, heading, table, code, plot and formula were visually reviewed in the browser.
- All six PDFs were regenerated and their extracted text checked for executed results. Representative first, middle and final pages were visually inspected. The final table, chart-label and margin fixes were rechecked. Page counts: 7, 13, 20, 7, 7, 7. No blank pages or text outside physical page bounds remain.
- PDF export now removes a trailing page only when both text extraction and zero CMYK ink establish that it is empty; image-only chart pages are retained.
- Website link checks pass. The PDF ZIP contains exactly the six approved PDFs. The RStudio ZIP includes every notebook, the shared R helper, current data, configuration, theme and required render scripts.
- Instructor files, publisher books/workbooks, archives and retired students/funds/cereals/inferential extracts are excluded from student website and ZIPs.
- The extracted student project renders independently of maintainer books/instructor folders. All six isolated import cells additionally run from both extracted working locations (12 fresh sessions). Latest packaged data, helper and print CSS match maintainer sources.

The publisher writes source revision and publication time to `deployment.json`.
Verify that live record, all seven primary HTML pages, six PDFs, both ZIPs and
current data downloads after every deployment. This file records prepublication
checks; the generated deployment record identifies the published revision.
