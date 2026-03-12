import requests, webbrowser

API_KEY = open("API_KEY").read().strip()
CX = open("SEARCH_ENGINE_ID").read().strip()

query = input("Enter something to Search: ")

url = "https://www.googleapis.com/customsearch/v1"
data = requests.get(url, params={"q": query, 
                                 "key": API_KEY, 
                                 "cx": CX}).json() #'searchType': 'image',  "fileType":"pdf"

if "items" in data:
    link = data["items"][0]["link"]
    print("Opening:", link)
    webbrowser.open(link)
else:
    print("No results found")