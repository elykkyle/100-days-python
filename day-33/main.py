import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

iss_position = (data["iss_position"]["latitude"], data["iss_position"]["longitude"])
print(iss_position)