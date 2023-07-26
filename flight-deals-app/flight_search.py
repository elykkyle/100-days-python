from pprint import pprint
import requests
from datetime import datetime, timedelta
from flight_data import FlightData
from dotenv import load_dotenv
import os

load_dotenv()
KIWI_API_KEY = os.environ.get("KIWI_API_KEY")

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.URL = "https://api.tequila.kiwi.com"
        self.api_key = KIWI_API_KEY
        self.req_headers = {"apikey": self.api_key, "Accept":"application/json"}
        self.date_format = f"%d/%m/%Y"
        self.min_nights = 7
        self.max_nights = 28

    def get_iata_codes(self, location):
        url = f"{self.URL}/locations/query"
        req_params = {
            "term": location,
            "location_types": "city",
            # "location_types": "airport",
        }
        response = requests.get(url, headers=self.req_headers, params=req_params)
        response.raise_for_status()
        code = response.json()["locations"][0]["code"]
        return code

    def get_fares(self, start_code, dest_code, stop_overs=0):
        self.start_code = start_code
        self.dest_code = dest_code
        today = datetime.today()
        tomorrow = today + timedelta(days=1)
        tomorrow_str = datetime.strftime(tomorrow, self.date_format)
        six_months_ahead = today + timedelta(days=180)
        six_months_str = datetime.strftime(six_months_ahead, self.date_format)
        url = f"{self.URL}/v2/search"
        req_params = {
            "fly_from": start_code,
            "fly_to": dest_code,
            "date_from": tomorrow_str,
            "date_to": six_months_str,
            "nights_in_dst_from": self.min_nights,
            "nights_in_dst_to": self.max_nights,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": stop_overs,
            "sort": "price",
            "curr": "GBP",
            "limit": 1
        }
        response = requests.get(url, headers=self.req_headers, params=req_params)
        response.raise_for_status()
        try:
            fare = response.json()["data"][0]
        except IndexError:
            req_params["max_stopovers"] = 1
            response = requests.get(url, headers=self.req_headers, params=req_params)
            response.raise_for_status()
            pprint(response.json())
            fare = response.json()["data"][0]

            flight_data = FlightData(
                price=fare["price"],
                origin_city=fare["route"][0]["cityFrom"],
                origin_airport=fare["route"][0]["flyFrom"],
                destination_city=fare["route"][0]["cityTo"],
                destination_airport=fare["route"][0]["flyTo"],
                out_date=fare["route"][0]["local_departure"].split("T")[0],
                return_date=fare["route"][2]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=fare["route"][0]["cityTo"]
            )
            return flight_data
        else:
            flight_data = FlightData(
                price=fare["price"],
                origin_city=fare["route"][0]["cityFrom"],
                origin_airport=fare["route"][0]["flyFrom"],
                destination_city=fare["route"][0]["cityTo"],
                destination_airport=fare["route"][0]["flyTo"],
                out_date=fare["route"][0]["local_departure"].split("T")[0],
                return_date=fare["route"][1]["local_departure"].split("T")[0],
            )
            return flight_data
