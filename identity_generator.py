import random
import requests
import json

def generate_identity():
    response = requests.get("https://randomuser.me/api/")
    data = response.json()['results'][0]
    identity = {
        "name": f"{data['name']['first']} {data['name']['last']}",
        "email": data['email'],
        "username": data['login']['username'],
        "password": data['login']['password'],
        "phone": data['phone'],
        "picture": data['picture']['large'],
        "location": f"{data['location']['city']}, {data['location']['country']}"
    }
    return identity

if __name__ == "__main__":
    identity = generate_identity()
    print(json.dumps(identity, indent=2))
