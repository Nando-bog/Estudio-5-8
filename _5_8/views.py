#coding=utf-8
#Views para el proyecto general.
from django.views.generic.base import TemplateView


class QueEs(TemplateView):
    template_name='quees.html'