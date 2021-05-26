

def home(request):
    return HttpResponse('welcome to page')
def emp_data_view(request):
    emp_data = {
        'eno':5000,
        'ename':'rao',
        'esal':50000,
        'eaddr':'bglr'
    }
    # response = '<h1>Employee no:{}<br>Employee name:{}<br>Employee salary:{}<br>Employee address:{}'.format(emp_data['eno'],emp_data['ename'],emp_data['eaddr'],emp_data['esal'])
    # return HttpResponse(response)
    response = f'Emp No : {emp_data["eno"]} </br>Emp name:{emp_data["ename"]}<br> Emp sal: {emp_data["esal"]} <br>Emp addr:{emp_data["eaddr"]}'
    return HttpResponse(response)


import json
def emp_data_jsonview(request):
    emp_data = {
        'eno':5000,
        'ename':'rao',
        'esal':50000,
        'eaddr':'bglr'
    }
    json_data = json.dumps(emp_data)
    response = '<h1>Employee no:{}<br>Employee name:{}<br>Employee salary:{}<br>Employee address:{}'.format(emp_data['eno'],emp_data['ename'],emp_data['eaddr'],emp_data['esal'])
    return HttpResponse(json_data,content_type='application/json')

from django.http import JsonResponse, HttpResponse


def emp_data_jsonview2(request):
    emp_data = {
        'eno':5000,
        'ename':'rao',
        'esal':50000,
        'eaddr':'bglr'
    }
    return JsonResponse(emp_data)

from django.views.generic import View

class JsonCBV(View):
    def get(self,request,*args,**kwargs):
        json_data = json.dumps({'msg': 'this is get method'})
        return HttpResponse(json_data, content_type='application/json')


    def post(self,request,*args,**kwargs):
            json_data = json.dumps({'msg':'this is post method'})
            return HttpResponse(json_data,content_type='application/json')

    def put(self,request,*args,**kwargs):
        json_data = json.dumps({'msg': 'this is put method'})
        return HttpResponse(json_data, content_type='application/json')


    def delete(self,request,*args,**kwargs):
        json_data = json.dumps({'msg': 'this is delete method'})
        return HttpResponse(json_data, content_type='application/json')
