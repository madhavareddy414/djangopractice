from django.shortcuts import render
from django.http import HttpResponse

def emp_data_view(request):
    emp_data = {
        'eno':5000,
        'ename':'rao',
        'esal':50000,
        'eaddr':'bglr'


}
    response = f' <h1>Emp No : {emp_data["eno"]} <br>Emp name:{emp_data["ename"]} <br>Emp sal: {emp_data["esal"]} <br>Emp addr:{emp_data["eaddr"]}</h1>'
    return HttpResponse(response)# shouel dobule quote "eno"

import json
def emp_data_json_view(request):
    emp_data = {
        'eno': 5000,
        'ename': 'rao',
        'esal': 50000,
        'eaddr': 'bglr'

    }

    json_data = json.dumps(emp_data)
    return HttpResponse(json_data,content_type='application/json')  #

from django.http import JsonResponse
from django.views.generic import View
def emp_data_json_view2(request):
    emp_data = {
        'eno': 5000,
        'ename': 'rao',
        'esal': 50000,
        'eaddr': 'bglr'

    }


    return JsonResponse(emp_data,content_type='application/json')

from testing.mixins import HttpResponseMixins
class JsonCBV(HttpResponseMixins,View):
    def get(self,request,*args,**kwargs):
        json_data = json.dumps({'message':'this is get method' })
        return self.render_to_HttpRespnose(json_data)

    def post(self,request,*args,**kwargs):
        json_data = json.dumps({'message':'this is post method' })
        return self.render_to_HttpRespnose(json_data)

    def put(self,request,*args,**kwargs):
        json_data = json.dumps({'message':'this is put method' })
        return self.render_to_HttpRespnose(json_data)

    def delete(self,request,*args,**kwargs):
        json_data = json.dumps({'message':'this is delete method' })
        return self.render_to_HttpRespnose(json_data)