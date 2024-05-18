from datetime import datetime

import requests

pixcelend_point = "https://pixe.la/v1/users"
USERNAME = "Enter username"
TOKEN = "Enter token"
GRAPH_ID = "graph1"

params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# response = requests.post(url=pixcelend_point, json=params)
# print(response.text)

graph_endpoint = f"{pixcelend_point}/{USERNAME}/graphs"

graph_contents = {
    "id" : GRAPH_ID,
    "name" : "Daily Code Timeing's",
    "unit" : "min",
    "type" : "float",
    "color" : "sora",
    }

header = {
    "X-USER-TOKEN" : TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_contents, headers=header)
# print(response.text)

pixcel_creation_endpoint = f"{pixcelend_point}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()


pixcel_data = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : float(input("Enter min you had worked :"))
}

# response = requests.post(url=pixcel_creation_endpoint, json=pixcel_data, headers=header)
# print(response.text)

# update_pixcel = f"{pixcelend_point}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# new_pixcel = {
#     "quantity" : "110"
# }
#
# response = requests.put(url=update_pixcel, json=new_pixcel, headers=header)
# print(response.text)
#
# delete_pixcel = f"{pixcelend_point}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_pixcel, headers=header)