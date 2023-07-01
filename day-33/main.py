import requests
from datetime import datetime
from dateutil import tz

MY_LAT = 44.977753
MY_LNG = -93.265015

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
#
# iss_position = (data["iss_position"]["latitude"], data["iss_position"]["longitude"])
# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": "0"
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise)
print(sunset.split("T")[1].split(":")[0])

time_now = datetime.now(tz.tzutc())

print(time_now)