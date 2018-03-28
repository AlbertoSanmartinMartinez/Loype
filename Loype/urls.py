# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin
from shop import views
from shop import urls

admin.site.site_header = 'LOYPE'
admin.autodiscover()

urlpatterns = [

    url(r'^administracion/', admin.site.urls),

    url(r'^tienda/', include('shop.urls', namespace='shop')),

    url(r'^$', views.home, name='home'),
]
