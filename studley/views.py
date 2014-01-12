from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Herramienta


class HerramientaListView(ListView):
    model=Herramienta
    context_object_name='herramientas'
    template_name='herramientas_index.html'

