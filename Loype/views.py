# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from Loype import forms
from shop import forms as shop_forms
from django.contrib.auth import authenticate, login, logout

# General Views
def home(request):
    #last_products = models.Product.objects.filter(status=1).order_by("-creation_date")[:3]

    return render(request, 'home.html', {
        #'last_products': last_products,
        "search_form": getSearchForm,
    })


def know_us(request):

    return render(request, 'know_us.html', {
        #"search_form": getSearchForm,
    })


def custom_login(request):
    if request.method == 'POST':
        form = forms.CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
    else:
        form = forms.CustomAuthenticationForm()

    return render(request, 'login.html', {
        #"search_form": getSearchForm,
        "form": form,
        #'subscribe_form': getSubscribeForm(),
    })


def custom_logout(request):
    logout(request)
    return redirect('home')


def register(request):
    if request.method == 'POST':
        form = forms.CustomRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = forms.CustomRegisterForm()

    return render(request, 'register.html', {
        #"search_form": getSearchForm,
        "form": form,
        #'subscribe_form': getSubscribeForm(),
    })


def contact(request):
    form = forms.ContactForm(request.POST or None)
    if form.is_valid():
        email_form = form.cleaned_data.get("email")
        message_form = form.cleaned_data.get("mensaje")
        name_form = form.cleaned_data.get("nombre")
        asunto = 'Mensaje de contacto'
        email_to = email
        email_from = settings.EMAIL_HOST_USER
        email_message = "%s: %a enviado por %s" %(name_form, message_form, email_form)
        send_mail(asunto, email_from, email_to, email_message, fail_silently=True)
    context = {
        "contact_form": form,
        #"search_form":getSearchForm(),
        #'subscribe_form': getSubscribeForm(),
    }
    return render(request, "contact.html", context)


def legal_information(request):

    return render(request, 'aviso_legal.html', {
        #"search_form":getSearchForm(),
        #'subscribe_form': getSubscribeForm(),
    })


def getSearchForm():
    return shop_forms.SearchForm()
