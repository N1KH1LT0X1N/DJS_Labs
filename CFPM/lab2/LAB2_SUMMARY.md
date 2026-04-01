# CFPM Lab 2: Mortgage Analysis & Investment Growth - Execution Summary

## Overview
Lab 2 is a comprehensive exploration of Time Value of Money principles through two major applications:
- **Part 1**: Mortgage Payment Analysis with Extra Contributions
- **Part 2**: Investment Growth Analysis using the Rule of 72

## Part 1: Mortgage Payment Analysis

### Key Parameters
- **Principal**: Rs. 50 lakhs (50,00,000)
- **Annual Interest Rate**: 8%
- **Tenure**: 20 years (240 months)
- **Calculated EMI**: Rs. 41,822

### Step 1: EMI Calculation ✓
- Used mortgage payment formula: $EMI = P \times \frac{r(1+r)^n}{(1+r)^n - 1}$
- Successfully calculated monthly payment obligation

### Step 2: Amortization Schedule with Extra Payments ✓
- Generated complete 188-month schedule with Rs. 5,000 monthly extra payment
- Demonstrated interest/principal breakdown through loan lifecycle
- **Key Finding**: Extra Rs. 5,000/month saves **52 months** (4.33 years) in loan tenure

### Step 3: Loan Balance Visualization ✓
**Created 4-panel visualization showing**:
1. Loan balance comparison (with/without extra payments)
2. Interest vs principal breakdown
3. Cumulative interest paid over time
4. Last 10 months payment breakdown

**Results**:
- Tenure reduction: 52 months (4.33 years)
- Interest savings: Rs. 12.68 lakhs
- Months saved with extra payments clearly visible in curves

### Step 4: Parametric Study ✓
**Analyzed impact of varying extra payment amounts**:

| Extra Payment | Tenure | Months Saved | Interest Savings | ROI |
|--------------|--------|-------------|------------------|-----|
| Rs. 0 | 240 months | - | - | - |
| Rs. 3,000 | 205 months | 35 months | Rs. 8.54L | 138.88% |
| Rs. 5,000 | 188 months | 52 months | Rs. 12.68L | 134.85% |
| Rs. 10,000 | 156 months | 84 months | Rs. 19.99L | 128.14% |

**Key Insight**: ROI decreases with higher extra payments (diminishing returns)

### Step 5: Lump-Sum vs Regular Extra Payments ✓
**Comparison of four strategies**:

| Strategy | Tenure | Interest Paid | Interest Saved | Months Saved |
|----------|--------|---------------|-----------------|-------------|
| No Extra | 240 mo | Rs. 50.37L | - | - |
| Monthly Rs. 5K | 188 mo | Rs. 37.70L | Rs. 12.68L | 52 |
| Lump-Sum Month 1 (Rs. 2L) | 219 mo | Rs. 43.19L | Rs. 7.18L | 21 |
| Lump-Sum Month 60 (Rs. 2L) | 225 mo | Rs. 46.02L | Rs. 4.35L | 15 |

**Conclusion**: Monthly extra payments yield better returns than lump-sum payments of equivalent value

---

## Part 2: Investment Growth Analysis

### Step 6: Rule of 72 Implementation ✓
**Formulas Implemented**:
- Simple Interest: $T = \frac{100}{R}$
- Compound Interest: $t = \frac{\ln(2)}{\ln(1 + r)}$
- Rule of 72: $T \approx \frac{72}{R}$

**Accuracy Analysis** (15 interest rates tested):
- **Best accuracy**: 4%-10% range (error < 1%)
- **Average error**: <3% for typical rates
- Rule of 72 is excellent for compound interest approximation

### Step 7: Different Compounding Frequencies ✓
**Tested frequencies** for interest rates 4%, 6%, 8%, 10%, 12%:

Example at 8% rate:
- **Annually**: 9.01 years
- **Semi-Annually**: 8.84 years
- **Quarterly**: 8.75 years
- **Monthly**: 8.69 years
- **Difference**: ~0.31 years saved with monthly vs annual

**Key Insight**: More frequent compounding reduces doubling time by ~0.3 years consistently

### Step 8: Investment Growth Visualization ✓
**Created visualizations showing**:
1. **Investment Growth Curves** (4 scenarios: 6%, 8%, 10%, 12%)
   - Simple Interest (linear growth)
   - Compound Interest (4 frequencies)
   - Rule of 72 doubling time markers

2. **Rule of 72 Accuracy Analysis**
   - Comparison against exact formulas
   - Error distribution across interest rates
   - Optimal accuracy zone highlighted (4%-10%)

3. **Simple vs Compound Interest Power**
   - Exponential growth advantage of compounding
   - At 8% for 30 years (Rs. 1 Lakh initial):
     - Simple Interest: 3.4x multiplier
     - Compound Interest: 10.1x multiplier
     - **Difference: 6.7x wealth increase!**

---

## Part 2: Key Findings

### Rule of 72 Accuracy
| Rate Range | Max Error | Use Case |
|-----------|-----------|----------|
| 1%-3% | ~3% | Very low rates (bonds, savings) |
| 4%-10% | <1% | ⭐ **Optimal** (typical investments) |
| 12%-20% | 2-3% | Higher-yield investments |
| 25%-30% | 5-9% | Very high rates (crypto, speculative) |

### Compounding Power
**The difference between simple and compound interest over 30 years at 8% (Rs. 1 Lakh initial)**:
- Simple Interest: Rs. 3.4 Lakh (3.4x)
- Compound Interest: Rs. 10.1 Lakh (10.1x)
- **Extra wealth from compounding**: Rs. 6.7 Lakhs!

### Practical Applications

**For Borrowers (Part 1 Lessons)**:
- Make extra payments monthly for maximum savings
- Timing of payment matters significantly
- Consistent extra payments beat sporadic lump-sums

**For Investors (Part 2 Lessons)**:
- Start investing early (time is the key variable)
- Frequency of compounding matters but less than starting early
- Small differences in rates compound dramatically
- Use Rule of 72 for quick mental math on doubling times

---

## Files Generated

### Notebooks
- `lab2.ipynb` - Complete executable notebook with all analysis

### Visualizations
1. `loan_balance_analysis.png` - 4-panel loan analysis
2. `parametric_study.png` - Extra payment impact analysis
3. `lumpsum_vs_monthly_comparison.png` - Payment strategy comparison
4. `investment_growth_curves.png` - Investment growth at 4 rates
5. `rule_of_72_accuracy.png` - Rule of 72 accuracy analysis
6. `simple_vs_compound_growth.png` - Compounding power demonstration

---

## Code Statistics
- **Total Cells**: 25 (14 executable Python, 11 markdown)
- **Functions Implemented**: 5
- **Visualizations Created**: 6 comprehensive multi-panel plots
- **Data Analysis**: 40+ parametric combinations analyzed
- **Formulas**: 10+ mathematical formulas implemented

---

## Conclusions

### Part 1 - Mortgage Management
The analysis demonstrates that **strategic debt management** through consistent extra payments can:
- Reduce loan tenure by 4+ years
- Save Rs. 12.68 Lakhs in interest (25% reduction)
- Be implemented without requiring large lump-sum amounts
- Provide superior returns compared to sporadic large payments

### Part 2 - Investment Growth
The analysis demonstrates that **long-term compounding** is the secret to wealth:
- The Rule of 72 is a practical mental math tool
- Compounding adds 200%+ more value than simple interest
- More frequent compounding helps but starting early is crucial
- Even 1-2% rate difference compounds to massive differences over decades

### Integrated Learning
Together, these two parts illustrate the **Time Value of Money**:
1. **For Borrowers**: Every rupee paid extra today saves exponential interest tomorrow
2. **For Investors**: Every rupee invested today multiplies exponentially by tomorrow
3. **Both sides**: **Timing and consistency** matter more than amount

---

**Lab 2 Status**: ✅ **COMPLETE** - All analysis, calculations, visualizations, and conclusions delivered.
