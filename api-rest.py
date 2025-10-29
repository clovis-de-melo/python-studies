# API Rest 

"""A REST API (Representational State Transfer) follows a few architectural principles:

* Uses standard HTTP methods like GET, POST, PUT, DELETE.
* Has resources identified by URLs (for example /api/breeds/list/all).
* Returns structured representations of those resources (usually JSON).
* Is stateless - each request contains everything the server needs (no session storage)
"""

import requests
import json 

# bash: pip show requests

""" If requests is installed, you’ll see details like:
Name: requests
Version: 2.31.0
Summary: Python HTTP for Humans.
Location: /usr/local/lib/python3.11/site-packages
Requires: certifi, charset-normalizer, idna, urllib3

If it's not installed, you'll see:
Warning: Package(s) not found: requests
"""

# bash: pip list

url = "https://dog.ceo/api/breeds/list/all"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Dog breeds loaded successfully!")
    
    # Save the data to a JSON file
    with open("dog_breeds.json", "w") as file:
        json.dump(data, file, indent=4)
    print("Data saved to 'dog_breeds.json'")

else:
    print(f"Request failed: {response.status_code}")


