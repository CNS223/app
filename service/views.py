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

class ServiceDetailView(View):
    template_name = 'services/service-detail.html'
    base_template = 'base.html'

    def get(self, request, provider_service):
        context = {'base_template': self.base_template}
        try:
            user = User.objects.get(pk=request.user_id)
            context['user_type'] = user.user_type.user_type
            context['user'] = user
            provider_service = ProviderService.objects.get(pk = provider_service)
            service_availability = ProviderAvailability.objects.filter(service = provider_service)
            context['provider_service'] = provider_service
            context['service_availability'] = service_availability
        except Exception as e:
            pass
        return render(request, self.template_name, context=context)

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


class ServiceCreateView(View):
    template_name = 'services/service-create.html'
    base_template = 'base.html'
    active_header = 'providers'
    form_class = ServiceCreateForm

    def get_initial_data(self, provider_service=None, service_avalibilities=None):
        initial_data = {}
        if provider_service:
            initial_data = {
                'title': provider_service.title,
                'category': provider_service.category.name,
                'price': provider_service.price,
                'description': provider_service.desc,
                'add1': provider_service.address.add1,
                'add2': provider_service.address.add2,
                'country': provider_service.address.country,
                'city': provider_service.address.city,
                'provision': provider_service.address.provision,
                'pincode': provider_service.address.postal_code,
                'image': provider_service.picture
            }
            initial_data = set_availability_initial_data(initial_data, provider_service)

        return initial_data

    def get(self, request, *args, **kwargs):
        context = {"base_template": self.base_template, "active_header": self.active_header}
        provider_service_id = request.GET.get('provider_service_id', None)
        try:
            user = User.objects.get(pk=request.user_id)
            context['user_type'] = user.user_type.user_type
            context['user'] = user
            if provider_service_id is not None:
                provider_service = ProviderService.objects.get(pk=provider_service_id, provider=user)
                initial_data = self.get_initial_data(provider_service)
                context['initial_data'] = initial_data
                form = self.form_class(initial=initial_data)
            else:
                print("No provider_service_id provided")
                form = self.form_class()
            context['form'] = form
            context['category'] = ServiceCategory.objects.all()
            if request.GET.get('error', None) is not None:
                context['alert'] = request.GET.get('error')
            if request.GET.get('updated', None) is not None:
                context['alert'] = "Updated Service Successfully."
            return render(request, self.template_name, context=context)
        except Exception as e:
            print("187----", e)
            print("Exception:", e)  # Print any exceptions for debugging
            return redirect('user:user_signin')

    def post(self, request, *args, **kwargs):
        provider_service_id = request.GET.get('provider_service_id', None)
        context = {"base_template": self.base_template, "active_header": self.active_header}
        form = self.form_class(request.POST, request.FILES)
        context['form'] = form
        provider_service_id = request.GET.get('provider_service_id', None)
        if provider_service_id is not None:
            provider_service = ProviderService.objects.get(pk=provider_service_id)
        else:
            provider_service = None
        user = User.objects.get(pk=request.user_id)
        if form.is_valid():
            title = form.cleaned_data['title']
            category = form.cleaned_data['category']
            price = form.cleaned_data['price']
            description = form.cleaned_data['description']
            monday_from_time = form.cleaned_data['monday_from_time']
            monday_to_time = form.cleaned_data['monday_to_time']
            tuesday_from_time = form.cleaned_data['tuesday_from_time']
            tuesday_to_time = form.cleaned_data['tuesday_to_time']
            wednesday_from_time = form.cleaned_data['wednesday_from_time']
            wednesday_to_time = form.cleaned_data['wednesday_to_time']
            thursday_from_time = form.cleaned_data['thursday_from_time']
            thursday_to_time = form.cleaned_data['thursday_to_time']
            friday_from_time = form.cleaned_data['friday_from_time']
            friday_to_time = form.cleaned_data['friday_to_time']
            saturday_from_time = form.cleaned_data['saturday_from_time']
            saturday_to_time = form.cleaned_data['saturday_to_time']
            sunday_from_time = form.cleaned_data['sunday_from_time']
            sunday_to_time = form.cleaned_data['sunday_to_time']
            add1 = form.cleaned_data['add1']
            add2 = form.cleaned_data['add2']
            country = form.cleaned_data['country']
            city = form.cleaned_data['city']
            provision = form.cleaned_data['provision']
            pincode = form.cleaned_data['pincode']
            image = request.FILES.get('image')
            if provider_service:
                pass
            else:
                provider_service, created = ProviderService.objects.get_or_create(title=title, provider=user)
            if provider_service.address:
                address = provider_service.address
            else:
                address = Address.objects.create(address_type='serviceprovider')
            category = ServiceCategory.objects.get(name=category)
            provider_service.category = category
            provider_service.title = title
            provider_service.price = price
            provider_service.active = True
            provider_service.desc = description
            provider_service.address = address
            if image:
                provider_service.picture = image
            provider_service.save()
            monday_avail, created = create_or_update_availability(provider_service, "Monday", True, monday_from_time,
                                                                  monday_to_time)
            tuesday_avail, created = create_or_update_availability(provider_service, "Tuesday", True, tuesday_from_time,
                                                                   tuesday_to_time)
            wed_avail, created = create_or_update_availability(provider_service, "Wednesday", True, wednesday_from_time,
                                                               wednesday_to_time)
            thurs_avail, created = create_or_update_availability(provider_service, "Thursday", True, thursday_from_time,
                                                                 thursday_to_time)
            friday_avail, created = create_or_update_availability(provider_service, "Friday", True, friday_from_time,
                                                                  friday_to_time)
            saturday_avail, created = create_or_update_availability(provider_service, "Saturday", True,
                                                                    saturday_from_time, saturday_to_time)
            sunday_avail, created = create_or_update_availability(provider_service, "Sunday", True, sunday_from_time,
                                                                  sunday_to_time)

            address.add1 = add1
            address.add2 = add2
            address.city = city
            address.provision = provision
            address.country = country
            address.postal_code = pincode
            address.save()
        else:
            print("Form is not valid")
            print("Errors:", form.errors)
            return HttpResponseRedirect(
                reverse('service:service_create') + f'?provider_service_id={provider_service.id}')

        # Process POST request data here
        return HttpResponseRedirect(
            reverse('service:service_create') + f'?provider_service_id={provider_service.id}&updated=true')


