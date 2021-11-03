import json

import requests


def client_registration():
    data = {"username": "wangkaiyu",
            "password1": "xintent123", "password2": "xintent123"}
    response = requests.post(
        "http://localhost:8000/api/rest-auth/registration/", data=data)
    print(response.status_code)
    # print(response.content)


def client_login():
    data = {"username": "wangkaiyu", "password": "xintent123"}
    response = requests.post(
        "http://localhost:8000/api/rest-auth/login/", data=data)
    print(response.status_code)
    print(response.content)


def client_list_profile():
    data = "Token 6923b2126f003fcaf3b566527113ce6d75f7a048"
    headers = {"Authorization": data}
    response = requests.get(
        "http://localhost:8000/api/profiles/", headers=headers)
    print(response.status_code)
    print(json.loads(response.content))


def client_update_profile():
    headers = {"Authorization":  "Token 6923b2126f003fcaf3b566527113ce6d75f7a048"}
    data = {"city": "hangzhou"}
    response = requests.put(
        "http://localhost:8000/api/profiles/5/", headers=headers, data=data)
    print(response.status_code)
    print(json.loads(response.content))


if __name__ == "__main__":
    client_update_profile()
