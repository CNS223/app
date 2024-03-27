from django import forms
from django.contrib.auth.forms import PasswordResetForm
from drf_yasg.openapi import Contact

from service.models import *
from user.models import *
from info_pages.models import *
from django.core.exceptions import ValidationError

def validate_phone_number(value):
    # Check if the phone number contains only digits and is not empty
    if not value.isdigit() or len(value) < 10:
        raise ValidationError('Phone number must contain at least 10 digits and only numbers.')

class ContactUsForm(forms.ModelForm):
    phone = forms.CharField(label='Phone Number', max_length=10, required=False, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg group_formcontrol', 'placeholder': '(256) 789-6253'}), validators=[validate_phone_number])

    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'phone', 'message']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email field is required.")
        return email