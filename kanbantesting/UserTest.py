import requests

url = "http://localhost:8080/users"


response = requests.get(url)

print(response.status_code)