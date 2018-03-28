# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render

# General Views
def home(request):
    return render(request, 'home.html', {})


# Shop Views
def product_list(request, shop_category_slug=None):
    category = None
    products= models.Product.objects.filter(stock>=1)
    if shop_category_slug:
        category = get_object_or_404(ShopCategory, slug=shop_category_slug)
        products = products.filter(category=category)

    return render(request, 'product_list.html', {
        'category': category,
        'products': products,
        'categories': getShopCategories()
    })


def product_detail(request, product_slug):
    product = get_object_or_404(slug=product_slug)
    # formularios
    return render(request, 'product_list.html', {
        'category': category,
        'product': product,
        'categories': getShopCategories()
    })


def shoping_chart(request):
    pass


# Common Methods
def getShopCategories():
    return models.ShopCategory.objects.all()
