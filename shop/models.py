# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from shop.decorators import autoconnect
from payments import PurchasedItem
from payments.models import BasePayment

# General Models
class CustomUser():
    pass


class Address(models.Model):
    pass


class BannkInformation(models.Model):
    pass


# Shop Models
@autoconnect
class ShopCategory(models.Model):
    """
    Model for categories from a shop
    """
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.CharField(max_length=500, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return self.name

    def pre_save(self):
        self.slug = self.name.replace(' ', '_').lower()


@autoconnect
class Product(models.Model):
    category = models.ForeignKey(ShopCategory)
    name = models.CharField(max_length=100, db_index=True, unique=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True, blank=True)
    description = models.CharField(max_length=500, blank=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now=True)
    stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    # images

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __unicode__(self):
        return self.name

    def pre_save(self):
        self.slug = self.name.replace(' ', '_').lower()

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.slug])


class ShopingChart(models.Model):
    # name = models.CharField(max_length=100, db_index=True)
    created_date = models.DateTimeField(auto_now=True)
    code = models.CharField(max_length=300, default="")
    products = models.CharField(max_length=300, default="")
    # controlar el estado del carrito
    # convertir en pedido cuando se finaliza el pedido
    # saber de quien es el carrito

    def __unicode__(self):
        return self.code


# https://www.wordstream.com/blog/ws/2016/03/17/shopping-cart-abandonment
class Order(models.Model):
    code = models.CharField(max_length=300, default="")
    created_date = models.DateTimeField(auto_now=True)
    OrderStatus = ((1, 'Pendiente de pago'), (2, 'Cancelado'), (3, 'Pagado'), (4, 'En preparación'), (5, 'Enviado'), (6, 'Entregado'))
    status = models.IntegerField(choices=OrderStatus, default=1)

    def __unicode__(self):
        return self.code


class Provider(models.Model):
    name = models.CharField(max_length=100, db_index=True, default='proveedor')
    created_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class ShopTag(models.Model):
    name = models.CharField(max_length=100, db_index=True, default='etiqueta')
    created_date = models.DateTimeField(auto_now=True)
    # slug

    def __unicode__(self):
        return self.name


# Gallery Models
class Image(models.Model):
    pass


# SEO Models
class MetaData(models.Model):
    pass


# Payment Models
class CustomPayment(BasePayment):

    def get_failure_url(self):
        pass

    def get_success_url(self):
        pass

    def get_purchased_url(self):
        pass


"""
https://www.youtube.com/watch?v=Z5dBopZWOzo
https://django-payments.readthedocs.io/en/latest/index.html

"""
