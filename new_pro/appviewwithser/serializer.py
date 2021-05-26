from rest_framework import serializers
from modelApp.models import Employee


class EmpSer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("__all__")