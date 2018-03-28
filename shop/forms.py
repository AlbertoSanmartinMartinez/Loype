#!/usr/local/bin/python
# coding: utf-8

from django import forms

# General Forms
class ContactForm(forms.Form):
    """Formulario de contacto"""
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
    mensaje = forms.CharField(max_length=500)
