# Lead Scoring with Bank Marketing Dataset

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.3.2-orange?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter&logoColor=white)](https://jupyter.org/)

---

## Overview

This notebook demonstrates building a **lead scoring model** using the Bank Marketing dataset. The goal is to predict whether a client will **convert** (sign up for a service) based on various features.

We cover:

1. Data preparation and handling missing values.
2. Feature importance using ROC AUC for numerical variables.
3. Logistic regression modeling with **one-hot encoding**.
4. Precision, recall, and F1 score analysis to select thresholds.
5. 5-fold cross-validation to check model stability.
6. Hyperparameter tuning to select the best regularization parameter.

---

## Key Results

- **Best numerical feature (ROC AUC):** `number_of_courses_viewed`  
- **Validation AUC:** `0.794`  
- **Threshold where precision ≈ recall:** `0.59`  
- **Threshold with max F1:** `0.47`  
- **Standard deviation of AUC across folds:** `0.01`  
- **Best regularization parameter C:** `0.001`  

---

## Lessons Learned

- ROC AUC can help identify predictive features even before modeling.
- Logistic regression combined with one-hot encoding provides a strong baseline.
- Threshold tuning is crucial for balancing precision and recall based on business needs.
- Cross-validation confirms the robustness of the model and prevents overfitting.
- Hyperparameter tuning improves model performance and reliability.

---

## Environment

- Python 3.12  
- Jupyter Notebook  
- Libraries: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`

---

## Dataset

Bank Marketing dataset used in this project is publicly available:  
[Bank Marketing Dataset CSV](https://raw.githubusercontent.com/alexeygrigorev/datasets/master/course_lead_scoring.csv)

---

## Author

Created as part of **ML Zoomcamp 2025 Homework 4**.

