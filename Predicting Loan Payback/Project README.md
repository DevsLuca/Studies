# Loan Repayment Prediction — Kaggle Playground 2025
Supervised Machine Learning Project
<p align="left"> <!-- Language --> <img src="https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white" /> <!-- Libraries --> <img src="https://img.shields.io/badge/Scikit--Learn-Modeling%20%26%20Evaluation-F7931E?logo=scikit-learn&logoColor=white" /> <img src="https://img.shields.io/badge/XGBoost-Boosted%20Trees-EB5E28?logo=xgboost&logoColor=white" /> <!-- Kaggle --> <img src="https://img.shields.io/badge/Kaggle-Playground%20Series%202025-blueviolet?logo=kaggle&logoColor=white" /> <!-- Status --> <img src="https://img.shields.io/badge/Status-Completed-success" /> </p>

Predicting whether a borrower will repay their loan using Python, Machine Learning, and advanced feature engineering. This project demonstrates a full end-to-end workflow, from exploratory data analysis (EDA) to model selection and evaluation.

---

## Project Overview

The goal of this project is to **predict the probability that a borrower will pay back their loan**. Accurate predictions can help financial institutions manage risk, improve lending decisions, and reduce defaults.

**Key objectives:**

- Explore and clean the dataset
- Engineer meaningful features and ratios
- Encode categorical variables appropriately
- Compare Logistic Regression and XGBoost models
- Evaluate performance using accuracy, F1-score, ROC-AUC, and confusion matrices

---

## Dataset

The dataset comes from **Kaggle Playground Series - Season 5, Episode 11**. It contains both numerical and categorical features related to borrowers and loans:

- `loan_amount`, `interest_rate`, `annual_income`, `credit_score`, `debt_to_income_ratio`, etc.
- Categorical: `gender`, `marital_status`, `education_level`, `employment_status`, `loan_purpose`, `grade_subgrade`

> **Note:** The dataset is not included due to Kaggle competition rules. Instructions to download the dataset are provided in the notebook.

---

## Features & Engineering

- **Ratios & interactions:** `loan_to_income`, `loan_dti_interaction`, `loan_interest_interaction`, `credit_income_interaction`
- **Log-transformations** for skewed numeric features (`annual_income`, `debt_to_income_ratio`)
- **Ordinal encoding** for `grade_subgrade`
- **Rare category handling** and **one-hot encoding** for nominal features

---

## Modeling Approach

Two models were trained and evaluated:

1. **Logistic Regression** – baseline model, interpretable.
2. **XGBoost** – gradient boosting, high performance on tabular data.

**Hyperparameter tuning** and cross-validation were applied to optimize XGBoost performance.

---

## Evaluation Metrics

| Model               | Accuracy | F1 Score | ROC-AUC |
|--------------------|---------|----------|---------|
| Logistic Regression | 0.900   | 0.939    | 0.910   |
| XGBoost (tuned)    | 0.903   | 0.942    | 0.916   |

> Confusion matrices and classification reports are included in the notebook for detailed analysis of false positives/negatives.

---

## How to Run

1. Clone the repository:  
```bash
git clone https://github.com/yourusername/loan-payback-prediction.git
