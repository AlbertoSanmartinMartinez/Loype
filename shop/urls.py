# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.conf.urls import url, include
from django.conf.urls.static import static
from shop import views as shop_views
from django.conf import settings

urlpatterns = [

    #General Shop Urls
    url(r'^tienda/$', shop_views.product_list, name='product_list'),

    # Category Urls
    url(r'^categorias/(?P<shop_category_slug>\w+)/$', shop_views.product_list, name='product_list_category'),

    # Product Urls
    url(r'^productos/(?P<product_slug>\w+)/$', shop_views.product_detail, name='product_detail'),

    #Search Urls
    url(r'^tienda/$', shop_views.shop_search, name='shop_search'),

    # Payments Urls
    url(r'^pago/$', shop_views.payment_checkout, name='payment_checkout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
