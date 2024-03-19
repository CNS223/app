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