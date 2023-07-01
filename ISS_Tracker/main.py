import requests
import smtplib
import time
from config import *
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
env_var = os.environ

EMAIL_ACCOUNT = env_var["EMAIL_ACCOUNT"]
EMAIL_PASSWORD = env_var["EMAIL_PASSWORD"]
NOTIFY_EMAIL = env_var["NOTIFY_EMAIL"]


def is_iss_overhead(lat, long):
    """Compares location of ISS to """
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return lat - 5 <= iss_latitude <= lat + 5 and long - 5 >= iss_longitude >= long + 5


def is_dark(lat, long):
    """Evaluates if it's dark (after sunset, before sunrise) returns True/False"""
    parameters = {
        "lat": lat,
        "lng": long,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()["results"]

    sunrise = datetime.strptime(data["sunrise"], '%Y-%m-%dT%H:%M:%S+00:00')
    sunset = datetime.strptime(data["sunset"], '%Y-%m-%dT%H:%M:%S+00:00')

    now = datetime.utcnow()

    return now < sunrise or now > sunset

while True:
    print(is_iss_overhead(MY_LAT, MY_LONG))
    print(is_dark(MY_LAT, MY_LONG))
    if is_dark(MY_LAT, MY_LONG) and is_iss_overhead(MY_LAT, MY_LONG):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL_ACCOUNT, password=EMAIL_PASSWORD)
            connection.sendmail(from_addr=EMAIL_ACCOUNT,
                                to_addrs=NOTIFY_EMAIL,
                                msg=f"Subject:🛰 ISS Tracker!\n\nLook up! the ISS's coordinates are:\n"
                                "lat: {iss_latitude}\nlong: {iss_longitude}")
    time.sleep(60)




