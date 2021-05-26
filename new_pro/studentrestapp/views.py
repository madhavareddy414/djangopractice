from django.shortcuts import render

from django.http import JsonResponse
from studentrestapp.models import Student

def studentList(request):
    s = Student.objects.all()
    data = {"results":"data"}
    return JsonResponse(data)