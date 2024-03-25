from django import forms
from django.contrib.auth.forms import PasswordResetForm

from service.models import *
from user.models import *


class ProviderSignupForm(forms.Form):
    first_name = forms.CharField(max_length=100, label='First Name', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your First Name', 'required': True}))
    last_name = forms.CharField(max_length=100, label='Last Name', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your Last Name', 'required': True}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'johndoe@example.com', 'required': True}))
    phone = forms.CharField(max_length=15, label='Phone Number', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '(256) 789-6253', 'required': True}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control pass-input', 'placeholder': '*************', 'id': 'password-field',
               'required': True}))


class UserSignupForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your First Name', 'required': True}))
    last_name = forms.CharField(label='Last Name', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your Last Name', 'required': True}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'johndoe@example.com', 'required': True}))
    phone = forms.CharField(label='Phone Number', max_length=15, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg group_formcontrol', 'placeholder': '(256) 789-6253',
               'required': True}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control pass-input', 'placeholder': '*************', 'required': True}))


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'johndoe@example.com'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': '*************'}))
    remember_me = forms.BooleanField(label='Remember Me', required=False,
                                     widget=forms.CheckboxInput(attrs={'class': 'rememberme'}))


class AccountSettingsForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your First Name', 'required': True}))
    last_name = forms.CharField(label='Last Name', max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your Last Name', 'required': True}))
    username = forms.CharField(label='User Name', max_length=255, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Username', 'required': True}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'johndoe@example.com', 'readonly': True}))
    phone_number = forms.CharField(label='Phone Number', max_length=15, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '(256) 789-6253', 'readonly': True, 'required': True}))
    gender = forms.ChoiceField(label='Gender', choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
                               required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    bio = forms.CharField(label='Bio', widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Enter your shor bio', 'rows': 5}), required=False)
    add1 = forms.CharField(label='Address 1', max_length=255,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address Line 1'}))
    add2 = forms.CharField(label='Address 2', max_length=255,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address Line 2'}))
    country = forms.CharField(label='Country', max_length=255,
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}))
    provision = forms.CharField(label='Provision', max_length=255,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Provision'}))
    city = forms.CharField(label='City', max_length=255,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}))
    postal_code = forms.CharField(label='Postal Code', max_length=10,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'N9A 5E3'}))
    currency_code = forms.ChoiceField(label='Currency Code', choices=[('cad', 'CAD'), ('usd', 'USD')], required=False,
                                      widget=forms.Select(attrs={'class': 'form-select'}))
    profile_picture_upload = forms.FileField(label='Profile Picture', required=False, widget=forms.ClearableFileInput(
        attrs={'class': 'form-control', 'accept': 'image/*'}))

    def clean_mobile_number(self):
        mobile_number = self.cleaned_data.get('mobile_number')
        # Custom validation for mobile number format
        if not mobile_number.startswith('+'):
            raise forms.ValidationError('Mobile number must start with a country code.')
        return mobile_number

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        username = cleaned_data.get('username')

        # Custom validation for unique email and username
        if email == 'admin@example.com':
            raise forms.ValidationError('Email cannot be admin@example.com.')

        if username == 'admin':
            raise forms.ValidationError('Username cannot be admin.')

        return cleaned_data


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'johndoe@example.com'}), required=True)


class ReSetPasswordForm(forms.Form):
    password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control pass-input', 'id': 'password-1', 'placeholder': '*************',
               'required': True}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control pass-input', 'id': 'password-2', 'placeholder': '*************',
               'required': True}))

class RatingForm(forms.Form):
    RATING_CHOICES = (
        ('5', '😊 Highest'),
        ('4', '😐 Good'),
        ('3', '😃 Moderate'),
        ('2', '😄 Limited'),
        ('1', '😠 Lowest'),
    )
    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect(attrs={'class': 'hidden-radio'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Please write your review'}))


class ProviderContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your Full Name'}))
    email = forms.EmailField(label='Email', max_length=100, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Email Address'}))
    phone_number = forms.CharField(label='Phone Number', max_length=15, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}))
    message = forms.CharField(label='Message', widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter your Comments'}))


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

