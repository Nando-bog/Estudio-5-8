#coding=utf-8
# URLS para el app "Studley"
# studley.urls
# Version 0.2

from django.conf.urls import url
from .views import HerramientaClaseListView, HerramientaClaseDetailView, HerramientaBaseDetailView, HerramientaTipoDetailView, HerramientaDetailView, ColeccionesListView, ColeccionDetailView

urlpatterns = [
    url(r'categorias/(?P<nombre>[A-Za-z0-9-_]{1,30})/?$', HerramientaClaseDetailView.as_view(), name='herramienta_clase_detalle'),
    url(r'categorias/$', HerramientaClaseListView.as_view(), name='herramientas_clase_lista'),
    url(r'tipos/(?P<nombre_corto>[A-Za-z0-9-_]{1,30})/?$', HerramientaTipoDetailView.as_view(), name='herramienta_tipo_detalle'),
    url(r'herramientas/(?P<nombre_corto>[A-Za-z0-9-_]{1,30})/?$', HerramientaBaseDetailView.as_view(), name='herramienta_base_detalle'),
    url(r'herramientas/herramienta/(?P<pk>[0-9]{1,100000})/?$', HerramientaDetailView.as_view(), name='herramienta_version_detalle'),
    url(r'colecciones/(?P<nombre_corto>[A-Za-z0-9-_]{1,30})/?$', ColeccionDetailView.as_view(), name='coleccion_detalle'),
    url(r'colecciones/$', ColeccionesListView.as_view(), name='colecciones_lista'),
    url(r'$', HerramientaClaseListView.as_view(), name='herramientas_clase_lista'),
]