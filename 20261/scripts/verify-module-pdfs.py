#!/usr/bin/env python3
"""Check every distributed PDF link and the assembled module navigation."""
from pathlib import Path
import importlib.util
import json
from urllib.parse import unquote, urlsplit

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT/'_output/pdf-modules'
spec = importlib.util.spec_from_file_location('module_pdfs', ROOT/'scripts/module-pdfs.py')
modules = importlib.util.module_from_spec(spec)
spec.loader.exec_module(modules)


def main():
    manifest = json.loads((OUTPUT/'module-pdf-manifest.json').read_text())
    readers = {name: PdfReader(OUTPUT/name) for name in manifest['outputs']}
    links = 0
    for name, reader in readers.items():
        page_refs = {p.indirect_reference.idnum for p in reader.pages}
        for number, page in enumerate(reader.pages):
            for ref in page.get('/Annots', []):
                annotation = ref.get_object()
                a = annotation.get('/A', {})
                kind = a.get('/S')
                if kind == '/GoTo':
                    dest = a['/D']
                    if isinstance(dest, str):
                        assert dest in reader.named_destinations, (name, number, dest)
                    else:
                        assert dest[0].idnum in page_refs, (name, number, dest)
                    links += 1
                elif kind in {'/GoToR', '/URI'}:
                    uri = urlsplit(str(a['/F'] if kind == '/GoToR' else a['/URI']))
                    if uri.scheme or uri.netloc or not uri.path:
                        continue
                    target = (OUTPUT/name).parent/unquote(uri.path)
                    assert target.is_file(), (name, number, str(target))
                    assert target.resolve().is_relative_to(OUTPUT.resolve()), (name, str(target))
                    if kind == '/GoToR':
                        linked = readers.get(str(target.resolve().relative_to(OUTPUT.resolve()))) or PdfReader(target)
                        dest = a['/D']
                        if isinstance(dest, str):
                            assert dest in linked.named_destinations, (name, str(target), dest)
                        else:
                            assert 0 <= int(dest[0]) < len(linked.pages), (name, str(target), dest)
                    links += 1
    groups = modules.module_sources()
    assert len(list((OUTPUT/'modules').glob('*.pdf'))) == len(groups)
    for slug, sources in groups.items():
        reader = readers[f'modules/{slug}.pdf']
        cover_links = [ref.get_object() for ref in reader.pages[0].get('/Annots', [])]
        assert len(cover_links) == len(sources), slug
        cursor = 1
        for section, source in enumerate(sources):
            original = PdfReader(modules.INPUT/source.with_suffix('.pdf'))
            assert cover_links[section]['/A']['/D'][0] == reader.pages[cursor].indirect_reference, (slug, source)
            for local_number, original_page in enumerate(original.pages):
                page = reader.pages[cursor+local_number]
                expected = 1 + (section > 0) + (section+1 < len(sources))
                annotations = list(page.get('/Annots', []))
                assert len(annotations) == len(list(original_page.get('/Annots', []))) + expected, (slug, source, local_number, 'Lost links')
                navigation = [ref.get_object() for ref in annotations[-expected:]]
                assert navigation[0]['/A']['/D'][0] == reader.pages[0].indirect_reference
                index = 1
                if section > 0:
                    assert navigation[index]['/A']['/D'][0] == cover_links[section-1]['/A']['/D'][0]
                    index += 1
                if section+1 < len(sources):
                    assert navigation[index]['/A']['/D'][0] == cover_links[section+1]['/A']['/D'][0]
            cursor += len(original.pages)
        assert cursor == len(reader.pages), slug
    print(f'Checked {len(groups)} module PDFs and {links} local/internal links; topic order, contents targets, footer navigation, and annotation preservation passed.')


if __name__ == '__main__':
    main()
