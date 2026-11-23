# Petra burgundy teaching theme

Approved revision: **23 November 2026**. The user chose the look of the 307307
Generative AI website for **all** courses so that they stay in sync: Petra burgundy
`#7a1f3d` on Quarto's `cosmo` theme. Headings and links are burgundy text on white,
and the navbar is burgundy with **white** links and a white search icon. This
supersedes the 6 November 2026 burgundy heading bands, the burgundy title panel
and the blue links. Reading surfaces, charcoal body text, neutral gray tables and
diagrams, and analytical chart colors are unchanged. This is a teaching-document
theme inspired by the University of Petra context, not an official identity manual.

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
- `lessons/_includes/course-tools.R`: shared R chart styling.

Paths are relative to the Applied Statistics course root. References to `20261/`
and the former `COURSE_STYLE.md` describe the retired course and are not active
implementation paths. Maintain one shared CSS implementation per role, rather
than separate heading-color rules in individual notebooks.

## Exact interface palette

| Role | Hex | Usage |
|---|---|---|
| Reading surface | `#FFFFFF` | Main content and diagram backgrounds |
| Brand burgundy | `#7a1f3d` | Navbar fill, headings (H1-H4), document title, links, active TOC item |
| Brand burgundy, dark | `#5a1730` | Link hover, button hover |
| Navbar text and icons | `#FFFFFF` | Navbar brand, links, search icon: always white, never gray |
| H2 rule | `#D6D6D6` | Thin rule under H2 |
| Diagram labels | `#262626` | Dark text on light gray content fills |
| Diagram connectors and borders | `#A3A3A3` | Neutral gray |
| Body text | `#303030` | Dark text on white |
| Secondary text | `#666666` | Captions, metadata, subtitles |
| Diagram root and table header | `#F2F2F2` | Neutral header surface |
| Diagram node | `#F7F7F7` | Light content fill |
| Diagram leaf and table row header | `#FAFAFA` | Lightest content fill |
| Table and code divider | `#D6D6D6` | Subtle separators |
| Note header / rule | `#F5F5F5` / `#A3A3A3` | Neutral callouts |

The hex values define the palette. Burgundy distinguishes authored headings, links and the navbar. In the approved median,
mean-absolute-deviation and squared-deviation diagrams it also marks the middle values or mean
reference line. Other diagram boxes, table headers and note surfaces remain
neutral gray.
Existing university logos and preserved source figures retain their original
colors and attribution. Meaningful analytical chart colors (blue/orange) remain
appropriate; do not recolor every visual indiscriminately.

## Heading hierarchy and layout

| Semantic role | Treatment |
|---|---|
| Document title (YAML `title`) | Burgundy `#7a1f3d` text on white, no panel; subtitle in `#666666` |
| H2 / `##` | Burgundy text, semibold, thin `#D6D6D6` rule underneath |
| H3, H4 | Burgundy text, semibold, no fill |
| H5/H6 | Plain dark headings |
| Navbar | `#7a1f3d` fill, white links, white search icon |
| Links | Burgundy, darker burgundy on hover |
| Landing pages | Module/part list as burgundy links with bold titles, a Downloads section, no cards required |

No filled heading bands and no title panels. Keep genuine heading levels and normal
navigation. Body content stays on white; avoid shadows and filled paragraph backgrounds.
Burgundy appears in text, links and the navbar, and as a marker for analytical emphasis
(median, mean reference line in the approved diagrams, token `--course-topic-bg`).
Use a readable sans-serif face with line spacing around 1.5-1.65. Keep headings with
their following content in print.

Shared CSS tokens: `--course-brand`, `--course-brand-dark`, `--course-heading-text`.
Keep them separate from content tokens (`--course-diagram-*-bg`, `--course-table-*-bg`,
`--course-title-text`, `--course-accent`). Do not reuse burgundy for diagram boxes or table headers.

## Diagrams, tables and notes

Editable diagrams use white outer containers, neutral borders and dark labels.
Root/section nodes use `#F2F2F2`, ordinary nodes `#F7F7F7`, and subordinate nodes
`#FAFAFA`. Connectors use `#A3A3A3`. Use bold labels and clear spacing to distinguish
levels; the diagram should not depend on color alone.

Tables use neutral headers, subtle horizontal rules, white data cells and a light
gray row-heading column where useful. Preserve readable formula notation. Notes
use neutral gray headers and rules. Inline code uses dark neutral text. Code blocks retain readable syntax
highlighting; the surrounding layout stays neutral.

## Figures and analytical colors

- Center instructional images and R plots horizontally, including captionless
  figures and lightbox-linked images.
- Small source-slide illustrations have a minimum width of 50% of their content
  area. Compact covariance panels in a comparison grid are an exception; their
  images use the panel width without that minimum. Typeset formulas as modest
  native math rather than enlarging formula screenshots. Larger figures keep
  their existing widths, up to the available width.
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
practical PDFs and both student bundles, test the extracted Positron workspace, and
verify the live website and downloads. A source push alone is not publication.
The Positron bundle includes the tracked theme guide for future reference.

## Reference implementations

- Applied Statistics: `assets/petra-brand.css` (this repo).
- 307307 Generative AI: `20261/site/styles.css` in that repo (Quarto `cosmo` plus the same burgundy rules).
When the theme changes, update both CSS files, this document (and its copy in
`../petra_theme/petra_theme.md`), and each course's publishing instructions.
