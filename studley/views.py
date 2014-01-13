#coding=utf-8
#Views para el app Studley. Versión 0.1.

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import HerramientaBase, ClaseHerramienta

class HerramientaListView(ListView):
    model=HerramientaBase
    context_object_name='herramientas'
    template_name='herramientas_index.html'


class HerramientaBaseDetailView(DetailView):
    model=ClaseHerramienta
    context_object_name='clase'
    template_name='herramientas_clase.html'
    slug_field='nombre'
    slug_url_kwarg='nombre'