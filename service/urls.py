from django.urls import path, include
from service import views
from service.views import *


app_name = 'service'

urlpatterns = [
    path('service-create', ServiceCreateView.as_view(), name='service_create'),
    path('serviceindex', serviceindex, name='service-index'),
    path('provider_signup', views.provider_signup, name='provider_signup'),
    path('servicedetail', views.servicedetail, name='servicedetail'),
    path('service-list', ServiceListView.as_view(), name='service_list'),

    # path('generate_otp', views.GenerateOTP.as_view(), name='generate-otp'),
]