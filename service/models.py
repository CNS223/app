from django.db import models
from user.models import User

# Create your models here.
class ServiceCategory(models.Model):
    name = models.CharField(max_length=255,null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ServicePost(models.Model):
    category = models.CharField(max_length=255,null=False, blank=False)
    add2 = models.CharField(max_length=255,null=True,blank=True)
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    desc = models.TextField(null=True, blank=True)
    per_hrs_rate = models.FloatField(default=0)
    hrs_of_work = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)