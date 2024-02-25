from django.db import models
from user.models import User

# Create your models here.
class ServiceCategory(models.Model):
    name = models.CharField(max_length=255,null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ServicePost(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    desc = models.TextField(null=True, blank=True)
    per_hrs_rate = models.FloatField(default=0)
    hrs_of_work = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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