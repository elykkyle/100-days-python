from datetime import date

import requests

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "kylewill44"
TOKEN = "2a98ac7048a64cd4a168a5300ba9b120"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

req_header = {
    "X-USER-TOKEN": TOKEN
}

graph_config = {
    "id": "graph1",
    "name": "A Tracked Habit",
    "unit": "Minutes",
    "type": "int",
    "color": "sora",
    "timezone": "America/Chicago"
}

graph_id = graph_config["id"]
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# response = requests.post(graph_endpoint, headers=req_header, json=graph_config)

graph_update_config_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"
# response = requests.put(graph_update_config_endpoint, headers=req_header, json=graph_config)
# print(response.text)

today = date.today().strftime("%Y%m%d")

add_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"
pixel_data = {
    "date": "20230702",
    "quantity": "23"
}

response = requests.post(add_pixel_endpoint, headers=req_header, json=pixel_data)
print(response.text)