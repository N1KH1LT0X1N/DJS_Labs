# 🎓 DJS_Labs - Complete Computer Science Laboratory Portfolio

A comprehensive collection of laboratory exercises spanning five major computer science domains: **Corporate Finance & Project Management**, **Data Structures & Algorithms**, **Machine Learning**, **Spatial Data Science**, and **Web Development**. This repository demonstrates practical implementation of fundamental concepts through hands-on projects and experiments.

---

## 📊 Repository Overview

| Domain | Labs | Language | Focus Area |
|--------|------|----------|------------|
| **CFPM** | 0-7 | Python | Financial calculations, amortization, time value of money |
| **DSA** | 0-10 | C | Data structures, algorithms, searching, sorting |
| **ML** | 0-8 | Python | ML pipelines, regression, classification, deployment |
| **SDS** | 1-11 | Python | Spatial analysis, statistics, data visualization |
| **Web** | 0-8 | HTML/CSS/JS | Frontend development, responsive design, frameworks |

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone <repository-url>
cd DJS_Labs

# Python labs (CFPM, ML, SDS) - Setup virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac

# Install dependencies (create requirements.txt if needed)
pip install pandas numpy matplotlib seaborn scikit-learn jupyter

# C labs (DSA) - Compile with GCC
gcc lab0/D095_Nikhil-Pise_Lab0.c -o lab0/lab0.exe
./lab0/lab0.exe  # Linux/Mac
# lab0\lab0.exe  # Windows

# Web labs - Open directly in browser
# Simply double-click .html files or use: start lab1/1_static_page.html
```

---

## 📁 Detailed Lab Structure

### 💰 CFPM - Corporate Finance & Project Management

**Language:** Python | **Labs:** 8 (0-7)

**Core Concepts:**
- Time Value of Money calculations
- Loan amortization schedules
- Financial modeling and analysis
- Investment evaluation techniques

**Lab Breakdown:**
- **Lab 0:** Time Value of Money - Compound interest, present value, annuities, perpetuities
- **Lab 1:** Loan Amortization - EMI calculations, 20-year schedules, parametric studies
- **Lab 2-7:** Advanced financial analysis, project management, investment growth curves

**Key Outputs:**
- Amortization schedules (CSV exports)
- Financial visualizations (PNG charts)
- Parametric analysis reports
- Complete Python implementations with formula verification

**Documentation:** `CFPM/README.md`, `CFPM/COMPLETION_SUMMARY.txt`

---

### 🔧 DSA - Data Structures & Algorithms

**Language:** C | **Labs:** 11 (0-10)

**Core Concepts:**
- Searching algorithms (Linear, Binary)
- Sorting algorithms (Selection, Quick, Bubble)
- Linear data structures (Arrays, Linked Lists, Stacks, Queues)
- Non-linear structures (Binary Search Trees)
- Hashing and collision resolution

**Lab Breakdown:**
- **Lab 0:** Searching Algorithms - Linear search vs Binary search implementation
- **Lab 1:** Sorting Algorithms - Selection sort and Quick sort with performance comparison
- **Lab 2:** Singly Linked List - Insert, delete, search operations
- **Lab 3:** Infix to Postfix Conversion - Stack-based expression evaluation
- **Lab 4:** Linear Queue - FIFO operations and implementation
- **Lab 5:** Binary Search Tree - Insert, search, traversal operations
- **Lab 6:** Searching and Sorting - Combined algorithms with analysis
- **Lab 7:** Hashing - Hash functions, collision resolution (linear probing)
- **Lab 8:** Merging Sorted Linked Lists - Two-pointer technique
- **Lab 9:** Stack for Parenthesis Validation - Balanced bracket checking
- **Lab 10:** Circular Queue - Josephus problem implementation

**Key Features:**
- Complete C implementations with proper memory management
- Time complexity analysis for each algorithm
- Performance comparisons and benchmarks
- Comprehensive guide: `DSA/DSA_Labs_Complete_Guide.md`

---

### 🤖 ML - Machine Learning

**Language:** Python | **Labs:** 9 (0-8)

**Core Concepts:**
- Data preprocessing and cleaning
- Regression analysis
- Classification algorithms
- Model training and evaluation
- Deployment with Gradio

**Lab Breakdown:**
- **Lab 0:** Complete ML Pipeline - Cafe sales prediction system
  - Data cleaning (10,000 rows → 3,089 cleaned)
  - Feature engineering and selection
  - Model training (Gradient Boosting Regressor)
  - Gradio dashboard deployment
  - Comprehensive documentation (7 files, 75+ KB)

- **Lab 1:** Regression Analysis - Boston Housing dataset
- **Lab 2:** Multi-Dataset Analysis - California Housing, Iris, Wine datasets
- **Lab 3:** Classification & Clustering - Breast cancer, medical datasets
- **Lab 4-8:** Advanced ML concepts and specialized techniques

**Lab 0 Highlights:**
- Production-ready ML pipeline
- Data leakage detection and resolution
- Model comparison (Ridge vs Gradient Boosting)
- Interactive web dashboard with Gradio
- 50+ test cases for validation
- Complete documentation index: `ML/Lab_0/DOCUMENTATION_INDEX.md`

**Technologies:** scikit-learn, pandas, NumPy, matplotlib, seaborn, Gradio

---

### 🗺️ SDS - Spatial Data Science

**Language:** Python | **Labs:** 11 (1-11)

**Core Concepts:**
- Spatial data analysis
- Statistical methods
- Data visualization
- Sampling distributions
- Hypothesis testing

**Lab Breakdown:**
- **Lab 1:** Cross-check and validation exercises
- **Lab 2-9:** Spatial analysis techniques, statistical methods
- **Lab 10:** Linear Discriminant Analysis (LDA)
- **Lab 11:** Hypothesis testing for large samples (blood pressure analysis)

**Key Features:**
- Real-world datasets
- Statistical validation
- Visualization outputs
- Comprehensive documentation

---

### 🌐 Web - Web Development

**Languages:** HTML, CSS, JavaScript, Bootstrap | **Labs:** 9 (0-8)

**Core Concepts:**
- HTML5 fundamentals and semantic markup
- CSS3 styling and responsive design
- Bootstrap framework integration
- Form validation and local storage
- Modern web development practices

**Lab Breakdown:**
- **Lab 0:** Student Registration - Basic HTML form
- **Lab 1:** HTML Fundamentals
  - Static web page (college portal)
  - Class timetable with data tables
  - Registration form with validation
  - Semantic HTML5 news portal

- **Lab 2:** CSS & Bootstrap
  - External CSS stylesheet (450+ lines)
  - Responsive CSS3 with media queries (4 breakpoints)
  - Bootstrap component showcase
  - Bootstrap admission form (25+ fields)

- **Lab 3:** JavaScript Integration
  - Calculator implementation
  - Enhanced student registration form
  - Fetch API integration

- **Lab 4, 6-8:** Advanced web development projects

**Key Features:**
- 2,900+ lines of professional code
- 35+ web components
- 4 responsive breakpoints tested
- LocalStorage data persistence
- Font Awesome icons integration
- Complete documentation: `Web/README.md`, `Web/COMPLETION_SUMMARY.md`

**Documentation Files:**
- `QUICK_START.md` - Quick reference guide
- `IMPLEMENTATION_COMPLETE.md` - Detailed implementation report
- `CROSS_CHECK_FINAL.md` - Validation results
- `COMPLETION_CERTIFICATE.md` - Achievement summary

---

## 🛠️ Technologies & Tools

### Python Ecosystem
- **Data Science:** pandas, NumPy, scikit-learn
- **Visualization:** matplotlib, seaborn
- **Development:** Jupyter Notebooks, Python scripts
- **Deployment:** Gradio (ML Lab 0)

### C Programming
- **Compiler:** GCC
- **Environment:** Command line
- **Features:** Memory management, pointers, data structures

### Web Development
- **Core:** HTML5, CSS3, JavaScript
- **Frameworks:** Bootstrap 5
- **Icons:** Font Awesome
- **Tools:** Browser DevTools, LocalStorage API

---

## 📋 Prerequisites

### For Python Labs (CFPM, ML, SDS)
```bash
Python 3.8+
pip install pandas numpy matplotlib seaborn scikit-learn jupyter python-docx gradio
```

### For C Labs (DSA)
```bash
GCC Compiler (MinGW on Windows, Xcode on Mac, GCC on Linux)
```

### For Web Labs (Web)
```bash
Modern web browser (Chrome, Firefox, Edge, Safari)
No installation required - open .html files directly
```

### General
- Git for version control
- Text editor or IDE (VS Code recommended)
- Basic command line knowledge

---

## 📊 Project Statistics

| Metric | Count |
|--------|-------|
| **Total Labs** | 48+ |
| **Code Files** | 100+ |
| **Documentation Files** | 30+ |
| **Lines of Code** | 15,000+ |
| **Languages Used** | 5 (Python, C, HTML, CSS, JS) |
| **Datasets** | 10+ |
| **Models Trained** | 5+ |
| **Web Pages** | 15+ |

---

## 🎯 Learning Path

### Beginner Level
1. Start with **DSA Lab 0** (Searching algorithms in C)
2. Move to **Web Lab 1** (HTML fundamentals)
3. Explore **CFPM Lab 0** (Basic financial calculations)

### Intermediate Level
1. Complete **DSA Labs 2-5** (Data structures)
2. Work on **Web Lab 2** (CSS and responsive design)
3. Study **ML Lab 1** (Regression analysis)

### Advanced Level
1. Tackle **ML Lab 0** (Complete ML pipeline)
2. Implement **DSA Labs 7-10** (Advanced algorithms)
3. Build **Web Labs 3-8** (JavaScript and frameworks)
4. Explore **SDS Labs** (Spatial data science)

---

## 📖 Documentation Guide

### CFPM Documentation
- **Main:** `CFPM/README.md` - Complete lab documentation
- **Summary:** `CFPM/COMPLETION_SUMMARY.txt` - Project overview

### DSA Documentation
- **Guide:** `DSA/DSA_Labs_Complete_Guide.md` - 896-line comprehensive guide covering all labs
- **Manual:** `DSA/DS Lab Manual 25-26-New.docx` - Official lab manual

### ML Documentation
- **Index:** `ML/Lab_0/DOCUMENTATION_INDEX.md` - Navigation guide for 7 documentation files
- **Analysis:** `ML/Lab_0/FINAL_ANALYSIS.md` - Most comprehensive technical analysis
- **Quick Start:** `ML/Lab_0/QUICK_REFERENCE.md` - 30-second quick start guide

### Web Documentation
- **Main:** `Web/README.md` - Complete lab index with file descriptions
- **Summary:** `Web/COMPLETION_SUMMARY.md` - Achievement summary
- **Quick Start:** `Web/QUICK_START.md` - How to use the labs
- **Certificate:** `Web/COMPLETION_CERTIFICATE.md` - Validation results

---

## ✨ Key Achievements

### ML Lab 0 - Cafe Sales System
- ✅ Complete data cleaning pipeline (10,000 → 3,089 rows)
- ✅ Data leakage detection and resolution
- ✅ Model optimization (R² improved from -0.89 to 0.85)
- ✅ Production-ready Gradio dashboard
- ✅ 75+ KB of comprehensive documentation
- ✅ 50+ test cases validated

### Web Development Labs
- ✅ 8 complete web projects
- ✅ Responsive design (4 breakpoints)
- ✅ Bootstrap integration
- ✅ LocalStorage data persistence
- ✅ 2,900+ lines of professional code

### DSA Labs
- ✅ 11 complete algorithm implementations
- ✅ Time complexity analysis for all
- ✅ Memory management best practices
- ✅ 896-line comprehensive guide

### CFPM Labs
- ✅ 8 complete financial experiments
- ✅ Mathematical formula verification
- ✅ Professional visualizations
- ✅ Parametric analysis reports

---

## 🧪 Testing & Validation

### ML Lab 0 Testing
- 50+ test cases passed
- Data leakage validation
- Model performance benchmarks
- Deployment testing

### Web Labs Testing
- Multi-browser compatibility
- Responsive design validation
- Form functionality testing
- LocalStorage verification

### DSA Labs Testing
- Algorithm correctness validation
- Time complexity verification
- Memory leak checks
- Edge case testing

---

## 📝 License

This repository contains educational laboratory work completed as part of academic coursework. All code and documentation are provided for educational purposes. Please refer to individual lab directories for specific licensing information.

---

## 🤝 Contributing

This is an educational repository documenting laboratory coursework. For questions or suggestions about the implementations, please refer to the documentation files in each respective domain directory.

---

## 📞 Support & Resources

### Getting Help
1. Check domain-specific README files (CFPM, DSA, ML, SDS, Web)
2. Review comprehensive guides (DSA guide, ML documentation index)
3. Examine code comments and inline documentation
4. Refer to lab manuals and assignment documents

### Learning Resources
- **DSA:** `DSA/DSA_Labs_Complete_Guide.md` - Complete algorithm explanations
- **ML:** `ML/Lab_0/DOCUMENTATION_INDEX.md` - Navigate 7 documentation files
- **Web:** `Web/QUICK_START.md` - Quick reference for web labs

---

## 🎉 Summary

This repository represents a complete computer science education journey across five major domains:

- **8 CFPM labs** covering financial mathematics and analysis
- **11 DSA labs** implementing fundamental algorithms and data structures
- **9 ML labs** from basic regression to production deployment
- **11 SDS labs** in spatial data science and statistics
- **9 Web labs** from HTML basics to modern responsive design

All labs include complete implementations, comprehensive documentation, validation reports, and real-world applications. The repository demonstrates strong proficiency in multiple programming languages, frameworks, and computer science concepts.

---

**Repository Status:** ✅ Complete & Validated
**Last Updated:** April 2026
**Total Domains:** 5
**Total Labs:** 48+
**Documentation:** 30+ files
**Quality:** Production-ready code with comprehensive testing
