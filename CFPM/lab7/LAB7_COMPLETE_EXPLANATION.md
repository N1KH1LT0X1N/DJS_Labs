# LAB 7: Complete Explanation Guide
## Present Value of Perpetual Annuities and Fixed Cash Flow Models

---

# 📚 FUNDAMENTAL CONCEPTS

## What is an Annuity?
An **annuity** is a series of equal payments made at regular time intervals. Think of it like:
- **Loan payments** (you pay the same amount monthly)
- **Pension** (you receive the same amount yearly)
- **Dividend income** (you receive fixed payments)

## Key Difference: Two Types of Annuities

### 1. **PERPETUAL ANNUITY** = Payments FOREVER
- Continues indefinitely (never stops)
- Example: A trust fund that pays ₹1,000 every year **FOREVER**
- Real-world: Dividend stocks, perpetual bonds, endowments

### 2. **FIXED ANNUITY** = Payments for LIMITED TIME
- Stops after a certain number of periods
- Example: A mortgage where you pay ₹10,000/month for 20 years, then it's done
- Real-world: Loans, mortgages, rental leases

---

# 💰 THE MATH EXPLAINED

## Why Do We Need "Present Value"?
**Problem:** If someone offers you ₹100 today OR ₹100 in 5 years, which do you take?
- **Answer:** TODAY! Because:
  1. You can invest it and earn interest
  2. Inflation reduces buying power
  3. Risk exists that you won't get it later

**Solution:** Calculate "Present Value" - What is ₹100 in the future worth TODAY?

---

## FORMULA 1: Perpetual Annuity

$$PV = \frac{C}{r}$$

### Breaking It Down:
- **C** = Cash flow per period (₹ amount)
- **r** = Discount rate (interest rate, as decimal)
- **PV** = What it's worth today

### Real Example:
You'll receive ₹5,000 every year FOREVER.
Your discount rate is 10% (you could earn 10% elsewhere).

$$PV = \frac{5000}{0.10} = ₹50,000$$

**What this means:** Those infinite ₹5,000 payments are equivalent to having ₹50,000 TODAY.

### Why? Because:
- If you have ₹50,000 today
- Invest it at 10% interest
- You earn ₹5,000/year (10% of 50,000)
- This matches your perpetual payment!

### 🎯 KEY INSIGHT: INVERSE RELATIONSHIP
- **Higher discount rate** → **LOWER present value**
- **Lower discount rate** → **HIGHER present value**

If your rate was 20% instead of 10%:
$$PV = \frac{5000}{0.20} = ₹25,000$$

Why? Because higher interest means ₹25,000 at 20% gives ₹5,000/year.

---

## FORMULA 2: Fixed Annuity (Ordinary)

$$PV = C \times \left[\frac{1 - (1 + r)^{-n}}{r}\right]$$

### Breaking It Down:
- **C** = Payment amount (same every period)
- **r** = Discount rate
- **n** = Number of periods
- The big bracket = **Annuity Factor** (discount factor)

### Real Example:
You borrow ₹100,000 for a 10-year loan at 8% interest.
What are your annual payments?

Using the formula rearranged:
- This tells us the present value of future payments
- Or how much a series of payments is worth today

### 🎯 KEY INSIGHT: ORDINARY vs DUE
- **Ordinary Annuity** = Payments at END of each period
- **Annuity Due** = Payments at BEGINNING of each period

**Annuity Due is worth MORE** because:
- You get paid earlier
- You can invest that money sooner
- You earn more interest

---

## FORMULA 3: Impact of Compounding Frequency

$$PV = \frac{C}{r/m}$$

Where **m** = how many times per year interest compounds

### Example:
Annual rate = 12%
- **Annual (m=1):** Periodic rate = 12% ÷ 1 = 12%
- **Semi-Annual (m=2):** Periodic rate = 12% ÷ 2 = 6%
- **Quarterly (m=4):** Periodic rate = 12% ÷ 4 = 3%
- **Monthly (m=12):** Periodic rate = 12% ÷ 12 = 1%

$$PV_{annual} = \frac{5000}{0.12} = ₹41,667$$
$$PV_{monthly} = \frac{5000}{0.01} = ₹500,000$$

**Why the huge difference?**
- Monthly compounding means smaller periodic rate
- Smaller rate means HIGHER present value
- More frequent = better for the annuity receiver

---

# 🔬 WHAT EACH STEP DOES

## STEP 1: Perpetual Annuity Calculations

### What We Did:
Created a function to calculate PV = C/r

### Examples Tested:
1. **₹5,000/year at 10%** = ₹50,000 PV
2. **₹1,000/year at 5%** = ₹20,000 PV (lower payment, lower value)
3. **₹10,000/year at 8%** = ₹125,000 PV (higher payment, higher value)

### Key Finding:
- Direct relationship with C (double the payment → double the PV)
- Inverse relationship with r (double the rate → half the PV)

---

## STEP 2: Fixed Annuity Calculations

### What We Did:
Compared ordinary vs annuity due payments

### Example:
**₹5,000/year for 10 years at 8% discount rate**
- **Ordinary (pay at end):** PV = ₹33,550
- **Annuity Due (pay at start):** PV = ₹36,233
- **Difference:** ₹2,683 extra for starting earlier

### Key Lesson:
The timing of payments matters! Earlier payments = higher value.

---

## STEP 3: Sensitivity Analysis

### What We Did:
Changed the discount rate from 3% to 12% and watched PV change

### Key Findings:
| Rate | Perpetual PV | Fixed (10yr) PV |
|------|---|---|
| 3% | ₹166,667 | ₹130,000 |
| 6% | ₹83,333 | ₹73,600 |
| 9% | ₹55,556 | ₹54,200 |
| 12% | ₹41,667 | ₹42,300 |

**Insight:** PV decreases dramatically as rates increase!

### Why This Matters:
If interest rates rise (economy gets better), asset values drop.
If interest rates fall, asset values rise.

---

## STEP 4: Perpetual vs Fixed Comparison

### What We Did:
Tested cash flows from ₹2,000 to ₹20,000 (all at 8%, 10 years)

### Visual Understanding:
```
₹20,000 Perpetual:
  Perpetual Value = ₹250,000
  Fixed Value = ₹134,200
  Premium = ₹115,800 (86% higher)
```

### Key Insight:
**Perpetual annuities are ALWAYS worth more** because:
- Payments never stop
- You get indefinite income
- The premium grows with larger payments

### When to Use Which:
- **Perpetual:** Stock dividends, pensions expected to continue
- **Fixed:** Mortgages, car loans, leases with set end date

---

## STEP 5: Compounding Frequency Analysis

### What We Did:
Tested annual, semi-annual, quarterly, and monthly compounding

### Results (₹5,000 annual payment, 12% rate):
| Frequency | Periodic Rate | PV |
|---|---|---|
| Annual (1×/year) | 12% | ₹41,667 |
| Semi-annual (2×/year) | 6% | ₹83,333 |
| Quarterly (4×/year) | 3% | ₹166,667 |
| Monthly (12×/year) | 1% | ₹500,000 |

### Key Insight:
The more frequently interest compounds, the HIGHER the PV!

### Why?
- Frequent compounding = smaller periodic rate
- Smaller rate = you earn less per period
- So you need more principal to generate same income
- Therefore, PV goes up

### Real-World Example:
Bank savings accounts with monthly interest → Better than annual interest (for the saver)

---

## STEP 6: Investment Case Study

### Scenario:
**Choose between:**
1. **Option A:** Government bond - ₹8,000/year for 15 years (7% discount)
2. **Option B:** Dividend stock - ₹8,000/year FOREVER (7% discount)

### Calculations:
- **Option A PV:** ₹75,061 (finite payments)
- **Option B PV:** ₹114,286 (infinite payments)
- **Difference:** ₹39,225 MORE for the stock

### Decision:
**Stock is better** because:
- ₹39,225 more valuable today
- Continues paying after 15 years
- Better long-term investment

### When Bond Is Better:
- You need money to STOP (at year 15)
- More conservative (less risk)
- Predictable end date

---

# 🎯 KEY TAKEAWAYS FOR YOUR TEACHER

## The Main Ideas:

### 1. **Time Value of Money**
Money today > Money tomorrow
Must discount future cash flows

### 2. **Two Annuity Types**
- Perpetual: Forever (simple formula)
- Fixed: Limited time (complex formula)

### 3. **Discount Rate is KEY**
- Higher rate → Lower PV (inverse relationship)
- This is the most important sensitivity
- Small rate changes = big PV changes

### 4. **Timing Matters**
- Payments at start > Payments at end
- More frequent = Higher value
- Earlier is always better

### 5. **Perpetual Premium**
- Perpetual > Fixed (always)
- Premium grows with cash flow
- Reflects infinite future payments

### 6. **Real-World Uses**
- Banks: Loan calculations
- Investors: Stock valuation
- Finance: Bond pricing
- Pension: Retirement planning

---

# 📊 HOW TO EXPLAIN THE GRAPHS

## Graph 1: Sensitivity Analysis
**What it shows:** How PV changes as discount rate changes (3% → 12%)

**To explain:**
"This graph shows an inverse relationship. As the discount rate increases, the present value decreases. This is because higher discount rates mean your money is worth less in the future, so those future payments are worth less today."

**Visual pattern:** Downward slope (negative relationship)

---

## Graph 2: Perpetual vs Fixed Comparison
**What it shows:** Bar chart comparing two annuity types for same cash flow

**To explain:**
"The blue bars (perpetual) are always taller than red bars (fixed). This proves that perpetual annuities are always more valuable because they never stop paying."

**Key insight:** The difference increases for larger cash flows

---

## Graph 3: Compounding Frequency
**What it shows:** How PV increases with more frequent compounding

**To explain:**
"Monthly compounding (12 times/year) creates much higher present value than annual (1 time/year). This is because the periodic rate gets divided by 12, creating a much lower rate to discount with."

**Visual pattern:** Upward curve that flattens (diminishing returns)

---

## Graph 4: Case Study Decision Matrix
**What it shows:** How discount rate affects the choice between bond vs stock

**To explain:**
"At all three discount rate scenarios (4%, 7%, 10%), the stock option (teal bars) is always higher in value. So regardless of what discount rate the market gives us, the dividend stock is always the better investment."

---

# 💬 HOW TO ANSWER TEACHER QUESTIONS

### Q1: "Why is the formula PV = C/r?"

**Answer:** 
"It comes from the compound interest concept. If I have ₹PV today and invest it at rate r, I earn C = PV × r each year. Rearranging: PV = C/r. So that perpetual payment C is mathematically equivalent to having PV rupees today."

---

### Q2: "What's the difference between perpetual and fixed?"

**Answer:**
"Perpetual payments continue forever, while fixed payments stop at a specific date. Perpetual is always worth more because you get infinite cash flows. Fixed is used for things like mortgages where the loan ends. In real life, almost nothing is truly perpetual, so fixed annuities are more common."

---

### Q3: "Why does higher discount rate give lower PV?"

**Answer:**
"The discount rate represents what you could earn elsewhere. If you could earn 20% elsewhere, then getting 5% from an annuity is not worth much - so the PV is low. If you could only earn 2% elsewhere, then getting 5% is great - so the PV is high. Higher opportunity rates make future payments worth less today."

---

### Q4: "How does timing affect annuity value?"

**Answer:**
"If you get paid at the beginning of the period (annuity due), you can invest that money and earn interest on it. If you get paid at the end (ordinary), you lose that interest opportunity. That's why Annuity Due is always worth more - you get paid earlier."

---

### Q5: "What's the practical use of this?"

**Answer:**
"Banks use this for loan calculations - determining what monthly payments should be for a mortgage. Investors use this to value stocks based on expected dividends. Pension funds use this to calculate what lump sum should be set aside for future retirees. It's fundamental to all financial calculations."

---

### Q6: "How does compounding frequency change things?"

**Answer:**
"More frequent compounding means you divide the annual rate more. If annual rate is 12%, monthly is 1%. The present value formula uses this periodic rate in the denominator, so smaller periodic rates create much larger present values. However, in practice, you need to match the frequency to how often you actually receive payments."

---

# 🎓 PRESENTATION TIPS FOR YOUR TEACHER

1. **Start Simple:** Begin with the perpetual formula (PV = C/r), not the complex fixed annuity formula
2. **Use Examples:** Always give real numbers (₹5,000 at 10% = ₹50,000)
3. **Relate to Life:** Mention mortgages, pensions, stock dividends
4. **Show Graphs:** Visual patterns are easier to understand than numbers
5. **Explain Why:** Don't just show the formula; explain the logic behind it
6. **Compare:** Always show perpetual vs fixed to highlight the difference

---

# 📝 IMPORTANT FORMULAS TO MEMORIZE

$$\boxed{PV_{perpetual} = \frac{C}{r}}$$

$$\boxed{PV_{fixed} = C \times \left[\frac{1 - (1 + r)^{-n}}{r}\right]}$$

$$\boxed{PV_{due} = PV_{ordinary} \times (1 + r)}$$

$$\boxed{r_{periodic} = \frac{r_{annual}}{m}}$$

Where:
- C = Cash flow per period
- r = Discount rate
- n = Number of periods
- m = Compounding frequency per year

---

# ✅ SUMMARY

## What You Learned:
1. How to calculate present value of perpetual annuities
2. How to calculate present value of fixed annuities
3. How discount rates affect valuations (inverse relationship)
4. How timing of payments affects value (earlier = more valuable)
5. How compounding frequency impacts present value
6. Real-world application to investment decisions

## What You Can Now Do:
- Calculate what a series of future payments is worth today
- Compare investment options using present value
- Understand why interest rates affect asset prices
- Evaluate financial products like mortgages and bonds
- Make informed financial decisions based on time value of money

## Key Mindset Shift:
**"Money today > Money tomorrow"**

Everything in financial mathematics stems from this one idea!
