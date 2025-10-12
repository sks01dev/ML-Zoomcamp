# Machine Learning Zoomcamp 2025 - Homework 3

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-1.5.3-orange?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3.1-green?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/stable/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-yellow?logo=jupyter&logoColor=white)](https://jupyter.org/)

---

## Homework 3: Machine Learning for Classification

This repository contains solutions for **Homework 3** of **Machine Learning Zoomcamp 2025**, focused on **classification tasks** using the Bank Marketing dataset.

---

## 📂 Project Overview

- **Dataset:** [Bank Marketing Dataset](https://raw.githubusercontent.com/alexeygrigorev/datasets/master/course_lead_scoring.csv)  
- **Target variable:** `converted` (whether the client signed up)  
- **Objective:** Data preprocessing, exploratory analysis, feature selection, and training logistic regression models (regularized and unregularized).  

**Tech Stack:**  
- **Python 3.11** – core programming language  
- **Pandas** – data manipulation  
- **NumPy** – numerical operations  
- **Scikit-Learn** – machine learning models, feature selection, evaluation  
- **Jupyter Notebook** – interactive coding and documentation  

---

## 🔹 Questions & Answers

| Question | Task | Answer |
|----------|------|--------|
| 1 | Mode of `industry` | `retail` |
| 2 | Biggest correlation (numerical features) | `annual_income` and `interaction_count` |
| 3 | Biggest mutual information (categorical features) | `lead_source` |
| 4 | Logistic regression validation accuracy | 0.74 |
| 5 | Least useful feature (feature elimination) | `lead_score` |
| 6 | Best `C` value for regularized logistic regression | 1 |

---

## 📌 Approach / Key Steps

1. **Data Cleaning & Preparation**  
   - Filled missing values: categorical → `'NA'`, numerical → `0.0`  
   - Verified feature types and correlations  

2. **Exploratory Analysis**  
   - Mode of categorical variables  
   - Correlation matrix for numerical features  

3. **Feature Selection**  
   - Calculated mutual information for categorical variables using `mutual_info_score`  
   - Identified least useful features via feature elimination  

4. **Model Training**  
   - Logistic Regression with one-hot encoded categorical variables  
   - Regularized logistic regression with hyperparameter tuning (`C` values)  

---

## 📈 Results

- Baseline logistic regression accuracy: **0.74**  
- Least useful feature: **`lead_score`**  
- Best regularization parameter `C`: **1**  

---

## ⚙ How to Run

1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/ml-zoomcamp-hw3.git
   ```

2. Install requirements:  
   ```bash
   pip install -r requirements.txt
   ```

3. Open the Jupyter Notebook and run cells sequentially:  
   ```bash
   jupyter notebook
   ```

---

## 📚 References

- [Bank Marketing Dataset](https://raw.githubusercontent.com/alexeygrigorev/datasets/master/course_lead_scoring.csv)  
- [Scikit-Learn Documentation](https://scikit-learn.org/stable/)  
- [Pandas Documentation](https://pandas.pydata.org/)  
- [NumPy Documentation](https://numpy.org/)  
- [Jupyter Notebook Documentation](https://jupyter.org/)

---

