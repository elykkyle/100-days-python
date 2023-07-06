import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
NL_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/83e982eaa2c6f35ad75ba929d10115f3/workoutTracking/workouts"

current_date = datetime.now().strftime("%m/%d/%Y")
current_time = datetime.now().strftime("%H:%M:%S")
print(current_time)



nutritionix_req_headers = {
    "x-app-id": os.environ.get("NUTRITIONIX_APP_ID"),
    "x-app-key": os.environ.get("NUTRITIONIX_APP_KEY"),
    "Content-Type": "application/json"
}

user_input = input("Tell me what exercises you did: ")

nutritionix_req_body = {
    "query": user_input,
    "gender": os.environ.get("GENDER"),
    "weight_kg": os.environ.get("WEIGHT_KG"),
    "height_cm": os.environ.get("HEIGHT_KG"),
    "age": os.environ.get("AGE")
}

nutritionix_response = requests.post(NL_ENDPOINT, headers=nutritionix_req_headers, json=nutritionix_req_body)
nutritionix_response.raise_for_status()
nutritionix_data = nutritionix_response.json()["exercises"]

sheety_req_headers = {
    "Authorization": f"Bearer {os.environ.get('SHEETY_AUTH_TOKEN')}",
    "Content-Type": "application/json"
}

for exercise in nutritionix_data:

    sheety_req_body = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise["name"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheety_response = requests.post(url=SHEETY_ENDPOINT, headers=sheety_req_headers, json=sheety_req_body)
    sheety_response.raise_for_status()
    if sheety_response.status_code == 200:
        print(f"Added {sheety_response.json()['workout']['exercise']} successfully.")