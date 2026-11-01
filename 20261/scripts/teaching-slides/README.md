# Reduced teaching presentations

These are sequential companions to the extended Quarto lessons, with short teaching cues, the instructor's diagrams and examples, and full source passages in PowerPoint notes. They are not a replacement for the practical lessons. Module 1 has 183 slides; Module 2 has 192 slides across five lessons. Frequent, light slides allow pauses while students use Quarto.

The authored `author-moduleNN.py` files preserve the teaching order and map each slide to the corresponding source heading. The generated private coverage report checks every heading. `render-module02.R` executes the original evaluated R chunks, preserving their assertions, data, plots and quartile conventions. Raw publisher workbooks and instructor answers are never inputs to the deck build.

Run from the repository root using the bundled Python environment (Pillow, pypdf, CairoSVG and lxml), Node with `@oai/artifact-tool`, R with course packages, and LibreOffice:

```sh
python3 20261/scripts/teaching-slides/build.py --module 1 --revision review-20261101
python3 20261/scripts/teaching-slides/build.py --module 2 --revision review-20261101
```

Each build uses a unique final filename, validates editable text/tables and package geometry, and adds PDF lesson bookmarks. Private build records are under `_output/.moduleNN-teaching-build/`. Inspect rendered slides and content coverage before selecting a revision. Copy its unchanged PDF/PPTX bytes to `_output/teaching-slides/module01-introduction-to-r.{pdf,pptx}` or `module02-descriptive-statistics.{pdf,pptx}`. Then run:

```sh
python3 20261/scripts/teaching-slides/materials.py --stamp
```

The manifest binds the outputs to lesson sources, scripts, assets, data, and shared style. Packaging rejects missing or stale downloads. All three student packages include the four stable teaching files; HTML lesson and module links point to them. Student packages include the finished presentations and ordinary Quarto sources, without requiring these maintainer scripts. Follow `PUBLISHING.md` to build, package and publish.

Module 2 retains the supplied measurement-level, boxplot, statistical toolbox, and summary images. The seven-dollar example, five equal-mean sets, equal-range comparison, mean/median limitations, variance versus absolute deviation, sample denominator, and range/IQR limitations remain explicit. Caveats correct misleading fence labels and distinguish a population-style variance diagram from sample variance. Generated R plots retain the source observations and conventions. Source notes in each slide support access to the extended explanation.

Module 2 includes 34 practical R slides. Their code is extracted verbatim from named, evaluated Quarto chunks, including comments; it is not maintained as a separate slide-code copy. Visible imports identify the CSV and variables before use. The R renderer executes 79 source chunks, records practical outputs privately, and retains the original statistical assertions. `r-code-coverage.json` maps every R slide to its exact Quarto chunk. Concept, code, and result appear together in the original lesson sequence.
