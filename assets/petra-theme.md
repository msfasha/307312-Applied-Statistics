# Petra burgundy and gray teaching theme

Approved revision: **6 November 2026**. The user approved the preview with muted
burgundy heading bands and white title text, retaining gray charts and tables.
This supersedes the earlier all-gray heading palette and the original pale pink
palette. White reading surfaces and charcoal body text remain unchanged. This
teaching-document theme is inspired by the University of Petra context; it is
not an official university identity manual.

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
| Main title surface | `#542638` | Deep burgundy document title panel |
| Heading text | `#FFFFFF` | White text on document title and H2–H4 bands |
| Main title top rule and heading accent | `#542638` | Burgundy rules for headings only |
| Subtitle | `#F3EAF0` | Light text inside the burgundy title panel |
| H2, H3 and H4 surface | `#763D52` | Approved muted burgundy topic bands |
| Diagram labels | `#262626` | Dark text on light gray content fills |
| Diagram connectors and borders | `#A3A3A3` | Neutral gray, independent of heading accents |
| Body text | `#303030` | Dark text on white |
| Secondary text | `#666666` | Captions, metadata and minor labels |
| Diagram root and table header | `#F2F2F2` | Neutral header surface |
| Diagram node | `#F7F7F7` | Light content fill |
| Diagram leaf and table row header | `#FAFAFA` | Lightest content fill |
| Inline code text | `#303030` | Variable names and short code references |
| Table and code divider | `#D6D6D6` | Subtle separators |
| Note header | `#F5F5F5` | Neutral note surface |
| Note left rule | `#A3A3A3` | Neutral callout accent |
| Links | `#356B8C` | Readable blue interactive links |
| Link hover | `#244D68` | Darker blue |

The hex values define the palette. Burgundy distinguishes authored title and heading bands. In the approved median
and mean-absolute-deviation diagrams it also marks the middle values or mean
reference line. Other diagram boxes, table headers and note surfaces remain
neutral gray.
Existing university logos and preserved source figures retain their original
colors and attribution. Blue links and meaningful analytical chart colors remain
appropriate; do not recolor every visual indiscriminately.

## Heading hierarchy and layout

| Semantic role | Source | Treatment |
|---|---|---|
| Document title | YAML `title`, or one H1 in a native notebook | `#542638` deep burgundy panel, white text, 3 px dark top rule |
| Subtitle | YAML `subtitle`, or a subtitle paragraph | Smaller `#F3EAF0` text within the title panel |
| Main section | H2 / `##` | `#763D52` burgundy fill, white text and a thin deep burgundy left rule |
| Topic | H3 / `###` | Same approved burgundy fill and white text |
| Subtopic | H4 / `####` | Same approved burgundy fill and white text, with smaller type and padding |
| Minor labels | H5/H6 | Plain dark headings on white |

The main title panel is deeper burgundy than the H2–H4 bands. Apply the topic
bands to all slide/topic titles, such as “Types of data”, across lessons and
practicals, not only the document's opening title. White on `#763D52` has a
contrast ratio of approximately 8.2:1; white on `#542638` approximately 12.3:1.
Keep links, bold text and inline code inside heading bands white as well.

Keep heading tokens (`--course-title-bg`, `--course-section-bg`,
`--course-topic-bg`, `--course-subtopic-bg`, `--course-heading-text`,
`--course-heading-accent`) separate from content tokens
(`--course-diagram-*-bg`, `--course-table-*-bg`, `--course-title-text` for dark
diagram labels, and `--course-accent` for gray diagram connectors). Do not reuse
heading text or fill colors for diagram boxes or table headers.

Keep genuine heading levels and normal navigation; do not promote all topics to
H2 just to imitate slides. Distinguish levels through size, weight, whitespace and
consistent burgundy bands. Body content stays on white. Avoid heavy shadows
and filled backgrounds behind paragraphs; burgundy belongs to headings only.

The current HTML title panel uses `1.5rem 1.75rem` padding and 8 px lower corner
rounding. H2 uses `.75rem 1.1rem` padding with about `2.3rem` preceding space.
H3/H4 have progressively smaller padding. Full-width heading bands should wrap
cleanly on narrow screens. Reduce padding before shrinking essential text.

Use a readable sans-serif face and comfortable line spacing, around 1.5–1.65.
Preserve the platform's normal type hierarchy. Keep breadcrumbs above the title
panel on white. Keep headings with their following content in print.

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
