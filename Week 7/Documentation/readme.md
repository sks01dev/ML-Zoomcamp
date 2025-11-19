## 📱 Mobile Price Classification API

Machine Learning Zoomcamp – Midterm Project

This project implements a solution to classify mobile phone specifications into one of four price ranges using a trained **XGBoost Classifier**.

The model is deployed as a **FastAPI** service running inside a **Docker** container, following the recommended ML Zoomcamp deployment workflow.

-----

## 📌 Project Overview

| Component | Detail |
| :--- | :--- |
| **Goal** | Predict a mobile phone's price range (0, 1, 2, or 3) based on 20 hardware features. |
| **Model** | `XGBoostClassifier` (e.g., `mobile_price.bin` or `.json`) |
| **API** | FastAPI REST endpoint (`/predict`) |
| **Containerization** | Docker |
| **Deployment** | Render Web Service |
| **Input** | JSON with hardware specifications |
| **Output** | Human-readable price range prediction (e.g., "Low Cost", "Medium Cost", etc.) |

-----

## 📁 Project Structure

```
midterm_deployment_mobile/
│
├── app.py                  # FastAPI application for inference
├── Dockerfile              # Docker instructions to containerize the app
├── requirements.txt        # Python dependencies
├── mobile_price.json       # Trained XGBoost model (or similar classifier)
└── README.md               # Project documentation
```

-----

## 🔧 Installation (Local)

1.  **Clone repo**
    ```bash
    git clone https://github.com/<your-username>/mobile-price-api.git
    cd mobile-price-api
    ```
2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run API locally**
    ```bash
    uvicorn app:app --reload
    ```
    Open in browser:
    👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

-----

## 🧪 Example API Usage

**POST** `/predict`

**Sample Input:** (A selection of features is shown; the final model requires all 20 features.)

```json
{
  "battery_power": 1100,
  "blue": 0,
  "clock_speed": 2.2,
  "dual_sim": 1,
  "fc": 1,
  "four_g": 1,
  "int_mem": 32,
  "m_dep": 0.1,
  "mobile_wt": 120,
  "n_cores": 4,
  "pc": 5,
  "px_height": 700,
  "px_width": 1200,
  "ram": 2500,
  "sc_h": 15,
  "sc_w": 7,
  "talk_time": 10,
  "three_g": 1,
  "touch_screen": 1,
  "wifi": 1
}
```

**Sample Output:**

```json
{
  "prediction": "Price Range: 2 (High Cost)"
}
```

-----

## 🐳 Run with Docker (Local)

1.  **Build Docker image**
    ```bash
    docker build -t mobile-price-api .
    ```
2.  **Run container**
    ```bash
    docker run -p 8000:8000 mobile-price-api
    ```
    Visit:
    👉 **http://localhost:8000/docs**

-----

## 🌐 Deployment on Render (Docker)

1.  Create GitHub repo and push these files.
2.  Go to **Render** → “New Web Service.”
3.  Select the repo containing this `Dockerfile`.
4.  Render auto-detects it as a Docker service.
5.  Choose:
      * **Instance:** Free
      * **Region:** Singapore (closest to India)
6.  Click Deploy.

Your live API will appear at:

**https://\<your-render-app\>[.onrender.com/docs](https://www.google.com/search?q=https://.onrender.com/docs)**

-----

## 📊 Model Details

| Detail | Specification |
| :--- | :--- |
| **Algorithm** | `XGBoostClassifier` (Multiclass Classification) |
| **Training Split** | Standard 60/20/20 or similar methodology. |
| **Evaluation** | Accuracy Score |
| **Saved As** | `mobile_price.json` (XGBoost native format or similar persistence) |
| **Target Classes** | 4 Price Ranges (0, 1, 2, 3) |

### 🎯 Features Used

The model uses 20 hardware and capability features to determine the price bucket:

| Feature | Description | Feature | Description |
| :--- | :--- | :--- | :--- |
| `battery_power` | Total battery power (mAh) | `mobile_wt` | Mobile phone weight |
| `blue` | Bluetooth support (0/1) | `n_cores` | Number of processor cores |
| `clock_speed` | Speed at which microprocessor executes instructions | `pc` | Primary camera megapixels |
| `dual_sim` | Dual SIM support (0/1) | `px_height` | Pixel resolution height |
| `fc` | Front camera megapixels | `px_width` | Pixel resolution width |
| `four_g` | 4G support (0/1) | `ram` | Random Access Memory (MB) |
| `int_mem` | Internal Memory (GB) | `sc_h` | Screen height (cm) |
| `m_dep` | Mobile depth (cm) | `sc_w` | Screen width (cm) |
| `talk_time` | Longest time a single battery charge will last when you are | `three_g` | 3G support (0/1) |
| `touch_screen` | Touch screen support (0/1) | `wifi` | WiFi support (0/1) |

-----

Grateful to be a part of this ML Zoomcamp Cohort!
