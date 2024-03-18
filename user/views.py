from django.contrib.auth import authenticate, login
from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.urls import reverse_lazy, reverse
from pyexpat.errors import messages

from cns import settings
from service.models import Provider
from user.forms import *
from user.models import User, UserSignup, Login_main

from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'base.html')


def choose_register(request):
    return render(request, 'register/choose_signup.html')


def provider_signup(request):
    if request.method == 'POST':
        form = ProviderSignupForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            names = form.cleaned_data['name']
            emails = form.cleaned_data['email']
            phones = form.cleaned_data['phone']
            passwords = form.cleaned_data['password']

            # Save the data to the database
            provider = Provider(name=names, email=emails, phone=phones, password=passwords)
            provider.save()

            # Redirect to a success page or return a success message
            return redirect('user:index')  # Redirect to the index page
    else:
        form = ProviderSignupForm()

    return render(request, 'register/provider_signup.html', {'form': form})


def user_signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        # Create a new User_s object and save it to the database

        user = UserSignup(name=name, email=email, phone=phone, password=password)
        user.save()

        # Redirect the user to a different page after signup
        return redirect('user:index')
    else:
        return render(request, 'register/user_signup.html')



def user_signin(request):
    return render(request, 'login/login.html')


def forgot_password(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            return redirect('user:reset_password')  # Redirect to password reset page or any other page
    else:
        form = ForgotPasswordForm()

    return render(request, 'login/forgot_password.html', {'form': form})


def reset_password(request):
    return render(request, 'login/reset_password.html')


def provider_dashboard(request):
    return render(request, 'provider/provider-dashboard.html')


def customer_profile_creation(request):
    if request.method == 'POST':
        user_form = UserProfileForm(request.POST)
        address_form = AddressForm(request.POST)
        if user_form.is_valid() and address_form.is_valid():
            user = user_form.save(commit=False)
            address = address_form.save(commit=False)
            user.save()
            address.user = user
            address.save()
            return redirect('success_page')
    else:
        user_form = UserProfileForm()
        address_form = AddressForm()
    return render(request, 'customer/customer_profile_creation.html', {'user_form': user_form, 'address_form': address_form})



