from django.http import HttpResponse
from django.views.generic import View
from .models import Employee
from testapp.mixins import SerializeMixin
import json
from testapp.mixins import HttpResponseMixins

class EmployeedetailCBV(SerializeMixin,HttpResponseMixins,View):
    def get(self, request, id, *args, **kwargs):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            json_data = json.dumps({'message':'The requested data not available'})
            return self.render_to_http_response(json_data,status=404)
        else:
            json_data = self.serialize([emp])
        return self.render_to_http_response(json_data)

class EmployeeListCBV(SerializeMixin,HttpResponseMixins,View):
    def get(self, request, *args, **kwargs):
        qs = Employee.objects.all()
        json_data =self.serialize(qs)
        return self.render_to_http_response(json_data,status=200)