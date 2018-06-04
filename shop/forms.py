#!/usr/local/bin/python
# coding: utf-8

from django import forms
from shop import models as shop_models
#from shop.templatetags import calculateStockItem

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)]
#totalStock = calculateStockItem()

# General Forms
class SearchForm(forms.Form):
    """Formulario de busqueda"""
    word = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Busca lo que quieras'}))


class PaymentCheckout(forms.Form):
    credir_card_number = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Número de tarjeta'}))
    credir_card_date = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Número de tarjeta'}))
    credir_card_code = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Número de tarjeta'}))


class ProductFilter(forms.ModelForm):
    #category = forms.ChoiceField(label='Categoria', required=False)
    #category = forms.ModelForm()
    name = forms.CharField(label='Nombre', required=False, widget=forms.TextInput(attrs={'placeholder':'Busca un producto'}))
    price = forms.CharField(label='Precio', required=False)
    stock = forms.BooleanField(label='En stock', required=False)

    def __init__(self, user, *args, **kwargs):
        super(ProductFilter, self).__init__(*args, **kwargs)
        self.fields['category'] = forms.ModelChoiceField(
            label='Categoria',
            required=False,
            queryset=shop_models.ShopCategory.objects.all())

    class Meta:
        model = shop_models.Product
        #include = ['category', 'name', 'price']
        exclude = ['description', 'slug']


class ShoppingCartForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    #update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


#
