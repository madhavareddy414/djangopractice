from django.shortcuts import render
from . import forms

def studentinputview(request):
    form = forms.StudentForm()
    my_dict = {'formobj':form}
    return  render(request, 'formTest/input.html', context=my_dict)
