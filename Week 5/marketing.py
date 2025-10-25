import requests

url = 'http://localhost:9696/predict'

customer = { 
    "lead_source": "paid_ads", 
    "number_of_courses_viewed": 5, 
    "annual_income": 79450.0 
}

response = requests.post(url, json=customer)
predictions = response.json()

print(f"Respose: {predictions}")
if predictions['converted'] >= 0.5:
    print('Customer is likely to convert, send promo mails')
else:
    print('Customer is not likely to convert')