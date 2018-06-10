# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.conf.urls import url, include
from django.conf.urls.static import static
from shop import views as shop_views
from django.conf import settings

urlpatterns = [

    # Products Shop Urls
    url(r'^productos/$', shop_views.product_list, name='product_list'),
    url(r'^productos/(?P<product_slug>\w+)/$', shop_views.product_detail, name='product_detail'),

    # Category Urls
    url(r'^categorias/(?P<shop_category_slug>\w+)/$', shop_views.product_list, name='product_list_category'),

    #Search Urls
    #url(r'^productos/resultado_busqueda$', shop_views.shop_search, name='shop_search'),
    url(r'^productos/$', shop_views.product_list, name='shop_search'),

    # Payments Urls
    url(r'^pago/realizado$', shop_views.payment_done, name='payment_done'),
    url(r'^pago/cancelado$', shop_views.payment_canceled, name='payment_canceled'),
    url(r'^pago/$', shop_views.payment_checkout, name='payment_checkout'),

    # ShopingChart Urls
    url(r'^carrito/$', shop_views.cartDetail, name='shoppingcart_detail'),
    url(r'^carrito/añadir/(?P<product_id>\d+)/$', shop_views.cartAdd, name='shoppingcart_add'),
    url(r'^carrito/borrar/(?P<product_id>\d+)/$', shop_views.cartRemove, name='shoppingcart_remove'),
    url(r'^carrito/actualizar/(?P<product_id>\d+)/$', shop_views.cartUpdate, name='shoppingcart_update'),
]
