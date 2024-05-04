import pytest
import requests

URL  = "https://fakerestapi.azurewebsites.net/api/v1/Users"


def test_GET_Validation():

    response = requests.get(URL)

    assert response.status_code == 200



def test_Create_User_Validation():

    Payload = {
        "id": 2,
        "userName": "User 2",
        "password": "Password2"
    }

    Create_response = requests.post(URL, json=Payload)

    assert Create_response.status_code == 200

    data = Create_response.json()

    assert data["id"] == 2

    Get_response = requests.get(url=URL+'/2')

    assert Get_response.status_code == 200
    assert Get_response.json()["userName"] == "User 2"
    assert Get_response.json()["password"] == "Password2"

    print(Get_response.json())




def test_Updata_User_Validation():

    Payload = {
        "id": 21,
        "userName": "User 21",
        "password": "Password21"
    }

    response = requests.put(url=URL+'/21', json=Payload)

    assert response.status_code == 200