import requests
from requests.models import Response

def client_login():
    data= {"username":"admin","password":"xintent123"}
    response = requests.post("http://localhost:8000/api/rest_auth/login/",data=data)
    print(response.status_code)
    print(response.content)

def client_token():
    data = "Token 0e5757c364573c6cd2f14abc4302ce83a9f595b0"
    headers = {"Authorization": data}
    response = requests.get("http://localhost:8000/api/profiles/",headers=headers)
    print(response.status_code)

if __name__ =="__main__":
    client_login()