from django.shortcuts import render
from . import forms
# Create your views here.

# this file is responsible to send the form to the template html file
def studentinputview(request):
    form = forms.StudentForm()
    my_dict = {'formobj':form}
    return render(request,'formTest/input.html', context=my_dict)

