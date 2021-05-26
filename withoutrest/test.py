import requests

BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'apijsonCBV/'
response = requests.delete(BASE_URL+ENDPOINT)
data = response.json()
print(data)