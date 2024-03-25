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
def about_us(request):
    context = {"base_template":"base.html", "active_header":"about"}
    return render(request, 'aboutus/about-us.html', context=context)

def privacy_policy(request):
    context = {"base_template":"base.html"}
    return render(request, 'privacypolicy/privacy-policy.html', context=context)

def terms_n_conditions(request):
    context = {"base_template":"base.html"}
    return render(request, 'termsncondition/terms-and-condition.html', context=context)


class ContactUsView(View):
    template_name = 'contactus/contact-us.html'
    base_template = 'base.html'

    def get(self, request, *args, **kwargs):
        context = {"base_template":self.base_template, "active_header":"about"}
        form = ContactUsForm()
        context['form'] = form
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        context = {"base_template":self.base_template, "active_header":"about"}
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('info_pages:contact_us')
        context['form'] = form
        context['alert'] = "Submitted Successfully."
        return render(request, self.template_name, context=context)