# API Studies

# Weather API 


# Rick and Morty API 

## https://rickandmortyapi.com

# pip install requests 

import requests 

response = requests.get("https://rickandmortyapi.com/api/character")
data = response.json()
print(data)


