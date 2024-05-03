import requests

API = "https://fakerestapi.azurewebsites.net/api/v1/Activities"


Payload = {
    "id": 69,
    "title": "Activity 69",
    "dueDate": "2024-05-03T12:16:10.1837189+00:00",
    "completed": False
}


response = requests.post(API,  json = Payload)

print(response.status_code)
print(response.json())

data = response.json()
print(data['id'])

assert response.status_code == 200
assert data['id'] == 69


# Use data when you need to send raw data in a specific format other than JSON, and you're responsible for setting the Content-Type header manually.
# Use json when you're sending JSON data, and you want the requests library to handle the serialization and Content-Type header automatically for you.

# import requests
# import json

# API = "https://fakerestapi.azurewebsites.net/api/v1/Activities"

# Header = {
#     'Content-Type': 'application/json'  
# }

# Payload = {
#     "id": 69,
#     "title": "Activity 69",
#     "dueDate": "2024-05-03T12:16:10.1837189+00:00",
#     "completed": False
# }

# response = requests.post(API, headers=Header, data=json.dumps(Payload))

# print(response.status_code)
# print(response.json())

# data = response.json()
# print(data['id'])

# assert response.status_code == 200
# assert data['id'] == 69

