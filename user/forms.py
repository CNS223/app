from django import forms
from django.contrib.auth.forms import PasswordResetForm

from service.models import *
from user.models import *

class UserSignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

# class ProviderSignupForm(forms.ModelForm):
#     class Meta:
#         model = Provider
#         fields = ['name', 'email', 'phone', 'password']
#         widgets = {
#             'password': forms.PasswordInput(),
#         }

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'johndoe@example.com'}))


class UserProfileForm(forms.ModelForm):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    currency_code = forms.ChoiceField(choices=[('USD', 'USD'), ('EUR', 'EUR'), ('GBP', 'GBP')])  # Add currency dropdown
    language = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Language...'}))  # Use TextInput for language input
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'gender', 'phone_number', 'date_of_birth', 'currency_code',
                  'language']
        widgets = {
            field_name: forms.TextInput(
                attrs={'class': 'form-control form-group col-md-6 col-form-label"',
                       'placeholder': f'Enter {field_name.capitalize()}'})
            for field_name in fields
        }


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['add1', 'add2', 'city', 'provision', 'country', 'postal_code']
        widgets = {
            field_name: forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': f'Enter {field_name.capitalize()}'})
            for field_name in fields
        }
