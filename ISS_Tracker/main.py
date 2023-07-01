import requests
import smtplib
import time
from datetime import datetime
from dateutil import tz



MY_LAT = 44.977753 # Your latitude
MY_LONG = -93.265015 # Your longitude

MY_EMAIL = "kw2120713@gmail.com"
PASSWORD = "gulbouqazahmhhjs"


def is_iss_overhead(lat, long):

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(f"ISS Location: {iss_latitude}, {iss_longitude}")
    return lat - 5 <= iss_latitude <= lat + 5 and long - 5 >= iss_longitude >= long + 5

def is_dark(lat, long):

    parameters = {
        "lat": lat,
        "lng": long,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]
    sunrise_time = datetime.strptime(sunrise, "%Y-%m-%dT%H:%M:%S%z")
    sunset_time = datetime.strptime(sunset, "%Y-%m-%dT%H:%M:%S%z")
    local_sunrise_time = str(sunrise_time.astimezone(tz=tz.tzlocal()))
    local_sunset_time = str(sunset_time.astimezone(tz=tz.tzlocal()))


    sunrise_hour = int(local_sunrise_time.split(" ")[1].split(":")[0])
    sunset_hour = int(local_sunset_time.split(" ")[1].split(":")[0])
    now_hour = datetime.now().hour

    return now_hour < sunrise_hour or now_hour > sunset_hour

while True:
    print(is_iss_overhead(MY_LAT, MY_LONG))
    print(is_dark(MY_LAT, MY_LONG))


    if is_dark(MY_LAT, MY_LONG) and is_iss_overhead(MY_LAT, MY_LONG):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="kw2120713@yahoo.com",
                                msg=f"Subject:🛰 ISS Tracker!\n\nLook up! the ISS's coordinates are:\n"
                                "lat: {iss_latitude}\nlong: {iss_longitude}")
    time.sleep(60)


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



