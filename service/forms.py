from django import forms
from .models import *

class SearchForm(forms.Form):
    search_input = forms.CharField(label='What are you looking for?', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Car Repair Services'}), max_length=255)

class ServicePostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ServicePostForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Select category"
        self.fields['country'].empty_label = "Select country"
        self.fields['state'].empty_label = "Select state"
        self.fields['city'].empty_label = "Select city"

    class Meta:
        model = ProviderService
        fields = ['title', ]#'category', 'desc', 'price', 'duration', 'address', 'country', 'state', 'city', 'pincode', 'picture']
        labels = {
            'title': 'Title',
            'category': 'Category',
            'desc': 'Description',
            'price': 'Price',
            'duration': 'Duration',
            'address': 'Address',
            'country': 'Country',
            'state': 'State',
            'city': 'City',
            'pincode': 'Pincode',
            'picture': 'Picture',
        }
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        country = cleaned_data.get("country")
        state = cleaned_data.get("state")
        city = cleaned_data.get("city")

        # Add validation logic here to ensure city belongs to the selected state and country
        if city.state != state or city.state.country != country:
            raise forms.ValidationError("Invalid city selected")
