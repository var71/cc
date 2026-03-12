import requests

api_key = "pk.9b87a42d55aca821d3fa15d85f1e9354"

query = input("Enter location: ")

url = "https://us1.locationiq.com/v1/search.php"

# params = {
#     "key": api_key,
#     "q": query,
#     "format": "json"
# }

# response = requests.get(url, params=params)
# data = response.json()

data=requests.get(url,params={"q":query,"key":api_key,"format":"json"}).json()


print("Place ID:", data[0]["place_id"])
print("Latitude:", data[0]["lat"])
print("Longitude:", data[0]["lon"])
print("Display Name:", data[0]["display_name"])