"""Validate and copy generated teaching downloads into all student distributions."""
from pathlib import Path
import hashlib,json,shutil

ROOT=Path(__file__).resolve().parents[2]
REGISTRY=[
    ('module01-introduction-to-r','01-introduction-to-r'),
    ('module02-descriptive-statistics','02-data-and-descriptive-statistics'),
]

def dependencies(module):
    # Source and data hashes catch changed shared inputs as well as edited slides.
    result=list((ROOT/'modules'/module).glob('*.qmd'))
    result+=list((ROOT/'data/module02').glob('*.csv'))
    result+=list((ROOT/'scripts/teaching-slides').glob('*'))
    result+=[ROOT.parent/'COURSE_STYLE.md',ROOT/'assets/petra-brand.css']
    asset_folder=ROOT/('assets/module01' if module.startswith('01') else 'assets/module02')
    result += [p for p in asset_folder.rglob('*') if p.suffix.lower() in {'.png','.svg','.gif','.jpg','.jpeg','.md'}]
    return sorted(p for p in result if p.is_file())

def hashes(module):
    return {str(p.relative_to(ROOT.parent)):hashlib.sha256(p.read_bytes()).hexdigest() for p in dependencies(module)}

def stamp():
    records={}
    for stem,module in REGISTRY:
        records[stem]={'sources':hashes(module),'outputs':{}}
        for suffix in ['pdf','pptx']:
            p=ROOT/'_output/teaching-slides'/f'{stem}.{suffix}'
            if not p.exists():raise SystemExit(f'Missing teaching download: {p}')
            records[stem]['outputs'][p.name]=hashlib.sha256(p.read_bytes()).hexdigest()
    p=ROOT/'_output/teaching-slides/manifest.json'
    p.write_text(json.dumps(records,indent=2)+'\n')
    return records

def checked():
    source=ROOT/'_output/teaching-slides'
    manifest=source/'manifest.json'
    if not manifest.exists():raise SystemExit('Build the reduced teaching materials before packaging.')
    records=json.loads(manifest.read_text())
    for stem,module in REGISTRY:
        if records[stem]['sources']!=hashes(module):raise SystemExit(f'Stale teaching material sources: {stem}. Rebuild and validate the decks.')
        for name,digest in records[stem]['outputs'].items():
            p=source/name
            if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=digest:
                raise SystemExit(f'Stale or missing teaching download: {name}')
    return records

def copy_to(folder):
    records=checked()
    records={stem:{**record,'outputs':{name:digest for name,digest in record['outputs'].items() if name.endswith('.pdf')}} for stem,record in records.items()}
    dest=Path(folder)/'teaching-slides';dest.mkdir(parents=True,exist_ok=True)
    for old in dest.glob('*.pptx'): old.unlink()
    for record in records.values():
        for name in record['outputs']:
            shutil.copy2(ROOT/'_output/teaching-slides'/name,dest/name)
    (dest/'manifest.json').write_text(json.dumps(records,indent=2)+'\n')
    return records

if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--stamp',action='store_true')
    parser.add_argument('--copy-to',type=Path)
    args=parser.parse_args()
    if args.stamp:stamp()
    elif args.copy_to:copy_to(args.copy_to)
    else:checked()
