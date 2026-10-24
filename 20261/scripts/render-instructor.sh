#!/usr/bin/env bash
set -euo pipefail
project_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
quarto_bin="$(command -v quarto || true)"
if [[ -z "$quarto_bin" ]]; then quarto_bin=/usr/lib/rstudio/resources/app/bin/quarto/bin/quarto; fi
cd "$project_dir"
mkdir -p _instructor/_output
for source_file in _instructor/course-plan.qmd _instructor/solutions/module01/*.qmd _instructor/solutions/module02/*.qmd; do
  # Standalone documents embed their assets, so moving the finished HTML preserves it.
  "$quarto_bin" render "$source_file" --to html -M embed-resources:true
  python3 scripts/move-instructor-export.py "$source_file"
  rm -rf -- "${source_file%.qmd}_files"
done
