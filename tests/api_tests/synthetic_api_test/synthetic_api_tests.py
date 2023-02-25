import pytest
import requests

base_url = "https://example.com/api"
resource_id = 123

new_resource = {"name": "Test Resource", "description": "A synthetic test resource"}


def test_create():
    response = requests.post(f"{base_url}/resources", json=new_resource)
    assert response.status_code == 201
    assert response.json()["name"] == new_resource["name"]
    assert response.json()["description"] == new_resource["description"]
    global created_resource_id
    created_resource_id = response.json()["id"]


# Perform the Read test
def test_read():
    response = requests.get(f"{base_url}/resources/{resource_id}")
    assert response.status_code == 200
    assert response.json()["id"] == resource_id
    assert response.json()["name"] == "Existing Resource"
    assert response.json()["description"] == "An existing resource for testing"


# Perform the Update test
def test_update():
    updated_resource = {"name": "Updated Resource", "description": "An updated synthetic test resource"}
    response = requests.put(f"{base_url}/resources/{created_resource_id}", json=updated_resource)
    assert response.status_code in (200, 204)
    assert response.json()["name"] == updated_resource["name"]
    assert response.json()["description"] == updated_resource["description"]
    response = requests.get(f"{base_url}/resources/{created_resource_id}")
    assert response.status_code == 200
    assert response.json()["name"] == updated_resource["name"]
    assert response.json()["description"] == updated_resource["description"]


# Perform the Delete test
def test_delete():
    response = requests.delete(f"{base_url}/resources/{created_resource_id}")
    assert response.status_code == 204
    response = requests.get(f"{base_url}/resources/{created_resource_id}")
    assert response.status_code == 404
