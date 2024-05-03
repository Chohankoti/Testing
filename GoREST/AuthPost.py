import requests

URL = "https://gorest.co.in/public/v2/users"

TOKEN = "7226f96fd6be9b742d3fa21e66b2d29c40a4c84d8aa1b2de1fc98f4aae77212a"

Header = {
    'Authorization' : f'Bearer {TOKEN}'
}


Payload = {
    "name": "ABC_XYZ",
    "email": "ABC_XYZ@gmail.com",
    "gender": "female",
    "status": "active"
}

# ID : 6887949


response = requests.post(URL, headers = Header, json = Payload)

print(response.json())

assert response.status_code == 201