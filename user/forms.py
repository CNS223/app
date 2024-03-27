from django import forms
from django.contrib.auth.forms import PasswordResetForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, MaxLengthValidator
from service.models import *
from user.models import *
import json
from django.core.validators import MinLengthValidator

def validate_password(value):
    if not any(char.isupper() for char in value):
        raise ValidationError('Password must contain at least one uppercase letter.')
    if not any(char.isdigit() for char in value):
        raise ValidationError('Password must contain at least one digit.')
    if not any(char in '!@#$%^&*()_+-=[]{}|;:,.<>?/~`' for char in value):
        raise ValidationError('Password must contain at least one special character.')
    if len(value) < 8:
        raise ValidationError('Password must be at least 8 characters long.')

def validate_first_name(value):
    if not value.isalpha():
        raise ValidationError('First name should only contain alphabetic characters.')

def validate_phone_number(value):
    if not value.isdigit():
        raise ValidationError('Phone number should contain digits only.')
    if len(value) != 10:
        raise ValidationError('Phone number must have exactly 10 digits.')


class ProviderSignupForm(forms.Form):
    first_name = forms.CharField(max_length=100,label='First Name*',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your First Name', 'required': True}),validators=[RegexValidator(r'^[a-zA-Z]*$'),validate_first_name,])
    last_name = forms.CharField(label='Last Name*', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Last Name', 'required': True}),validators=[MaxLengthValidator(100),RegexValidator(r'^[a-zA-Z]*$', message='Last name should only contain alphabetic characters.'),validate_first_name,],error_messages={'required': 'Please enter your Last Name.','max_length': 'Last Name should not exceed 100 characters.',})
    email = forms.EmailField(label='Email*', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'johndoe@example.com', 'required': True}))
    phone = forms.CharField(max_length=10, label='Phone Number*', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg group_formcontrol', 'placeholder': '(256) 789-6253', 'required': True}),validators=[validate_phone_number, MinLengthValidator(10, message='Phone number must be at least 10 digits')],)
    password = forms.CharField(label='Password*', widget=forms.PasswordInput(attrs={'class': 'form-control pass-input', 'placeholder': '*************', 'id': 'password-field','required': True}),validators=[validate_password],error_messages={'required': 'Please enter your password.'})


class UserSignupForm(forms.Form):
    first_name = forms.CharField(max_length=100,label='First Name*',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your First Name', 'required': True}),validators=[MaxLengthValidator(100),RegexValidator(r'^[a-zA-Z]*$', message='First name should only contain alphabetic characters.'),validate_first_name,],error_messages={'required': 'Please enter your First Name.','max_length': 'First Name should not exceed 100 characters.',})
    last_name = forms.CharField(label='Last Name*', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Last Name', 'required': True}),validators=[MaxLengthValidator(100),RegexValidator(r'^[a-zA-Z]*$', message='Last name should only contain alphabetic characters.'),validate_first_name,],error_messages={'required': 'Please enter your Last Name.','max_length': 'Last Name should not exceed 100 characters.',})
    email = forms.EmailField(label='Email*', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'johndoe@example.com', 'required': True}))
    phone = forms.CharField(max_length=10, label='Phone Number*', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg group_formcontrol', 'placeholder': '(256) 789-6253', 'required': True}),validators=[validate_phone_number, MinLengthValidator(10, message='Phone number must be at least 10 digits')],)
    password = forms.CharField(label='Password*', widget=forms.PasswordInput(attrs={'class': 'form-control pass-input', 'id':"password-field", 'placeholder': '*************', 'required': True}), validators=[validate_password],error_messages={'required': 'Please enter your password.'})


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email*', max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'johndoe@example.com'}))
    password = forms.CharField(label='Password*', widget=forms.PasswordInput(attrs={'class': 'form-control pass-input', 'placeholder': '*************', 'id': 'password-field','required': True}),error_messages={'required': 'Please enter your password.'})



class AccountSettingsForm(forms.Form):
    first_name = forms.CharField(max_length=20,label='First Name*',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your First Name', 'required': True}),validators=[MaxLengthValidator(100),RegexValidator(r'^[a-zA-Z]*$', message='First name should only contain alphabetic characters.'),validate_first_name,],error_messages={'required': 'Please enter your First Name.','max_length': 'First Name should not exceed 100 characters.',})
    last_name = forms.CharField(label='Last Name*', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Last Name', 'required': True}),validators=[MaxLengthValidator(100),RegexValidator(r'^[a-zA-Z]*$', message='Last name should only contain alphabetic characters.'),validate_first_name,],error_messages={'required': 'Please enter your Last Name.','max_length': 'Last Name should not exceed 100 characters.',})
    username = forms.CharField(label='User Name', required=False, max_length=12, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username', 'readonly': True}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'johndoe@example.com', 'readonly': True}))
    phone_number = forms.CharField(max_length=10, label='Phone Number*', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg group_formcontrol', 'placeholder': '(256) 789-6253', 'readonly': True}),validators=[validate_phone_number, MinLengthValidator(10, message='Phone number must be at least 10 digits')],)
    gender = forms.ChoiceField(label='Gender', choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')],required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    bio = forms.CharField(label='Bio', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your shor bio', 'rows': 5}), required=False)
    add1 = forms.CharField(label='Address 1*', required=True, max_length=255,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address Line 1'}))
    add2 = forms.CharField(label='Address 2', required=False, max_length=255,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address Line 2', "values":""}))
    country = forms.ChoiceField(label='Country*', choices=[('Canada', 'Canada')], widget=forms.Select(attrs={'class': 'form-select'}))
    provision = forms.ChoiceField(label='Province*', choices=[], widget=forms.Select(attrs={'class': 'form-select', 'id':"provison-id"}))
    city = forms.ChoiceField(label='City*', choices=[], widget=forms.Select(attrs={'class': 'form-select'}))
    postal_code = forms.CharField(label='Postal Code*', max_length=7,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'N9A 5E3'}))
    currency_code = forms.ChoiceField(label='Currency Code*', choices=[('cad', 'CAD'), ('usd', 'USD')], required=False,widget=forms.Select(attrs={'class': 'form-select'}))
    profile_picture_upload = forms.FileField(label='Profile Picture', required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_provision_choices()
        self.load_city_choices()

    def load_provision_choices(self):
        try:
            # Load provision choices from JSON file
            with open('constants/cities.json') as f:
                provisions_data = json.load(f)
                provision_choices = [(key, key) for key in provisions_data.keys()]
                self.fields['provision'].choices = provision_choices
        except Exception as e:
            print("Error loading provision choices:", e)

    def load_city_choices(self, selected_provision=None):
        try:
            with open('constants/cities.json') as f:
                cities_data = json.load(f)
                if selected_provision:
                    cities = cities_data.get(selected_provision, [])
                else:
                    cities = [city for cities_list in cities_data.values() for city in cities_list]
                
                # Sort the cities by name
                sorted_cities = sorted(cities)
                
                city_choices = [(city, city) for city in sorted_cities]
                self.fields['city'].choices = city_choices
        except Exception as e:
            print("Error loading city choices:", e)

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
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'johndoe@example.com'}), required=True)


class ReSetPasswordForm(forms.Form):
    password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'class': 'form-control pass-input', 'placeholder': '*************', 'id': 'password-1','required': True}),validators=[validate_password],error_messages={'required': 'Please enter your new password.'})
    password2 = forms.CharField(label='onfirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control pass-input', 'placeholder': '*************', 'id': 'password-2','required': True}),validators=[validate_password],error_messages={'required': 'Please re-enter your new password.'})
    

class RatingForm(forms.Form):
    RATING_CHOICES = (
        ('5', '😊 Highest'),
        ('4', '😐 Good'),
        ('3', '😃 Moderate'),
        ('2', '😄 Limited'),
        ('1', '😠 Lowest'),
    )
    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect(attrs={'class': 'hidden-radio'}), required=False)
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Please write your review'}), required=False)


class ProviderContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Full Name'}))
    email = forms.EmailField(label='Email', max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email Address'}))
    phone_number = forms.CharField(max_length=10, label='Phone Number*', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg group_formcontrol', 'placeholder': '(256) 789-6253', 'required': True}),validators=[validate_phone_number, MinLengthValidator(10, message='Phone number must be at least 10 digits')],)
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter your Comments'}))


class UserProfileForm(forms.ModelForm):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    currency_code = forms.ChoiceField(choices=[('USD', 'USD'), ('EUR', 'EUR'), ('GBP', 'GBP')])  # Add currency dropdown
    language = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Language...'}))  # Use TextInput for language input
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'gender', 'phone_number', 'date_of_birth', 'currency_code','language']
        widgets = {field_name: forms.TextInput(attrs={'class': 'form-control form-group col-md-6 col-form-label"','placeholder': f'Enter {field_name.capitalize()}'})for field_name in fields}


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

