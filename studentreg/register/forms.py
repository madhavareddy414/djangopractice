from django import forms

class StudentForm(forms.Form):
    sname = forms.CharField(max_length=125)
    semail = forms.EmailField()
    smob = forms.CharField()
    sadd = forms.CharField(max_length=125)

    def __repr__(self):
        return self.sname

class SForm(forms.Form):
    sname = forms.CharField(max_length=125)