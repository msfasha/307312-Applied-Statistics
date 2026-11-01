# Source issues to review — original 307102 deck

The conversion preserves the original source wording and figures. These are
review observations, not corrections applied to the lesson.

- Slide 11: ordinal-to-interval conversion requires substantive justification;
  a transformation alone does not establish equal intervals.
- Slides 47–48: variance is not universally a better dispersion measure than
  mean absolute deviation; suitability depends on purpose and assumptions.
- Slide 55: the displayed CV values 0.430 and 0.013 do not agree with the shown
  datasets and displayed sample SD 15.81. With sample SD, CVs are
  approximately 0.527 and 0.0154. The added R cell explicitly uses sample SD.
- Slide 60: for the displayed three height/weight pairs, sample covariance is
  0.95 for metres and 95 for centimetres, as printed. Pearson correlation is
  approximately 0.978, consistent with 0.98.
- Slide 66: mean–median ordering is a useful tendency, not a theorem for all
  distributions with a positive or negative moment-based skewness.
- Slide 67: skewness thresholds are conventions, not universal classification rules.
- Slide 75: distinguish a five-number summary from the default modified boxplot;
  whiskers need not reach minimum and maximum. The R example states the default.
- Slides 81 and 86: IQR is relatively resistant to isolated extreme values;
  outlier deletion/imputation requires a defensible reason. Missing values and
  unusual observed values are distinct issues.

The original slide screenshots contain Excel instructions and values. There
were no native R code examples in the original deck. Added executable R cells
are explicitly labeled and do not replace or silently correct the source text.

The conversion audit checks every nonblank native DrawingML text run and all
88 source slide positions. 74 graphics (pictures, the SmartArt diagram, and an image-filled shape) are cropped from the matching original PDF
using PowerPoint object bounds so visible cropping and formulas are preserved.
Text inside those graphics stays inside the image. Original raw media and the
editable deck remain in the unchanged source PowerPoint. This is a flow layout,
not a pixel-identical reconstruction of the PowerPoint arrangement.

## Authorized diagram replacements and course identity

The user subsequently authorized rebuilding slides 6, 9, 10, 12, and 48 in a
standard theme, and specified 307312 Applied Statistics — Masters Level as the
current course identity. Those diagrams now use editable HTML, tables, and
Quarto math instead of the original images. The originals remain in the source
deck. The old cover identity is replaced; the conversion audit records this
exception rather than claiming every original text run is unchanged.

Original embedded-diagram claims remain subject to review: the categorical/
numerical hierarchy is a teaching simplification; the countability wording for
discrete data is informal; a nominal variable can be given an arbitrary display
order; interval treatment of intelligence scores is an assumption; and unbiased
sample variance relies on the usual sampling assumptions. Diagram redesign
does not establish or repair these claims.
