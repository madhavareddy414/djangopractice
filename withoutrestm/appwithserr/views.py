from appwithserr.models import Emp
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from appwithserr.serializer import EmpSer


class EmpView(APIView):
    def get(self,request):
        emps = Emp.objects.all()
        serializer = EmpSer(emps,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = EmpSer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data added into database successfully'})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class EmpDetView(APIView):
    def get(self,request,pk):
        emp = Emp.objects.get(eno=pk)
        serializer = EmpSer(emp)
        return Response(serializer.data)

    def put(self, request, pk):
        emps = Emp.objects.get(eno=pk)
        serializer = EmpSer(emps, data=request.data)
        if serializer.is_valid():

            serializer.save()
            return Response({'msg': 'data updated successfully'})
        else:
            return Response({'msg': 'data not updated successfully'})
    def delete(self,request,pk):
        emp = Emp.objects.get(eno=pk)
        emp.delete()
        return Response({'msg':'deleted scuccessfully'})