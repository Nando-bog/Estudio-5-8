#coding=utf-8
# URLS para el app "Studley"
# studley.urls
# Version 0.1

from django.conf.urls import patterns, url
from .views import HerramientaListView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', '_5_8.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'herramientas/(?P<nombre_corto>[A-Z]{1,30})/?$', HerramientaListView.as_view(), name='herramientas_lista'),
    url(r'herramientas/?$', HerramientaListView.as_view(), name='herramientas_lista'),
    url(r'/?$', HerramientaListView.as_view(), name='herramientas_lista'),
)
