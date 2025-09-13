import requests

# Cambia estos valores por los que desees consultar
data = {
    "bedrooms": 3,
    "bathrooms": 2,
    "sqft_living": 1800,
    "sqft_lot": 5000,
    "floors": 1,
    "waterfront": 0,
    "condition": 3
}

url = "http://127.0.0.1:5000/predict"
response = requests.post(url, json=data)

if response.status_code == 200:
    print("Precio predicho:", response.json()["predicted_price"])
else:
    print("Error:", response.text)