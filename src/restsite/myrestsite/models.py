from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):
    """helps custom user model"""
    def create_user(self,name,email,password=None):
        if not email:
            raise ValueError('User must have email address')
        email=self.normalize_email(email)
        user=self.model(email=email,name=name)

        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self,name,email,password):
        user=self.create_user(name,email,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self.db)
        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """reprsents user profile"""
    email=models.EmailField(max_length=200,unique=True)
    name=models.CharField(max_length=200)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserProfileManager()
    
    USERNAME_FIELD='email'

    REQUIRED_FIELDS=['name']

    #helper fucnctions

    def get_full_name(self):
        """use to get user fullname"""
        return self.name
    def get_short_name(self):
        """used to get user short name"""
        return self.name

    def __str__(self):
        return self.email
