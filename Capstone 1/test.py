import requests

url = "http://localhost:8000/predict"

employee = {
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

print(requests.post(url, json=employee).json())
