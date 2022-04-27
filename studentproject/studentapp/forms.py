from django import forms
from studentapp.models import Student

class Register(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
