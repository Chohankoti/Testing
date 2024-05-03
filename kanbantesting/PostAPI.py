import requests

API = "http://localhost:8080/users"


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
