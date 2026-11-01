"""Copy student chapter companions with their maintained source text and card data."""
from pathlib import Path
import shutil,hashlib
ROOT=Path(__file__).resolve().parents[2]
def copy_to(destination):
 records={}
 for old in (Path(destination)/'book-chapters').rglob('*.pptx'): old.unlink()
 for source in sorted((ROOT/'book-chapters').rglob('*')):
  if source.is_file():
   target=Path(destination)/source.relative_to(ROOT);target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,target)
   records[str(source.relative_to(ROOT))]=hashlib.sha256(source.read_bytes()).hexdigest()
 generated=ROOT/'_output/book-chapters'
 for source in sorted(generated.rglob('*')):
  if source.is_file() and source.suffix == '.pdf':
   target=Path(destination)/'book-chapters'/source.relative_to(generated);target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,target)
   records[str(target.relative_to(destination))]=hashlib.sha256(source.read_bytes()).hexdigest()
 expected='book-chapters/basic-business-statistics-13e/'
 for name in ['chapter01-original.pdf','chapter01-flashcards.pdf']:
  if expected+name not in records:raise SystemExit('Missing chapter companion: '+name)
 return records
