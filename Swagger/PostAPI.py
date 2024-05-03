import requests

API = "https://fakerestapi.azurewebsites.net/api/v1/Activities"


Payload = {
    "firstname": "koti",
    "lastname": "chohan",
    "username": "koti chohan",
    "company": "ABCD",
    "empid": 31265,
    "email": "chohankoti@gmail.com",
    "password": "chohanPASSWORD@1"
}


response = requests.post(API,  json = Payload)

print(response.status_code)
print(response.json())
