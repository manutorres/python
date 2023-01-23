from urllib.request import urlopen
import requests

# Hacer el pedido (request)
response = requests.get('https://api.github.com/')

print(response)
print(response.status_code)

#######################################################
print("#" * 50)

url = 'https://google.com/'

with urlopen(url) as response:
    body = response.read()
    print(response.status)
    print(body[:15])
