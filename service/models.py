from django.contrib.auth.models import User
from django.db import models
from user.models import *

def service_path(instance, filename):
    return 'service/{}/{}'.format(
        instance.id,
        filename
    )

class ServiceCategory(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id

class ProviderService(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, null=False, blank=False)
    provider = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    price = models.FloatField(default=0)
    active = models.BooleanField(default=True)
    desc = models.TextField(null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=False, blank=False)
    picture = models.ImageField(upload_to=service_path, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)