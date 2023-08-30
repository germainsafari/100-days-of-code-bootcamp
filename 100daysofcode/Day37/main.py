import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "germain"
Token = "fffghfggrtg4g4g55ge"
GRAPH = "graph3"
user_params = {
    "token": Token,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH,
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": Token
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)
pixela_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"
today = datetime(year=2023, month=7,day=23)
# print(today.strftime("%Y%m%d"))
pixel_data = {
    "date":today.strftime("%Y%m%d"),
    "quantity": "5",

}
response = requests.post(url=pixela_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)
