# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin
from shop import views
from shop import urls

admin.site.site_header = 'LOYPE'
admin.autodiscover()

urlpatterns = [

    # Administration Urls
    url(r'^administracion/', admin.site.urls),

    # Shop Urls
    url(r'^tienda/', include('shop.urls', namespace='shop')),
    url(r'^tienda/$', views.product_list, name='product_list'),

    # General Urls
    url(r'^$', views.home, name='home'),
    url(r'^conocenos/$', views.know_us, name='know_us'),
    url(r'^contacto/', views.contact, name='contact'),
    url(r'^contacto/', views.contact, name='profile'),

    # Register Urls
    url(r'^contacto/', views.contact, name='logout'),

    # Profile Urls
    url(r'^contacto/', views.contact, name='profile'),
    url(r'^tienda/$', views.product_list, name='ships'),
]
