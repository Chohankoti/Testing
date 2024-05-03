import requests

URL_By_Id = "https://gorest.co.in/public/v2/users/6887949"

TOKEN = "7226f96fd6be9b742d3fa21e66b2d29c40a4c84d8aa1b2de1fc98f4aae77212a"

Header = {
    'Authorization' : f'Bearer {TOKEN}'
}




response = requests.get(URL_By_Id, headers = Header)

print(response.json())

assert response.status_code == 200