from django.db import connection

from django.shortcuts import render, redirect

from info_pages.forms import *


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

def contact_us(request):
    context = {"base_template":"base.html"}
    return render(request, 'contactus/contact-us.html', context=context)

def contact_us(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('info_pages:contact_success')
    else:
        form = contactForm()
    context = {'form': form}
    return render(request, 'contactus/contact-us.html', context)

def contact_success(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(id) FROM info_pages_contactus")
        feedback_count = cursor.fetchone()[0]
    # feedback_count = Feedback.objects.count()
    return render(request, 'contactus/contact-success.html',  {'feedback_count': feedback_count})