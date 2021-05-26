from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello(request):
    return render(request, 'login/login.html')


def loginHandler(request):
    name = request.POST['uname']
    password = request.POST['psw']
    return HttpResponse(f"Hi {name}, successfully logged in")

def sayHitoUser(request,age=0):
    return HttpResponse(f"done1 {age}")

def sayHitoUser1(request):
    return HttpResponse("done2")
