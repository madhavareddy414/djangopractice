from django import forms

class StudentForm(forms.Form):
    rollno = forms.IntegerField()
    name = forms.CharField(max_length=64)
    dob = forms.IntegerField(required=False)
    marks = forms.IntegerField()
    email = forms.EmailField()
    phone_number = forms.IntegerField()
    address = forms.CharField(max_length=64)

class SForm(forms.Form):
    name = forms.CharField(max_length=64)