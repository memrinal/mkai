import json
import csv
from pathlib import Path

nb_file = Path('proj1/prog2_saved.ipynb')
csv_file = Path('proj1/prog2_cells.csv')

with nb_file.open('r', encoding='utf-8') as f:
    nb = json.load(f)

rows = []
for idx, cell in enumerate(nb.get('cells', []), start=1):
    source = cell.get('source', [])
    if isinstance(source, list):
        source_text = ''.join(source).replace('\n', '\\n')
    else:
        source_text = str(source).replace('\n', '\\n')
    rows.append({'cell_index': idx, 'cell_type': cell.get('cell_type'), 'source': source_text})

with csv_file.open('w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['cell_index', 'cell_type', 'source'])
    writer.writeheader()
    for r in rows:
        writer.writerow(r)

print(f'Wrote {len(rows)} rows to {csv_file}')
