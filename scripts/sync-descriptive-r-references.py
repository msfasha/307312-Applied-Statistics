#!/usr/bin/env python3
"""Copy the companion's R code into slide reference panels, without executing it."""
import argparse
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / 'lessons/02-descriptive-statistics.qmd'
PRACTICAL = ROOT / 'practicals/descriptive-statistics-r-practical.qmd'


def synchronize(check=False):
    original = LESSON.read_text()
    result = re.sub(r'\n<!-- BEGIN TRY IN R [\w-]+ -->.*?<!-- END TRY IN R [\w-]+ -->\n',
                    '', original, flags=re.S)
    sections = re.findall(
        r'^## (\d+[ab]?)\. ([^\n]+)\n(.*?)(?=^## |\Z)',
        PRACTICAL.read_text(), re.M | re.S)
    if len(sections) != 20:
        raise RuntimeError('Expected 18 original descriptive R examples and two added charts')
    for number, title, body in sections:
        match = re.search(r'^```\{r\}\n#\| label: r-slide-([\w-]+)\n(.*?)^```',
                          body, re.M | re.S)
        if not match:
            raise RuntimeError('Missing R code for example ' + number)
        slide, code = match.groups()
        explicit_anchor = re.search(r' \{#([\w-]+)\}$', title)
        if explicit_anchor:
            title = title[:explicit_anchor.start()]
        # Figure captions belong to executed output, not displayed reference code.
        code = re.sub(r'^#\| fig-cap:.*\n', '', code, flags=re.M)
        anchor = re.sub(r'[^\w\s-]', '', title.lower())
        anchor = re.sub(r'\s+', '-', anchor)
        if explicit_anchor:
            anchor = explicit_anchor[1]
        panel = (
            f'\n<!-- BEGIN TRY IN R {slide} -->\n'
            f':::: {{.try-in-r #try-r-{slide}}}\n\n'
            f'#### Try this in R {{.unlisted}}\n\n'
            f'**Example {number}: {title}**\n\n'
            f'```r\n{code}```\n\n'
            f'[Open example {number} in the R practical]'
            f'(../practicals/descriptive-statistics-r-practical.html#{anchor}).\n\n'
            f'::::\n<!-- END TRY IN R {slide} -->\n'
        )
        pattern = rf'(::: {{\.source-slide #slide-{slide}}}\n.*?)(\n:::\n)'
        result, count = re.subn(pattern, lambda m: m[1] + panel + m[2],
                                result, count=1, flags=re.S)
        if count != 1:
            raise RuntimeError('Missing source slide ' + slide)
    if check:
        if result != original:
            raise RuntimeError('Slide R references need refreshing: run scripts/sync-descriptive-r-references.py')
    else:
        LESSON.write_text(result)
    print('Verified 20 slide R references.' if check else 'Updated 20 slide R references.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    synchronize(parser.parse_args().check)
