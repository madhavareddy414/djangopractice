import requests

# def get_source(id):
#     BASE_URL = "http://127.0.0.1:8000/"
#     END_POINT = 'api'
#     resp = requests.get(BASE_URL+END_POINT+'/')
#     if resp.status_code in range(200,300):
#         print(resp.json())
#     else:
#         print('something went wrong')
#     print(resp.status_code)
#     print(resp.json())
#
# get_source('2')
#
# def get_all():
#     BASE_URL = "http://127.0.0.1:8000/"
#     END_POINT = 'api'
#     resp = requests.get(BASE_URL+END_POINT)
#     print(resp.json())
# get_all()

import json
#
def create_source():
    BASE_URL = "http://127.0.0.1:8000/"
    END_POINT = 'api-list/'
    new_emp = {
        'eno':400,
        'ename':'raogopal',
        'esal':1000,
        'eaddr':'bglr'
    }
    resp =requests.post(BASE_URL+END_POINT,data=json.dumps(new_emp))
    print(resp.json())
    print(resp.status_code)
create_source()

# def update_source(id):
#     BASE_URL = "http://127.0.0.1:8000/"
#     END_POINT = 'api/'
#     new_emp = {
#
#
#         'esal':100,
#         'eaddr':'vizag'
#     }
#     resp =requests.put(BASE_URL+END_POINT+str(id)+'/',data=json.dumps(new_emp))
#     print(resp.json())
#     print(resp.status_code)
# update_source(5)

def delete_source(id):
    BASE_URL = "http://127.0.0.1:8000/"
    END_POINT = 'api/'
    resp =requests.delete(BASE_URL+END_POINT+str(id)+'/')
    print(resp.json())
    print(resp.status_code)
delete_source(50)