# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.conf.urls import url, include
from shop import views
from django.conf import settings

urlpatterns = [
    url(r'^tienda/$', views.product_list, name='product_list'),

    url(r'^categorias/(?P<shop_category_slug>\w+)/$', views.product_list, name='product_list_category'),

    url(r'^productos/(?P<product_slug>\w+)/$', views.product_detail, name='product_detail'),
]
