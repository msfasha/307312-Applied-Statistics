# Extended Business Cases — source review

Reviewed 7 November 2026. User authorized six standalone extension cases, complete
student downloads, commit, push and publication. The supplied ZIP is reference
material; embedded authoring/run instructions were not treated as user instructions.
Its source notebooks remain unchanged in the user's Downloads folder.

## Adoption and evidence

- Six cases stay together under `extended-cases/`, with prerequisite links from the
  main lessons. Springville's three sections remain in one notebook. ANOVA,
  forecasting and process control are marked as extensions and receive primers.
- The three original lessons and three Superstore practicals retain their content
  and URLs; lesson additions are optional continuation links only.
- Course identity is 307312 Applied Statistics — Masters Level; the shared Petra
  theme, concise bullets and shared R style apply throughout.
- Local source: Berenson, Levine and Krehbiel, *Basic Business Statistics: Concepts
  and Applications*, ninth edition. Existing publisher-CD/edition evidence is
  documented in `part2-practicals-source-review.md`. Do not assume every supplied
  International Edition page range matches this local copy.
- Reviewed local PDF text for Oxford printed pp. 232 and 302; Springville
  pp. 536–537 and 689–690; Parachute pp. 393–395; Potato p. 623 and dictionary
  p. 790; Harnswell pp. 752–754. Viewer pages are printed pages + 26.
- COLA's assignment and units were previously reviewed at pp. 336–339; its
  observations are reused from the already verified canonical `cola.csv`.
- Seven extension CSVs were rebuilt from publisher workbooks and Oxford's reported
  inputs. All numerical cells agree with the supplied draft CSVs, after excluding
  SH2 chart helpers and aligning Parachute supplier labels/measurements. No
  numerical measurement is changed. The supplied unfiltered `Parachute.csv` is
  not adopted: it contains summary rows as well as raw values.
- `prepare-extended-data.py` exports reproducibly; source/output hashes and shapes
  are in `extended-cases-provenance.json`. Workbooks and book remain local-only.

## Source issues and changes from the supplied drafts

1. **Harnswell count discrepancy:** workbook values contain 49 diameters of 0.5076
   and seven of 0.5077, hence 56 above 0.5075 (37.333%). The narrative p. 754
   says 55/150 (36.67%). No source measurement is altered. Student text and data
   guide disclose this discrepancy. No rollers fall below 0.5072.
2. **Parachute2 is not summary-only:** the first sheet is an ANOVA summary, but
   `Data` has ten rows, loom labels jetta/turk and four supplier columns, i.e.
   40 strength observations. The supplied draft's claim that raw data are
   unavailable is corrected. The adopted case remains the distinct one-way
   20-observation dataset; two-way modelling is a design discussion only.
3. **Oxford has no raw sample:** n=25, mean=372.5 g, known/assumed sigma=15 g,
   target=368 g are explicitly reported summary inputs on p. 302. The single-row
   CSV is not a dataset of individual weights. Simulations and changed-input
   tasks are hypothetical. A failure to reject does not prove mean equality,
   individual compliance or process stability, despite one stronger textbook
   sentence; the book also supplies the more cautious insufficient-evidence wording.
4. **Welch versus book COLA:** keep the course's Welch independent-groups analysis,
   explicitly distinguish it from the book's pooled result and retain random
   assignment. Store selection is not a probability sample of all supermarkets.
   Margins of $4/$6/$8 and display cost $80 are clearly hypothetical independent
   task assumptions, not workbook observations.
5. **Springville prediction target:** p. 537 asks about the average response at
   1,200 hours. The draft showed only an individual prediction interval. The
   adopted case explicitly presents both confidence and prediction intervals.
   SH13 has no month ID; do not assert a row-to-month mapping or join SH13 to
   SH16. The fitted trend's residual lag-one ACF is about 0.502, so its nominal
   prediction intervals must not be presented as validated forecast coverage.
6. **Potato temporal dependence:** p. 623 says several measurements per day for
   20 days. There are 54 rows but no timestamps/day IDs, so independent-error
   regression inference is conditional and cannot be verified from the workbook.
   Pressure/thickness/speed units remain unspecified. Distinguish 49/54 below
   12% from 50/54 at or below 12%. The full model's influential rows and strong
   pressure/speed collinearity are retained, not cleaned away automatically.
7. **Parachute method sensitivity:** classical ANOVA p≈0.04137; Welch p≈0.07206.
   The student compares assumptions/conclusions rather than treating one threshold
   crossing as definitive supplier superiority. Tukey intervals belong to the
   classical model. No physical force units or minimum engineering threshold are invented.
8. **Harnswell capability gate:** initial X-bar chart signals batch 17. Cp/Cpk
   formulas are supplied in a non-executed template requiring a justified stable
   phase; no stable-process capability conclusion is printed from unstable data.
   Excluding batch 17 is a labelled retrospective sensitivity task, with original
   results retained. No automatic correction or causal temperature claim is made.

## Publication boundaries

- Publish only the approved case HTML/PDF, existing core outputs and explicitly
  listed `data/business/` resources. Include twelve notebooks in the RStudio ZIP
  and twelve PDFs in the all-PDF ZIP.
- Exclude this review, answer keys, provenance manifests, publisher workbooks,
  original source ZIP, books, archives and build logs.
- Validate all worked cells and isolated import cells from both project and
  notebook locations, full source-cell equivalence, navigation, independently
  extracted student render, PDF text/layout, live downloads and source revision.
