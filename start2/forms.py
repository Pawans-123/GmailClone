from django import forms
from django.contrib.auth.models import User
from . import models

class IssueBookForm(forms.Form):
    
    name2 = forms.ModelChoiceField(queryset=models.Student.objects.all(), empty_label="Name [Branch] [Class] [Roll No]", to_field_name="user", label="Student Details")
    
   
    name2.widget.attrs.update({'class':'form-control'})
