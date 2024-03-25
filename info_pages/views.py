from django.shortcuts import render
from django.views import View
from user.models import User
from info_pages.models import *
from info_pages.forms import *
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.urls import reverse_lazy, reverse
from pyexpat.errors import messages
# Create your views here.

class AboutUsView(View):
    template_name = 'aboutus/about-us.html'
    base_template = 'base.html'

    def get(self, request, *args, **kwargs):
        context = {"base_template":self.base_template, "active_header":"about"}
        try:
            user_id = request.user_id
            user = User.objects.get(pk = user_id)
            context['user_type'] = user.user_type.user_type
            context['user'] = user
        except Exception as e:
            pass
        return render(request, self.template_name, context=context)


class ContactUsView(View):
    template_name = 'contactus/contact-us.html'
    base_template = 'base.html'

    def get(self, request, *args, **kwargs):
        context = {"base_template":self.base_template, "active_header":"contactus"}
        form = ContactUsForm()
        context['form'] = form
        try:
            user_id = request.user_id
            user = User.objects.get(pk = user_id)
            context['user_type'] = user.user_type.user_type
            context['user'] = user
        except Exception as e:
            pass
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        context = {"base_template":self.base_template, "active_header":"contactus"}
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('info_pages:contact_us')
        context['form'] = form
        context['alert'] = "Submitted Successfully."
        return render(request, self.template_name, context=context)

class PrivacyPolicyView(View):
    template_name = 'privacypolicy/privacy-policy.html'
    base_template = 'base.html'

    def get(self, request, *args, **kwargs):
        context = {"base_template":"base.html"}
        try:
            user_id = request.user_id
            user = User.objects.get(pk = user_id)
            context['user_type'] = user.user_type.user_type
            context['user'] = user
        except Exception as e:
            pass
        return render(request, self.template_name, context=context)

class TermsAndConditionsView(View):
    template_name = 'termsncondition/terms-and-condition.html'
    base_template = 'base.html'

    def get(self, request, *args, **kwargs):
        context = {"base_template":"base.html"}
        try:
            user_id = request.user_id
            user = User.objects.get(pk = user_id)
            context['user_type'] = user.user_type.user_type
            context['user'] = user
        except Exception as e:
            pass
        return render(request, self.template_name, context=context)