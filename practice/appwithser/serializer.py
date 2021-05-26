from rest_framework import serializers
from appwithser.models import Employee

class EmpSer(serializers.ModelSerializer):
    model = Employee
    fields = '__all__'