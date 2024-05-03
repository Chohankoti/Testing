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
