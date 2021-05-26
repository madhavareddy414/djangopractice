import requests
BASE_URL ='http://127.0.0.1:8000/'
END_POINT ='api/'

def get_resource(id):
    resp = requests.get(BASE_URL+END_POINT+id+'/')
    print(resp.status_code)
    print(resp.json())
id = input('enter id')
get_resource(id)

# def get_all():
#     resp = requests.get(BASE_URL+END_POINT)
#     print(resp.status_code)
#     print(resp.json())
# get_all()