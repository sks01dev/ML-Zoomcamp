
# Customer Conversion Prediction API

[![Python](https://img.shields.io/badge/python-3.12%2F3.13-blue)](https://www.python.org/)

This project demonstrates **deploying a machine learning model with FastAPI and Docker**.  
The model predicts the probability of a lead converting to a customer based on simple features.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Requirements](#requirements)
- [Setup & Installation](#setup--installation)
- [Running Locally](#running-locally)
- [Docker Deployment](#docker-deployment)
- [Using the API](#using-the-api)
- [Project Structure](#project-structure)
- [License](#license)

---

## Project Overview

We use a pre-trained **Logistic Regression model** with a `DictVectorizer` to process input features:

- `lead_source` (categorical: `organic_search`, `social_media`, `paid_ads`, `referral`, `events`)
- `annual_income` (numeric)
- `number_of_courses_viewed` (numeric)

The model is served via **FastAPI**, and can be deployed using **Docker**.

---

## Requirements

- Python 3.12 or 3.13
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [uv](https://uv-lang.org/) (for dependency management)
- [Docker](https://www.docker.com/)

---

## Setup & Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd <repo-folder>
````

### 2. Install dependencies with `uv`

```bash
# Install uv globally if not already
pip install uv

# Initialize uv project
uv init

# Install dependencies from pyproject.toml
uv sync --frozen
```

### 3. Verify Python and library versions

```bash
python --version
uv --version
```

---

## Running Locally

1. Make sure the `model.bin` file is in the project directory.
2. Run the FastAPI server:

```bash
uvicorn predict:app --host 0.0.0.0 --port 9696
```

3. Open API docs in your browser:
   [http://localhost:9696/docs](http://localhost:9696/docs)

---

## Docker Deployment

### 1. Build Docker image

```bash
docker build -t customer-conversion-prediction .
```

### 2. Run container

```bash
docker run -d -p 9696:9696 customer-conversion-prediction
```

* Access the API at `http://localhost:9696/predict`.

### 3. Test API inside Python

```python
import requests

url = "http://localhost:9696/predict"
client = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}

response = requests.post(url, json=client)
print(response.json())
```

---

## Using the API

### Request format

```json
{
    "lead_source": "paid_ads",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0
}
```

### Response format

```json
{
    "convert_probability": 0.533,
    "converted": true
}
```

* `convert_probability`: probability of conversion
* `converted`: True if probability >= 0.5, else False

---

## Project Structure

```
.
├── Dockerfile
├── model.bin
├── pyproject.toml
├── uv.lock
├── predict.py
└── README.md
```

* `Dockerfile`: defines container image
* `predict.py`: FastAPI app and prediction code
* `model.bin`: pre-trained ML model
* `pyproject.toml` & `uv.lock`: dependency management
* `README.md`: project documentation

---

## License

This project is for educational purposes for **ML Zoomcamp 2025**.

---

## References

* [FastAPI Documentation](https://fastapi.tiangolo.com/)
* [Uvicorn Documentation](https://www.uvicorn.org/)
* [Docker Documentation](https://docs.docker.com/)
* [Scikit-Learn Pipeline](https://scikit-learn.org/stable/modules/compose.html)

```
