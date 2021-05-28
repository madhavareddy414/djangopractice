from django.shortcuts import render
from django.views.generic import View
from testapp.models import Empdata
from django.core.serializers import serialize
from django.http import HttpResponse
from testapp.mixins import MixinSerialize,HttpResponseMixin
import json
from django.utils.decorators import  method_decorator
from django.views.decorators.csrf import csrf_exempt
from testapp.forms import EmployeeForm
from testapp.utils import is_json

@method_decorator(csrf_exempt,name='dispatch')
class EmpDetailView(MixinSerialize,View,HttpResponseMixin):

    def get_obj_by_id(self,id):
        try:
            emp = Empdata.objects.get(id=id)
        except Empdata.DoesNotExist:
            emp= None
        return emp

    def put(self,request,id,*args,**kwargs):
        emp = self.get_obj_by_id(id)
        if emp is None:
            json_data = json.dumps({'msg':'No match found '})
            return self.render_to_http_respnose(json_data,status=404)
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps('not a valid json data')
            return self.render_to_http_respnose(json_data,status=404)
        provided_data = json.loads(data)
        original_data={
            'eno':emp.eno,
            'ename':emp.ename,
            'esal':emp.esal,
            'eaddr':emp.eaddr
        }
        original_data.update(provided_data)
        form = EmployeeForm(original_data,instance=emp)
        if form.is_valid:
            form.save()
            json_data = json.dumps({'msg':'updated successfull'})
            return self.render_to_http_respnose(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_respnose(json_data,status=400)

    def delete(self,request,id,*args,**kwargs):
        emp = self.get_obj_by_id(id)
        if emp is None:
            json_data = json.dumps({'msg': 'No match found for deletion '})
            return self.render_to_http_respnose(json_data, status=404)
        status,deleted_item = emp.delete()
        if status == 1:
            json_data = json.dumps({'msg':'deleted successfully'})
            return self.render_to_http_respnose(json_data)
        else:
            json_data = json.dumps({'msg': 'unable to delete try later'})
            return self.render_to_http_respnose(json_data)






    def get(self,request,id,*args,**kwargs):
        try:
            emp = Empdata.objects.get(id=id)
        except Empdata.DoesNotExist:
            json_data = json.dumps({'msg':'Emp details does not exit'})
            return self.render_to_http_respnose(json_data, status=400)
        else:

            json_data = self.serialize1([emp])
        return self.render_to_http_respnose(json_data)

from testapp.forms import EmployeeForm
from testapp.utils import is_json
@method_decorator(csrf_exempt,name='dispatch')
class EmpListView(MixinSerialize,View,HttpResponseMixin):
    def get(self,request,*args,**kwargs):
        qs = Empdata.objects.all()
        json_data = self.serialize1(qs)
        return HttpResponse(json_data,content_type='application/json')
    def post(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'send valid json only'})
            return self.render_to_http_respnose(json_data,status=404)
        empdata = json.loads(data)
        form = EmployeeForm(empdata)
        if form.is_valid():
            form.save()
            json_data = json.dumps({'msg':'data added successfully'})

            return self.render_to_http_respnose(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_respnose(json_data,status=404)

