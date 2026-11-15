# R introduction review

## Correction on 15 November 2026

The user requested a substantive data-frame foundation, restoration of the original pipe/layer diagrams, and legible, meaningful plots. The previous Sales boxplot was dominated by the long upper tail and the small Sales/Profit scatter obscured most lines. Neither example is retained in the introduction.

The original mtcars example supplies 32 historical car models (1973–1974 models, 1974 Motor Trend source). R help documents mpg as miles per US gallon and wt as thousands of pounds. Weight conversion is wt × 453.59237 kilograms. All observations are retained. Cylinder counts are recorded historical codes; the R help notes legacy coding choices including the Mazda rotary engine. These data are descriptive and observational, not a representative sample of modern cars or a causal experiment.

Recorded groups have n = 11, 7 and 14 and medians 26.0, 19.7 and 15.2 mpg. The ggplot boxplot suppresses only duplicate outlier symbols in its box layer; its jittered point layer includes all 32 observations with zero vertical jitter and a fixed display seed. Base-R hinges and ggplot quartiles can differ for small samples; the lesson states that distinction.

The pipe and static stacked Grammar of Graphics images are retained byte-for-byte. The supplied notebooks do not identify their external creators; retain attribution to the supplied 307307 material without inventing an external attribution. The separate animated GIF is not required to explain the restored static diagram. The explanation separates aesthetic mappings from scales, which the static image's short labels conflate.

User correction belongs only to the combined R introduction. Other course lessons, cases, data and original reference materials remain unchanged.
