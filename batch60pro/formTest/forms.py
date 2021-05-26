from django import forms
class StudentForm(forms.Form):
    name = forms.CharField()
    marks = forms.IntegerField(max_value=100)








    # name and marks are the field names which will be avaiable in html form