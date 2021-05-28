from django import forms
from testapp.models import Empdata

class EmployeeForm(forms.ModelForm):
    def clean_esal(self):
        inpu_sal = self.cleaned_data['esal']
        if inpu_sal <5000:
            raise forms.ValidationError('the min sal should greater than 5000')
        return inpu_sal
    class Meta:
        model = Empdata
        fields = "__all__"