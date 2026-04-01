import json

# Validate Exp1A
try:
    with open('SDS_Exp1A_Data_Structures.ipynb', 'r') as f:
        data_a = json.load(f)
    print(f"✓ Exp1A: Valid JSON - {len(data_a['cells'])} cells")
    code_cells_a = sum(1 for c in data_a['cells'] if c['cell_type'] == 'code')
    print(f"  Code cells: {code_cells_a}, Markdown cells: {len(data_a['cells']) - code_cells_a}")
except Exception as e:
    print(f"✗ Exp1A: Error - {e}")

# Validate Exp1B
try:
    with open('SDS_Exp1B_Central_Tendency_Dispersion.ipynb', 'r') as f:
        data_b = json.load(f)
    print(f"\n✓ Exp1B: Valid JSON - {len(data_b['cells'])} cells")
    code_cells_b = sum(1 for c in data_b['cells'] if c['cell_type'] == 'code')
    print(f"  Code cells: {code_cells_b}, Markdown cells: {len(data_b['cells']) - code_cells_b}")
except Exception as e:
    print(f"✗ Exp1B: Error - {e}")

# Check for syntax errors
import ast
import sys

print("\n" + "="*50)
print("SYNTAX VALIDATION")
print("="*50)

for cell in data_a['cells']:
    if cell['cell_type'] == 'code':
        code = ''.join(cell['source'])
        try:
            ast.parse(code)
        except SyntaxError as e:
            print(f"Exp1A - Syntax Error: {e}")
            print(f"  Code: {code[:50]}...")

for cell in data_b['cells']:
    if cell['cell_type'] == 'code':
        code = ''.join(cell['source'])
        try:
            ast.parse(code)
        except SyntaxError as e:
            print(f"Exp1B - Syntax Error: {e}")
            print(f"  Code: {code[:50]}...")

print("\nValidation complete!")
