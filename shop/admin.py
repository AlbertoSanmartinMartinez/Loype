# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from shop import models

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_date', 'stock', 'price']
    #list_filter = ['name', 'created_date', 'stock', 'price']
    #list_editable = ['name', 'created_date', 'stock']
    #search_fields = ['name', 'created_date', 'stock', 'price']
    # prepopulated_fields

admin.site.register(models.Product, ProductAdmin)


class ShopCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'parent']
    #list_filter = ['name', 'description', 'parent']
    #list_editable = ['name', 'description', 'parent']
    #search_fields = ['name', 'description', 'parent']
    # prepopulated_fields

admin.site.register(models.ShopCategory, ShopCategoryAdmin)

"""
class ShopingChartAdmin(admin.ModelAdmin):

admin.site.register(models.ShopingChart, ShopingChartAdmin)


class ProviderAdmin(admin.ModelAdmin):

admin.site.register(models.Provider, ProviderAdmin)


class ShopTagAdmin(admin.ModelAdmin):

admin.site.register(models.ShopTag, ShopTagAdmin)
"""
