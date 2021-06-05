from django.shortcuts import render
from testapp.models import Student
from testapp.forms import StudentForm,SForm
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponse

def student_view(request):
    students = Student.objects.filter()
    return render(request,'testapp/results.html',{'students':students})

def student_register(request):
    if request.method == 'POST':
        form = SForm(request.POST or None)
        if form.is_valid():

            srollno= form.cleaned_data['rollno']
            sname = form.cleaned_data['name']
            sdob = form.cleaned_data['dob']
            smarks = form.cleaned_data['marks']
            sphone_number= form.cleaned_data['phone_number']
            saddress = form.cleaned_data['address']
            p = Student(rollno=srollno,name=sname,dob=sdob,marks=smarks,phone_number=sphone_number,address=saddress)
            p.save()
            messages.success(request, f'Details created successfully for the user {sname}! ')


    else:
        form= StudentForm()
    return render(request,'testapp/register.html',{'form':form})

def student_search(request):
    form =SForm(request.POST or None)
    if form.is_valid():
        sname=form.cleaned_data['name']
        students = Student.objects.filter(name=sname)
        return render(request,'testapp/results.html',{'students':students})
    else:
        form=SForm()
        return render(request,'testapp/search.html',{'form':form})
