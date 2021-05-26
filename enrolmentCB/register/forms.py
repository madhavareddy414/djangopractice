from django import forms

from register.models import Student


class StudentForm(forms.Form):

    sname = forms.CharField(label='Name',widget=forms.TextInput(attrs={'class': 'form-control','style': 'width:170px','placeholder':'Enter your Name'},))
    semail = forms.CharField(label='Email.:',widget=forms.TextInput(attrs={'class': 'special','style': 'width:180px','placeholder':'Enter your email'}))
    smob = forms.CharField(label='Mob.:',widget=forms.TextInput(attrs={'class': 'special','style': 'width:180px','placeholder':'Enter your Department'}),)
    ssch = forms.CharField(label='Sch.:',widget=forms.TextInput(attrs={'class': 'special','style': 'width:180px','placeholder':'Enter your School Name'}))

class SForm(forms.Form):
    sname = forms.CharField(max_length=30,label='Nmae' )

# class StudentsForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = ('sname','saddr','sdep','ssch')
#         widgets = {
#             'sname':forms.TextInput(attrs={'place holder':'please enter','class': 'special','style': 'width:10px'}),
#             'saddr': forms.TextInput(attrs={'class': 'form-control'}),
#             'sdep': forms.TextInput(attrs={'class': 'form-control'}),
#             'ssch': forms.TextInput(attrs={'class': 'form-control'}),
#         }

class EmpForm(forms.Form):
    eno = forms.IntegerField()
    ename = forms.CharField(max_length=30)
    esal = forms.FloatField()
    eaddr = forms.CharField(max_length=30)
