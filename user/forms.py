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
    class Meta:
        model = User
        # profile_picture = forms.ImageField(required=False)
        fields = ['first_name', 'last_name','username', 'email',  'phone_number','avatar']
        widgets = {
            field_name: forms.TextInput(
                attrs={'class': 'form-control form-group col-md-6 col-form-label"',
                       'placeholder': f'Enter {field_name.capitalize()}'})
            for field_name in fields if field_name != 'avatar'

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

#
# class AddressForm(forms.ModelForm):
#     STATE_CHOICES = [
#         ('AB', 'Alberta'),
#         ('BC', 'British Columbia'),
#         ('MB', 'Manitoba'),
#         ('NB', 'New Brunswick'),
#         ('NL', 'Newfoundland and Labrador'),
#         ('NS', 'Nova Scotia'),
#         ('NT', 'Northwest Territories'),
#         ('NU', 'Nunavut'),
#         ('ON', 'Ontario'),
#         ('PE', 'Prince Edward Island'),
#         ('QC', 'Quebec'),
#         ('SK', 'Saskatchewan'),
#         ('YT', 'Yukon'),
#     # ]
#
#     # state = forms.ChoiceField(choices=STATE_CHOICES, required=True)
#     # city = forms.CharField(max_length=100, required=True)
#
#     class Meta:
#         model = Address
#         fields = ['add1', 'add2', 'state', 'city', 'provision', 'country', 'postal_code']
#         widgets = {
#             'add1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Address Line 1'}),
#             'add2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Address Line 2'}),
#             'provision': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Provision'}),
#             'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Country', 'value': 'Canada', 'readonly': True}),
#             'postal_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Postal Code'}),
#         }
#
#     def __init__(self, *args, **kwargs):
#         super(AddressForm, self).__init__(*args, **kwargs)
#         if 'state' in self.data:
#             state_name = self.data.get('state')
#             state_cities = Address.objects.filter(state=state_name).values_list('city', flat=True).distinct()
#             self.fields['city'].widget = forms.Select(choices=[(city, city) for city in state_cities])
#
#     def __init__(self, *args, **kwargs):
#         super(AddressForm, self).__init__(*args, **kwargs)
#         if 'state' in self.data:
#             try:
#                 state_name = self.data.get('state')
#                 state_cities = Address.objects.filter(state=state_name).values_list('city', flat=True).distinct()
#                 self.fields['city'].widget = forms.Select(choices=[(city, city) for city in state_cities])
#             except Exception as e:
#                 print(e)  # Handle exception appropriately
>>>>>>> Stashed changes
=======
>>>>>>> f626cddad2e97bc8b65ae306634e1bc52782f52e
