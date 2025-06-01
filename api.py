# API Studies

# Weather API 

import requests 

response = requests.get("https://rickandmortyapi.com/api/character")
data = response.json()
print(data)
