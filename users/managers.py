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
    
    def create_superuser(self,username, email, password=None, **extra_fields):
        user = self.create_user(
            username,
            email,
            password,
            **extra_fields,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user