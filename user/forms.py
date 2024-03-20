from django import forms
from django.contrib.auth.forms import PasswordResetForm

from service.models import *
from user.models import *

class ProviderSignupForm(forms.Form):
    first_name = forms.CharField(max_length=100, label='First Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your First Name', 'required': True}))
    last_name = forms.CharField(max_length=100, label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Last Name', 'required': True}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'johndoe@example.com', 'required': True}))
    phone = forms.CharField(max_length=15, label='Phone Number', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(256) 789-6253', 'required': True}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control pass-input', 'placeholder': '*************', 'required': True}))

class UserSignupForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your First Name', 'required': True}))
    last_name = forms.CharField(label='Last Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Last Name', 'required': True}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'johndoe@example.com', 'required': True}))
    phone = forms.CharField(label='Phone Number', max_length=15, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg group_formcontrol', 'placeholder': '(256) 789-6253', 'required': True}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control pass-input', 'placeholder': '*************', 'required': True}))

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'johndoe@example.com'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '*************'}))
    remember_me = forms.BooleanField(label='Remember Me', required=False, widget=forms.CheckboxInput(attrs={'class': 'rememberme'}))
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

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['feedback']
        widgets = {
            'user': forms.HiddenInput(attrs={'value': 8}),  # Set user_id to 8
            'service': forms.HiddenInput(attrs={'value': 2}),  # Set service_id to 2
        }