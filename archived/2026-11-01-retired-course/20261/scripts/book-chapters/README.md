# Supplementary chapter companions

Chapter 1 is based solely on the user-supplied 13th-edition summary and teaching
guide. Preserve `book-chapters/basic-business-statistics-13e/chapter01-original.txt`
verbatim. It is not a verified publisher chapter or a data source for invented results.
The book/edition folder keeps future books distinct from the active lesson sequence.

Run from the repository root with the bundled runtimes:

1. `python3 20261/scripts/book-chapters/prepare.py` regenerates the maintained card JSON.
2. `python3 20261/scripts/book-chapters/build.py` creates the flashcard PDF (ReportLab) and formatted summary PDF (Quarto/XeLaTeX).
3. `node 20261/scripts/book-chapters/build.mjs` creates and validates the editable PPTX
   with Artifact Tool and renders the slides for review. The finalizer requires a new
   output path when revising an existing deck. Move the old generated PPTX aside first.

Inspect the generated materials under `20261/_output/book-chapters/` and the private
previews under `_output/.chapter01-build/`. Each of 50 questions has a following answer
page, preceded by one introduction, for 101 slides/pages. The original-text PDF keeps
all original wording, rendering Markdown headings, lists, tables, and emphasis. The source text remains unchanged.
Case introductions appear bilingually on the Book chapters page. Review cards retain
English conceptual content and case takeaways. Separate questionnaires/datasets were
not attached and edition-specific page claims have not been independently verified.

`materials.py` copies the original text, card data, PDF guide and flashcard PDF
into the site, PDF bundle, and RStudio project. The publication manifest records their
hashes and the packager verifies the PDF archive's copies against these current files.
Follow `PUBLISHING.md` to rebuild the site, commit sources, and deploy `gh-pages`.

Editable PPTX outputs are instructor-only and stay local.
