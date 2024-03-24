from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from service.models import *
from django.shortcuts import render, redirect
from .forms import ServicePostForm



# Create your views here.
def serviceindex(request):
    return render(request, 'servicebase.html')

def servicedetail(request):
    return render(request, 'servicedetail.html')


def provider_signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        # Create a new Provider object and save it to the database
        provider = Provider(name=name, email=email, phone=phone, password=password)
        provider.save()

        # You might want to redirect the user to a different page after signup
        return redirect('user:index')

    return render(request, 'user/provider-signup.html')


#def create_service(request):
#    return render(request, 'create_service.html')


def create_service(request):
    if request.method == 'POST':
        form = ServicePostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = ServicePostForm()
    return render(request, 'create_service.html', {'form': form})
