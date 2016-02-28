# coding=utf-8
# Formularios para todo el sitio. Búsqueda, contacto, etc.
# Version 0.1

from django import forms
from django.forms import Form, CharField, TextInput


class SiteSearch(Form):
    """Simple formulario para buscar en todo el sitio.
    """
    query = CharField(
        label="",
        max_length=500,
        widget=TextInput(attrs={'size': '20'}))
