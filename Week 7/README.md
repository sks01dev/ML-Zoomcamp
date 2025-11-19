# Midterm Project
# 📱 Mobile Price Prediction API

This API predicts the **price range** of a mobile phone (0 = low, 3 = very high).

---

## 🚀 Run Locally (without Docker)

```bash
pip install -r requirements.txt
uvicorn app:app --reload --port 9000
```

API Docs:

👉 **[http://127.0.0.1:9000/docs](http://127.0.0.1:9000/docs)**

---

## 🐳 Run with Docker

Build the image:

```bash
docker build -t mobile-api .
```

Run the container on port **9000**:

```bash
docker run -p 9000:9000 mobile-api
```

Docs inside container:

👉 **[http://localhost:9000/docs](http://localhost:9000/docs)**

---

## 📤 Use the `/predict` Endpoint

Send a **POST** request to:

```
http://localhost:9000/predict
```

With a JSON body like:

```json
{
  "battery_power": 842,
  "blue": 0,
  "clock_speed": 2.2,
  "dual_sim": 0,
  "fc": 1,
  "four_g": 0,
  "int_memory": 7,
  "m_dep": 0.6,
  "mobile_wt": 188,
  "n_cores": 2,
  "pc": 2,
  "px_height": 20,
  "px_width": 756,
  "ram": 2549,
  "sc_h": 9,
  "sc_w": 7,
  "talk_time": 19,
  "three_g": 0,
  "touch_screen": 0,
  "wifi": 1
}
```

### Kaggle Dataset used: https://www.kaggle.com/datasets/iabhishekofficial/mobile-price-classification
