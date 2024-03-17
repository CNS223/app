from django.urls import path, include
from user.views import *

app_name = 'user'

urlpatterns = [

    # Auth Routs
    path('', index, name='index'),
    path('index', index, name='index_html'),  # Add this line
    path('choose_register', choose_register, name='choose_register'),  # Add this line
    path('provide_signup', provide_signup, name='provide_signup'),
    path('user_signup', user_signup, name='user_signup'),
    path('forgot_password', forgot_password, name='forgot_password'),
    path('reset_password', reset_password, name='reset_password'),
    path('user_signin', user_signin, name='user_signin'),


    # Provider Routs
    path('provider_dashboard', provider_dashboard, name='provider_dashboard'),
]