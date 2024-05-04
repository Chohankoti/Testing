import pytest
import requests
import json

URL = "https://reqres.in"


def test_GetRequest_Validation():    

    response = requests.get(url=URL+'/api/users/3')    

    assert response.status_code == 200

    


def test_Payload_Upload_Validation():

    json_file = open('./User.json')
    json_payload = json.load(json_file)

    response = requests.post(url=URL+'/api/users', json=json_payload)

    assert response.status_code == 201

