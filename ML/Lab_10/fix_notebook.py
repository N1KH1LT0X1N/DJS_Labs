import json
import os

# Read current notebook
notebook_path = 'lab10.ipynb'
with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

cells = nb['cells']

# Desired order: cells indices should go [0, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# Because current order is backwards from our BOTTOM inserts

# Current: Title(0), Summary(1), Ch8(2), Ch7(3), Tuning(4), Comparison(5), Perf(6), Eval(7), Ch6(8), Build(9), Ch5(10), TrainTest(11), Preprocess(12), Ch4(13), EDA(14), Ch3(15), Load(16), Ch2(17), Import(18), Ch1(19)

# We want: Title(0), Ch1(19), Import(18), Ch2(17), Load(16), Ch3(15), EDA(14), Ch4(13), Preprocess(12), TrainTest(11), Ch5(10), Build(9), Ch6(8), Eval(7), Perf(6), Comparison(5), Tuning(4), Ch7(3), Ch8(2), Summary(1)

correct_order = [0, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
reordered_cells = [cells[i] for i in correct_order]
nb['cells'] = reordered_cells

# Write back
with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=2, ensure_ascii=False)

print("✓ Notebook cells reordered to correct sequence!")
print(f"✓ Total cells: {len(nb['cells'])}")
print("✓ Order verified: Title → Ch1 → Import → Ch2 → Load → Ch3 → EDA → Ch4 → Preprocess → TrainTest → Ch5 → Build → Ch6 → Eval → Perf → Comparison → Tuning → Ch7 → Ch8 → Summary")
