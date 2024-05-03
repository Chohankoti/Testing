import requests
import json

URL = "https://reqres.in"

# Payload = {
#     "name": "KOTI CHOHAN",
#     "Job": "SDE",
#     "where": "this code file"
# }

# response = requests.get(url=URL+'/api/users', json=Payload)

json_file = open('./User.json')
json_payload = json.load(json_file)

response = requests.post(url=URL+'/api/users', json=json_payload)

print(response.status_code)
print(response.json())