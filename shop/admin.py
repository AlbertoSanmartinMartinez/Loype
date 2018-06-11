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


class ShopingChartAdmin(admin.ModelAdmin):
    list_display = ['code', 'created_date', 'products']

admin.site.register(models.ShopingChart, ShopingChartAdmin)


class ProviderAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_date']

admin.site.register(models.Provider, ProviderAdmin)


class ShopTagAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_date']

admin.site.register(models.ShopTag, ShopTagAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['code', 'created_date', 'status']

admin.site.register(models.Order, OrderAdmin)

class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'description', 'alt', 'album')

class ImageInLine(admin.TabularInline):
    model = models.Image
    list_display = ('id', 'image', 'description', 'alt')
    extra = 1

admin.site.register(models.Image, ImageAdmin)

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    inlines = [ImageInLine,]

admin.site.register(models.Album, AlbumAdmin)

#
