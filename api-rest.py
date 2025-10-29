# API Rest 

"""A REST API (Representational State Transfer) follows a few architectural principles:

* Uses standard HTTP methods like GET, POST, PUT, DELETE.
* Has resources identified by URLs (for example /api/breeds/list/all).
* Returns structured representations of those resources (usually JSON).
* Is stateless - each request contains everything the server needs (no session storage)
"""

import requests

url = "https://dog.ceo/api/breeds/list/all"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Dog breeds loaded successfully!")
    for breed in data["message"]:
        print(breed)
else:
    print(f"Request failed: {response.status_code}")


