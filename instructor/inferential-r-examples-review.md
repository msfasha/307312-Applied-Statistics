# R delivery adaptation — 19 November 2026

The user instructed keeping the original slide-based teaching material and using
R in place of spreadsheet instructions, with a single HTML/PDF/Positron source.
All 141 source positions, original sequence and non-software theory are retained.
The untouched PPTX/PDF references remain under sources/slides/.

Thirty-six explained R cells cover the original examples. Existing paired/group
comparisons are split between data-introduction and implementation positions;
confidence-interval implementation is placed on the original software slide.
The six supplied original teaching CSVs remain the only Part 3 datasets.

Removed visible spreadsheet formula/dialog/output screenshots, instructions and
standalone Python listings at the specified software positions. Original data,
questions, statistical figures and non-software explanations remain. R supplies
computed outputs in the same notebook. Removed alternatives and separate practical
sources are recoverable from Git history, not additional active course items.

## Source issues to retain

- Source probability slide 37 asks above 90 but its old software illustration uses
  75 and confuses probability/percentage. The R replacement answers the stated
  above-90 question; slide 36 keeps its separate above-75 example.
- Estimated versus known SD determines t versus z; n > 30 does not make SD known.
  The R explanations distinguish the two stated confidence-interval settings.
- Simulation illustrates SE behaviour, rather than proving the CLT. The original
  slide title is retained as requested; the R explanation states the limit.
- Pairing alone does not prove a tutorial caused improvement. The source causal
  sentence is retained, while the R interpretation identifies the design limit.
- Source salary currency labels conflict; do not assign an invented correction.
- Chi-square inference concerns association. One-way ANOVA does not show every
  pair differs. Regression output is conditional on assumptions; original source
  interpretation problems remain documented in inferential-source-review.md.

The content manifest hashes non-software slide bodies after excluding R additions.
Build checks guard their preservation along with all 141 positions and 36 cells.
