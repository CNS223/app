from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from .models import Provider

class MultiTableAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            pass

        try:
            provider = Provider.objects.get(email=username)
            if provider.check_password(password):
                return provider
        except Provider.DoesNotExist:
            pass

        return None
