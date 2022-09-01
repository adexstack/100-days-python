import requests
from datetime import datetime

ENDPOINT = "https://pixe.la/v1/users"
TOKEN = "se32xfth34kl5rt"
USERNAME = "seyiadex"

parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(ENDPOINT, json=parameters)
# print(response.text)

graph_parameters = {
    "id":"graph1",
    "name":"habit-tracking",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

create_graph_endpoint = f"{ENDPOINT}/{USERNAME}/graphs"

# create_graph_response = requests.post(url=create_graph_endpoint, json=graph_parameters, headers=headers)
# print(create_graph_response.text)
# View graph: https://pixe.la/v1/users/seyiadex/graphs/graph1.html

day = datetime(year=2021, month=6, day=23)
day_stringify = day.strftime("%Y%m%d")

today= datetime.now().strftime("%Y%m%d")


create_pixel_parameters = {
    "date":day_stringify,
    "quantity":"6.74"
}

create_pixel_endpoint = f"{ENDPOINT}/{USERNAME}/graphs/graph1"

# create_pixel_response = requests.post(create_pixel_endpoint, json=create_pixel_parameters, headers=headers)
# print(create_pixel_response.text)

update_pixel_parameters = {
    "quantity":"8.56"
}

# update_pixel_endpoint = f"{ENDPOINT}/{USERNAME}/graphs/graph1/{today}"
# update_pixel_response = requests.put(update_pixel_endpoint, json=update_pixel_parameters, headers=headers)
# print(update_pixel_response.text)

#DELETE https://pixe.la/v1/users/a-know/graphs/test-graph/20180915 -H 'X-USER-TOKEN:thisissecret'
delete_response = requests.delete(url=f"{create_pixel_endpoint}/{day_stringify}", headers=headers)
print(delete_response.text)
