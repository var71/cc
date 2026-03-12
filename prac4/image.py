
import requests

API_KEY = open("API_KEY").read()
CX = open("SEARCH_ENGINE_ID").read()

query = "car"

url = "https://www.googleapis.com/customsearch/v1"

params = {
    'q': query,
    'key': API_KEY,
    'cx': CX,
 
}

response = requests.get(url, params=params)
results = response.json()['items']

for item in results:
    print(item['link'])