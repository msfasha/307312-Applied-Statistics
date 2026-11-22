"""Generate R Jupyter notebooks from the approved, canonical Quarto sources.

Quarto performs cell conversion with an explicit R kernelspec. Presentation-only
adaptations make includes, grid tables and manual installation cells readable
without a Quarto renderer. No installed Jupyter R kernel is needed for export.
"""
from pathlib import Path
import argparse
import hashlib
import json
import posixpath
import re
import subprocess
import tempfile
import yaml
from course_documents import DOCUMENTS

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = 'https://msfasha.github.io/307312-Applied-Statistics/'
KERNEL = {'name': 'ir', 'language': 'R', 'display_name': 'R'}
SETUP = '''# Notebook sessions may start in the notebook folder.
# Find the opened course folder so the original data/... paths work unchanged.
.course_root <- normalizePath(getwd(), winslash = "/")
while (!file.exists(file.path(.course_root, "_quarto.yml")) ||
       !dir.exists(file.path(.course_root, "data"))) {
  .course_parent <- dirname(.course_root)
  if (identical(.course_parent, .course_root)) {
    stop("Open the complete course folder containing _quarto.yml and data/.")
  }
  .course_root <- .course_parent
}
setwd(.course_root)
rm(.course_root)
if (exists(".course_parent", inherits = FALSE)) rm(.course_parent)
'''


def cell_text(cell):
    return ''.join(cell['source'])


def expand_includes(name, text, sources, stack=()):
    if name in stack:
        raise ValueError('Circular Quarto include: '+name)
    def include(match):
        target = posixpath.normpath(posixpath.join(posixpath.dirname(name), match[1]))
        included = expand_includes(target, sources[target], sources, (*stack, name))
        # Include image/link paths are relative to the included file.
        def rebase(m):
            link = m[1]
            if re.match(r'(?:[a-z]+:|/|#)', link):
                return m[0]
            resolved = posixpath.normpath(posixpath.join(posixpath.dirname(target), link))
            return m[0].replace(link, posixpath.relpath(resolved, posixpath.dirname(name)), 1)
        return re.sub(r'(?:\]\(|src=")([^\s"\)]+)', rebase, included)
    return re.sub(r'{{<\s*include\s+([^\s]+)\s*>}}', include, text)


def notebook(name, sources):
    original = sources[name]
    match = re.match(r'\A---\n(.*?)\n---\n', original, re.S)
    if not match:
        raise ValueError('Missing YAML header: '+name)
    config = yaml.safe_load(match[1])
    body = expand_includes(name, original[match.end():], sources)
    front = yaml.safe_dump({'jupyter': {'kernelspec': KERNEL}}, sort_keys=False)
    with tempfile.TemporaryDirectory(prefix='course-jupyter-') as tmp:
        source = Path(tmp)/'source.qmd'
        output = Path(tmp)/'source.ipynb'
        source.write_text('---\n'+front+'---\n\n'+body)
        subprocess.run(['quarto', 'convert', str(source), '--output', str(output)],
                       check=True, capture_output=True, text=True)
        result = json.loads(output.read_text())

    # Keep presentation YAML out of students' reading cells.
    cells = [c for c in result['cells'] if not cell_text(c).startswith('---\n')]
    title = config.get('title', Path(name).stem)
    intro = (f'# {title}\n\n'
             'R Jupyter version of the course material. Select an **R** kernel in Positron '
             'and run cells from top to bottom, starting with the setup cell. '
             'Keep the complete course folder, data and images together.\n\n'
             'Generated from the matching QMD; make teaching edits in the QMD and regenerate. '
             'The published HTML/PDF retains the full course styling.\n')
    result['cells'] = [dict(cell_type='markdown', metadata={}, source=intro.splitlines(True)),
                       dict(cell_type='code', metadata={'tags': ['course-root-setup']},
                            source=SETUP.splitlines(True), execution_count=None, outputs=[])]
    expected = re.findall(r'^```\{r[^\n]*\}\n(.*?)^```\s*$', body, re.M | re.S)
    actual = []
    for cell in cells:
        text = cell_text(cell)
        if cell['cell_type'] == 'code':
            # Quarto moves options to metadata; restore the exact source cell,
            # including comments/options, so code fidelity can be checked.
            code = expected[len(actual)]
            stripped = lambda s: re.sub(r'^#\|[^\n]*\n?', '', s, flags=re.M).strip()
            if stripped(text) != stripped(code):
                raise ValueError('Quarto changed teaching code: '+name)
            actual.append(code)
            cell['source'] = code.splitlines(True)
            cell['metadata']['course_source_cell'] = len(actual)
            if re.search(r'^#\|\s*eval:\s*false\s*$', code, re.M):
                # Jupyter Run All does not honour knitr's eval:false.
                cell = dict(cell_type='markdown', metadata=cell['metadata'], source=(
                    '**Manual setup — run once in the R Console if needed.** '
                    'This cell is excluded from Run All.\n\n```r\n'+code+'```\n').splitlines(True))
            result['cells'].append(cell)
        elif cell['cell_type'] == 'markdown' and text.strip():
            # Fenced divs can span code cells. Their styling wrappers are not
            # notebook content; remove only wrappers, preserving their contents.
            text = re.sub(r'^:{3,}[^\n]*\n?', '', text, flags=re.M)
            text = re.sub(r'^```\{=html\}\n(.*?)^```', r'\1', text, flags=re.M | re.S)
            text = re.sub(r'<!--.*?-->', '', text, flags=re.S)
            converted = subprocess.run(
                ['quarto', 'pandoc', '--from=markdown', '--to=gfm+tex_math_dollars', '--wrap=none'],
                input=text, text=True, capture_output=True, check=True).stdout
            # Teaching navigation opens the published material rather than
            # attempting to open non-existent local HTML beside the notebook.
            def link(m):
                target = m[1]
                if re.match(r'(?:[a-z]+:|/|#)', target):
                    return m[0]
                path, sep, fragment = target.partition('#')
                if not path.endswith(('.qmd', '.html')):
                    return m[0]
                resolved = posixpath.normpath(posixpath.join(posixpath.dirname(name), path))
                if resolved.endswith('.qmd'):
                    resolved = resolved[:-4]+'.html'
                return ']('+PUBLIC+resolved+(sep+fragment if sep else '')+')'
            converted = re.sub(r'\]\(([^\s)]+)\)', link, converted)
            cell['source'] = converted.splitlines(True)
            result['cells'].append(cell)
    if actual != expected:
        raise ValueError('Missing teaching cells: '+name)
    result['nbformat_minor'] = 5
    for i, cell in enumerate(result['cells']):
        cell['id'] = f'course-{i:03d}'
    result['metadata'] = {
        'kernelspec': KERNEL,
        'language_info': {'name': 'R', 'file_extension': '.r', 'mimetype': 'text/x-r-source'},
        'course': {'source': name, 'source_sha256': hashlib.sha256(original.encode()).hexdigest(),
                   'teaching_cells': len(expected), 'generator': 'scripts/jupyter_notebooks.py'},
    }
    validate_notebook(result)
    return result


def validate_notebook(result):
    assert result['metadata']['kernelspec'] == KERNEL
    assert result['nbformat'] == 4 and result['nbformat_minor'] == 5
    teaching = [c for c in result['cells'] if 'course_source_cell' in c['metadata']]
    assert len(teaching) == result['metadata']['course']['teaching_cells']
    assert [c['metadata']['course_source_cell'] for c in teaching] == list(range(1, len(teaching)+1))
    assert len({c['id'] for c in result['cells']}) == len(result['cells'])
    for c in result['cells']:
        if c['cell_type'] == 'code':
            assert c['execution_count'] is None and c['outputs'] == []
        assert '{{< include' not in cell_text(c)


def serialize(result):
    return json.dumps(result, ensure_ascii=False, indent=1)+'\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Check generated files without writing.')
    args = parser.parse_args()
    from student_project import project_files
    sources = {n: (ROOT/n).read_text() for n in project_files() if n.endswith('.qmd')}
    for folder, stem in DOCUMENTS:
        name = f'{folder}/{stem}.qmd'
        content = serialize(notebook(name, sources))
        output = ROOT/Path(name).with_suffix('.ipynb')
        if args.check:
            if not output.exists() or output.read_text() != content:
                raise RuntimeError('Stale Jupyter notebook; run python3 scripts/jupyter_notebooks.py: '+name)
        else:
            output.write_text(content)
        print(('Checked ' if args.check else 'Generated ')+str(output.relative_to(ROOT)), flush=True)


if __name__ == '__main__':
    main()
