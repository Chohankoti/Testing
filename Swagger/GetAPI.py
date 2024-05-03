import requests

url = "https://fakerestapi.azurewebsites.net/api/v1/Activities"


response = requests.get(url)

print(response.status_code)

print(response.json()[0])