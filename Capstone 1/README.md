

# Employee Attrition Prediction – ML Zoomcamp Capstone

## Problem Description

Employee attrition is a major cost driver for organizations.
The goal of this project is to **predict the probability that an employee will leave the company**, based on HR-related attributes.

This is a **binary classification** problem built using a **classical machine learning approach**, deployed as a **production-ready REST API**.

---

## Dataset

* **Source**: IBM HR Analytics Employee Attrition Dataset (Kaggle)
* **Rows**: Employees
* **Target variable**: `Attrition`

  * `Yes` → employee left
  * `No` → employee stayed
* **Features**:

  * Demographics (Age, Education, etc.)
  * Job attributes (JobRole, JobLevel, Department)
  * Work conditions (OverTime, WorkLifeBalance, DistanceFromHome)
* Dataset is **tabular, clean, and non-anonymized**, suitable for real API usage.

---

## Exploratory Data Analysis (EDA)

Only essential EDA was performed:

* Dataset shape and schema inspection
* Target class distribution (moderate class imbalance)
* Missing value check (none critical)
* Quick model comparison using ROC-AUC

**Conclusion from EDA**:

* Problem is well-suited for classical ML
* Non-linear models outperform linear baselines
* ROC-AUC is the appropriate evaluation metric

EDA is available in `notebooks/eda.ipynb`.

---

## Modeling Approach

### Feature Engineering

* Categorical features encoded using `pandas.get_dummies`
* Numerical features used as-is
* Feature alignment ensured between training and inference

### Models Evaluated

* Logistic Regression (baseline)
* Random Forest
* XGBoost (final selected model)

### Evaluation Metric

* **ROC-AUC**, due to class imbalance and probabilistic output requirement

### Model Selection

* Models trained on train split
* Evaluated on validation split
* Best model automatically selected based on ROC-AUC

The final trained model is saved as:

* `model.bin`
* `feature_columns.bin`

---

## Project Structure

```
capstone1-2/
│
├── data/
│   └── data.csv
│
├── notebooks/
│   └── eda.ipynb
│
├── train.py
├── predict.py
├── test.py
│
├── model.bin
├── feature_columns.bin
│
├── Dockerfile
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## Training the Model

```bash
python train.py
```

This will:

* Load the dataset
* Train multiple models
* Select the best one
* Save model artifacts for inference

---

## API Service

The model is served using **FastAPI**.

### Endpoints

#### Health Check

```
GET /ping
```

Response:

```json
{"status": "ok"}
```

#### Prediction

```
POST /predict
```

Example request:

```json
{
  "Age": 35,
  "BusinessTravel": "Travel_Rarely",
  "DailyRate": 800,
  "Department": "Research & Development",
  "DistanceFromHome": 10,
  "Education": 3,
  "EducationField": "Life Sciences",
  "EnvironmentSatisfaction": 3,
  "JobInvolvement": 3,
  "JobLevel": 2,
  "JobRole": "Research Scientist",
  "JobSatisfaction": 3,
  "MonthlyIncome": 6000,
  "NumCompaniesWorked": 1,
  "OverTime": "No",
  "WorkLifeBalance": 3,
  "YearsAtCompany": 5
}
```

Response:

```json
{
  "attrition_probability": 0.27,
  "attrition": false
}
```

---

## Running the API Locally

```bash
uvicorn predict:app --reload
```

Test:

```bash
python test.py
```

---

## Dockerization

The project is fully containerized.

### Build Docker Image

```bash
docker build -t employee-attrition .
```

### Run Container

```bash
docker run -p 8000:8000 employee-attrition
```

---

## Cloud Deployment (Render)

Deployment is done using **Docker on Render**.

### Steps

1. Push project to GitHub
2. Create a new **Web Service** on Render
3. Select:

   * Environment: **Docker**
   * Root Directory: project folder (if in subdirectory)
   * Port: `8000`
4. Deploy

Render automatically builds and runs the Docker container.

---

## Reproducibility

* Python version locked via `.python-version`
* Dependencies managed using `pyproject.toml`
* Docker ensures consistent runtime environment
* Model artifacts committed for deterministic inference

---

## Technologies Used

* Python 3.11
* pandas, scikit-learn
* XGBoost
* FastAPI
* Docker
* Render

---

## Notes

* This project intentionally avoids over-engineering
* No deep learning or unnecessary MLOps tooling
* Focused on correctness, clarity, and production readiness
* Fully aligned with **ML Zoomcamp capstone evaluation criteria**

---

## Author

Capstone project for **ML Zoomcamp**
Built following real-world machine learning engineering practices.

---

If you want, next I can:

* Review this README against the **official Zoomcamp rubric**
* Shorten it for submission version
* Help you write a **2-minute oral explanation** for viva/interview
