"""Contains the acceptance tests to all user endpoints"""
import json


def test_create_user(client):
    data = {
        "first_name": "Victorine",
        "last_name": "Osewe",
        "email": "victorineosewe@gmail.com",
        "password": "password",
        "gender": "female",
        "job_role": "software engineer",
        "department": "Software",
        "address": "Kisumo",
    }
    response = client.post("/auth/create-user", json.dumps(data))
    assert response.status_code == 201
    assert response.json()["first_name"] == "Victorine"
    assert response.json()["department"] == "Software"
