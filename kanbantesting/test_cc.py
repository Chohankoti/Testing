import pytest
import requests

URL = "http://localhost:8080/CC"


def test_GET_All_CCs_Validation():

    response = requests.get(URL)

    assert response.status_code == 200


def test_GET_By_ID_CC_Validation():

    Payload = Get_Payload()

    create_response = create_CC(Payload)

    assert create_response.status_code == 201

    data = create_response.json()

    get_by_id_response = requests.get(url=URL+f'/{data["id"]}')

    assert get_by_id_response.status_code == 200

    # Checking whether the created data is equal to get by id data
    assert get_by_id_response.json() == create_response.json()

    print(get_by_id_response.json())

     # Finaly Delete 
    delete_response = delete_CC(data["id"])

    assert delete_response.status_code == 204


def test_Update_CC_Validation():

    Payload = Get_Payload()

    create_response = create_CC(Payload)

    assert create_response.status_code == 201

    data = create_response.json()

    Update_Payload = Updated_Payload()

    update_response = requests.put(url=URL+f'/{data["id"]}', json=Update_Payload)

    assert update_response.status_code == 200

    # Checking whether the created data not equal to updated data
    assert create_response.json() != update_response.json()

    print(update_response.json())

    # Finaly Delete 
    delete_response = delete_CC(data["id"])

    assert delete_response.status_code == 204


def test_Delete_CC_Validation():

    Payload = Get_Payload()

    create_response = create_CC(Payload)

    assert create_response.status_code == 201

    data = create_response.json()

    print(create_response.json())


    # Finaly Delete 
    delete_response = delete_CC(data["id"])

    assert delete_response.status_code == 204


    # Check whether properly deleted or not by getting the id
    get_by_id_response = requests.get(url=URL+f'/{data["id"]}')

    assert get_by_id_response.status_code == 404



def create_CC(Payload):

    response = requests.post(URL, json=Payload)

    return response


def delete_CC(id):
    
    response = requests.delete(url=URL+f'/{id}')

    return response


def Get_Payload():
    return {
    "ccode": 999,
    "owner": "chohan payload"
   }

def Updated_Payload():
    return {
        "ccode": 999,
        "owner": "chohan payload updated"
    }