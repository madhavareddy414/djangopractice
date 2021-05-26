from django.shortcuts import render
from django.views import View
from django.views.generic import UpdateView,DetailView,CreateView,ListView

from django.http import HttpResponse
from register.forms import StudentForm, SForm, EmpForm
from register.models import Student, Employee



def home(request):
    return render(request ,'register/index.html')
class Studentslist(View):
    def get(self,request):
        form = StudentForm()
        context = {'form':form}
        return render(request,'register/stud_list.html',context)

    def post(self,request):
        form = StudentForm(request.POST or None)
        context = {'form':form}
        if form.is_valid():
            name = form.cleaned_data['sname']
            email = form.cleaned_data['semail']
            dep = form.cleaned_data['sdep']
            sch = form.cleaned_data['ssch']
            q = Student(sname=name,semail=email,sdep=dep,ssch=sch)
            q.save()
        return render(request,'register/stud_reg.html',context)

class StudentRegister(CreateView):
    model = Student
    fields = '__all__'
    template_name = 'register/stud_reg.html'
    success_url = "/"


class StudentUpdateView(UpdateView):
    model = Student
    fields = '__all__'
    template_name = 'register/student_update.html'
    success_url = "/"


#---------------------------------------------------

def stud_register(request):
    title = 'Student Registration'
    form = StudentForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['sname']
        email = form.cleaned_data['semail']
        mob = form.cleaned_data['smob']
        sch = form.cleaned_data['ssch']
        res = Student.objects.filter(sname=name)
        if len(res)>0:
            return render(request, 'register/ack.html', {'title': 'Student details already exists'})
        else:
            p = Student(sname=name,semai=email,smob=mob,ssch=sch)
            p.save()
            return render(request,'register/ack.html',{'title':'Registered Successfully'})
    my_dict = {
        'title':title,
        'form':form
    }
    return render(request,'register/stud_reg.html',context=my_dict)

def stud_update(request):
    title = 'Student Update'
    form = StudentForm(request.POST)

    my_dict = {
        'title': title,
        'form': form
    }
    return render(request, 'register/select.html', context=my_dict)


def stud_delete(request):
    title='Student Delete'
    form = SForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['sname']
        list = Student.objects.filter(sname=name)
        if len(list)==0:
            return render(request,'register/ack.html',{'title':'Student details not found please enter correct details'})
        else:
            list= Student.objects.filter(sname=name).delete()
            return render(request,'register/ack.html',{'title':'Student deleted successfully'})
    context ={
        'title':title,
        'form':form
    }
    return render(request,'register/delete.html',context)


def stud_all(request):
    title ='Registered Students'
    list = Student.objects.all()
    context = {
        'title':title,
        'list':list
    }
    return render(request,'register/stud_list.html',context)




def stud_search(request):
    title = 'Search Student'
    form = SForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['sname']
        list=Student.objects.filter(sname=name)
        if len(list)==0:
            return render(request,'register/ack.html',{'title':'Student details not found try another'})
        my_dict={
            'title':title,
            'list':list
        }
        return render(request,'register/stud_list.html',my_dict)
    my_dict = {
        'title': title,
        'form': form
    }
    return render(request,'register/search.html',my_dict)



class StudentUpdateView(UpdateView):
    model = Student
    fields = [
        "sname","saddr","sdep","ssch"
    ]
    template_name = 'register/student_update.html'
    success_url = "/stud-all"


class StudDetailView(DetailView):
    model = Student
    template_name = 'register/stud_detail.html'

# def empregister(request):
#     title = 'Employee Registration'
#     form = EmpForm(request.POST or None)
#     if form.is_valid():
#         no = form.cleaned_data['eno']
#         name = form.cleaned_data['ename']
#         sal = form.cleaned_data['esal']
#         addr = form.cleaned_data['eaddr']
#         q = Employee(eno =no,ename=name,esal=sal,eaddr=addr)
#         q.save()
#         context = {
#             'title':title,
#             'form':form
#         }
#     return render(request,'register/emp_reg.html',context)

def empdelete(request):
    title ='emp registrtion'
    form = EmpForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['ename']
        res = Employee.objects.filter(ename=name)
        if len(res)>0:
            return render(request,'reg/ack.html',{'title':'emp not foud'})
        else:
            Employee.objects.filter(ename=name).delete()
            return render(request,'reg/ack.html',{'title':'deleted'})
    context= {
        'title':title,
        'form':form
    }
    return render(request,'reg/search',context)


class StudDetailView(DetailView):
    model = Student
    template_name = 'register/stud_detail.html'
    success_url = '/'


class StudListView(ListView):    # we have to loop through object_list in template
    model = Student
    template_name = 'register/stud_list.html'
    success_url = '/'


