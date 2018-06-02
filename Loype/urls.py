# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin
from shop import views as shop_views
from shop import urls
import views as general_views
from django.contrib.auth import views as auth_views

admin.site.site_header = 'LOYPE'
admin.autodiscover()

urlpatterns = [

    # Administration Urls
    url(r'^administracion/', admin.site.urls),

    # Shop Urls
    url(r'^tienda/', include('shop.urls', namespace='shop')),
    #url(r'^tienda/$', shop_views.product_list, name='product_list'),

    # General Urls
    url(r'^$', general_views.home, name='home'),
    url(r'^conocenos/$', general_views.know_us, name='know_us'),
    url(r'^contacto/', general_views.contact, name='contact'),
    url(r'^informacion_legal/', general_views.legal_information, name='legal_information'),

    # Register Urls
    url(r'^acceso/login$', general_views.login, name='login'),
    url(r'^acceso/registro$', general_views.register, name='register'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

    url(r'^mi_cuenta/password_change/$', auth_views.PasswordChangeView.as_view(), name='password_change'),
    url(r'^mi_cuenta/password_change_done/$', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    url(r'^mi_cuenta/password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    url(r'^mi_cuenta/password_reset_done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^mi_cuenta/password_confirm/$', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^mi_cuenta/password_reset_complete/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # Profile Urls
    url(r'^perfil/', general_views.contact, name='profile'),
    url(r'^tienda/$', shop_views.product_list, name='ships'),
]
