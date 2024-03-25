from django.urls import path, include
from user.views import *

app_name = 'user'

urlpatterns = [
    # path('', dashboard, name='dashboard'),
    path('choose_register', ChooseRegisterView.as_view(), name='choose_register'),  # Add this line
    path('provider_signup', ProviderSignupView.as_view(), name='provide_signup'),
    path('verify-email', VerifyEmailView.as_view(), name='verify_email'),
    path('verify-mail', VerifyEmailSuccessView.as_view(), name='verify_email_successful'),
    path('user_signup', UserSignupView.as_view(), name='user_signup'),
    path('forgot-password', ForgotPasswordView.as_view(), name='forgot_password'),
    path('reset-password', ResetPasswordView.as_view(), name='reset_password'),
    path('user_signin', UserSigninView.as_view(), name='user_signin'),

    # Provider Routes
    path('provider-services', ProviderServicesView.as_view(), name='provider_services'),
    path('provider-booking', ProviderBookingView.as_view(), name='provider_booking'),
    path('provider-list', ProviderListView.as_view(), name='provider_list'),
    path('provider-details/<int:provider_id>', ProviderDetailsView.as_view(), name='provider_details'),
    path('provider-profile', ProviderProfileView.as_view(), name='provider_rofile'),
    path('service-complete/<int:service_id>', ServiceCompleteView.as_view(), name='service_complete'),

    # customer Routes
    path('customer-booking', CustomerBookingView.as_view(), name='customer_booking'),
    path('customer-profile', CustomerProfileView.as_view(), name='customer_rofile'),
]