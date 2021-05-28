import requests
import json
import time

BASE_URL = "http://127.0.0.1:8000/"
END_POINT="api/"
# def get_resource(id=None):
#
#     data = {}
#     if id is not None:
#        data = {
#            'id':id
#        }
#     resp = requests.get(BASE_URL+END_POINT,data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
#
# get_resource()
# time.sleep(5)
# print('creating resource')
#
# def create_resource():
#     data = {
#         'eno':900,
#         'ename':'radhika',
#         'esal':40000,
#         'eaddr':'bglr'
#     }
#     resp = requests.post(BASE_URL+END_POINT,data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
# create_resource()
#
# time.sleep(10)
# print('updating resource')

def update_resource(id):

    data = {
        'id':id,
        'ename':'Madhusudana reddy',
        'esal':5002
    }
    resp = requests.put(BASE_URL+END_POINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())
update_resource(2)

# time.sleep(15)
# print('deleting recored')
#
# def delete_resource(id):
#     data = {
#         'id':id,
#     }
#     resp = requests.delete(BASE_URL+END_POINT,data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
#
# delete_resource(1)