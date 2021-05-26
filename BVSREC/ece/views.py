from django.shortcuts import render
from ece.forms import StudentForm, SForm, FacultyForm,SubForm
from ece.models import Student, Faculty,Subjects
from ece.serializer import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


def Home(request):
    return render(request,'ece/home.html')

def contact(request):
    return render(request,'ece/contact.html')

def register(request):
    title = "Student Registration"
    form =StudentForm(request.POST or None)
    if form.is_valid():
        name =form.cleaned_data['sname']
        dep = form.cleaned_data['sdep']
        rno= form.cleaned_data['srno']
        mail = form.cleaned_data['semail']
        mob = form.cleaned_data['smob']

        p = Student(sname=name,sdep=dep,srno=rno,semail=mail,smob=mob)
        p.save()
        return render(request,'ece/ack.html',{'title':'Registered Successfully'})
    context= {
        'title':title,
        'form':form
    }
    return render(request,'ece/register.html',context)
@api_view(['POST'])
def studentUpdateView(request,pk):
    detail = Student.objects.get(id=pk)
    serializer = StudentSerializer(instance=Student,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


def totalstudents(request):
    title="List of Students"
    queryset = Student.objects.all()
    context = {
        'title':title,
        'queryset':queryset
    }
    return render(request,'ece/list.html',context)

def search(request):
    title = "Search Student"
    form = SForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['sname']
        queryset = Student.objects.filter(sname=name)
        if len(queryset)==0:
            return render(request,'ece/ack.html',{'title':"Student details not found Please enter correct details"})

        context={
                    'title':title,
                    'queryset':queryset
        }
        return render(request,'ece/list.html',context)
    context ={
        'ttile':title,
        'form':form
    }
    return render(request,'ece/search.html',context)

def delete(request):
    title="Delete Student"
    form = SForm(request.POST or None)
    if form.is_valid():
        name= form.cleaned_data['sname']
        querset = Student.objects.filter(sname=name)
        if len(querset)==0:
            return render(request,'ece/ack.html',{'title':'Student details not found Please enter correct date'})
        else:
            querset= Student.objects.filter(sname=name).delete()
            return render(request,'ece/ack.html',{'title':'Student deleted Sccessfully'})
    context={
        'title':title,
        'form':form
    }
    return render(request,'ece/search.html',context)



def fregister(request):
    title = "Faculty Registration"
    form =FacultyForm(request.POST or None)
    if form.is_valid():
        name =form.cleaned_data['fname']
        dep = form.cleaned_data['fdep']
        sal= form.cleaned_data['fsal']

        p = Faculty(fname=name,fdep=dep,fsal=sal)
        p.save()
        return render(request,'ece/ack.html',{'title':'Registered Successfully'})
    context= {
        'title':title,
        'form':form
    }
    return render(request,'ece/fregister.html',context)
def totalfac(request):
    title="List of Faculty"
    queryset = Faculty.objects.all()
    context = {
        'title':title,
        'queryset':queryset
    }
    return render(request,'ece/flist.html',context)


def marks(request):
    title ='Marks Entry'
    form = SubForm(request.POST)
    if request.method=='POST':
        if form.is_valid():
            tmarks = form.cleaned_data['telugu']
            hmarks = form.cleaned_data['hindi']
            emarks = form.cleaned_data['english']
            mmarks = form.cleaned_data['maths']
            smarks = form.cleaned_data['science']
            socmarks = form.cleaned_data['social']

            p = Subjects(telugu=tmarks,hindi=hmarks,english=emarks,maths=mmarks,science=smarks,social=socmarks)
            p.save()
            return render(request,'ece/ack.html',{'title':'Marks Entry Successful'})
    context = {
        'title':title,
        'form':form
    }
    return render(request,'ece/marks.html',context)