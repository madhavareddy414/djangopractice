from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from modelApp.models import Employee as Emp
from .serializer import EmpSer
from rest_framework import status


class EmpView(APIView):
    def get(self,request):
        x = []
        emps = Emp.objects.all()
        serializer = EmpSer(emps,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = EmpSer(data=request.data)
        if serializer. is_valid():
            serializer.save()
            return Response({'message':'new object added to database'})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class EmpDet(APIView):
    def get(self,request,pk):
        emp = Emp.objects.get(eno=pk)
        serializer = EmpSer(emp)
        return Response(serializer.data)
    def put(self,request,pk):
        emp = Emp.objects.get(eno=pk)
        serializer = EmpSer(emp,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'record updated successfully'})
        else:
            return Response({'message':'record not updated successfully'})

    def delte(self,request,pk):
        emp = Emp.objects.get(eno=pk)
        emp.delete()
       # serializer = EmpSer(emp,data=request.data)
        return Response({'message':'record deleted successfully'})


