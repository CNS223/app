import pytz
import random
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.core.validators import ValidationError
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from math import sin, cos, sqrt, atan2, radians
import string
import uuid
from django.utils import timezone

def avatar_path(instance, filename):
    return 'avatar/{}/{}'.format(
        instance.id,
        filename
    )

class UserManager(BaseUserManager):
    def create_user(self, username, password):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not username:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=self.normalize_email(username),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class UserType(models.Model):
    USER_TYPE_CHOICES = (
        ('customer', 'Customer'),
        ('provider', 'Provider')
    )
    user_type = models.CharField(max_length=50, choices=USER_TYPE_CHOICES, default='user', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.get_user_type_display()

class Address(models.Model):
    ADDRESS_TYPE_CHOICES = (
        ('user', 'User'),
        ('serviceprovider', 'ServiceProvider'),
        ('servicebooking', 'ServiceBooking')
    )
    add1 = models.CharField(max_length=255, null=False, blank=False)
    add2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=50, null=False, blank=False)
    address_type = models.CharField(choices=ADDRESS_TYPE_CHOICES, default="user", max_length=50, null=False, blank=False)
    provision = models.CharField(max_length=50, null=False, blank=False)
    country = models.CharField(max_length=50, null=False, blank=False)
    postal_code = models.CharField(max_length=20, null=False, blank=False)
    latitude = models.CharField(max_length=20, null=False, blank=False)
    longitude = models.CharField(max_length=20, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}"



class User(AbstractBaseUser):
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE, null=False, blank=False)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    username = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=30, null=False, blank=False, unique=True)
    phone_number = models.CharField(max_length=20, null=False, blank=False, unique=True)
    password = models.CharField(max_length=128)
    avatar = models.ImageField(upload_to=avatar_path, blank=True, null=True)
    availability = models.FloatField(default=0.0)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    rating = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

class UserAddress(models.Model):
    add1 = models.CharField(max_length=255, null=False, blank=False)
    add2 = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    city = models.CharField(max_length=50, null=False, blank=False)
    provision = models.CharField(max_length=50, null=False, blank=False)
    country = models.CharField(max_length=50, null=False, blank=False)
    postal_code = models.CharField(max_length=20, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.city}, {self.country}"

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    feedback = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} - {self.user.username}"


class UserSignup(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=255)

class Login_main(models.Model):
    email = models.EmailField()
    result = models.CharField(max_length=10)  # 'success' or 'failure'

    def __str__(self):
        return f"{self.email} - {self.result} "