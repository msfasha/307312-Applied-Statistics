"""Locate teaching sections using their existing Quarto identifiers."""
import re

def inferential_blocks(source):
    for block in re.split(r'(?=^:::::: \{\.source-slide #)', source, flags=re.M)[1:]:
        found = re.match(r':::::: \{\.source-slide #part3-(\d+)-slide-(\d+)', block)
        if found:
            yield '-'.join(str(int(n)) for n in found.groups()), block

def r_panel(block):
    return re.search(r'\n:::: \{\.try-in-r #r-example-[\d-]+\}\n.*?^::::\n', block, re.M | re.S)
