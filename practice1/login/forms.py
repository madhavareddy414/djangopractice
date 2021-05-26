from django import forms

class LabourForm(forms.Form):
    lname = forms.CharField(max_length=125)
    address = forms.CharField(max_length=500)