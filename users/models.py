from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils import timezone
from .managers import CustomUserManager
# from bson import ObjectId

# Create your models here.

class User(AbstractBaseUser,PermissionsMixin):
    # TypeError: Field 'id' expected a number but got ObjectId('654a83ed0ea0e8e7c086b4cb')" typically occurs when you're trying to use a non-integer value for the 'id' field, which is expected to be an integer by default in Django models.


    id = models.CharField(primary_key=True, editable=False, unique=True,max_length=100)
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True,blank=False,null=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS =['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email


