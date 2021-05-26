from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse

from sutdentrestapp.models import Student


def studentList(requset):
    # s= Student.objects.all()
    data = { "results": "data"}
    return JsonResponse(data)
