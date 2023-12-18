from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils import timezone
from .managers import CustomUserManager
# from bson import ObjectId

# Create your models here.
class CustomUser(AbstractBaseUser,PermissionsMixin):

    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True,blank=False,null=False)
    date_joined = models.DateTimeField(default=timezone.now)

    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS =['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    


