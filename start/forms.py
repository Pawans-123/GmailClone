from django.core import validators
from django import forms
from .models import User
from .models import Register
from .models import Question
from .models import Copmail

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['username','first_name','last_name', 'email', 'password', 'confirm_password']



class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['aadhar','whatsapp','aadharfront','aadharback', 'email', 'picture', 'address','schoolname','marital','date_of_birth','college_name','pincode','father_name','mother_name','sibling','friend_name','animal_name','eat','profile_name']


class ComposeForm(forms.ModelForm):
    class Meta:
        model = Copmail
        fields = ['email','subject','message','file_field']
