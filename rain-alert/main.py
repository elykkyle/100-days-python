import requests
import dotenv
import os
from twilio.rest import Client

dotenv.load_dotenv()
# twilio
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

# openweathermap API
WEATHER_URL = "https://api.openweathermap.org/data/3.0/onecall"

params = {
    "lat": os.environ["MY_LAT"],
    "lon": os.environ["MY_LONG"],
    "appid": os.environ['OPENWEATHERMAP_API_TOKEN'],
    "exclude": "current,minutely,daily"
}

response = requests.get(WEATHER_URL, params=params)
response.raise_for_status()

data = response.json()
# print(data)


def will_rain_twelve_hour(weather_data):
    output = False
    hours_slice = weather_data["hourly"][:12]
    for hour in range(len(hours_slice)):
        condition_code = (hours_slice[hour]["weather"][0]["id"])
        if condition_code < 700:
            output = True
    return output

# def send_sms(message_body: str):
#     message


if will_rain_twelve_hour(data):
    message = client.messages.create(
        from_='+18444233550',
        body='Bring an umbrella!',
        to=os.environ["MY_PHONE"]
    )

print(message.sid)
