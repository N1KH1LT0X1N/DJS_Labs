# LAB 7: CODE WALKTHROUGH
## Understanding What Each Step Does

---

# 🔧 STEP 1: PERPETUAL ANNUITY CALCULATIONS

## The Function
```python
def pv_perpetual_annuity(C, r):
    if r <= 0:
        return float('inf')
    return C / r
```

### What It Does:
- Takes in C (cash flow) and r (discount rate)
- Checks if rate is valid (must be positive)
- Returns the present value using PV = C/r

### Why the Check?
- If r = 0, you'd divide by zero → infinite value (technically correct!)
- If r < 0, doesn't make sense financially

### How to Use It:
```python
pv = pv_perpetual_annuity(5000, 0.10)  # Returns 50,000
```

---

## The Examples
```python
C1 = 5000      # ₹5,000 per year
r1 = 0.10      # 10% discount rate
pv1 = pv_perpetual_annuity(C1, r1)
print(f"PV = ₹{pv1:,.2f}")  # Output: ₹50,000.00
```

### What Each Line Does:
1. **C1 = 5000** → Set payment amount to 5,000
2. **r1 = 0.10** → Set discount rate to 10% (note: 10% = 0.10, not 10!)
3. **pv1 = ...** → Call function and store result
4. **print** → Display result with comma formatting

### The Three Example Scenarios:
```
Scenario 1: C=1000, r=5%   → PV = 1000/0.05 = 20,000
Scenario 2: C=10000, r=8%  → PV = 10000/0.08 = 125,000
Scenario 3: C=7500, r=12%  → PV = 7500/0.12 = 62,500
```

**Pattern:** Higher C or lower r → Higher PV

---

# 🔧 STEP 2: FIXED ANNUITY CALCULATIONS

## The Function
```python
def pv_fixed_annuity(C, r, n, annuity_due=False):
    if r == 0:
        return C * n
    pv = C * ((1 - (1 + r) ** (-n)) / r)
    if annuity_due:
        pv = pv * (1 + r)
    return pv
```

### Breaking Down the Formula:

**Part 1: The Bracket**
```python
(1 - (1 + r) ** (-n)) / r
```
- **(1 + r)** = Growth factor (1 plus the rate)
- **(1 + r) ** (-n)** = Decay factor (inverse growth over n periods)
- **1 - [decay]** = How much is "recovered"
- **Divide by r** = Normalize to discount rate

**Example with numbers (C=5000, r=0.08, n=10):**
- (1 + 0.08) = 1.08
- (1.08) ** (-10) = 0.4632
- 1 - 0.4632 = 0.5368
- 0.5368 / 0.08 = 6.71 (this is the annuity factor)
- 5000 × 6.71 = 33,550 (the present value!)

**Part 2: Annuity Due Adjustment**
```python
if annuity_due:
    pv = pv * (1 + r)
```
- Multiplies by (1 + r) to account for earlier payments
- Makes it worth ~8% more (for 8% rate)

### How to Use It:
```python
# Ordinary annuity (payments at end)
pv_ordinary = pv_fixed_annuity(5000, 0.08, 10, annuity_due=False)
# Result: 33,550

# Annuity due (payments at beginning)
pv_due = pv_fixed_annuity(5000, 0.08, 10, annuity_due=True)
# Result: 36,233 (8% higher)
```

---

## The Examples
```python
scenarios = [
    {"C": 5000, "r": 0.06, "n": 5, "description": "5 years, 6% rate"},
    {"C": 5000, "r": 0.06, "n": 10, "description": "10 years, 6% rate"},
    # ... more scenarios
]

for i, scenario in enumerate(scenarios, 1):
    pv_ord = pv_fixed_annuity(scenario["C"], scenario["r"], 
                              scenario["n"], annuity_due=False)
    pv_d = pv_fixed_annuity(scenario["C"], scenario["r"], 
                            scenario["n"], annuity_due=True)
```

### What enumerate() Does:
- Loops through list with index (i starts at 1)
- Accesses C, r, n from scenario dictionary
- Calculates both ordinary and annuity due

### Results Summary:
```
Scenario 1: 5 years  at 6% → Ordinary: 21,062 | Due: 22,336
Scenario 2: 10 years at 6% → Ordinary: 36,807 | Due: 39,015
Scenario 3: 15 years at 6% → Ordinary: 48,932 | Due: 51,868
```

**Pattern:** More years → Higher value (more payments)

---

# 🔧 STEP 3: SENSITIVITY ANALYSIS (DISCOUNT RATE)

## The Loop
```python
rates = np.arange(0.03, 0.13, 0.01)  # 3% to 12%, step 0.01
pv_perpetual_list = [pv_perpetual_annuity(5000, r) for r in rates]
pv_fixed_list = [pv_fixed_annuity(5000, r, 10) for r in rates]
```

### What It Does:
- **np.arange(0.03, 0.13, 0.01)** = Creates rates: 0.03, 0.04, 0.05, ..., 0.12
- **List comprehension** = Calculates PV for each rate
- **Result:** Two lists of PV values

### Example Output:
```
Rate 3%  → Perpetual: 166,667  | Fixed: 130,000
Rate 6%  → Perpetual: 83,333   | Fixed: 73,600
Rate 9%  → Perpetual: 55,556   | Fixed: 54,200
Rate 12% → Perpetual: 41,667   | Fixed: 42,300
```

**Key Finding:** As rate doubles (3% → 6%), PV is cut in half!

## The Visualization
```python
ax1.plot(rates * 100, pv_perpetual_list, 'b-o', label='Perpetual')
ax1.plot(rates * 100, pv_fixed_list, 'r-s', label='Fixed')
```

### What This Draws:
- **rates * 100** = Converts 0.10 to 10 (for x-axis percentage)
- **'b-o'** = Blue color, solid line, circle markers
- **'r-s'** = Red color, solid line, square markers
- **label** = Legend text

---

# 🔧 STEP 4: PERPETUAL VS FIXED COMPARISON

## The Loop
```python
cash_flows = [2000, 5000, 10000, 15000, 20000]
for cf in cash_flows:
    pv_perp = pv_perpetual_annuity(cf, 0.08)
    pv_fixed = pv_fixed_annuity(cf, 0.08, 10)
    difference = pv_perp - pv_fixed
    pct_diff = (difference / pv_fixed) * 100
```

### What It Does:
- Tests different cash flow amounts (same 8% rate, 10 years)
- Calculates perpetual and fixed PV for each
- Computes absolute difference
- Computes percentage difference (how much higher)

### Example Calculation:
```
For C = 5000:
  pv_perp = 5000 / 0.08 = 62,500
  pv_fixed = 5000 × 6.71 = 33,550
  difference = 62,500 - 33,550 = 28,950
  pct_diff = (28,950 / 33,550) × 100 = 86.3%
  
"Perpetual is 86.3% more valuable than 10-year fixed"
```

## The Visualization
```python
bars1 = ax1.bar(x_pos - width/2, pv_perp_vals, width, label='Perpetual')
bars2 = ax1.bar(x_pos + width/2, pv_fixed_vals, width, label='Fixed')
```

### What This Draws:
- **x_pos - width/2** = First bar (left side)
- **x_pos + width/2** = Second bar (right side)
- **width = 0.35** = Bar width (with gap between)
- Creates side-by-side comparison

---

# 🔧 STEP 5: COMPOUNDING FREQUENCY ANALYSIS

## The Function
```python
def pv_perpetual_with_frequency(C, annual_rate, m):
    periodic_rate = annual_rate / m
    return C / periodic_rate
```

### What It Does:
- Takes annual rate and divides by m (frequency)
- Uses adjusted rate in PV = C / r formula

### Example Calculation:
```
Annual rate = 12%, C = 5000

Annual (m=1):
  periodic_rate = 0.12 / 1 = 0.12 (12%)
  PV = 5000 / 0.12 = 41,667

Quarterly (m=4):
  periodic_rate = 0.12 / 4 = 0.03 (3%)
  PV = 5000 / 0.03 = 166,667

Monthly (m=12):
  periodic_rate = 0.12 / 12 = 0.01 (1%)
  PV = 5000 / 0.01 = 500,000
```

**Key:** Lower periodic rate → Higher PV!

## The Loop
```python
frequencies = {
    'Annual': 1,
    'Semi-Annual': 2,
    'Quarterly': 4,
    'Monthly': 12
}

for freq_name, m in frequencies.items():
    pv = pv_perpetual_with_frequency(5000, 0.12, m)
```

### What It Does:
- Iterates through frequency dictionary
- freq_name = 'Annual', 'Semi-Annual', etc.
- m = 1, 2, 4, 12
- Calculates PV for each frequency

## The Visualization (4 Subplots)
```python
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
```

### Creates:
- **ax1** (top-left): Bar chart of PVs
- **ax2** (top-right): Percentage increase
- **ax3** (bottom-left): Periodic rates
- **ax4** (bottom-right): Trend line

---

# 🔧 STEP 6: CASE STUDY - INVESTMENT DECISION

## The Scenario
```python
C_case = 8000    # ₹8,000 payment
r_case = 0.07    # 7% discount rate
n_case = 15      # 15 years

pv_option_a = pv_fixed_annuity(8000, 0.07, 15)    # ₹75,061
pv_option_b = pv_perpetual_annuity(8000, 0.07)    # ₹114,286
```

### The Calculations:

**Option A (Fixed):**
```
C = 8000, r = 0.07, n = 15
Factor = (1 - 1.07^-15) / 0.07 = 9.38
PV = 8000 × 9.38 = 75,061

This means: ₹75,061 today = ₹8,000/year for 15 years
```

**Option B (Perpetual):**
```
C = 8000, r = 0.07
PV = 8000 / 0.07 = 114,286

This means: ₹114,286 today = ₹8,000/year forever
```

**Difference:**
```
114,286 - 75,061 = 39,225
39,225 / 75,061 × 100 = 52.2% more!
```

## Sensitivity Analysis Loop
```python
for r_sens in np.arange(0.04, 0.11, 0.01):
    pv_a_sens = pv_fixed_annuity(8000, r_sens, 15)
    pv_b_sens = pv_perpetual_annuity(8000, r_sens)
    diff_sens = pv_b_sens - pv_a_sens
```

### What It Does:
- Tests different rates (4%, 5%, 6%, ..., 10%)
- For each rate, calculates both option values
- Shows that Option B is always better

### Results:
```
Rate 4%  → Option A: 94,685   | Option B: 200,000  | Difference: 105,315
Rate 7%  → Option A: 75,061   | Option B: 114,286  | Difference: 39,225
Rate 10% → Option A: 60,071   | Option B: 80,000   | Difference: 19,929
```

**Key:** Even as rates change, Stock (perpetual) stays better!

## The Visualization (4 Subplots)
```python
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
```

### Subplot 1: Simple Comparison
- Compares ₹75,061 (bond) vs ₹114,286 (stock) at 7%
- Shows the ₹39,225 difference with annotation arrow

### Subplot 2: Sensitivity Curve
- Shows both options' values across different rates (4% to 10%)
- Lines cross? No - perpetual always on top

### Subplot 3: Cumulative Payment
- Shows ₹8,000 × years for the bond
- Shows perpetual value as horizontal line
- After year 15 (bond ends), perpetual keeps paying

### Subplot 4: Decision Matrix
- Compares both at 3 different scenarios (4%, 7%, 10%)
- Bar chart showing perpetual always taller

---

# 🔧 STEP 7: CONCLUSIONS

## The Output
```python
print("=" * 80)
print(" " * 15 + "COMPREHENSIVE CONCLUSIONS FROM LAB 7 ANALYSIS")
print("=" * 80)
```

### What It Does:
- Prints decorative lines (80 characters)
- Prints centered title
- Repeats for each section

## The Content Structure
```
1. PERPETUAL ANNUITIES
   ✓ Key Findings (3-4 bullets)
   ✓ Practical Applications (3-4 examples)
   ✓ Sensitivity Insights (why rates matter)

2. FIXED ANNUITIES
   ✓ Key Findings (formulas and concepts)
   ✓ Practical Applications (real-world uses)
   ✓ Comparison with Perpetual

3. DISCOUNT RATE SENSITIVITY
   ✓ Key Findings (inverse relationship)
   ✓ Rate Ranges (low/medium/high effects)
   ✓ Practical Implications

... (continues for 10 major points)
```

### Why This Format?
- Easy to remember
- Clear bullets with explanations
- Real-world connections
- Covers all major concepts

---

# 📚 PROGRAMMING CONCEPTS YOU'RE LEARNING

## 1. Functions
```python
def pv_perpetual_annuity(C, r):
    # Reusable code block
    return C / r
```
- Define once, use many times
- Takes inputs (parameters)
- Returns output

## 2. Lists and Loops
```python
rates = [0.03, 0.04, 0.05, ..., 0.12]
pv_list = [pv_perpetual_annuity(5000, r) for r in rates]
```
- Iterates through multiple values
- Creates new list of results
- Much faster than manual calculation

## 3. Data Structures (Dictionaries)
```python
scenario = {"C": 5000, "r": 0.08, "n": 10}
pv = pv_fixed_annuity(scenario["C"], scenario["r"], scenario["n"])
```
- Stores related data together
- Accessed by key name, not index
- Cleaner, more readable code

## 4. DataFrames
```python
df = pd.DataFrame({
    'Cash Flow': [2000, 5000, 10000],
    'PV Perpetual': [25000, 62500, 125000],
    'PV Fixed': [13412, 33550, 67100]
})
print(df)
```
- Spreadsheet-like data structure
- Easy to display as tables
- Can perform calculations on columns

## 5. Plotting
```python
plt.plot(rates, pv_values, 'b-o')
plt.xlabel('Discount Rate')
plt.ylabel('Present Value')
plt.show()
```
- Visualizes data with graphs
- 'b-o' = blue color, lines, circles
- Multiple subplots tell complete story

---

# 💻 CODE BEST PRACTICES DEMONSTRATED

1. **Readable variable names**
   - `pv_perpetual` (clear what it is)
   - Not: `pp` (too vague)

2. **Comments and docstrings**
   ```python
   def pv_perpetual_annuity(C, r):
       """
       Calculate Present Value of Perpetual Annuity
       Parameters: C (cash), r (rate)
       Returns: float (present value)
       """
   ```

3. **Meaningful output formatting**
   ```python
   print(f"₹{pv:,.2f}")  # Adds comma, 2 decimals, currency symbol
   # Not: print(pv)     # Just raw number
   ```

4. **Validation checks**
   ```python
   if r <= 0:
       return float('inf')
   ```
   - Prevents errors or nonsensical results

5. **Modular code**
   - Small functions that do one thing
   - Reusable across different scenarios
   - Easier to test and debug

---

# 🎓 KEY PROGRAMMING PATTERNS

## Pattern 1: List Comprehension
```python
pv_list = [pv_perpetual_annuity(5000, r) for r in rates]
```
**Alternative (more verbose):**
```python
pv_list = []
for r in rates:
    pv = pv_perpetual_annuity(5000, r)
    pv_list.append(pv)
```
First way is more "Pythonic" (concise and elegant)

## Pattern 2: Dictionary Iteration
```python
for freq_name, m in frequencies.items():
    pv = pv_perpetual_with_frequency(5000, 0.12, m)
    print(f"{freq_name}: {pv}")
```
Gets both key (freq_name) and value (m) from dictionary

## Pattern 3: Conditional Assignment
```python
if annuity_due:
    pv = pv * (1 + r)
```
Modifies calculation based on condition

## Pattern 4: Multi-dimensional Arrays
```python
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
# Creates 2×2 grid of subplots
# Access with ax1, ax2, ax3, ax4
```

---

# 🐛 COMMON MISTAKES & HOW TO AVOID

## Mistake 1: Forgetting to Convert Percentage
```python
# ❌ WRONG
r = 10  # Treating 10% as 10
pv = 5000 / 10  # = 500 (way too low!)

# ✅ CORRECT
r = 0.10  # 10% = 0.10
pv = 5000 / 0.10  # = 50,000 (correct!)
```

## Mistake 2: Using Wrong Formula
```python
# ❌ WRONG for fixed annuity
pv = 5000 / 0.08  # This is perpetual formula!

# ✅ CORRECT for fixed annuity
pv = 5000 * ((1 - 1.08**(-10)) / 0.08)
```

## Mistake 3: Not Validating Inputs
```python
# ❌ Might crash with bad data
pv = C / r  # If r=0, division by zero error!

# ✅ Check first
if r <= 0:
    return float('inf')
return C / r
```

## Mistake 4: Forgetting DataFrame Operations
```python
# ❌ Trying to access like list
df['PV'][0]  # Might not work as expected

# ✅ Use proper indexing
df.iloc[0]['PV']  # Get first row, PV column
# Or
df['PV'].iloc[0]  # Get PV column, first row
```

---

**Now you understand the code! 🎉**

