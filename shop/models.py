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
    name = models.CharField(max_length=100, db_index=True)

    def __unicode__(self):
        return self.name


class Provider(models.Model):
    name = models.CharField(max_length=100, db_index=True, default='proveedor')

    def __unicode__(self):
        return self.name


class ShopTag(models.Model):
    name = models.CharField(max_length=100, db_index=True, default='etiqueta')
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
