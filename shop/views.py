# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.template.response import TemplateResponse
from shop import models
from shop import forms
from payments import get_payment_model, RedirectNeeded
from Loype import settings

# Shop Views
def product_list(request, shop_category_slug=None):
    category = None
    products = models.Product.objects.filter(stock__gt=1)
    if shop_category_slug:
        category = get_object_or_404(models.ShopCategory, slug=shop_category_slug)
        products = products.filter(category=category)

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


def shop_search(request):
    form = forms.SearchForm(request.POST)
    if form.is_valid():
        word = form.cleaned_data['word']
        #posts = models.Post.objects.filter(status=1, title__contains=word).order_by("-creation_date")
        products = models.Product.objects.filter(stock__gt=1)
    else:
        form = getSearchForm
        products = None

    category = None

    return render(request, 'product_list.html', {
        'category': category,
        'products': products,
        'categories': getShopCategories()
    })

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


def payment_checkout(request):
    stripe_key = settings.STRIPE_TEST_API_KEY
    payment_checkout_form = forms.PaymentCheckput()

    """
    token = stripe.
    charge = stripe.Charge.create(
        amount=999,
        currency='usd',
        description='Example charge',
        source=token,
    )
    """
    return render(request, 'payment_checkout.html', {
        "payment_checkout_form": payment_checkout_form,
        "stripe_key": stripe_key,
    })


# Common Methods
def getShopCategories():
    return models.ShopCategory.objects.all()
