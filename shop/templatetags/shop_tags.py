#!/usr/local/bin/python
# coding: utf-8

from django import template
from django.shortcuts import render

register = template.Library()

@register.simple_tag
def calculateStockItem(product_id):
    product = shop_models.Product.objects.filter(id=product_id)

    return product.stock
