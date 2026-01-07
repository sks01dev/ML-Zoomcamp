import pickle
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field

# Load artifacts
with open("model.bin", "rb") as f:
    model = pickle.load(f)
with open("feature_columns.bin", "rb") as f:
    feature_columns = pickle.load(f)

app = FastAPI(title="Employee Attrition API")

class Employee(BaseModel):
    # Numeric limits with ge (>=) and le (<=)
    Age: int = Field(..., ge=18, le=100, description="Age of the employee")
    BusinessTravel: str = Field(..., description="Frequency of travel")
    DailyRate: int = Field(..., ge=100, le=2000)
    Department: str = Field(...)
    DistanceFromHome: int = Field(..., ge=1, le=50)
    Education: int = Field(..., ge=1, le=5)
    EducationField: str = Field(...)
    EnvironmentSatisfaction: int = Field(..., ge=1, le=4)
    JobInvolvement: int = Field(..., ge=1, le=4)
    JobLevel: int = Field(..., ge=1, le=5)
    JobRole: str = Field(...)
    JobSatisfaction: int = Field(..., ge=1, le=4)
    MonthlyIncome: int = Field(..., ge=1000, le=20000)
    NumCompaniesWorked: int = Field(..., ge=0, le=10)
    OverTime: str = Field(..., pattern="^(Yes|No)$", description="Must be 'Yes' or 'No'")
    WorkLifeBalance: int = Field(..., ge=1, le=4)
    YearsAtCompany: int = Field(..., ge=0, le=40)

    # Provide a sample for the /docs page
    model_config = {
        "json_schema_extra": {
            "example": {
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
                "YearsAtCompany": 5,
            }
        }
    }

@app.post("/predict")
def predict(employee: Employee):
    # Convert validated input to DataFrame
    df = pd.DataFrame([employee.model_dump()]) # model_dump replaces .dict() in Pydantic v2
    
    # Encode and align
    df_encoded = pd.get_dummies(df, drop_first=True)
    df_final = df_encoded.reindex(columns=feature_columns, fill_value=0)

    # Predict
    proba = model.predict_proba(df_final)[0, 1]

    return {
        "attrition_probability": round(float(proba), 4),
        "attrition": bool(proba >= 0.5),
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)