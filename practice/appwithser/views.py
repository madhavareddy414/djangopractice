from appwithser.models import Employee
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from appwithser.serializer import EmpSer


class EmpView(APIView):
    def get(self,request):
        emp = Employee.objects.all()
        serializer = EmpSer(emp,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = EmpSer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data added into database successfully'})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)