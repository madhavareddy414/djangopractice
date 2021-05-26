from rest_framework import serializers
from appwithserr.models import Emp

class EmpSer(serializers.ModelSerializer):
    class Meta:
        model = Emp
        fields = ('__all__')