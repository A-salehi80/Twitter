from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin,AbstractBaseUser
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin, models.Model):
    phone =models.CharField(max_length=20, unique=True)
    email=models.EmailField(unique=True)
    is_active = models.BooleanField(default=True, verbose_name="Active")
    is_staff = models.BooleanField(default=False, verbose_name="Staff Member")
    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["email"]
    objects = UserManager()
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField()
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"


