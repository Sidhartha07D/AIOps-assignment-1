# AIOps Assignment 1
**Course:** DA3408 | **Student:** Sidhartha Durgam (Roll: DA24B003)

---

## 📋 Overview

This assignment explores MLOps fundamentals through technical debt diagnosis and experiment tracking using MLflow.

---

## 📂 Repository Structure

```
AIops-assignment-1/
├── question1/                    # Technical Debt Diagnosis
│   └── README.md                # Detailed analysis
├── question2/                    # MLflow Experiment Tracking
│   ├── README.md                # Experiment methodology
│   ├── train_mnist_mlp.py      # Training script
│   └── mflow_comparison_table.png
├── question3_updated/            # Advanced MLflow & DVC
│   └── [Related files]
├── data/                         # Dataset (Q3 related)
├── screenshots/                  # Visual documentation
├── Report/                       # FINAL REPORT (required)
│   └── AI_Ops_Assignment_1_Report.pdf
└── README.md                     # This file
```

---

##  How to Read This Assignment

### **Question 1: Technical Debt Diagnosis**
📖 **Read:** `question1/README.md`  
📄 **Full Report:** `Report/AI_Ops_Assignment_1_Report.pdf` (Section: Question 1)  
🖼️ **Screenshots:** `screenshots/question1-*` files

**Summary:** Identified 3 sources of hidden technical debt in ML systems (Entanglement, Undeclared Consumers, Configuration Debt) and proposed MLflow as mitigation.

---

### **Question 2: Applied MLflow Experiment Comparison**
📖 **Read:** `question2/README.md`  
📄 **Full Report:** `Report/AI_Ops_Assignment_1_Report.pdf` (Section: Question 2)  
🖼️ **Screenshots:** `screenshots/question2-*` files  
📊 **Comparison Table:** `question2/mflow_comparison_table.png`

**Summary:** Conducted 6 MLflow-tracked experiments comparing MLP architectures and learning rates on MNIST. Best run achieved 95.2% validation accuracy with learning rate being the dominant hyperparameter.

---

### **Question 3: Advanced MLflow & DVC**
🖼️ **Screenshots:** `screenshots/question3-*` files  
📄 **Full Report:** `Report/AI_Ops_Assignment_1_Report.pdf` (Section: Question 3)  
⚠️ **Note:** Related data files are in `data/` and `question3_updated/` folders 

---

### **Question 4: CI/CD Pipeline Implementation**
🔗 **External Repository:** https://github.com/eshikanahata/DA3408_Assignment1_Question4  
📄 **Full Report:** `Report/AI_Ops_Assignment_1_Report.pdf` (Section: Question 4)

---

## 🖼️ Screenshots Guide

All visual documentation is in the `screenshots/` folder organized as:
- `2-*` — Experiment results and comparisons
- `3-*` — DVC versioning and advanced features
- `4-*` — CI/CD pipeline implementation 

---

## 📄 Final Submission Report

**→ See:** `Report/AI_Ops_Assignment_1_Report.pdf`

This document contains:
- All 4 questions answered
- Key findings and analysis
- code snippets
- Experiment results

---

##  Quick Start (For Running Question 2 Experiments)

```bash
# Install dependencies
pip install mlflow scikit-learn pandas matplotlib numpy

# Run experiments
cd question2
python train_mnist_mlp.py

# View results
mlflow ui
# Open http://localhost:5000
```

---

## 🤖 AI Disclosure

This README and documentation were created with assistance from Claude AI to improve clarity and organization. The following were generated or enhanced by AI:
- README.md structure and formatting
- Documentation organization
- Technical explanations and summaries
- Also gemini was used for assistance for solving small issues while running commands

**However, all original work is done by me**
- Questions 1, 2, 3: Original analysis, experiments, and implementation by Sidhartha Durgam
- Question 4: implementation from https://github.com/eshikanahata/DA3408_Assignment1_Question4
- All experiment results, code, and findings are authentic

---

## 📚 Where to Find Everything

| What | Where |
|------|-------|
| **Q1 Analysis** | `question1/README.md` + Report |
| **Q2 Code & Results** | `question2/` + Screenshots |
| **Q3 Implementation** | `question3_updated/` + Screenshots |
| **Q4 Reference** | External GitHub repo (link above) |
| **All Answers** | `Report/AI_Ops_Assignment_1_Report.pdf` |
| **Visualizations** | `screenshots/` folder |

---

*For complete details, please refer to the individual README files and the final report.*
