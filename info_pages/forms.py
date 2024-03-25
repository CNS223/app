from django import forms
from django.contrib.auth.forms import PasswordResetForm
from drf_yasg.openapi import Contact

from service.models import *
from user.models import *
from info_pages.models import *

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'phone', 'message']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email field is required.")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and len(phone) < 10:
            raise forms.ValidationError("Phone number must be at least 10 digits.")
        return phone