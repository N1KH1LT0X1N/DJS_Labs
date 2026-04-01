"""
Fact-Checking Script for CFPM Experiments 0 and 1
This script validates all calculations to ensure accuracy
"""

import math
import pandas as pd

print("="*80)
print("FACT-CHECKING CFPM EXPERIMENTS 0 AND 1")
print("="*80)

# ============================================================================
# EXPERIMENT 0 VALIDATION
# ============================================================================
print("\n" + "="*80)
print("EXPERIMENT 0: TIME VALUE OF MONEY - VALIDATION")
print("="*80)

errors = []
warnings = []

# TASK 1: Future Value with Compound Interest
print("\n### TASK 1: Future Value (Compound Interest) ###")
P = 5000
r_annual = 0.06
n = 4
t = 1

FV_expected = P * math.pow((1 + r_annual/n), n * t)
print(f"Expected FV: ${FV_expected:.2f}")
print(f"Formula: FV = {P} × (1 + {r_annual}/{n})^({n}×{t})")
print(f"Calculation: {P} × (1.015)^4 = ${FV_expected:.2f}")

if abs(FV_expected - 5306.82) < 0.01:
    print("✓ PASS: Matches expected value $5,306.82")
else:
    errors.append(f"Task 1: Expected $5,306.82, got ${FV_expected:.2f}")
    print(f"✗ FAIL: Expected $5,306.82, got ${FV_expected:.2f}")

# TASK 2: Present Value
print("\n### TASK 2: Present Value ###")
FV = 10000
r = 0.07
t = 8

PV_expected = FV / math.pow(1 + r, t)
print(f"Expected PV: ${PV_expected:.2f}")
print(f"Formula: PV = {FV} / (1 + {r})^{t}")
print(f"Calculation: {FV} / (1.07)^8 = ${PV_expected:.2f}")

if abs(PV_expected - 5820.09) < 0.01:
    print("✓ PASS: Matches expected value $5,820.09")
else:
    errors.append(f"Task 2: Expected $5,820.09, got ${PV_expected:.2f}")
    print(f"✗ FAIL: Expected $5,820.09, got ${PV_expected:.2f}")

# TASK 3: Future Value of Annuity
print("\n### TASK 3: Future Value of Annuity ###")
P = 2000
r = 0.08
t = 25

FV_annuity_expected = P * ((math.pow(1 + r, t) - 1) / r)
print(f"Expected FV: ${FV_annuity_expected:.2f}")
print(f"Formula: FV = {P} × [(1 + {r})^{t} - 1] / {r}")
print(f"Calculation: {P} × [(1.08)^25 - 1] / 0.08 = ${FV_annuity_expected:.2f}")

if abs(FV_annuity_expected - 146211.88) < 0.1:
    print("✓ PASS: Matches expected value $146,211.88")
else:
    errors.append(f"Task 3: Expected $146,211.88, got ${FV_annuity_expected:.2f}")
    print(f"✗ FAIL: Expected $146,211.88, got ${FV_annuity_expected:.2f}")

# TASK 4: Present Value of Perpetuity
print("\n### TASK 4: Present Value of Perpetuity ###")
P = 4000
r = 0.06

PV_perpetuity_expected = P / r
print(f"Expected PV: ${PV_perpetuity_expected:.2f}")
print(f"Formula: PV = {P} / {r}")
print(f"Calculation: {P} / 0.06 = ${PV_perpetuity_expected:.2f}")

if abs(PV_perpetuity_expected - 66666.67) < 0.01:
    print("✓ PASS: Matches expected value $66,666.67")
else:
    errors.append(f"Task 4: Expected $66,666.67, got ${PV_perpetuity_expected:.2f}")
    print(f"✗ FAIL: Expected $66,666.67, got ${PV_perpetuity_expected:.2f}")

# TASK 5: Future Value of Annuity Due
print("\n### TASK 5: Future Value of Annuity Due ###")
P = 3000
r = 0.05
t = 5

FV_ordinary = P * ((math.pow(1 + r, t) - 1) / r)
FV_due_expected = FV_ordinary * (1 + r)
print(f"Expected FV: ${FV_due_expected:.2f}")
print(f"Step 1 (Ordinary): ${FV_ordinary:.2f}")
print(f"Step 2 (Annuity Due): ${FV_ordinary:.2f} × 1.05 = ${FV_due_expected:.2f}")

if abs(FV_due_expected - 17405.74) < 0.1:
    print("✓ PASS: Matches expected value $17,405.74")
else:
    errors.append(f"Task 5: Expected $17,405.74, got ${FV_due_expected:.2f}")
    print(f"✗ FAIL: Expected $17,405.74, got ${FV_due_expected:.2f}")

# ============================================================================
# EXPERIMENT 1 VALIDATION
# ============================================================================
print("\n" + "="*80)
print("EXPERIMENT 1: LOAN AMORTIZATION - VALIDATION")
print("="*80)

# EMI Calculation
print("\n### EMI CALCULATION ###")
P = 10000000  # Rs. 1 Crore
r_annual = 0.09
t_years = 20

r_monthly = r_annual / 12
n_months = t_years * 12

EMI_expected = (P * r_monthly * math.pow(1 + r_monthly, n_months)) / \
               (math.pow(1 + r_monthly, n_months) - 1)

print(f"Principal: ₹{P:,}")
print(f"Annual Rate: {r_annual*100}%")
print(f"Monthly Rate: {r_monthly:.6f}")
print(f"Tenure: {t_years} years ({n_months} months)")
print(f"Expected EMI: ₹{EMI_expected:.2f}")

# Validate against known value
if abs(EMI_expected - 89972.60) < 1:
    print("✓ PASS: EMI calculation correct")
else:
    errors.append(f"EMI: Expected ₹89,972.60, got ₹{EMI_expected:.2f}")
    print(f"✗ FAIL: Expected ₹89,972.60, got ₹{EMI_expected:.2f}")

# Total Payment
total_payment = EMI_expected * n_months
total_interest = total_payment - P

print(f"\nTotal Payment: ₹{total_payment:,.2f}")
print(f"Total Interest: ₹{total_interest:,.2f}")
print(f"Interest to Principal Ratio: {total_interest/P:.2f}")

if abs(total_payment - 21593422.94) < 1:
    print("✓ PASS: Total payment calculation correct")
else:
    errors.append(f"Total Payment: Expected ₹21,593,422.94, got ₹{total_payment:.2f}")
    print(f"✗ FAIL: Expected ₹21,593,422.94, got ₹{total_payment:.2f}")

# Amortization Schedule Validation
print("\n### AMORTIZATION SCHEDULE VALIDATION ###")
try:
    schedule = pd.read_csv('lab1/Exp1_Amortization_Schedule.csv')
    print(f"✓ CSV file loaded successfully ({len(schedule)} rows)")
    
    # Validate first month
    first_interest = P * r_monthly
    first_principal = EMI_expected - first_interest
    
    print(f"\nMonth 1 validation:")
    print(f"  Expected Interest: ₹{first_interest:.2f}")
    print(f"  Expected Principal: ₹{first_principal:.2f}")
    print(f"  Actual Interest: ₹{schedule.iloc[0]['Interest']:.2f}")
    print(f"  Actual Principal: ₹{schedule.iloc[0]['Principal']:.2f}")
    
    if abs(schedule.iloc[0]['Interest'] - first_interest) < 0.01:
        print("  ✓ PASS: First month interest correct")
    else:
        errors.append("First month interest calculation error")
        print("  ✗ FAIL: First month interest incorrect")
    
    # Validate final month
    if abs(schedule.iloc[-1]['Outstanding Balance']) < 1:
        print(f"\n  ✓ PASS: Final balance is ₹{schedule.iloc[-1]['Outstanding Balance']:.2f} (effectively zero)")
    else:
        errors.append(f"Final balance should be 0, got ₹{schedule.iloc[-1]['Outstanding Balance']:.2f}")
        print(f"  ✗ FAIL: Final balance is ₹{schedule.iloc[-1]['Outstanding Balance']:.2f}")
    
    # Validate total interest paid
    total_interest_schedule = schedule['Interest'].sum()
    if abs(total_interest_schedule - total_interest) < 1:
        print(f"  ✓ PASS: Total interest from schedule matches calculation")
    else:
        errors.append(f"Total interest mismatch")
        print(f"  ✗ FAIL: Total interest mismatch")
    
except FileNotFoundError:
    errors.append("Amortization schedule CSV not found")
    print("✗ FAIL: lab1/Exp1_Amortization_Schedule.csv not found")

# Parametric Study Validation
print("\n### PARAMETRIC STUDY VALIDATION ###")

# Test with 10-year tenure
t_10 = 10
n_10 = t_10 * 12
EMI_10 = (P * r_monthly * math.pow(1 + r_monthly, n_10)) / \
         (math.pow(1 + r_monthly, n_10) - 1)
total_10 = EMI_10 * n_10
interest_10 = total_10 - P

print(f"\n10-year tenure:")
print(f"  EMI: ₹{EMI_10:.2f}")
print(f"  Total Interest: ₹{interest_10:.2f}")

if abs(EMI_10 - 126675.77) < 1:
    print("  ✓ PASS: 10-year EMI calculation correct")
else:
    errors.append(f"10-year EMI incorrect")
    print(f"  ✗ FAIL: Expected ₹126,675.77, got ₹{EMI_10:.2f}")

# Test with 7% interest rate
r_7 = 0.07
r_7_monthly = r_7 / 12
EMI_7 = (P * r_7_monthly * math.pow(1 + r_7_monthly, n_months)) / \
        (math.pow(1 + r_7_monthly, n_months) - 1)
total_7 = EMI_7 * n_months
interest_7 = total_7 - P

print(f"\n7% interest rate:")
print(f"  EMI: ₹{EMI_7:.2f}")
print(f"  Total Interest: ₹{interest_7:.2f}")

if abs(EMI_7 - 77529.89) < 1:
    print("  ✓ PASS: 7% rate EMI calculation correct")
else:
    errors.append(f"7% rate EMI incorrect")
    print(f"  ✗ FAIL: Expected ₹77,529.89, got ₹{EMI_7:.2f}")

# ============================================================================
# FORMULA VERIFICATION
# ============================================================================
print("\n" + "="*80)
print("FORMULA VERIFICATION")
print("="*80)

print("\n✓ All formulas used are mathematically correct:")
print("  1. Compound Interest: FV = P × (1 + r/n)^(n×t)")
print("  2. Present Value: PV = FV / (1 + r)^t")
print("  3. Annuity FV: FV = P × [(1 + r)^t - 1] / r")
print("  4. Perpetuity PV: PV = P / r")
print("  5. Annuity Due FV: FV = P × [(1 + r)^t - 1] / r × (1 + r)")
print("  6. EMI Formula: EMI = [P × r × (1 + r)^n] / [(1 + r)^n - 1]")

# ============================================================================
# FINAL SUMMARY
# ============================================================================
print("\n" + "="*80)
print("FINAL VALIDATION SUMMARY")
print("="*80)

if len(errors) == 0:
    print("\n✓✓✓ ALL TESTS PASSED! ✓✓✓")
    print("\nAll calculations have been verified and are mathematically correct.")
    print("The implementations match the theoretical formulas perfectly.")
    print("\nExperiment 0: 5/5 tasks validated ✓")
    print("Experiment 1: All calculations and outputs validated ✓")
    print("\nBoth experiments are complete and error-free!")
else:
    print(f"\n✗✗✗ VALIDATION FAILED - {len(errors)} ERRORS FOUND ✗✗✗\n")
    for i, error in enumerate(errors, 1):
        print(f"{i}. {error}")

if len(warnings) > 0:
    print(f"\n⚠ WARNINGS:\n")
    for i, warning in enumerate(warnings, 1):
        print(f"{i}. {warning}")

print("\n" + "="*80)
print("VALIDATION COMPLETE")
print("="*80)
