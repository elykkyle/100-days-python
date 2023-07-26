from pprint import pprint
import requests
import os
from dotenv import load_dotenv

load_dotenv()

SHEETY_URL = os.environ.get("SHEETY_URL")
SHEETY_AUTH_TOKEN = os.environ.get("SHEETY_AUTH_TOKEN")
req_headers = {
            "Authorization": f"Bearer {SHEETY_AUTH_TOKEN}"
        }
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}


    def get_sheet_data(self):
        response = requests.get(SHEETY_URL, headers=req_headers)
        response.raise_for_status()
        self.destination_data = response.json()["prices"]
        return self.destination_data

    def update_row(self, new_data):
        URL = f"{SHEETY_URL}/{new_data['id']}"
        update = {
            "price": new_data
        }
        response = requests.put(URL, headers=req_headers, json=update)
        response.raise_for_status()

