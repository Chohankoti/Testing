import requests

URL = "https://gorest.co.in/public/v2/users"

Params = {
    'page': 1,
    'per_page': 3
}

response = requests.get(URL, params= Params)

print(response.json())

assert response.status_code == 200