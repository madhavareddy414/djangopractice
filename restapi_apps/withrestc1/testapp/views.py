import io

from rest_framework.renderers import JSONRenderer

from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from django.views.generic import View
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt,name='dispatch')
class EmployeeCRUDCBV(View):
    def get(self,request,*args,**kwargs):
        json_data = request.body
        stream= io.BytesIO(json_data)
        p_data = JSONParser().parse(stream)
        id = p_data.get('id',None)
        if id is not None:
            emp = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(emp)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        qs= Employee.objects.all()
        serializer= EmployeeSerializer(qs,many=True)
        json_data= JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')

    def post(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        p_data = JSONParser().parse(stream)
        serializer= EmployeeSerializer(data=p_data)
        if serializer.is_valid():
            serializer.save()
            msg = {'resource created successfully'}
            json_data= JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,'application/json')

    def put(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        p_data = JSONParser().parse(stream)
        id = p_data.get('id')
        emp = Employee.objects.get(id=id)
        serializer= EmployeeSerializer(emp,data=p_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            msg = {'resource updated successfully'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, 'application/json')

    def delete(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        p_data = JSONParser().parse(stream)
        id = p_data.get('id')
        emp = Employee.objects.get(id=id)
        emp.delete()
        msg = {'resource deleted successfully'}
        json_data = JSONRenderer().render(msg)
        print('')
        return HttpResponse(json_data, content_type='application/json')



