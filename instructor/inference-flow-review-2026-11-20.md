# Probability and inference teaching flow — 20 November 2026

The user approved separating probability foundations (Part 3) from statistical inference and estimation, including tests and regression (Part 4). Quarto remains the editable source used for HTML, PDF and the student project.

## Changes and statistical qualifications

- Added definitions of experiments/outcomes/sample spaces/events, basic event rules, conditional probability, independence and the mapping to random variables. The fair-die and coin examples are mathematical models, not observed data.
- Moved four introductory inference positions from the probability opening to the start of Part 4.
- Added sampling-distribution definitions and distinguished observations per sample from simulation repetitions.
- Rewrote the CLT statement: independent identically distributed observations with finite positive variance; convergence concerns increasing sample size, not increasing simulation repetitions. There is no universal n=30 guarantee. Normal-population means are exactly normal at every sample size.
- Explained that the mean and variance identities and SE sigma/sqrt(n) follow from independence, not from the CLT. Sampling without replacement may require a finite-population correction.
- Put the CLT before point/interval estimation and confidence-interval calculations. The normal-population SE simulation remains an illustration, not proof of the CLT; its misleading proof heading is corrected. The duplicated/corrupted symmetry heading is corrected.
- Added the normal-pivot-to-CI rearrangement, repeated-sampling interpretation and distinction between known-sigma normal and unknown-sigma t methods. These qualifications do not validate other historical source claims; retain existing source-review notes.
- Kept original images, data and all 36 canonical R listings unchanged. Historical source IDs remain internal identifiers, not displayed provenance comments. The instructor manifest records the explicitly authorized teaching order and current native-body hashes separately from historical guards.

## References checked

- Penn State STAT 414, Lesson 27, Central Limit Theorem: https://online.stat.psu.edu/stat414/Lesson27
- Penn State STAT 414, Lesson 26, normal sampling distributions: https://online.stat.psu.edu/stat414/Lesson26
- OpenStax Introductory Business Statistics 2e, chapters 7–8: sampling distributions/CLT precede confidence intervals. Existing source attribution remains in the teaching material.
