#!/usr/bin/env python3
"""Validate the 20 executable R examples in the combined descriptive lesson.

The historical command name is retained for existing build workflows. There is
one canonical notebook now, so there is no second code copy to synchronize.
"""
import argparse
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / 'lessons/02-descriptive-statistics.qmd'
EXPECTED = ['16','17','18','19','23','24','26','added-line-chart','added-dot-plot',
            '28','33','42','50','55','63','68','72','74','76','79']

def synchronize(check=False):
    text = LESSON.read_text()
    labels = re.findall(r'^#\| label: r-slide-([\w-]+)$', text, re.M)
    assert labels == EXPECTED, ('Missing or reordered descriptive R examples', labels)
    assert re.findall(r'<!-- BEGIN TRY IN R ([\w-]+) -->', text) == EXPECTED
    assert len(re.findall(r'^```\{r\}$', text, re.M)) == 20
    assert not re.search(r'^```r$', text, re.M), 'R examples must be executable Quarto cells'
    assert 'Open example ' not in text, 'Examples must not send students to a separate practical'
    for slide in EXPECTED:
        panel = re.search(rf'<!-- BEGIN TRY IN R {slide} -->(.*?)<!-- END TRY IN R {slide} -->',text,re.S)[1]
        assert ('**What we are doing:**' in panel or '**Purpose:**' in panel), slide
        assert ('**How to read the result:**' in panel or '**Read the chart:**' in panel), slide
        assert f'#| label: r-slide-{slide}' in panel, slide
    print('Verified 20 explained executable R examples in the combined Part 2 notebook.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Check the combined notebook (the default).')
    synchronize(parser.parse_args().check)
