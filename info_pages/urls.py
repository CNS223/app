from django.urls import path, include
from info_pages.views import *

app_name = 'info_pages'

urlpatterns = [

    # Auth Routs
    path('about-us', about_us, name='about_us'),
    path('privacy-policy', privacy_policy, name='privacy_policy'),
    path('terms-and-conditions', terms_n_conditions, name='terms_n_conditions'),
]