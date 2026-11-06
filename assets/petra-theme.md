# Petra grayscale teaching theme

Approved revision: **6 November 2026**. This replaces the previous lavender/pink
teaching palette. The design uses white reading surfaces, charcoal text and a
clear grayscale hierarchy. It is a teaching-document theme inspired by the
University of Petra context, not an official university identity manual.

## Scope and sources of truth

Use this theme consistently across newly created lessons, practicals, diagrams,
tables, slides and fresh exports. A scrolling lesson should feel like a sequence
of teaching slides, with a topic heading followed by its explanation, example,
code or practice. Fixed-height slides and a page break after every heading are
not required.

The portable specification is `petra_theme/petra_theme.md`, beside the course
folder. The tracked course copy is `307312-Applied-Statistics/assets/petra-theme.md`.
Keep these two Markdown copies identical when revising the theme.

Active course implementations:

- `assets/petra-brand.css`: shared colors, title panels and semantic headings.
- `assets/source-slides.css`: slide-like layout, editable diagrams and figure sizing.
- `assets/practical-print.css`: practical readability and print layout.
- `practicals/_includes/petra-plots.R`: shared R chart styling.

Paths are relative to the Applied Statistics course root. References to `20261/`
and the former `COURSE_STYLE.md` describe the retired course and are not active
implementation paths. Maintain one shared CSS implementation per role, rather
than separate heading-color rules in individual notebooks.

## Exact interface palette

| Role | Hex | Usage |
|---|---|---|
| Reading surface | `#FFFFFF` | Main content and diagram backgrounds |
| Main title surface | `#F3F3F3` | Light gray title panel |
| Main title and H2 text | `#262626` | Charcoal text |
| Main title top rule | `#404040` | Thin dark gray rule |
| Subtitle | `#666666` | Secondary title text |
| H2 surface | `#E8E8E8` | Strongest section fill |
| H3 surface | `#F3F3F3` | Lighter topic fill |
| H4 surface | `#F8F8F8` | Lightest subtopic fill |
| Heading accent and diagram connectors | `#A3A3A3` | Thin rules, borders and connectors |
| Body text | `#303030` | Dark text on white |
| Secondary text | `#666666` | Captions, metadata and minor labels |
| Table header | `#F3F3F3` | Neutral header surface |
| Inline code text | `#303030` | Variable names and short code references |
| Table and code divider | `#D6D6D6` | Subtle separators |
| Note header | `#F5F5F5` | Neutral note surface |
| Note left rule | `#A3A3A3` | Neutral callout accent |
| Links | `#356B8C` | Readable blue interactive links |
| Link hover | `#244D68` | Darker blue |

The hex values define the palette. Pink, lavender and purple are no longer used
for authored heading bands, content panels or diagram fills. Existing university
logos and preserved source figures retain their original colors and attribution.
Links and analytical chart colors are purposeful exceptions to the grayscale
interface; do not recolor every visual indiscriminately.

## Heading hierarchy and layout

| Semantic role | Source | Treatment |
|---|---|---|
| Document title | YAML `title`, or one H1 in a native notebook | Light gray panel, charcoal text, 3 px dark top rule |
| Subtitle | YAML `subtitle`, or a subtitle paragraph | Smaller gray text, subordinate to the title |
| Main section | H2 / `##` | `#E8E8E8` fill and a thin gray left rule |
| Topic | H3 / `###` | `#F3F3F3` fill and a thin gray left rule |
| Subtopic | H4 / `####` | `#F8F8F8` fill and a thin gray left rule |
| Minor labels | H5/H6 | Plain dark headings |

Keep genuine heading levels and normal navigation; do not promote all topics to
H2 just to imitate slides. Distinguish levels through size, weight, whitespace and
progressively lighter fills. Body content stays on white. Avoid heavy shadows,
large dark panels and filled backgrounds behind every paragraph.

The current HTML title panel uses `1.5rem 1.75rem` padding and 8 px lower corner
rounding. H2 uses `.75rem 1.1rem` padding with about `2.3rem` preceding space.
H3/H4 have progressively smaller padding. Full-width heading bands should wrap
cleanly on narrow screens. Reduce padding before shrinking essential text.

Use a readable sans-serif face and comfortable line spacing, around 1.5–1.65.
Preserve the platform's normal type hierarchy. Keep breadcrumbs above the title
panel on white. Keep headings with their following content in print.

## Diagrams, tables and notes

Editable diagrams use white outer containers, neutral borders and dark labels.
Root/section nodes use `#E8E8E8`, ordinary nodes `#F3F3F3`, and subordinate nodes
`#F8F8F8`. Connectors use `#A3A3A3`. Use bold labels and clear spacing to distinguish
levels; the diagram should not depend on color alone.

Tables use neutral headers, subtle horizontal rules, white data cells and a light
gray row-heading column where useful. Preserve readable formula notation. Notes
use neutral gray headers and rules. Inline code uses dark neutral text. Code blocks retain readable syntax
highlighting; the surrounding layout stays neutral.

## Figures and analytical colors

- Center instructional images and R plots horizontally, including captionless
  figures and lightbox-linked images.
- Small source-slide illustrations have a minimum width of 50% of their content
  area. Larger figures keep their existing widths, up to the available width.
  Preserve aspect ratio and check clarity; do not stretch images or invent detail.
- Keep original cover artwork sizing and intentional logo placement. Original
  reference PowerPoints, publisher files and source images remain unchanged.
- Single-series charts use charcoal `#4B4B4B` and light gray `#D4D4D4` by default.
- Use muted blue `#3B6B8A` and orange `#B56A3A` for analytical groups when a
  distinction matters; retain labels and stable mappings across related charts.
- Ordered categories can use the light-to-dark blue scale `#EFF3F6`, `#CBDCE8`,
  `#91B3CC`, `#557F9D`, `#244860`, with explicit category labels.
- Binary comparisons may use gray `#777777` and blue `#3B6B8A`. Choose meanings
  deliberately; color is not an automatic good/bad judgment.
- Charts may retain other suitable analytical palettes. Do not force data
  encodings into grayscale when it makes interpretation harder. Source figures
  retain their original colors and attribution.

## Applying the theme

For a Quarto website, configure shared styles in `_quarto.yml`:

```yaml
format:
  html:
    css:
      - assets/petra-brand.css
      - assets/source-slides.css
```

Adjust paths for standalone notebooks. Keep existing format settings and add CSS
to the appropriate HTML or Reveal configuration. Native Jupyter interfaces use
different HTML structures; a Quarto CSS reference alone does not style the native
notebook UI. Map the same semantic roles in a shared notebook template or export
stylesheet and verify the interface and export separately.

For PowerPoint, Word or a separate LaTeX/PDF workflow, reproduce these roles in
that format's styles; HTML CSS does not automatically style native Office files.
The current Applied Statistics PDFs are printed from rendered HTML, so they must
be regenerated to pick up theme changes. Existing PDFs are static snapshots.

The theme controls presentation, not lesson sequence, datasets, case selection or
language policy. Follow each project's agreed teaching and language rules.
Existing `.case-narration[lang="ar"]` support remains available for projects using
Arabic case introductions; it does not require adding translations to a course.

## Review and publication

Inspect a title/subtitle, H2–H4 sequence, long heading, table, note, editable
diagram, source image, code cell and chart. Check wide and narrow layouts and
representative PDF pages. Confirm image centering, readable figures and labels,
correct group-color mappings, adequate contrast and no clipped content.

In Applied Statistics, follow `PUBLISHING.md`: rebuild all six approved lesson and
practical PDFs and both student bundles, test the extracted RStudio project, and
verify the live website and downloads. A source push alone is not publication.
The RStudio bundle includes the tracked theme guide for future reference.
