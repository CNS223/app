from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone = models.CharField(max_length=20)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.id)