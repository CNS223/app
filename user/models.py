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
from django.core.validators import MinValueValidator

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
        user.phone_number = "1234567890"
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
        user.phone_number = "1234567890"
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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}"

class User(AbstractBaseUser):
    GENDER_CHOICES = (('male', 'Male'), ('female', 'Female'), ('other', 'Other'))
    CURRENCY_CHOICES = (('cad', 'CAD'), ('usd', 'USD'))
    def save(self, *args, **kwargs):
        if self.pk == None:
            if not (self.email == None or self.email == ""):
                if User.objects.filter(email=self.email).exists():
                    return ValidationError("User Already Exist in  this mail id")

            if (self.username == None or self.username == ""):
                first_name = self.first_name
                if first_name:
                    username = "_".join(first_name.split(" "))+str(random.randrange(99999, 999999, 12))
                    if User.objects.filter(username=username).exists():
                        uid = User.objects.last().id + 1
                        self.username = f"{username}_{uid}"
                    else:
                        self.username = f"{username}"

                email = self.email
                if email and not self.username:
                    mail_id = email.split("@")[0].lower()
                    if User.objects.filter(username=mail_id).exists():
                        uid = User.objects.last().id + 1
                        self.username = f"{mail_id}_{uid}"
                    else:
                        self.username = f"{mail_id}"

            self.username = self.username.lower()
            if self.email:
                self.email = self.email.lower()

        super(User, self).save(*args, **kwargs)
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE, default = 1, null=False, blank=False)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    username = models.CharField(max_length=100, null=False, blank=False, unique=True)
    email = models.EmailField(blank=True, null=True, unique=True, db_index=True)
    email_verified = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False, unique=True)
    avatar = models.ImageField(upload_to=avatar_path, blank=True, null=True)
    availability = models.FloatField(default=0.0)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    bio = models.TextField(blank = True)
    experience = models.FloatField(default=0, validators=[MinValueValidator(0)])
    gender = models.CharField(choices=GENDER_CHOICES, default='male', max_length=50, null=False, blank=False)
    currency_code = models.CharField(choices=CURRENCY_CHOICES, default='cad', max_length=50, null=False, blank=False)
    groups = models.ManyToManyField('auth.Group', blank=True, related_name="cutom_user_group")
    objects = UserManager()

    USERNAME_FIELD = "username"

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

    def has_perm(self, perm, obj=None):
        user_perms = []
        if self.is_staff:
            groups = self.groups.all()
            for group in groups:
                perms = [(f"{x.content_type.app_label}.{x.codename}") for x in group.permissions.all()]
                user_perms += perms

            if perm in user_perms:
                return True
        return (self.is_admin or self.is_superuser)

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    def get_tokens_for_user(self):
        refresh = RefreshToken.for_user(self)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }   
        return data

    def generate_random_string(length):
        characters = string.ascii_letters + string.digits  # include both letters and digits
        random_string = ''.join(random.choice(characters) for _ in range(length))
        return random_string


class EmailVerification(models.Model):
    email_to = models.ForeignKey(User, on_delete=models.CASCADE, null = False, blank = False)
    verification_token = models.CharField(max_length=255, blank=False, null=False, )
    validity = models.DateTimeField(blank=True, null=True, )

    def validate_email(self, email_to, verification_token):
        # Checking if the email and verification token match the instance
        valid = (self.email_to == email_to and 
                self.verification_token == verification_token and 
                self.validity >= timezone.now())

        # Deleting the instance if validation is successful
        if valid:
            self.delete()

        return valid

from service.models import ServiceBooking


class ProviderGetInTouch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender_contacts', null=False, blank=False)
    provider = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='recipient_contacts', blank=False)
    full_name = models.CharField(max_length=80, blank=False, null=False, )
    email = models.EmailField(blank=True, null=True, db_index=True)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    message = models.TextField(blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.username)

class UserSystemVisit(models.Model):
    created_at = models.DateTimeField(timezone.now)
    daily_count = models.IntegerField(default=0)
    total_count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.created_at)

        