#!/usr/bin/env python3
"""Assemble rendered student pages into one internally linked PDF per module.

Run with Python containing pypdf and reportlab. Topic exports remain private build
inputs in _output/pdf; only this script's _output/pdf-modules tree is distributed.
"""
from collections import OrderedDict
from io import BytesIO
from pathlib import Path
import hashlib
import json
import os
import posixpath
import re
import shutil
from urllib.parse import unquote, urlsplit

from pypdf import PdfReader, PdfWriter
from pypdf.generic import ArrayObject, DictionaryObject, NameObject, NumberObject, TextStringObject
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / '_output/pdf'
OUTPUT = ROOT / '_output/pdf-modules'
pdfmetrics.registerFont(TTFont('PetraSans', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('PetraBold', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))


def module_sources():
    """Use the website sidebar as the single maintained teaching sequence."""
    groups = OrderedDict()
    for href in re.findall(r'^\s+href: (modules/[^\s]+\.qmd)\s*$', (ROOT/'_quarto.yml').read_text(), re.M):
        source = Path(href)
        group = groups.setdefault(source.parts[1], [])
        if source not in group:
            group.append(source)
    actual = {p.relative_to(ROOT) for p in (ROOT/'modules').rglob('*.qmd')}
    if actual != {p for group in groups.values() for p in group}:
        raise SystemExit('Every module source must appear exactly once in the website sidebar.')
    return groups


def title(source):
    match = re.search(r'^title:\s*(.+)$', (ROOT/source).read_text(), re.M)
    if not match:
        raise ValueError(f'Missing title: {source}')
    return match[1].strip().strip('"\'')


def action(destination):
    return DictionaryObject({NameObject('/S'): NameObject('/GoTo'), NameObject('/D'): destination})


def page_destination(writer, page, tail=None):
    return ArrayObject([writer.pages[page].indirect_reference] + (list(tail) if tail else [NameObject('/Fit')]))


def local_destination(reader, destination):
    """Resolve source-local names before merging, avoiding repeated LaTeX names."""
    if isinstance(destination, str):
        resolved = reader.named_destinations.get(destination)
        if resolved is None:
            # Quarto cross-file links use HTML heading slugs, while XeLaTeX uses
            # generated subsection names. Bookmarks retain the visible headings.
            def find(items):
                for item in items:
                    if isinstance(item, list):
                        found = find(item)
                        if found is not None:
                            return found
                    else:
                        slug = re.sub(r'[^\w\s-]', '', item.title.lower())
                        slug = re.sub(r'\s+', '-', slug)
                        if slug == destination:
                            return item
                return None
            resolved = find(reader.outline)
        if resolved is None:
            # Some existing headings are absent from PDF bookmarks (for example,
            # below the outline depth). Resolve an exact visible heading line.
            pattern = r'(?:^|\n|#{1,6}\s+)' + r'[\s-]+'.join(re.escape(word) for word in destination.split('-')) + r'\s*(?:\n|$)'
            matches = [number for number, page in enumerate(reader.pages)
                       if re.search(pattern, page.extract_text(), re.I)]
            if len(matches) == 1:
                return matches[0], None
            raise ValueError(f'Unknown or ambiguous internal destination: {destination}')
        return reader.get_destination_page_number(resolved), resolved.dest_array[1:]
    destination = destination.get_object()
    reference = destination[0]
    if isinstance(reference, int):
        return int(reference), destination[1:]
    for number, page in enumerate(reader.pages):
        if page.indirect_reference == reference:
            return number, destination[1:]
    raise ValueError(f'Unresolved destination: {destination}')


def add_outline(writer, reader, offset, parent):
    previous = parent
    for item in reader.outline:
        if isinstance(item, list):
            # pypdf represents children as a list following their parent.
            def children(items, node):
                last = node
                for child in items:
                    if isinstance(child, list):
                        children(child, last)
                    else:
                        last = writer.add_outline_item(child.title, offset + reader.get_destination_page_number(child), parent=node)
            children(item, previous)
        else:
            previous = writer.add_outline_item(item.title, offset + reader.get_destination_page_number(item), parent=parent)


def contents(module_title, sources, offsets):
    stream = BytesIO()
    c = canvas.Canvas(stream, pagesize=A4)
    width, height = A4
    c.setFillColor(HexColor('#A83296'))
    c.rect(48, height-55, width-96, 3, fill=1, stroke=0)
    c.setFillColor(HexColor('#F5EDF4'))
    c.rect(48, height-145, width-96, 88, fill=1, stroke=0)
    c.setFillColor(HexColor('#493347'))
    c.setFont('PetraBold', 18)
    # Module names are long; wrap without shrinking the document's typography.
    words, lines = module_title.split(), ['']
    for word in words:
        candidate = (lines[-1]+' '+word).strip()
        if c.stringWidth(candidate, 'PetraBold', 18) > width-125:
            lines.append(word)
        else:
            lines[-1] = candidate
    for number, line in enumerate(lines):
        c.drawString(62, height-87-number*24, line)
    c.setFillColor(HexColor('#2F343B'))
    c.setFont('PetraSans', 11)
    c.drawString(48, height-174, '307312 Applied Statistics | University of Petra')
    c.setFont('PetraBold', 14)
    c.drawString(48, height-214, 'Module contents')
    c.setFont('PetraSans', 10)
    c.drawString(48, height-236, 'Click a topic below, or use the PDF reader bookmarks.')
    c.drawString(48, height-252, 'Every page has links to contents and the previous/next topic.')
    rectangles = []
    y = height-288
    for source in sources:
        label = 'Overview' if source.name == 'index.qmd' else title(source)
        # Keep each contents entry on one readable line (wrap only if necessary).
        words, lines = label.split(), ['']
        for word in words:
            candidate = (lines[-1]+' '+word).strip()
            if c.stringWidth(candidate, 'PetraSans', 10) > width-155:
                lines.append(word)
            else:
                lines[-1] = candidate
        c.setFillColor(HexColor('#356B8C'))
        for line in lines:
            c.drawString(52, y, line)
            y -= 14
        c.drawRightString(width-52, y+14, str(offsets[source]+1))
        rectangles.append((source, (48, y+10, width-48, y+len(lines)*14+12)))
        y -= 15
    if y < 90:
        raise ValueError('Module contents needs an additional page; extend pagination before adding topics.')
    c.save()
    return PdfReader(stream), rectangles


def rewrite_links(writer, reader, source, target, offset, mapping, readers):
    """Rebase data/companion links and convert same-module links to GoTo."""
    for number, original in enumerate(reader.pages):
        copied = writer.pages[offset+number]
        for original_ref, copied_ref in zip(original.get('/Annots', []), copied.get('/Annots', [])):
            old, new = original_ref.get_object(), copied_ref.get_object()
            a = old.get('/A', {})
            internal = old.get('/Dest') or (a.get('/D') if a.get('/S') == '/GoTo' else None)
            if internal is not None:
                page, tail = local_destination(reader, internal)
                new[NameObject('/A')] = action(page_destination(writer, offset+page, tail))
                new.pop('/Dest', None)
                continue
            kind = a.get('/S')
            if kind not in {'/URI', '/GoToR'}:
                continue
            raw = str(a.get('/URI') if kind == '/URI' else a.get('/F'))
            uri = urlsplit(raw)
            if uri.scheme or uri.netloc or not uri.path:
                continue
            resolved = Path(posixpath.normpath(str(source.parent / unquote(uri.path))))
            if resolved.suffix in {'.qmd', '.Rmd'}:
                resolved = resolved.with_suffix('.pdf')
            if resolved in mapping:
                destination_file, start = mapping[resolved]
                tail = None
                dest = a.get('/D') if kind == '/GoToR' else None
                fragment = unquote(uri.fragment)
                if fragment:
                    dest = fragment
                if dest is not None:
                    linked_reader = readers[resolved]
                    page, tail = local_destination(linked_reader, dest)
                    start += page
                if destination_file == target:
                    new[NameObject('/A')] = action(page_destination(writer, start, tail))
                else:
                    relative = os.path.relpath(destination_file, target.parent)
                    new[NameObject('/A')] = DictionaryObject({
                        NameObject('/S'): NameObject('/GoToR'),
                        NameObject('/F'): TextStringObject(relative),
                        NameObject('/D'): ArrayObject([NumberObject(start), NameObject('/Fit')]),
                    })
            else:
                relative = os.path.relpath(resolved, target.parent)
                replacement = DictionaryObject(a)
                replacement[NameObject('/URI' if kind == '/URI' else '/F')] = TextStringObject(relative + (('#'+uri.fragment) if uri.fragment else ''))
                new[NameObject('/A')] = replacement


def footer(writer, page_number, section, sources, offsets, total):
    page = writer.pages[page_number]
    width, height = float(page.mediabox.width), float(page.mediabox.height)
    stream = BytesIO()
    c = canvas.Canvas(stream, pagesize=(width, height))
    # Place the new navigation in the lower margin, below the existing text.
    c.setFillColor(HexColor('#FFFFFF'))
    c.rect(40, 12, width-80, 32, fill=1, stroke=0)
    c.setStrokeColor(HexColor('#DEE2E6'))
    c.line(48, 42, width-48, 42)
    c.setFont('PetraSans', 8)
    c.setFillColor(HexColor('#356B8C'))
    links = [('Contents', 48, 0)]
    if section > 0:
        links.append(('Previous topic', 135, offsets[sources[section-1]]))
    if section+1 < len(sources):
        links.append(('Next topic', 245, offsets[sources[section+1]]))
    for label, x, destination in links:
        c.drawString(x, 27, label)
        writer.add_annotation(page_number, DictionaryObject({
            NameObject('/Type'): NameObject('/Annot'), NameObject('/Subtype'): NameObject('/Link'),
            NameObject('/Rect'): ArrayObject([NumberObject(x), NumberObject(23), NumberObject(x+80), NumberObject(38)]),
            NameObject('/Border'): ArrayObject([NumberObject(0)]*3),
            NameObject('/A'): action(page_destination(writer, destination)),
        }))
    c.setFillColor(HexColor('#56616D'))
    c.drawString(355, 27, f'Topic p. {page_number-offsets[sources[section]]+1}')
    c.drawRightString(width-48, 27, f'{page_number+1} / {total}')
    c.save()
    page.merge_page(PdfReader(stream).pages[0])


def main():
    groups = module_sources()
    sources = [Path('index.qmd')] + [p for group in groups.values() for p in group]
    sources += sorted(p.relative_to(ROOT) for p in (ROOT/'resources').rglob('*') if p.suffix in {'.qmd', '.Rmd'})
    for source in sources:
        exported = INPUT/source.with_suffix('.pdf')
        if not exported.exists() or exported.stat().st_mtime < (ROOT/source).stat().st_mtime:
            raise SystemExit(f'Missing or stale topic PDF: {source}. Render it before assembling modules.')
    readers = {s.with_suffix('.pdf'): PdfReader(INPUT/s.with_suffix('.pdf')) for s in sources}
    mapping, plans = {}, []
    for slug, group in groups.items():
        target = Path('modules')/(slug+'.pdf')
        offsets, cursor = {}, 1
        for source in group:
            offsets[source] = cursor
            mapping[source.with_suffix('.pdf')] = (target, cursor)
            cursor += len(readers[source.with_suffix('.pdf')].pages)
        plans.append((target, group, offsets, cursor))
    standalone = [s for s in sources if s.parts[0] != 'modules']
    for source in standalone:
        mapping[source.with_suffix('.pdf')] = (source.with_suffix('.pdf'), 0)
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir(parents=True)
    for target, group, offsets, total in plans:
        writer = PdfWriter()
        cover, rectangles = contents(title(group[0]), group, offsets)
        for page in cover.pages:
            writer.add_page(page)
        writer.add_outline_item('Module contents', 0)
        for source in group:
            reader = readers[source.with_suffix('.pdf')]
            for page in reader.pages:
                writer.add_page(page)
            label = 'Overview' if source.name == 'index.qmd' else title(source)
            parent = writer.add_outline_item(label, offsets[source])
            add_outline(writer, reader, offsets[source], parent)
        for source, rectangle in rectangles:
            writer.add_annotation(0, DictionaryObject({
                NameObject('/Type'): NameObject('/Annot'), NameObject('/Subtype'): NameObject('/Link'),
                NameObject('/Rect'): ArrayObject([NumberObject(n) for n in rectangle]),
                NameObject('/Border'): ArrayObject([NumberObject(0)]*3),
                NameObject('/A'): action(page_destination(writer, offsets[source])),
            }))
        for section, source in enumerate(group):
            reader = readers[source.with_suffix('.pdf')]
            rewrite_links(writer, reader, source, target, offsets[source], mapping, readers)
            for number in range(offsets[source], offsets[source]+len(reader.pages)):
                footer(writer, number, section, group, offsets, total)
        writer.add_metadata({'/Title': title(group[0]), '/Author': 'University of Petra | 307312 Applied Statistics'})
        writer.page_mode = '/UseOutlines'
        destination = OUTPUT/target
        destination.parent.mkdir(parents=True, exist_ok=True)
        writer.write(destination)
        print(f'{target}: {total} pages, {len(group)} topics', flush=True)
    for source in standalone:
        target = source.with_suffix('.pdf')
        reader = readers[target]
        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
        add_outline(writer, reader, 0, None)
        rewrite_links(writer, reader, source, target, 0, mapping, readers)
        (OUTPUT/target).parent.mkdir(parents=True, exist_ok=True)
        writer.write(OUTPUT/target)
    # Packaging checks these exact inputs/outputs, including shared build code.
    inputs = sources + [Path(p) for p in [
        '_quarto.yml', '_quarto-pdf.yml', 'scripts/module-pdfs.py',
        'scripts/verify-module-pdfs.py', 'scripts/build-pdfs.py',
        'scripts/pdf-layout.lua', 'assets/pdf/petra-print.tex',
    ]]
    record = {
        'inputs': {str(p): hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs},
        'topic_exports': {str(s.with_suffix('.pdf')): hashlib.sha256((INPUT/s.with_suffix('.pdf')).read_bytes()).hexdigest() for s in sources},
        'outputs': {str(p.relative_to(OUTPUT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(OUTPUT.rglob('*.pdf'))},
    }
    (OUTPUT/'module-pdf-manifest.json').write_text(json.dumps(record, indent=2)+'\n')


if __name__ == '__main__':
    main()
