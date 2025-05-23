from django.contrib import admin
#from .models import User
from .models import Register
from .models import Question
from .models import Profile,Copmail
from .models import Student


class RegisterAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name','last_name', 'email','password', 'confirm_password')
admin.site.register(Register, RegisterAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('aadhar', 'whatsapp','aadharfront','aadharback', 'email','picture', 'address','schoolname','marital','date_of_birth','college_name','pincode','father_name','mother_name','sibling','friend_name','animal_name','eat','profilename')
admin.site.register(Question, QuestionAdmin)


class profileadmin(admin.ModelAdmin):
    list_display=('user', 'forget_password_token','create_at','is_verified')
admin.site.register(Profile,profileadmin)


class Composeadmin(admin.ModelAdmin):
    list_display=('email', 'subject','message','file_field')
admin.site.register(Copmail,Composeadmin)



admin.site.register(Student)
# admin.site.register(TrashCopmail)



