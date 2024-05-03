import requests

URL = "https://gorest.co.in/public/v2/users"

Params = {
    'page': 2,
    'per_page': 1
}

response = requests.get(URL, params= Params)

print(response.json())

assert response.status_code == 200