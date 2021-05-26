from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return render(request,'login/login.html')

def loginhandler(request):
    return HttpResponse(f'Hi,name successfully logged in')