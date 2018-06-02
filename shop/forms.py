#!/usr/local/bin/python
# coding: utf-8

from django import forms

# General Forms
class SearchForm(forms.Form):
    """Formulario de busqueda"""
    word = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Busca lo que quieras'}))


class PaymentCheckput(forms.Form):
    credir_card_number = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Número de tarjeta'}))
    credir_card_date = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Número de tarjeta'}))
    credir_card_code = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Número de tarjeta'}))
