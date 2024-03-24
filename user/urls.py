from django.urls import path, include
from user.views import *

app_name = 'user'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('choose_register', ChooseRegisterView.as_view(), name='choose_register'),  # Add this line
    path('provider_signup', ProviderSignupView.as_view(), name='provide_signup'),
    path('verify-email', VerifyEmailView.as_view(), name='verify_email'),
    path('verify-mail', VerifyEmailSuccessView.as_view(), name='verify_email_successful'),
    path('user_signup', UserSignupView.as_view(), name='user_signup'),
    path('forgot_password', forgot_password, name='forgot_password'),
    path('reset_password', reset_password, name='reset_password'),
    path('user_signin', UserSigninView.as_view(), name='user_signin'),

    # Provider Routes
    path('provider-profile', ProviderProfileView.as_view(), name='provider_rofile'),
    # path('provider-services', provider_services, name='provider_services'),
    # path('provider-booking', provider_booking, name='provider_booking'),
    # path('provider-list', provider_list, name='provider_list'),
    # path('provider-details', provider_details, name='provider_details'),
    #
    # customer Routes
    path('customer-profile', CustomerProfileView.as_view(), name='customer_rofile'),
    # # customer Routes
    # path('customer-booking', customer_booking, name='customer_booking'),
    path('customer_profile_creation', customer_profile_creation, name='customer_profile_creation'),

    # path('feedback', feedback, name='feedback'),
    path('feedback/', FeedbackCreateView.as_view(), name='feedback'),
    path('feedback/success/', feedback_success, name='feedback_success'),
    # Provider Routs
    path('provider_dashboard', provider_dashboard, name='provider_dashboard'),
    path('', dashboard, name='dashboard')
]