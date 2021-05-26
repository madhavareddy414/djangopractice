from django import forms

class StudentForm(forms.Form):
    # class Meta:
    #     model = Student
    #     fields = "__all__"
    sname = forms.CharField(max_length=30,required=True,label='Student Name')
    sdep = forms.CharField(max_length=30,required=True,label='Dep')
    srno= forms.CharField(max_length=30,required=True,label='Roll No')
    semail = forms.EmailField(max_length=30,required=True,label='Email')
    smob = forms.IntegerField(required=True,label='Mob No')
class SForm(forms.Form):

    sname = forms.CharField(max_length=30,label='Student Nmae' )
d
class FacultyForm(forms.Form):

    fname = forms.CharField(max_length=30,required=True,label='Faculty Name')
    fdep= forms.CharField(max_length=30,required=True,label='Dep')
    fsal= forms.IntegerField(required=True,label='Salary')

    def __str__(self):
        return self.fname

class FForm(forms.Form):

    fname = forms.CharField(max_length=30,label='Faculty Nmae' )

class SubForm(forms.Form):
    telugu=forms.IntegerField(required=True,max_value=100)
    hindi = forms.IntegerField(required=True,max_value=100)
    english = forms.IntegerField(required=True,max_value=100)
    maths = forms.IntegerField(required=True,max_value=100)
    science = forms.IntegerField(required=True,max_value=100)
    social = forms.IntegerField(required=True,max_value=100)
