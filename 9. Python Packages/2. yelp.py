import requests
import config

url = "https://api.yelp.com/v3/businesses/search"
headers = {
    "Authorization": "Bearer " + config.api_key
}
params = {
    "term": "Restaurant",
    "location": "Buenos Aires"
}
response = requests.get(url, headers=headers, params=params)
businesses = response.json()["businesses"]

for business in businesses:
    print(business["name"])
print()

tops = [b["name"] for b in businesses if b["rating"] > 4.5]
print("Los top:", tops)
