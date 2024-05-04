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
    assert Get_response.json()["userName"] == "User 2" and Get_response.json()["password"] == "Password2"

    print(Get_response.json())




def test_Updata_User_Validation():

    Payload = new_task_payload()

    Get_response = requests.get(url=URL+f'/{Payload["id"]}')

    assert Get_response.status_code == 200

    Update_response = requests.put(URL+f'/{Payload["id"]}', json=Payload)

    assert Update_response.status_code == 200

    assert Update_response.json()["id"] == Payload["id"]

    assert Update_response.json()["userName"] == "User Updated 2" and Update_response.json()["password"] == "Password Updated 2"

    assert Update_response.json() != Get_response.json()

    print(Update_response.json())


def test_Delete_User():
    
    Payload = new_task_payload()
    Create_task_response = create_task(Payload)

    assert Create_task_response.status_code == 200   
    

    Delete_response = requests.delete(URL+f'/{Payload["id"]}')

    assert Delete_response.status_code == 200



def create_task(Payload):
    response = requests.post(URL, json=Payload)
    return response
    


def new_task_payload():
    return  {
        "id": 2,
        "userName": "User Updated 2",
        "password": "Password Updated 2"
    }
