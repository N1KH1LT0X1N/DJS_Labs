import json

with open('lab8.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

print(f'Number of cells: {len(nb["cells"])}')
print(f'First cell type: {nb["cells"][0].get("cell_type", "unknown")}')
print(f'Last cell type: {nb["cells"][-1].get("cell_type", "unknown")}')

# Print first few cell titles
for i, cell in enumerate(nb['cells'][:5]):
    if cell['cell_type'] == 'markdown':
        content = cell['source'][0] if cell['source'] else ''
        print(f'Cell {i}: MARKDOWN - {content[:50]}')
    else:
        print(f'Cell {i}: CODE')
