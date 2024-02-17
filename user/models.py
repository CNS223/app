from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


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
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserType(models.Model):
    USER_TYPE_CHOICES = (
        ('user', 'User'),
        ('service_provider', 'Service Provider')
    )
    user_type = models.CharField(max_length=100, choices=USER_TYPE_CHOICES, default='user', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


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
