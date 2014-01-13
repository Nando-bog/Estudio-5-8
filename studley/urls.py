#coding=utf-8
# URLS para el app "Studley"
# studley.urls
# Version 0.1

from django.conf.urls import patterns, url
from .views import HerramientaListView, HerramientaBaseDetailView

urlpatterns = patterns('',
    url(r'herramientas/(?P<nombre_corto>[A-Z]{1,30})/?$', HerramientaListView.as_view(), name='herramientas_lista'),
    url(r'herramientas/?$', HerramientaListView.as_view(), name='herramientas_lista'),
    url(r'clases/(?P<nombre>[A-Za-z]{1,30})/?$', HerramientaBaseDetailView.as_view(), name='herramientas_clase'),
    url(r'$', HerramientaListView.as_view(), name='herramientas_lista'),
)
