#!/usr/bin/env python3
"""Check local function explanations in all active R teaching chunks and scripts.

R's parser inventories actual calls (excluding strings and comments). Each called
function must be named in a comment in the same chunk/script. This checks coverage,
not pedagogical quality: review the meaning of comments and argument values too.
Blank scaffolds remain untouched. The deliberately unfinished *:* loop and switch syntax template are reported
separately rather than parsed as an executable example.
"""
from pathlib import Path
import csv
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def main():
    blocks = []
    for source in sorted(ROOT.rglob('*')):
        if source.suffix not in {'.qmd', '.Rmd', '.R'}:
            continue
        if any(part in {'_site', '_output', '.quarto', '_freeze'} for part in source.parts):
            continue
        text = source.read_text()
        snippets = [text] if source.suffix == '.R' else re.findall(
            r'```(?:\{r[^\n]*\}|[ \t]*r[ \t]*)\n(.*?)```', text, re.S)
        for number, code in enumerate(snippets, 1):
            if any(line.strip() and not line.lstrip().startswith('#') for line in code.splitlines()):
                blocks.append((source.relative_to(ROOT), number, code))
    with tempfile.TemporaryDirectory(prefix='stats-code-audit-') as directory:
        temp = Path(directory)
        for index, (_, _, code) in enumerate(blocks):
            (temp / f'{index}.R').write_text(code)
        # Keep R parsing separate from evaluation: error demonstrations and exercises must not execute.
        parser = r'''
args <- commandArgs(trailingOnly=TRUE)
files <- list.files(args[1],pattern="[.]R$",full.names=TRUE)
for (file in files) {
  expr <- tryCatch(parse(file,keep.source=TRUE),error=function(e) NULL)
  if (is.null(expr)) {
    cat(basename(file),"PARSE_ERROR",sep="\t"); cat("\n")
  } else {
    tokens <- getParseData(expr)
    calls <- unique(tokens$text[tokens$token=="SYMBOL_FUNCTION_CALL"])
    cat(basename(file),paste(calls,collapse="|"),sep="\t"); cat("\n")
  }
}
'''
        result = subprocess.run(['Rscript', '-e', parser, str(temp)], check=True,
                                capture_output=True, text=True)
        errors = []
        scaffolds = 0
        for filename, names in csv.reader(result.stdout.splitlines(), delimiter='\t'):
            path, number, code = blocks[int(Path(filename).stem)]
            if names == 'PARSE_ERROR':
                if (('*:*' in code and 'practice' in code.lower()) or
                    ('switch(EXPR,' in code and '# Code for case' in code)):
                    scaffolds += 1
                    continue
                errors.append(f'{path} block {number}: could not parse R')
                continue
            comments = '\n'.join(line for line in code.splitlines()
                                 if line.lstrip().startswith('#') and not line.lstrip().startswith('#|'))
            for function in filter(None, names.split('|')):
                if not re.search(r'\b' + re.escape(function) + r'\s*\(', comments):
                    errors.append(f'{path} block {number}: explain {function}() locally')
            if 'modules' in path.parts and len([line for line in comments.splitlines() if line.strip()]) < 2:
                errors.append(f'{path} block {number}: fewer than two explanatory comments')
        if errors:
            raise SystemExit('\n'.join(errors))
        print(f'Checked {len(blocks)} nonempty R blocks/scripts; {scaffolds} documented unfinished scaffold(s).')
        print('Function-name coverage passed. Human review of explanations and consequential arguments is still required.')


if __name__ == '__main__':
    main()
