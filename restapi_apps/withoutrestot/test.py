import requests #sending response from python app using request

BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'apijsonCBV/'
response = requests.get(BASE_URL+ENDPOINT)
data = response.json()
print(data)