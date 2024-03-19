from django.urls import path, include
from user.views import *

app_name = 'user'

urlpatterns = [
    path('choose_register', choose_register, name='choose_register'),  # Add this line
    path('provider_signup', provider_signup, name='provide_signup'),
    path('user_signup', user_signup, name='user_signup'),
    path('forgot_password', forgot_password, name='forgot_password'),
    path('reset_password', reset_password, name='reset_password'),
    path('user_signin', user_signin, name='user_signin'),
    path('customer_profile_creation', customer_profile_creation, name='customer_profile_creation'),
    # path('feedback', feedback, name='feedback'),
    path('feedback/', FeedbackCreateView.as_view(), name='feedback'),
    path('feedback/success/', feedback_success, name='feedback_success'),
    # Provider Routs
    path('provider_dashboard', provider_dashboard, name='provider_dashboard'),
    path('', dashboard, name='dashboard')
]