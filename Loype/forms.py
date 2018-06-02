#!/usr/local/bin/python
# coding: utf-8

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# Login Forms
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Nombre o email de usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput())


# Register Forms
class CustomRegisterForm(UserCreationForm):
    """
    Formulario para de registro para usuarios
    https://docs.djangoproject.com/en/2.0/ref/forms/fields/
    """
    username = forms.CharField(label='Nombre de usuario')
    email = forms.EmailField(label='Email', widget=forms.EmailInput())
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ContactForm(forms.Form):
    """Formulario de contacto"""
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
    mensaje = forms.CharField(max_length=500)
