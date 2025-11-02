# 🚗 Fuel Efficiency Prediction using Decision Trees & Ensemble Models

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Modeling-orange)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-important)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📘 Overview

This project predicts **vehicle fuel efficiency (MPG)** using **Decision Trees** and **Ensemble Learning methods** like **Random Forests**.  
The notebook demonstrates the process of preparing data, training models, tuning hyperparameters, and evaluating model performance using regression metrics.

---

## 🧩 Steps Performed

### 1. Data Preprocessing
- Filled missing values with zeros.  
- Split the dataset into **train (60%)**, **validation (20%)**, and **test (20%)** sets.  
- Used `DictVectorizer(sparse=True)` to handle categorical columns and transform data into feature matrices.

### 2. Baseline Model – Decision Tree Regressor
- Trained an initial **Decision Tree Regressor** to predict `fuel_efficiency_mpg`.  
- Evaluated the effect of tree depth (`max_depth=1`, etc.) on model performance.  
- Interpreted how tree splits identify key predictors (e.g., `vehicle_weight`).

### 3. Random Forest Regressor
- Trained a **Random Forest** with parameters:
  ```python
  n_estimators=10
  random_state=1
  n_jobs=-1
````

* Calculated **RMSE** on the validation dataset (baseline result ≈ `0.46`).

### 4. Tuning `n_estimators`

* Tested `n_estimators` values from **10 to 200** (step of 10).
* Observed RMSE improvements until about **n_estimators ≈ 80**, after which performance stabilized.

### 5. Tuning `max_depth`

* Explored `max_depth` values: **[10, 15, 20, 25]**.
* For each depth, varied `n_estimators` and computed mean RMSE.
* Identified the **best combination** of parameters for optimal performance.

### 6. Evaluation & Insights

* Compared RMSE across different configurations.
* Visualized feature importance — most influential predictors included:

  * `vehicle_weight`
  * `horsepower`
  * `engine_displacement`
  * `acceleration`
  * `model_year`

---

## ⚙️ Technologies Used

| Category    | Tools                                           |
| ----------- | ----------------------------------------------- |
| Programming | Python 3.x                                      |
| Libraries   | `pandas`, `numpy`, `scikit-learn`, `matplotlib` |
| Environment | Jupyter / Google Colab                          |

---

## 📊 Key Results

| Model                    | RMSE (Validation) | Notes                            |
| ------------------------ | ----------------- | -------------------------------- |
| Decision Tree (depth=1)  | High              | Simple baseline                  |
| Random Forest (10 trees) | 0.46              | Improved performance             |
| Random Forest (80 trees) | ≈ Stable          | RMSE stopped improving           |
| Tuned Model              | Lowest RMSE       | Balanced accuracy and complexity |

---

## 🚀 How to Run

1. Open the notebook in **Google Colab** or Jupyter:
   [Fuel Efficiency Prediction Notebook](https://colab.research.google.com/drive/1nqa7rSsNev_pZoNhVedFUK_MkwrkKIhe?usp=sharing)
2. Run all cells sequentially to reproduce the results.
3. Review model outputs and visualizations.

---

## 🔮 Possible Improvements

* Add cross-validation and hyperparameter tuning (`GridSearchCV`)
* Extend to Gradient Boosting, LightGBM, or XGBoost
* Analyze model interpretability with SHAP values
* Deploy as a simple web API or dashboard

---

## 👤 Author

**Shivam Swarnkar**
[GitHub](https://github.com/sks01dev) | [Email](sswarnkar0001@gmail.com)


Would you like me to insert your actual name and GitHub link into this markdown before saving it as a ready-to-upload `README.md` file?
```
