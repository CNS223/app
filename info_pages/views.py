from django.shortcuts import render

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

