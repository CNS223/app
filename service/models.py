from django.contrib.auth.models import User
from django.db import models
from user.models import *

def service_path(instance, filename):
    return 'service/{}/{}'.format(
        instance.id,
        filename
    )