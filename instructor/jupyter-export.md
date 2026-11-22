# R Jupyter notebook exports

The thirteen approved QMD notebooks remain the editable teaching sources.
Each has a generated IPYNB beside it, and the student Positron ZIP includes
both representations. All thirteen documents also have generated plain-R exports.

After editing a QMD, run from the course root:

```sh
python3 scripts/jupyter_notebooks.py
python3 scripts/jupyter_notebooks.py --check
```

The local course builder regenerates these exports on every build. The student
packager converts its relocated QMDs separately, retaining the correct helper
and image paths. Neither command publishes the website.

The exporter uses `quarto convert` with explicit R kernel metadata in a
temporary source. It does not change canonical QMD execution to Jupyter or
require IRkernel to be installed on the export machine. It verifies that
Quarto preserves every R cell, then restores the exact original cell text.

Notebook-specific adaptations:

- A first code cell locates the ancestor course folder containing `_quarto.yml`
  and `data/`, and sets the working directory there. Existing teaching imports
  remain unchanged, including when opening nested Superstore notebooks.
- Expand Quarto includes and rebase their relative images/links.
- Convert prose/grid tables to notebook Markdown; remove presentation div
  delimiters and expose raw HTML diagrams. The HTML/PDF remains the fully
  styled reading version; notebook renderers may simplify HTML/CSS diagrams.
- Present `eval: false` installation examples as manual Markdown code blocks:
  ordinary Jupyter Run All does not honour knitr's execution options.
- Keep outputs empty and use deterministic cell IDs for reviewable Git diffs.
- Preserve source fingerprints and numbered teaching-cell metadata for checks.

In Positron, open the complete course folder, open an IPYNB, select an installed
R interpreter in its kernel selector, and run from the top. The R packages are
the same as for the QMD. Positron supplies its own notebook R kernel support;
other Jupyter applications may need IRkernel configured separately.

Do not edit the generated IPYNB files as teaching sources. Regeneration replaces
student edits and saved outputs; students should save their own working copy.
