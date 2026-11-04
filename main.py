import requests
import os
from datetime import datetime
from dotenv import load_dotenv

## API Info

load_dotenv()
API_KEY = os.getenv("API_KEY")
APP_ID = os.getenv("APP_ID")

## Constants
GENDER = "male"
AGE = 23
WEIGHT_KG = 68
HEIGHT_CM = 168
NOW = datetime.now()

## URLS
url = os.getenv("url")
let_url = os.getenv("let_url")

## Input
user_input = input("What did you do today?: ")

headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

p_headers = {
    "Authorization": os.getenv("Authorization"),
}

data = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url, headers=headers, json=data, timeout=10)
response.raise_for_status()

result = response.json()

ex = result["exercises"][0]

activity = ex["name"]
activity_duration = ex["duration_min"]
calories = ex["nf_calories"]

## SHEETY API

new_row = {
    "workout": {
        "date": NOW.strftime("%d/%m/%Y"),
        "time": NOW.strftime("%H:%M:%S"),
        "exercise": activity,
        "duration": activity_duration,
        "calories": calories,
    }
}

post_response = requests.post(let_url, json=new_row, headers=p_headers, timeout=10)
post_response.raise_for_status()

print(post_response.status_code)
print(post_response.text)
