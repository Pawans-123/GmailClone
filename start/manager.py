# from django.contrib.auth.base_user import BaseUserManager


# class UserManager(BaseUserManager):

#     def create_user(self, first_name , password = None, **extra_fields):
#         if not first_name:
#             raise ValueError("First Name Is required")
#         extra_fields['email'] = self.normalize_email (extra_fields['email'])

#         user=self.model(first_name = first_name, **extra_fields) 

#         user.set_password(password)
#         user.save(using = self.db)

#         return user
    
#     def create_superuser(self, first_name , password = None, **extra_fields):
#         extra_fields.setdefault('is_staff' , True)
#         extra_fields.setdefault('is_superuser' , True)
#         extra_fields.setdefault('is_active' , True)

#         return self.create_user(first_name , password , **extra_fields) 
