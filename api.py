# API Studies

# Weather API 


# Rick and Morty API 

## https://rickandmortyapi.com

# pip install requests 

""" import requests 

response = requests.get("https://rickandmortyapi.com/api/character")
data = response.json()
print(data) """


# API test 

import requests
response = requests.get("https://dog.ceo/api/breeds/list/all")
data = response.json()
print(response.status_code)
print(data)
