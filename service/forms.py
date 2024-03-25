from django import forms
from .models import *

class SearchForm(forms.Form):
    search_input = forms.CharField(label='What are you looking for?', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Car Repair Services'}), max_length=255)


class ServiceCreateForm(forms.Form):
    title = forms.CharField(label='Service Title', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Service Name'}))
    category = forms.CharField(label='Category', widget=forms.Select(attrs={'class': 'select'}))
    price = forms.DecimalField(label='Price', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Set 0 for free'}))
    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'class': 'form-control ck-editor'}))
    monday_from_time = forms.TimeField(label='Monday - From', widget=forms.TimeInput(attrs={'class': 'form-control timepicker', 'placeholder': 'From'}))
    monday_to_time = forms.TimeField(label='Monday - To', widget=forms.TimeInput(attrs={'class': 'form-control timepicker', 'placeholder': 'To'}))
    tuesday_from_time = forms.TimeField(label='Tuesday - From', widget=forms.TimeInput(attrs={'class': 'form-control timepicker', 'placeholder': 'From'}))
    tuesday_to_time = forms.TimeField(label='Tuesday - To', widget=forms.TimeInput(attrs={'class': 'form-control timepicker', 'placeholder': 'To'}))
    wednesday_from_time = forms.TimeField(label='Wednesday - From', widget=forms.TimeInput(attrs={'class': 'form-control timepicker', 'placeholder': 'From'}))
    wednesday_to_time = forms.TimeField(label='Wednesday - To', widget=forms.TimeInput(attrs={'class': 'form-control timepicker', 'placeholder': 'To'}))
    thursday_from_time = forms.TimeField(label='Thursday - From', widget=forms.TimeInput(attrs={'class': 'form-control timepicker', 'placeholder': 'From'}))
    thursday_to_time = forms.TimeField(label='Thursday - To', widget=forms.TimeInput(attrs={'class': 'form-control timepicker', 'placeholder': 'To'}))
    friday_from_time = forms.TimeField(label='Friday - From', widget=forms.TimeInput(attrs={'class': 'form-control timepicker', 'placeholder': 'From'}))
    friday_to_time = forms.TimeField(label='Friday - To', widget=forms.TimeInput(attrs={'class': 'form-control timepicker', 'placeholder': 'To'}))
    saturday_from_time = forms.TimeField(label='Saturday - From', widget=forms.TimeInput(attrs={'class': 'form-control timepicker', 'placeholder': 'From'}))
    saturday_to_time = forms.TimeField(label='Saturday - To', widget=forms.TimeInput(attrs={'class': 'form-control timepicker', 'placeholder': 'To'}))
    sunday_from_time = forms.TimeField(label='Sunday - From', widget=forms.TimeInput(attrs={'class': 'form-control timepicker', 'placeholder': 'From'}))
    sunday_to_time = forms.TimeField(label='Sunday - To', widget=forms.TimeInput(attrs={'class': 'form-control timepicker', 'placeholder': 'To'}))
    add1 = forms.CharField(label='Address 1', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Address 1'}))
    add2 = forms.CharField(label='Address 2', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Address 2'}))
    country = forms.CharField(label='Country', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Country'}))
    city = forms.CharField(label='City', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your City'}))
    provision = forms.CharField(label='Provision', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your State'}))
    pincode = forms.CharField(label='Pincode', max_length=10, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Pincode'}))
    image = forms.ImageField(label='Image', required=False, widget=forms.FileInput(attrs={'accept': 'image/*'}))

class ServiceBookingForm(forms.Form):
    add1 = forms.CharField(label='Address 1', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Address 1'}))
    add2 = forms.CharField(label='Address 2', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Address 2'}))
    city = forms.CharField(label='City', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your City'}))
    provision = forms.CharField(label='Provision', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your State'}))
    country = forms.CharField(label='Country', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Country'}))
    pincode = forms.CharField(label='Pincode', max_length=10, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Pincode'}))
    appointment = forms.CharField(label='Category', widget=forms.Select(attrs={'class': 'select'}))
   
class FeedbackForm(forms.Form):
    feedback = forms.CharField(label='Add Feedback', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Feedback'}))
    