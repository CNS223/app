from django import forms
from .models import *
import json
from django.core.validators import RegexValidator


class SearchForm(forms.Form):
    search_input = forms.CharField(label='What are you looking for?', required = False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Car Repair Services'}), max_length=255)


class ServiceCreateForm(forms.Form):
    title = forms.CharField(
        label='Service Title*',
        required=True,
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Service Name'}),
        validators=[RegexValidator(r'^[a-zA-Z\s]+$', message='Title should contain only letters and spaces.')],
        error_messages={
            'required': 'Please enter a service title.',
            'max_length': 'Service title should not exceed 255 characters.'
        }
    )
    category = forms.CharField(label='Category*', required=True, widget=forms.Select(attrs={'class': 'select'}))
    price = forms.DecimalField(label='Price*', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Set 0 for free'}))
    description = forms.CharField(label='Description*', widget=forms.Textarea(attrs={'class': 'form-control ck-editor'}))
    monday_from_time = forms.TimeField(required=False, label='Monday - From', widget=forms.TimeInput(attrs={'class': 'form-control timepicker', 'placeholder': 'From'}))
    monday_to_time = forms.TimeField(required=False, label='Monday - To', widget=forms.TimeInput(attrs={'class': 'form-control timepicker', 'placeholder': 'To'}))
    tuesday_from_time = forms.TimeField(required=False, label='Tuesday - From', widget=forms.TimeInput(attrs={'class': 'form-control timepicker', 'placeholder': 'From'}))
    tuesday_to_time = forms.TimeField(required=False, label='Tuesday - To', widget=forms.TimeInput(attrs={'class': 'form-control timepicker', 'placeholder': 'To'}))
    wednesday_from_time = forms.TimeField(required=False, label='Wednesday - From', widget=forms.TimeInput(attrs={'class': 'form-control timepicker', 'placeholder': 'From'}))
    wednesday_to_time = forms.TimeField(required=False, label='Wednesday - To', widget=forms.TimeInput(attrs={'class': 'form-control timepicker', 'placeholder': 'To'}))
    thursday_from_time = forms.TimeField(required=False, label='Thursday - From', widget=forms.TimeInput(attrs={'class': 'form-control timepicker', 'placeholder': 'From'}))
    thursday_to_time = forms.TimeField(required=False, label='Thursday - To', widget=forms.TimeInput(attrs={'class': 'form-control timepicker', 'placeholder': 'To'}))
    friday_from_time = forms.TimeField(required=False, label='Friday - From', widget=forms.TimeInput(attrs={'class': 'form-control timepicker', 'placeholder': 'From'}))
    friday_to_time = forms.TimeField(required=False, label='Friday - To', widget=forms.TimeInput(attrs={'class': 'form-control timepicker', 'placeholder': 'To'}))
    saturday_from_time = forms.TimeField(required=False, label='Saturday - From', widget=forms.TimeInput(attrs={'class': 'form-control timepicker', 'placeholder': 'From'}))
    saturday_to_time = forms.TimeField(required=False, label='Saturday - To', widget=forms.TimeInput(attrs={'class': 'form-control timepicker', 'placeholder': 'To'}))
    sunday_from_time = forms.TimeField(required=False, label='Sunday - From', widget=forms.TimeInput(attrs={'class': 'form-control timepicker', 'placeholder': 'From'}))
    sunday_to_time = forms.TimeField(required=False, label='Sunday - To', widget=forms.TimeInput(attrs={'class': 'form-control timepicker', 'placeholder': 'To'}))
    add1 = forms.CharField(label='Address 1', required=True, max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Address 1'}))
    add2 = forms.CharField(label='Address 2', required=False, max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Address 2'}))
    country = forms.ChoiceField(label='Country*', choices=[('Canada', 'Canada')], widget=forms.Select(attrs={'class': 'form-select'}))
    provision = forms.ChoiceField(label='Province*', choices=[], widget=forms.Select(attrs={'class': 'form-select', 'id':"provison-id"}))
    city = forms.ChoiceField(label='City*', choices=[], widget=forms.Select(attrs={'class': 'form-select'}))
    pincode = forms.CharField(label='Pincode*', max_length=7, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Pincode'}))
    image = forms.ImageField(label='Image', required=False, widget=forms.FileInput(attrs={'accept': 'image/*'}))

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

class ServiceBookingForm(forms.Form):
    add1 = forms.CharField(label='Address 1', required=True, max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Address 1'}))
    add2 = forms.CharField(label='Address 2', required=False, max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Address 2'}))
    country = forms.ChoiceField(label='Country*', choices=[('Canada', 'Canada')], widget=forms.Select(attrs={'class': 'form-select'}))
    provision = forms.ChoiceField(label='Province*', choices=[], widget=forms.Select(attrs={'class': 'form-select', 'id':"provison-id"}))
    city = forms.ChoiceField(label='City*', choices=[], widget=forms.Select(attrs={'class': 'form-select'}))
    pincode = forms.CharField(label='Pincode', max_length=7, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Pincode'}))
    # appointment = forms.CharField(label='Category', widget=forms.Select(attrs={'class': 'form-select'}))
    appointment = forms.ChoiceField(label='Appointment*', choices=[], widget=forms.Select(attrs={'class': 'form-select'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_provision_choices()
        self.load_city_choices()
        # self.load_appointment()

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

    # def load_appointment(self):
    #     try:

   
class FeedbackForm(forms.Form):
    feedback = forms.CharField(label='Add Feedback', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Feedback'}))
    