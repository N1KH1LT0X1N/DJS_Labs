# LAB 8 COMPLETION SUMMARY

**Date:** April 11, 2026

## Experiment: Chi-square Test Using Python

### Status: ✅ COMPLETED

---

## Overview
Lab 8 provides a comprehensive study of chi-square statistical tests, covering both test of independence and test of goodness of fit.

### Key Sections Completed

#### 1. **Test of Independence of Attributes** (Questions 1-5)
Tests whether two categorical variables are related using chi-square statistics.

- **Q1: Titanic Gender vs Survival**
  - χ² = 388.997, p-value ≈ 0.000
  - **Conclusion:** Gender and Survival are DEPENDENT (Related)

- **Q2: Titanic Class vs Survival**
  - χ² = 131.105, p-value ≈ 0.000
  - **Conclusion:** Class and Survival are DEPENDENT (Related)

- **Q3: Gender vs Pet Choice**
  - χ² = 3.161, p-value = 0.367
  - **Conclusion:** Gender and Pet Choice are INDEPENDENT (Not Related)

- **Q4: Drug Treatment Effectiveness**
  - χ² = 13.336, p-value ≈ 0.0003
  - **Conclusion:** Treatment and Cure Status are DEPENDENT (Related)

- **Q5: Age Group vs Political Affiliation**
  - χ² = 22.550, p-value ≈ 0.0010
  - **Conclusion:** Age Group and Political Affiliation are DEPENDENT (Related)

#### 2. **Test of Goodness of Fit** (Questions 6-8)
Tests whether observed data follows an expected distribution.

- **Q6: Student Party Affiliation Distribution**
  - χ² = 1.694, p-value = 0.429
  - **Conclusion:** Sample data follows the given distribution

- **Q7: Bulb Life Distribution (Normality Test)**
  - Shapiro-Wilk Statistic = 0.989, p-value = 0.964
  - **Conclusion:** Bulb life follows a normal distribution

- **Q8: Unbiased Dice Test**
  - χ² = 1.067, p-value = 0.957
  - **Conclusion:** The dice is UNBIASED (statistically fair)

---

## Libraries Used
- `numpy`: Numerical computations
- `pandas`: Data manipulation and contingency tables
- `scipy.stats`: Chi-square tests and statistical functions
- `math`: Mathematical operations

---

## Key Learning Outcomes

### ✓ Test of Independence
- Understand null hypothesis and alternative hypothesis
- Calculate chi-square statistics using contingency tables
- Interpret p-values and make statistical decisions
- Apply to real-world datasets (Titanic, drug effectiveness, etc.)

### ✓ Test of Goodness of Fit
- Compare observed frequencies with expected distributions
- Use Shapiro-Wilk test for normality assessment
- Validate data against theoretical distributions
- Apply to various scenarios (voting patterns, manufacturing, dice fairness)

---

## Statistical Concepts Reinforced

1. **Chi-square Test Formula:** χ² = Σ((O - E)² / E)
2. **P-value Interpretation:** If p < α, reject null hypothesis
3. **Degrees of Freedom:** (rows - 1) × (columns - 1)
4. **Significance Levels:** Standard α = 0.05 (5%)

---

## Applications Covered

✓ Market Research & Demographics  
✓ Quality Control & Manufacturing  
✓ Medical Research & Drug Testing  
✓ Social Science Studies  
✓ Data Validation for Machine Learning  

---

## Conclusion

Chi-square tests are invaluable statistical tools for categorical data analysis. Lab 8 successfully demonstrates:

1. How to identify relationships between categorical variables
2. How to verify if data matches expected distributions
3. How to make evidence-based statistical decisions
4. How to implement these tests using Python

**The lab comprehensively covers the theory and practical implementation of chi-square statistics with Python.**

---

**All cells executed successfully. Lab 8 is complete and ready for review.**
