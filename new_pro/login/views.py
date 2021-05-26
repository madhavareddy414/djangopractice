from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return render(request,'login/login.html')

def loginhandler(request):
    name = request.POST['uname']
    password = request.POST['psw']
    return HttpResponse(f'hi {name} successfllly loggedin ')

def SayHitoUser(request,age=0):
    return HttpResponse(f'done1 {age}')

def SayHitoUser1(request):
    return HttpResponse('done2')