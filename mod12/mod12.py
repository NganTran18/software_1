import requests
import json
#fetch
response = requests.get("https://api.chucknorris.io/jokes/random")
# print(response)

if response.status_code == 200:
    json_response = response.json()
    print(json_response["value"])
else:
    print("nah")

