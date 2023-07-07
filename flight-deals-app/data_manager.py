from pprint import pprint
import requests

SHEETY_URL = "https://api.sheety.co/83e982eaa2c6f35ad75ba929d10115f3/flightDeals/prices"
SHEETY_AUTH_TOKEN = "uTGT91t0LFPugtvQTmg3wgY3llG3GBpGcNI9PUL8NZN4UL"
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
        print(URL)
        pprint(update)
        response = requests.put(URL, headers=req_headers, json=update)
        response.raise_for_status()

