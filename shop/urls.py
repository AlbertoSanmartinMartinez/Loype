# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.conf.urls import url, include
from django.conf.urls.static import static
from shop import views
from django.conf import settings

urlpatterns = [

    # Category Urls
    url(r'^categorias/(?P<shop_category_slug>\w+)/$', views.product_list, name='product_list_category'),

    # Product Urls
    url(r'^productos/(?P<product_slug>\w+)/$', views.product_detail, name='product_detail'),

    # Payments Urls
    url('^payments/', include('payments.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
