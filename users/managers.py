from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self,username,email,password=None,**extra_fields):
        if not username :
            raise ValueError("Users must have a username")
        if not email:
            raise ValueError("Users must have a email")
        
        email = self.normalize_email(email)
        user = self.model(username=username,email=email,**extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user