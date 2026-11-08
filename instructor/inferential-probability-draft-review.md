# Section 3.1: source-mapped probability draft

Prepared as the first production section after the agreed skeleton and source
mapping. This is a separate proposal, not a replacement of the active lesson or
an update to the earlier full 141-position review notebook.

## Files and scope

- Editable source: `lessons/inferential-31-probability-distributions-draft.qmd`.
- Layout: `assets/inferential-draft.css`, using the existing shared Petra colors.
- Build/check command: `python3 scripts/preview-inferential-probability-draft.py`.
- HTML, PDF and portable editable bundle: `_build/inferential-probability-draft/preview/`.
- Scope: P1–P9, 22 teaching slides, 14 executable R cells including setup and
  figure/table-generation cells. Six short numerical R checks are visible;
  graphical implementation code is hidden while its output remains visible.
- No original PPTX/PDF, adopted lesson, approved course navigation, public bundle
  or publisher workbook was changed. No commit, push or publication was performed.

## Teaching map

| Slides | Unit | Sources / treatment |
|---|---|---|
| 1–2 | P1: inference and design | Original probability slides 3–6; book §§1.1–1.2 and 1.7, plus COLA study design p. 336. |
| 3–4 | P2: variables and models | Original slides 7–13; book §§1.8,5.1,6.1. Correctly distinguish mass, density and area. |
| 5 | P3: discrete uniform | Original die example; book §5.1 supports principles, not a claimed exact book exercise. |
| 6–8 | P4: binomial | Original car-defect example; book §5.3. Added shape explanation uses the same model rather than another compulsory case. |
| 9–10 | P5: Poisson | Book bank-arrival model, pp. 183–184. Replaces/consolidates the call-centre and context-free source calculations. |
| 11–12 | P6: continuous uniform | Original delivery/diameter models; book §6.3. Removes midpoint-as-peak/staffing inference. |
| 13–15 | P7: normal and empirical rule | Book §6.1 and p. 108; retains original exam scenario with explicit normal-model condition. |
| 16–17 | P8: z-scores | Original exam-comparison sequence; book standardisation §6.1. A z-score itself does not imply a normal percentile. |
| 18–20 | P9: normal areas and software | Original score-above-75 question; book §6.1 and Appendix 6. Consistent threshold and probability/percentage explanation. |
| 21–22 | Practice and synthesis | New course tasks on already stated models; explicit transition to unknown parameters and sampling. |

The optional automatic distribution-fitting enrichment is not part of this core
section. No observed business dataset is needed for the stipulated models here;
raw observations enter the mapped estimation/testing/regression sections.

## Independent activity: instructor answers

1. At least two defective cars: `1-pbinom(1,80,.02)` = 0.4770264967.
   More than two is 0.2155811130 approximately; the difference is P(X=2),
   0.2614453837. The exact at-least/more-than boundary matters.
2. No arrivals: `dpois(0,3)` = 0.0497870684.
3. Arrival between 10 and 11 under U(8,12): 0.25.
4. Score between 64 and 76: `pnorm(76,70,6)-pnorm(64,70,6)` = 0.6826894921.
5. A correct calculation is conditional on model inputs. It does not verify the
   event process, sampling/assignment design, independence or distribution shape.

Check assumptions in context rather than expecting a single memorised phrase.
For example, shared production faults undermine independent car outcomes;
group arrivals undermine a homogeneous independent-arrival model; real delivery
times may not be uniform; actual exam scores may be skewed or bounded in ways
that matter for the chosen approximation.

## Verification

- The builder checks the 22 sequential slide IDs and executes all 14 R cells in
  fresh environments, so visible checks do not depend on prior hidden variables.
- Numerical assertions cover binomial/Poisson tails, uniform probabilities,
  normal upper/interval areas and independent-task answers.
- HTML inspection checks internal anchor links, all rendered images and desktop/
  390-pixel mobile width. PDF inspection checks slide-to-page mapping and visual
  layout. Portable project rendering is checked separately.
- Book references remain printed-page references. PDF viewer pages are 26 higher.
- Original source errors are corrected only in this separate proposed draft.

## Clarity revision — 8 November 2026

- Reviewed all 22 slides against the user's clarity requirement: the opening must directly answer the title or define the concept before properties, notation or tables.
- Added explicit definitions of inference, probability mass/density, uniform/binomial/Poisson/normal distributions, cumulative probability, the complement rule, expected counts, the empirical rule and z-scores.
- Expanded interpretations of binomial, Poisson, uniform and normal results. Retained assumptions, source mapping, numerical inputs and all 14 executable R cells.
- Removed the inline topic-link chain and disabled heading anchor links. The right-hand contents panel provides navigation.
- Rebuilt HTML, PDF and editable ZIP. Verified 22 PDF pages (one teaching slide per page), all R checks, desktop/mobile rendering and all rendered page contact sheets.

## Full visible-code explanation audit — 8 November 2026

Reviewed all six student-visible R examples, not just the two initially identified:

| Slide | Explanation added before the code |
|---|---|
| 5 | Assignment, sequences, logical tests, TRUE/FALSE as 1/0, logical mean as proportion, remainder, conjunction, inclusive comparisons, c() and output labels; sum()/length() equivalent after the output. |
| 7 | dbinom vs pbinom, exact vs cumulative probabilities, d/p prefixes, x/q/size/prob, strict upper tail, cutoff selection and named output. |
| 10 | dpois vs ppois, x/q/lambda, rate window, upper tail and output labels. |
| 12 | punif, cutoff, lower/upper limits, continuous endpoints, upper tail, two separate contexts and interpretation of both outputs. |
| 17 | Arithmetic, parentheses and named vector results; z-scores are not probabilities. |
| 20 | pnorm, cutoff/mean/SD, upper tail, assignment and probability-to-percentage conversion. |

Named all arguments in the introductory binomial, Poisson, uniform and normal calculation calls. Hidden figure-generation code remains hidden. All 14 R cells pass; the refreshed PDF retains 22 pages. Inspected the refreshed page contact sheets and desktop/mobile HTML; no broken images, page overflow or browser errors were detected. Rebuilt the editable ZIP with the revised source.

## R function family and publication — 8 November 2026

- Added a new slide 14 introducing density/mass (d), cumulative probability (p), quantile (q) and random generation (r), illustrated with the normal family.
- The course section now has 23 slides and 15 executable R cells, seven visible. Original slides 14–22 move to 15–23; book mappings remain unchanged.
- The simulation creates twelve generated scores using set.seed(312), data.frame() and rnorm(), with every argument explained. Inputs specify a model, not an exact realised sample mean/SD or collected student records.
- Added the separate developing inferential practical, with probability examples and independent tasks. Later estimation/testing/power/regression sections are marked forthcoming, not presented as finished.
- User explicitly authorized publication; the original core slide lesson remains available unchanged.
