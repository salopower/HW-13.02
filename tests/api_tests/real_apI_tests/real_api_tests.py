import pytest
import requests
import json


@pytest.mark.api
def test_get_multiple_users():
    response = requests.get('https://reqres.in/api/users?page=2')
    assert response.status_code == 200
    parsed = json.loads(response.content)
    expected_data = [
        user.get('id') is not None and
        user.get('email') is not None and
        user.get('first_name') is not None and
        user.get('last_name') is not None
        for user in parsed.get('data')
    ]
    assert all(expected_data)


@pytest.mark.api
def test_get_single_user():
    response = requests.get('https://reqres.in/api/users/2')
    parsed = response.json()
    assert all([
        response.status_code == 200,
        parsed['data']['id'] == 2,
        parsed['data']['email'] == 'janet.weaver@reqres.in',
        parsed['data']['first_name'] == 'Janet',
        parsed['data']['last_name'] == 'Weaver',
        requests.get(parsed['data']['avatar']).status_code == 200
    ])



@pytest.mark.api
def test_get_with_auth():
    url = 'https://postman-echo.com/basic-auth'
    response = requests.get(url, auth=('username', 'password'))
    assert response.status_code == 200
    assert json.loads(response.text).get('authenticated')


@pytest.mark.api
def test_create_user():
    response = requests.post("https://www.example.com",
                             headers={"User-Agent": "MyApp/1.0", "Accept-Encoding": "gzip, deflate",
                                      "Accept": "application/json", "Content-Type": "application/json"},
                             json={"key": "value"})
    print(response.text)


import base64


def encode_base64(username: str, password: str) -> str:
    credentials = f'{username}:{password}'
    return base64.b64encode(credentials.encode()).decode()


def decode_base64(string: str) -> str:
    decoded_bytes = base64.b64decode(string)
    return decoded_bytes.decode()
