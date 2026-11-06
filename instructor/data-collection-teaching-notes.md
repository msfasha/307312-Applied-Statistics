# Data collection and surveys supplement — 3 November 2026

## Placement and scope

The user requested collection methods, survey methods with selection rationales,
and survey errors. The supplement is included after original descriptive slide 12
(measurement-level comparison) and before slide 13 (descriptive tools). The
converter inserts the same include on regeneration. Original slide blocks, their
order, source files, images and R cells are unchanged.

`lessons/_includes/data-collection-and-surveys.qmd` contains 21 slide-style blocks, including
learning objectives, a discussion activity and references. It distinguishes
collection approaches, sample selection and survey communication modes. No new
dataset is needed; examples are conceptual or explicitly hypothetical.

## Source review and additional coverage

Planning reference: archived Chapter 1 summary at
`archived/2026-11-01-retired-course/20261/book-chapters/basic-business-statistics-13e/chapter01-original.txt`.
It is a supplied teaching guide, not an independently verified publisher chapter.
Do not reintroduce its case datasets or numerical claims as verified resources.

Primary references checked on 3 November 2026 are linked in the supplement:
ABS census/sample and error guidance; AAPOR survey practices; Pew questionnaire
and mode-effect guidance. The new explanations avoid repeating the guide's narrow
description of secondary data as necessarily collected by another party: data
previously collected internally can also be secondary for a new purpose.

The existing descriptive slides already explain population/sample briefly, data
types, measurement scales, tables, visualization, location, dispersion,
association, skewness, percentiles and outliers. Do not add duplicate treatments.
The brief census/frame/operational-definition material supplies the missing
foundation for error diagnosis. Questionnaire pretesting, piloting, privacy and
documented cleaning connect collection quality with the subsequent analysis.
Detailed weighting, sample-size formulas and confidence-interval derivations are
outside this descriptive supplement.

The ABS error page uses some broad examples under sampling error. The added
material uses the narrower repeated-probability-sampling interpretation and keeps
selection bias conceptually separate from sampling variability.

## Activity discussion notes — instructor only

1. Population: all current retail customers at a specified reference date;
   observational unit: one customer. Define satisfaction for a named service and
   time period, with a consistent response scale and not-applicable option.
2. The app delivers an online response mode and restricts the reachable frame to
   app users. Merely posting a link creates voluntary-response selection; it is
   not a probability sample of all retail customers.
3. Use an updated customer frame and a probability sample. Stratification can
   support branch/channel comparisons. Offer online completion with suitable
   alternatives; the correct choice depends on access, cost and study objectives.
4. Coverage: non-app users omitted. Nonresponse: some reached customers do not
   reply. Measurement: praise in the question encourages favorable responses.
   A larger self-selected response count does not repair these mechanisms.
5. Example revision: “Thinking about your most recent service interaction in the
   past 30 days, how satisfied or dissatisfied were you with the service?”
   Provide a balanced response scale and an option for no relevant interaction.
   Pretest comprehension; pilot routing and the exported response codes.

## Optional next teaching step

Use the discussion activity before the original tables section. An additional
chapter-wide business case is unnecessary for this request. A future practical
exercise could ask students to write a short collection plan; do not invent
results for the source student dataset or claim its collection design is known.

## Clarified business examples — 3 November 2026

The bank comparison originally appeared only in the chat. At the user's request,
it is now included after the two sampling introductions, followed by a short
explanation of segments, strata, weights and branch clusters. All bank design
choices are explicitly hypothetical, with no fabricated survey results. Age
groups refer to adult retail customers and partition that example population.
The cluster example uses one designated branch per customer to avoid overlapping
selection units. Explain that stratification supports group comparisons but does
not guarantee achieved response numbers or adequate precision by itself.
