from django.shortcuts import render

from testapp.models import Employee

def emp_list(request):
    emps=Employee.objects.all()
    return render(request,'testapp/results.html',{'emps':emps})