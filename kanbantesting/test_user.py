import pytest
import requests


URL = "http://localhost:8080/users"

"""
GET BY ID:

> Create a new user
> Get the user by ID (Which is created in the above step)
> Validate the response code and the user details with payload passed and Get response
> Delete the user


Update User:

> Create a new user
> Get the user by ID (Which is created in the above step)
> Update the user details
> Validate the response code and the user details with Get response and Update response
> Delete the user


Delete User:

> Create a new user
> Get the user by ID (Which is created in the above step)
> Delete the user and validate the response code
> Try to get the user by ID and validate the response code

"""


def test_GET_All_Users_Validation():

    response = requests.get(URL)

    assert response.status_code == 200


def test_GET_By_ID_Validation():

    Payload = Get_Payload()

    create_response = create_user(Payload)

    assert create_response.status_code == 201

    data = create_response.json()

    get_by_id_response = requests.get(url=URL+f'/{data["id"]}')

    assert get_by_id_response.status_code == 200

    # Checking whether the created data is equal to get by id data
    assert create_response.json() == get_by_id_response.json()

    print(get_by_id_response.json())

    # Finaly Delete 
    delete_response = delete_user(data["id"])

    assert delete_response.status_code == 204


def test_Update_User_Validation():

    Payload = Get_Payload()

    create_response = create_user(Payload)

    assert create_response.status_code == 201

    data = create_response.json()

    print(create_response.json())

    Update_Payload = Updated_Payload()

    update_response = requests.put(url=URL+f'/{data["id"]}', json=Update_Payload)

    assert update_response.status_code == 200

    # Checking whether the created data not equal to updated data
    assert create_response.json() != update_response.json()

    print(update_response.json())

    # Finaly Delete 
    delete_response = delete_user(data["id"])

    assert delete_response.status_code == 204


def test_Delete_User_Validation():

    Payload = Get_Payload()

    create_response = create_user(Payload)

    assert create_response.status_code == 201

    data = create_response.json()

    print(create_response.json())


    # Finaly Delete 
    delete_response = delete_user(data["id"])

    assert delete_response.status_code == 204


    # Check whether properly deleted or not by getting the id
    get_by_id_response = requests.get(url=URL+f'/{data["id"]}')

    assert get_by_id_response.status_code == 404

  




def create_user(Payload):

    response = requests.post(URL, json=Payload)

    return response

def delete_user(id):
    
    response = requests.delete(url=URL+f'/{id}')

    return response


def Get_Payload():
    return {
        "firstname": "test_firstname",
        "lastname": "test_lastname",
        "username": "test_username",
        "company": "test_company",
        "empid":  2131265,
        "email": "test_email@gmail.com",
        "password": "test_password"
    }

def Updated_Payload():
    return {
        "firstname": "test_firstname_updated",
        "lastname": "test_lastname_updated",
        "username": "test_username_updated",
        "company": "test_company_updated",
        "empid":  31265,
        "email": "test_email_updated@gmail.com",
        "password": "test_password_updated"
    }

