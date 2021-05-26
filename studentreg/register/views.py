from django.shortcuts import render
from django.views.generic import CreateView
from register.models import Student
from register.forms import StudentForm, SForm


def home(request):
    return render(request,'register/home.html')

class StudentReg(CreateView):
    model = Student
    template_name = 'register/stud_reg.html'
    fields = '__all__'

def studentReg(request):
    form = StudentForm(request.POST or None)
    title = 'Registration'
    if form.is_valid():
        name = form.cleaned_data['sname']
        email = form.cleaned_data['semail']
        mob = form.cleaned_data['smob']
        addr = form.cleaned_data['sadd']
        p = Student(sname=name,semail=email,smob=mob,sadd=addr)
        p.save()
        return render(request,'register/ack.html',{'title':'Registered successfully'})
    context = {
        'form':form,
        'title':title
    }
    return render(request,'register/stud_reg.html',context)

def studall(request):
    title = 'All Students'
    res = Student.objects.all()
    context = {
        'title':title,
        'res':res
    }
    return render(request,'register/stud_all.html',context)

def delete(request):
    title = 'Delete Student'
    form = SForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['sname']
        Student.objects.filter(sname=name).delete
        return render(request,'register/ack.html',{'title':'Deleted successfully'})
    context = {
        'title':title,
        'form':form
    }
    return render(request,'register/stud_search.html',context)

def search(request):
    title = 'Student search'
    form = SForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['sname']
        res = Student.objects.filter(sname=name)
        return render(request, 'register/stud_all.html', {'title': title, 'res':res})
    return render(request,'register/stud_delete.html',{'title':title,'form':form})

