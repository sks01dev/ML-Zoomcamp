from fastapi import FastAPI
from typing import Literal
import uvicorn
import pickle
# for data validation, so the data input by the user is realistic
from pydantic import BaseModel, Field

# request data
class Customer(BaseModel):
    lead_source: Literal['organic_search', 'social_media', 'paid_ads', 'referral', 'events'] = Field(
        ...,
        description="Source of the lead",
    )
    annual_income: float = Field(..., ge=0, le=109899)
    number_of_courses_viewed: int = Field(..., ge=0, le=9)

    # sample data
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "lead_source": "paid_ads",
                    "annual_income": 79276.0,
                    "number_of_courses_viewed": 2,
                }
            ]
        }
    }

# response data
class PredictResponse(BaseModel):
    convert_probability: float
    converted: bool

app = FastAPI(title="Customer Conversion Predictor")

# Load the pre-trained model
with open("model.bin", "rb") as f_in:
    pipeline = pickle.load(f_in)

# Helper function to get prediction from the loaded model
def predict_single(customer_dict: dict) -> float:
    return pipeline.predict_proba(customer_dict)[0, 1]

# Define the prediction endpoint
@app.post("/predict", response_model=PredictResponse)
def predict(customer: Customer):
    prob = predict_single(customer)
    return PredictResponse(convert_probability=prob, converted=(prob >= 0.5))

# Run the app for local development
# The '__main__' block is for local development and will NOT run on Hugging Face Spaces
# if __name__ == "__main__":
#     uvicorn.run("predict:app", host="0.0.0.0", port=9696)
