from django.contrib.auth.models import User
from django.db import models



# Create your models here.
class ServiceCategory(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id


class Availability(models.Model):
    day = models.CharField(max_length=20)
    available = models.BooleanField(default=False)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.user.username}'s availability on {self.day}"

class ServicePost(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    desc = models.TextField(null=True, blank=True)
    per_hrs_rate = models.FloatField(default=0)
    hrs_of_work = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    availability = models.ManyToManyField(Availability)

    def __str__(self):
        return self.id


class UserService(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, null=False, blank=False)
    desc = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id


class UserServiceRating(models.Model):
    user_service = models.ForeignKey(UserService, on_delete=models.CASCADE, null=False, blank=False)
    rate = models.FloatField(default=0.0, null=False, blank=False)
    comment = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id


class Provider(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.id

class ServicePostComment(models.Model):
    comment = models.TextField(null=False, blank=False)
    interested = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id
