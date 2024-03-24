from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from service.models import *
from django.shortcuts import render, redirect
from service.forms import *
from user.models import *
from service.forms import *
from service.scripts import *
from django.urls import reverse_lazy, reverse


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

class ServiceListView(View):
    template_name = 'services/service-list.html'
    base_template = 'base.html'
    form_class = SearchForm

    def get(self, request, *args, **kwargs):
        context = {"base_template":self.base_template, "active_header":"providers"}
        try:
            user_id = request.user_id
            user = User.objects.get(pk = user_id)
            context['user_type'] = user.user_type.user_type
            if user.user_type.user_type == 'provider':
                provider_services = ProviderService.objects.filter(provider = user)
            else:
                provider_services = ProviderService.objects.all()
            service_ratings_data = {}
            for service in provider_services:
                service_ratings_data[service.id] = 0
                bookings = ServiceBooking.objects.filter(service = service)
                total_ratings = 0
                service_ratings_length = 1
                for booking in bookings:
                    service_ratings = ServiceRating.objects.filter(service=booking)
                    service_ratings_length = service_ratings_length+len(service_ratings)
                    for service_rate in service_ratings:
                        total_ratings = total_ratings+service_rate.rate
                if total_ratings != 0 or total_ratings != 0.0:
                    service_ratings_data[service.id] = round(total_ratings/service_ratings_length,1)
            context['provider_services'] = provider_services
            context['user'] = user
            context['user'] = user
            context['service_ratings'] = service_ratings_data
            context['form'] = self.form_class()
        except Exception as e:
            print("89-----",e)
            return redirect('user:user_signin')
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        context = {"base_template":self.base_template, "active_header":"providers"}
        form = self.form_class(request.POST)
        context['form'] = self.form_class()
        if form.is_valid():
            search_input = form.cleaned_data.get('search_input')
            user_id = request.user_id
            user = User.objects.get(pk = user_id)
            context['user_type'] = user.user_type.user_type
            if search_input != '':
                if user.user_type.user_type == 'provider':
                    provider_services = ProviderService.objects.filter(provider = user, title__icontains = search_input)
                else:
                    provider_services = ProviderService.objects.filter(title__icontains = search_input)
            else:
                provider_services = ProviderService.objects.filter(provider = user)
            service_ratings_data = {}
            for service in provider_services:
                service_ratings_data[service.id] = 0
                bookings = ServiceBooking.objects.filter(service = service)
                total_ratings = 0
                service_ratings_length = 1
                for booking in bookings:
                    service_ratings = ServiceRating.objects.filter(service=booking)
                    service_ratings_length = service_ratings_length+len(service_ratings)
                    for service_rate in service_ratings:
                        total_ratings = total_ratings+service_rate.rate
                if total_ratings != 0 or total_ratings != 0.0:
                    service_ratings_data[service.id] = round(total_ratings/service_ratings_length,1)
            context['provider_services'] = provider_services
            context['user'] = user
            context['service_ratings'] = service_ratings_data
            context['search_input'] = search_input
            return render(request, self.template_name, context=context)
        else:
            return render(request, self.template_name, context=context)

def create_service(request):
    if request.method == 'POST':
        form = ServicePostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = ServicePostForm()
    return render(request, 'create_service.html', {'form': form})
