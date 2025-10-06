# 🚗 Car Fuel Efficiency Predictor (ML Zoomcamp W2)

## ✍️ Description

This project develops a **Linear Regression model** to predict car fuel efficiency in Miles Per Gallon (`fuel_efficiency_mpg`) using a subset of car features. The primary focus is on mastering the fundamental machine learning workflow: handling missing data, proper train/validation/test splitting, and understanding model stability and regularization.

### Key Objectives:

* **Data Preprocessing:** Analyze missing values and compare imputation strategies (mean vs. zero).
* **Model Training:** Implement a Linear Regression model using `scikit-learn`.
* **Model Evaluation & Stability:** Use RMSE to evaluate model performance and assess the impact of different random seeds on model stability.
* **Regularization:** Test the effect of Ridge regularization (L2) to prevent overfitting.

---

## ⚙️ Installation

To run this notebook, you need a standard Python environment with the following dependencies.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/sks01dev/data-science-lab/](https://github.com/sks01dev/data-science-lab/)
    cd data-science-lab
    ```

2.  **Install dependencies:**
    ```bash
    pip install numpy pandas scikit-learn matplotlib seaborn
    ```

3.  **Download Data:** The dataset is fetched directly within the notebook from the official source:
    ```bash
    wget [https://raw.githubusercontent.com/alexeygrigorev/datasets/master/car_fuel_efficiency.csv](https://raw.githubusercontent.com/alexeygrigorev/datasets/master/car_fuel_efficiency.csv)
    ```

---

## 🏃 Usage

Execute the `week_2.ipynb` notebook cell-by-cell to follow the full machine learning workflow.

1.  **Data Selection:** Only the following columns are used: `'engine_displacement'`, `'horsepower'`, `'vehicle_weight'`, `'model_year'`, and `'fuel_efficiency_mpg'`.
2.  **Splitting:** The data is shuffled (seed 42) and split into Train (60%), Validation (20%), and Test (20%) sets.
3.  **Model Comparison:** Linear Regression models are trained to compare performance after filling missing `'horsepower'` values with 0 vs. the training set mean.
4.  **Final Evaluation:** The best configuration is tested on the final, unseen test set.

---

## 🛠️ Technologies Used

| Technology | Purpose | Badge/Icon |
| :--- | :--- | :--- |
| **Python** | Core programming and analysis language | [![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python&logoColor=white)](https://www.python.org/doc/) |
| **NumPy** | Numerical operations and RMSE calculation | [![NumPy](https://img.shields.io/badge/NumPy-1.x-blue?style=flat-square&logo=numpy&logoColor=white)](https://numpy.org/doc/) |
| **Pandas** | Data loading, manipulation, and missing value handling | [![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org/docs/) |
| **scikit-learn** | Linear Regression, Ridge, and `train_test_split` | [![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.x-orange?style=flat-square&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/stable/documentation.html) |
| **Seaborn/Matplotlib** | Data visualization and distribution checks | [![Seaborn](https://img.shields.io/badge/Seaborn-0.12-darkgreen?style=flat-square&logo=seaborn&logoColor=white)](https://seaborn.pydata.org/) |

---

## 📊 Dataset Used

* **Car Fuel Efficiency Dataset:** A collection of vehicle attributes (displacement, horsepower, weight, model year) used to predict fuel consumption (`fuel_efficiency_mpg`). [Image of Fuel Efficiency Distribution]
* **Source:** Alexey Grigorev's public datasets repository.

---

## 🧠 Key Learnings

1.  **Imputation Strategy:** The **mean imputation** of missing `'horsepower'` values (RMSE: 0.46) significantly outperformed filling with zero (RMSE: 0.51). Using the mean preserves the feature's distribution better than using an extreme outlier (0).
2.  **Model Stability:** By testing the split sensitivity across 10 random seeds, the model was determined to be **stable** ($\text{std} \approx 0.006$), confirming the reliability of the chosen split ratio.
3.  **Regularization Impact:** Ridge regularization (L2) had a negligible effect on the final RMSE scores, suggesting the Linear Regression model was not heavily overfitting the data.

---

## ✨ Results

| Question | Task | Result |
| :--- | :--- | :--- |
| **Q1** | Column with missing values | `horsepower` |
| **Q2** | Median Horsepower | 149.0 |
| **Q3** | Best Imputation (Validation RMSE) | **With mean** (0.46) |
| **Q4** | Best Regularization $\text{r}$ (alpha) | **0** (RMSE: 0.51) |
| **Q5** | Standard Deviation of RMSEs | **0.006** |
| **Q6** | Final Test RMSE ($\text{r}=0.001$, seed 9) | $\approx 0.520$ (Closest to 0.515) |

---

## 🚀 Future Work

* **Feature Engineering:** Engineer new features (e.g., age of car from `model_year`) to potentially improve the model's predictive power.
* **Categorical Features:** Incorporate the original categorical columns (`origin`, `fuel_type`, `drivetrain`) using one-hot encoding or other techniques.
* **Advanced Regression:** Test other models like Elastic Net or Random Forest for improved accuracy.

---

## 📚 References

* *Alexey Grigorev - ML Zoomcamp Week 2 Materials*
