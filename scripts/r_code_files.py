"""Export every approved notebook's R cells in teaching order as a plain R script."""
from pathlib import Path
import re
import yaml
from course_documents import DOCUMENTS
ROOT = Path(__file__).resolve().parents[1]

def r_code_source(filename):
    return next(f'{folder}/{name}.qmd' for folder, name in DOCUMENTS
                if filename == name+'.R')

def r_code_files():
    files = {}
    for folder, name in DOCUMENTS:
        source = (ROOT/folder/(name+'.qmd')).read_text()
        chunks = re.findall(r'^```\{r[^\n]*\}\n(.*?)^```', source, re.M | re.S)
        title = yaml.safe_load(source.split('---', 2)[1])['title']
        parts = [f'# 307312 Applied Statistics — {title}\n'
                 '# Run sections in order from the course root folder containing data/.\n'
                 '# Download the complete course ZIP for the required CSV files.\n'
                 '# Explanations and output interpretation are in the matching course notebook.\n']
        for i, chunk in enumerate(chunks, 1):
            # Chunk display options are Quarto metadata, not R instructions.
            code = re.sub(r'^#\|[^\n]*\n?', '', chunk, flags=re.M).strip()
            label = re.search(r'^#\| label: (.+)$', chunk, re.M)
            parts.append('\n# --- '+(label[1] if label else f'Section {i}')+' ---\n')
            if re.search(r'^#\|\s*eval:\s*false', chunk, re.M):
                parts.append('# Run manually once if the packages are not installed:\n')
                code = '\n'.join('# '+line for line in code.splitlines())
            parts.append(code+'\n')
        files[name+'.R'] = ''.join(parts)
    return files
