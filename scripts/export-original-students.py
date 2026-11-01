#!/usr/bin/env python3
"""Export the original 307102 worksheet columns without changing source data."""
from pathlib import Path
import openpyxl, csv, hashlib, json
ROOT=Path(__file__).resolve().parents[1]
src=ROOT.parent/'307102-Descriptive-Statistics-for-Business/Practical/1- Descriptive Statistics - Practical Exercises/students.xlsx'
wb=openpyxl.load_workbook(src,read_only=True,data_only=True)
rows=iter(wb['students'].values); header=next(rows)
columns=['gender','age','height','weight','country','major']
indexes=[header.index(c) for c in columns]
values=[[row[i] for i in indexes] for row in rows if any(v is not None for v in row)]
out=ROOT/'data/307102';out.mkdir(exist_ok=True)
with (out/'students.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(columns);w.writerows(values)
with (out/'students.csv').open() as f:
 restored=list(csv.reader(f))
assert len(restored)-1==len(values)==8239
assert restored[1:]==[[str(v) if v is not None else '' for v in row] for row in values]
(out/'provenance.json').write_text(json.dumps({'source':str(src),'sheet':'students','source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'rows':len(values),'columns':columns,'transformations':'Column selection only; no row filtering except entirely empty worksheet rows. CSV values verified cell by cell. IDs and names excluded.','units':{'age':'years','height':'cm','weight':'kg'},'units_basis':'Original slide/workbook context; not independently measured.','original_collection_provenance':'Not established. Do not describe as observed university student records.'},indent=2)+'\n')
print('Exported and verified all 8,239 rows × 6 selected columns.')
