from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomerUserManager(BaseUserManager):
    def create_user(self,email, password=None, **extra_fields):
        if not email:
            raise ValueError('the email field must be set')
        email = self.normalize_email(email)
        user = self.model(email = email , **extra_fields)
        user.set_password(password)
        user.save(using= self._db)
        
        return user 
    def create_superuser(self , email ,password=None , **extra_fields ):
        extra_fields.setdefault('is_staff' , True  )
        extra_fields.setdefault('is_superuser' , True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError("super user must have ")
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)
class CustomUser(AbstractBaseUser , PermissionsMixin):
    ROLE_CHOICES =  [
        ('learner' ,'Learner' ),
        ('tutor' ,'Tutor' ),
        ('admin' ,'Admin' ),
    ]
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10 ,  choices=ROLE_CHOICES , default='learner' )
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20 )
    country = models.CharField(max_length=100 ,blank=True , null = True )
    # Make email the username field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Other fields required for superuser creation

    objects = CustomerUserManager()  # Ensure email is unique    
    def __str__(self):
        return self.email 
    