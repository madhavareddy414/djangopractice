from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from login.models import Labour
from login.forms import LabourForm

def login1(requet):
    return HttpResponse('welcome to login page')

def login2(request):
    form = LabourForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['lname']
        addr = form.cleaned_data['address']
        p = Labour(lname=name,address=addr)
        p.save()
        messages.success(request, f' {name} Registered successfully')

    context = {
        'form':form
    }
    return render(request,'labour_form.html',context)

def labout_list(request):
    list = Labour.objects.all()
    context = {
        'list':list
    }
    return render(request,'labour_list.html',context)

class Login(CreateView):
    model = Labour
    templatename = 'labour_form.html'
    fields = '__all__'
    success_url = '/'