from fastapi import FastAPI
from pydantic import BaseModel, Field
import xgboost as xgb
import numpy as np


# Load Trained XGBoost Model
model = xgb.XGBClassifier()
model.load_model("mobile.json")     

# Initialize FastAPI App
app = FastAPI(
    title="Mobile Price Classification API",
    description="Predicts price range of a mobile phone (0 = low cost → 3 = very high cost).",
    version="1.0"
)


# Pydantic Input Schema
class MobileInput(BaseModel):
    battery_power: int = Field(..., example=842)      
    blue: int = Field(..., example=0)                 
    clock_speed: float = Field(..., example=2.2)
    dual_sim: int = Field(..., example=0)
    fc: int = Field(..., example=1)
    four_g: int = Field(..., example=0)
    int_memory: int = Field(..., example=7)
    m_dep: float = Field(..., example=0.6)
    mobile_wt: int = Field(..., example=188)
    n_cores: int = Field(..., example=2)
    pc: int = Field(..., example=2)
    px_height: int = Field(..., example=20)
    px_width: int = Field(..., example=756)
    ram: int = Field(..., example=2549)
    sc_h: int = Field(..., example=9)
    sc_w: int = Field(..., example=7)
    talk_time: int = Field(..., example=19)
    three_g: int = Field(..., example=0)
    touch_screen: int = Field(..., example=0)
    wifi: int = Field(..., example=1)

 
# Prediction Endpoint
@app.post("/predict")
def predict_mobile_price(data: MobileInput):

    # Convert input object → NumPy 2D array
    arr = np.array([[
        data.battery_power,
        data.blue,
        data.clock_speed,
        data.dual_sim,
        data.fc,
        data.four_g,
        data.int_memory,
        data.m_dep,
        data.mobile_wt,
        data.n_cores,
        data.pc,
        data.px_height,
        data.px_width,
        data.ram,
        data.sc_h,
        data.sc_w,
        data.talk_time,
        data.three_g,
        data.touch_screen,
        data.wifi
    ]])

    # Make prediction
    pred = model.predict(arr)[0]   # model returns array of predictions for a batch

    price_dict = {
        0: "LOW COST",
        1: "MEDIUM COST",
        2: "HIGH COST",
        3: "VERY HIGH COST"
    }

    return {
        "predicted_price_range": int(pred),
        "label": price_dict[int(pred)]
    }
