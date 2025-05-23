from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import Register
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Question
from .models import Copmail
from .models import Student
from django.contrib.auth.models import User
from . models import Profile 
import uuid
from django.core.mail import send_mail
from django.contrib.auth.forms import PasswordResetForm
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator,PasswordResetTokenGenerator
from django.core.mail import send_mail
from . helpers import send_forget_password_mail
import random
import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404, redirect




        

def index(request):
    return render(request, "index.html")

def imain(request):
    return render(request, "imain.html")


def details(request):
    if request.method =="POST":
        aadhar = request.POST.get('aadhar', '')
        whatsapp = request.POST.get('whatsapp', '')
        aadharfront = request.FILES.get('aadharfront', '')
        aadharback = request.FILES.get('aadharback', '')
        email = request.POST.get('email', '')
        picture = request.FILES.get('picture', '')
        address = request.POST.get('address', '')
        schoolname = request.POST.get('schoolname', '')
        marital = request.POST.get('marital', '')
        date_of_birth = request.POST.get('date_of_birth', '')
        college_name = request.POST.get('college_name', '')
        pincode = request.POST.get('pincode', '')
        father_name = request.POST.get('father_name', '')
        mother_name = request.POST.get('mother_name', '')
        sibling = request.POST.get('sibling', '')
        friend_name = request.POST.get('friend_name', '')
        animal_name = request.POST.get('animal_name', '')
        eat = request.POST.get('eat', '')
        profilename = request.POST.get('profilename', '')


        data = Question.objects.create(aadhar = aadhar, whatsapp = whatsapp, aadharfront = aadharfront,aadharback=aadharback,email= email, picture= picture,address=address,schoolname=schoolname,marital=marital,date_of_birth=date_of_birth,college_name=college_name,pincode=pincode,father_name=father_name,mother_name=mother_name,sibling=sibling,friend_name=friend_name,animal_name=animal_name,eat=eat,profilename=profilename)

        data.save()
       
        return redirect('pk')
    return render(request, "details.html")




import logging

logger = logging.getLogger(__name__)

def register(request):
    try:
        if request.method == 'POST':
            # Get form data
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            
            # Check if user already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username is taken.")
                return redirect('details')
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email is taken.")
                return redirect('details')
           
            # Check password match
            if password != confirm_password:
                messages.error(request, "Password and confirm password did not match. Please register again.")
                return redirect('register')

            # Create user
            user = User.objects.create(username=username, first_name=first_name, last_name=last_name, email=email)
            user.set_password(password)
            user.save()

            messages.success(request, "Your account has been successfully created.")
            return redirect('details')  # Assuming there's a URL named 'login' defined in your URLs

    except Exception as e:
        logger.error(f"Error in user registration: {e}")
        messages.error(request, "An error occurred during registration. Please try again later.")

    return render(request, 'register.html')


 







# def reset(request):
#     return render(request, "reset.html")


def signin(request):

     # if request.method == 'POST':
     #    username = request.POST['username']
     #    password = request.POST['password']

     #    user = authenticate(request, username=username, password=password)

     #    if user is not None:
     #        login(request, user)
     #        messages.success(request, f'You are logged in as {request.user}')
     #        return redirect('Profile_register')
     #    else:
     #        messages.error(request, 'Please enter a valid username and password')
     #        return redirect('signin')

     #        return render(request, 'signin.html')
    

        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
        

            try:
                user = authenticate(username=username, password=password)
            except:
                user = User.objects.filter(username=username, password=password)
                print(user)
            if user is not None:
                login(request, user)
                messages.success(request, f'You are login as using {request.user}')
                return redirect('Profile_register')
            else:
                messages.error(request, 'Please enter valid email and password')
                return redirect('signin')

        return render(request,'signin.html')



def ChangePassword(request,token):
    context = { }
    try:
        profile = Profile.objects.filter(forget_password_token=token).first()
        context = {'user_id':profile.user.id}

        if request.method =='POST':
            password=request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            user_id = request.POST.get('user_id')
            if user_id is None:
                messages.error(request, 'No user id found')
                print("error")
                return redirect(f'/ChangePassword/{token}/')
           
            if password != confirm_password:
                messages.error(request, 'both password not same')
                print("ok")  
                return redirect(f'/ChangePassword/{token}/')
                 
            user = User.objects.get(id=user_id)
            user.set_password(password)
            user.save()
            return redirect('signin')

           



       



        
    except Exception as e:
        print(e)


    return render(request,'reset2.html',context)


def reset(request):
    try:
        if request.method =='POST':
            username = request.POST.get('username')
            user = User.objects.filter(username=username).first()
            print(user)
            if not user:
                messages.error(request, 'No user found with this username')
                return redirect('reset')
             
                
            # Check if Profile exists for the user, create one if non  t
            profile, created = Profile.objects.get_or_create(user=user)
            
            # Generate token and save to profile
            token = str(uuid.uuid4())
            profile.forget_password_token = token
            profile.save()
            
            # Send email
            send_forget_password_mail(user.email, token)
            messages.success(request, 'An email has been sent to your email address.')
            return redirect('/reset/')
                
    except Exception as e:
        print(e)    
    return render(request,'reset.html')



def net(request):
    return render(request, "net.html")

def emailsent(request):
    dataa = Copmail.objects.all()
    return render(request, "next.html",{'dataa':dataa})

def draft(request):
    return render(request, "draft.html")

# def trash(request):
#     return render(request, "trash.html")

def Cmail(request):
    if request.method == "POST":
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        file_field = request.FILES.get('file_field', '')  # Assuming 'files' is a file input field

        # Check if required fields are not empty
        if email and subject and message:
            # Assuming Compose is a model with fields: email, subject, message, files
            dataa = Copmail.objects.create(email=email, subject=subject, message=message, file_field=file_field)
            dataa.save()
            return redirect('gmail')  # Redirect to some other view after successful submission
        else:
            # Handle the case where required fields are missing
            return render(request, "next.html", {'error': 'Please fill out all required fields'})
    else:
        return render(request, "gmail.html")




def pk(request):
    return render(request, "pk.html")

@login_required
def gk(request):
    return render(request, "gk.html")


def inbox(request):
    return render(request, "inbox.html")


def ttm(request):
    return render(request, "ttm.html")


def propic(request):
    Question = Question.objects.first()
    return render(request, "pk.html", {'Question': Question})




def delete_emailsent(request, myid):
    data = Copmail.objects.filter(id=myid)
    data.delete()
    return redirect("/emailsent")




def gmail(request):
    return render(request, "gmail.html")


def next(request):
    return render(request, "next.html")






def student_registration(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        branch = request.POST['branch']
        classroom = request.POST['classroom']
        roll_no = request.POST['roll_no']
        image = request.FILES['image']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            passnotmatch = True
            return render(request, "student_registration.html", {'passnotmatch':passnotmatch})

        user = User.objects.create_user(username=username, email=email, password=password,first_name=first_name, last_name=last_name)
        student = Student.objects.create(user=user, phone=phone, branch=branch, classroom=classroom,roll_no=roll_no, image=image)
        user.save()
        student.save()
        alert = True
        return render(request, "student_registration.html", {'alert':alert})
    return render(request, "student_registration.html")


@login_required(login_url = '/admin_login')
def view_students(request):
    students = Student.objects.all()
    return render(request, "view_students.html", {'students':students})


def student_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return HttpResponse("You are not a student!!")
            else:
                return redirect("/profile")
        else:
            alert = True
            return render(request, "student_login.html", {'alert':alert})
    return render(request, "student_login.html")


@login_required(login_url = '/student_login')
def profile(request):
    return render(request, "profile.html")



def gmail2(request):
    dataa = Copmail.objects.all()
    return render(request, "gmail2.html",{'dataa':dataa})






# def delete_next(request, myid):
#     data = Copmail.objects.filter(id=myid)
#     data.delete()
#     return redirect("/gmail")


def delete_next(request, myid):
    data = get_object_or_404(Copmail, id=myid)
    data.is_deleted = True
    data.save()
    return redirect("/gmail")




# def trash(request):
#     trashed_items = TrashCopmail.objects.all()
#     return render(request, 'trash.html', {'trashed_items': trashed_items})

# def restore_item(request, pk):
#     item = get_object_or_404(TrashCopmail, pk=pk)
#     item.restore()
#     return redirect('trash')

# def hard_delete_item(request, pk):
#     item = get_object_or_404(TrashCopmail, pk=pk)
#     item.delete()
#     return redirect('trash')


def restore_item(request, myid):
    data = get_object_or_404(Copmail, id=myid, is_deleted=True)
    data.is_deleted = False
    data.save()
    return redirect("/trash")

def hard_delete_item(request, myid):
    data = get_object_or_404(Copmail, id=myid, is_deleted=True)
    data.delete()
    return redirect("/trash")



def trash_view(request):
    trashed_items = Copmail.objects.filter(is_deleted=True)
    return render(request, 'trash.html', {'trashed_items': trashed_items})



def Profile_register(request):
    # user = User.objects.get(user=request.user)
    user = request.user
    print(user.first_name)
    return render(request, "Profile_register.html",{'user':user})




# @login_required
# def Profile_register(request):
#     try:
#         user = User.objects.get(user=request.user)
#         context = {
#             'user': request.user,
#             'user': user
#         }
#         return render(request, 'Profile_register.html', context)
#     except User.DoesNotExist:
#         messages.error(request, 'Profile information is incomplete.')
#         return redirect('Profile_register')




@login_required
def edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    print(pk)
    
    if request.method == 'POST':
        #Updating the User model fields
        user.username = request.POST.get('username')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        
        
        user.username = request.POST.get('username')
        print(user.username)
        
        user.first_name = request.POST.get('first_name')
        print(user.first_name)
        user.last_name = request.POST.get('last_name')
        print(user.last_name)
        # user.dob = request.POST.get('dob')
        # if request.FILES.get('image'):
        #     user.image = request.FILES.get('image')
        # print(user.image)
        user.save()
        
        return redirect('Profile_register')  # Redirect to profile page after successful update

    return render(request, 'edit.html', {'user': user})











