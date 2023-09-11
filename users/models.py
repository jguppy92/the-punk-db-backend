from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("An email is required.")
        if not password:
            raise ValueError("A password is required.")
        if not username:
            raise ValueError("A username is required.")
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, username, password=None):
        if not email:
            raise ValueError("An email is required.")
        if not password:
            raise ValueError("A password is required.")
        user = self.create_user(email, username, password)
        user.is_superuser = True
        user.save()
        return user

class ExtendUser(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True,blank=False,max_length=500,verbose_name="email")
    username= models.CharField(unique=True,blank=False,max_length=50)
    country = models.CharField(max_length=200, blank=True)

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    objects = UserManager()
    def __str__(self):
        return str(self.username)
