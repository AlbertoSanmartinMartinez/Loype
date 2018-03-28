# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.template.response import TemplateResponse
from shop import models
from shop import forms
from payments import get_payment_model, RedirectNeeded

# General Views
def home(request):
    return render(request, 'home.html', {})


def know_us(request):
    return render(request, 'know_us.html', {})


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
    }
    return render(request, "contact.html", context)


# Shop Views
def product_list(request, shop_category_slug=None):
    category = None
    products = models.Product.objects.filter(stock__gt=1)
    if shop_category_slug:
        category = get_object_or_404(models.ShopCategory, slug=shop_category_slug)
        products = products.filter(category=category)
    print(products)
    return render(request, 'product_list.html', {
        'category': category,
        'products': products,
        'categories': getShopCategories()
    })


def product_detail(request, product_slug):
    product = get_object_or_404(models.Product, slug=product_slug)
    # formularios
    return render(request, 'product_detail.html', {
        'product': product,
        'categories': getShopCategories()
    })


def shoping_chart(request):
    pass


# Payment Views
def payment_details(request, payment_id):
    payment = get_object_or_404(get_payment_model(), id=payment_id)
    try:
        form = payment.get_form(data=request.POST or None)
    except RedirectNeeded as redirect_to:
        return redirect(str(redirect_to))

    return TemplateResponse(request, 'payment.html', {
        'form': form,
        'payment': payment
    })


# Common Methods
def getShopCategories():
    return models.ShopCategory.objects.all()
