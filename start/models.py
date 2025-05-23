from django.db import models

from django.contrib.auth.models import User

class Register(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)  
    confirm_password = models.CharField(max_length=50)
    

class Question(models.Model):
    aadhar = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=100)
    aadharfront=models.FileField( upload_to='media', blank=True)
    aadharback=models.FileField( upload_to='media', blank=True)
    email = models.EmailField(max_length=254)
    picture=models.ImageField( upload_to='media', blank=True)
    address = models.CharField(max_length=100)
    schoolname = models.CharField(max_length=100)
    marital = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    college_name = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    sibling = models.CharField(max_length=100)
    friend_name = models.CharField(max_length=100)
    animal_name = models.CharField(max_length=100)
    eat = models.CharField(max_length=100)
    profilename = models.CharField(max_length=100)




class Profile(models.Model):
      user = models.OneToOneField(User,on_delete=models.CASCADE)
      forget_password_token = models.CharField(max_length=100)
      is_verified = models.BooleanField(default=False)
      create_at=models.DateTimeField(auto_now_add=True)
     



   

class Copmail(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    file_field = models.FileField(upload_to='media', blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.subject




def delete(self, *args, **kwargs):
        # Move data to the TrashCopmail before deleting
        TrashCopmail.objects.create(
            original_id=self.id,
            email=self.email,
            subject=self.subject,
            message=self.message,
            file_field=self.file_field,
        )
        super(Copmail, self).delete(*args, **kwargs)

def __str__(self):
        return self.subject


class TrashCopmail(models.Model):
    original_id = models.IntegerField()
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    file_field = models.FileField(upload_to='media', blank=True)
    deleted_at = models.DateTimeField(auto_now_add=True)
    # original = models.ForeignKey(Copmail, on_delete=models.CASCADE)

    # def restore(self):
    #     Copmail.objects.create(
    #         id=self.original_id,
    #         email=self.email,
    #         subject=self.subject,
    #         message=self.message,
    #         file_field=self.file_field,
    #     )
    #     self.delete()

def __str__(self):
        return f"TrashCopmail: {self.subject}"



class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    classroom = models.CharField(max_length=10)
    branch = models.CharField(max_length=10)
    roll_no = models.CharField(max_length=3, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    image = models.ImageField(upload_to="", blank=True)

    def __str__(self):
        return str(self.user) + " ["+str(self.branch)+']' + " ["+str(self.classroom)+']' + " ["+str(self.roll_no)+']'








