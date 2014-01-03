#coding=utf-8
# URLS para el app "Cursos"
# Version 0.1

from django.conf.urls import patterns, url
from .views import RecursoDetailView, DesempenoDeComprensionDetailView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', '_5_8.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'recurs/(?P<tipo>[A-Z]{3})/(?P<nombre_corto>[A-Za-z0-9-_]+)/?$', RecursoDetailView.as_view(), name='recurso_detalle'),
    url(r'leccion/(?P<nombre_corto>[A-Za-z0-9-_]+)/?$', DesempenoDeComprensionDetailView.as_view(), name='desempeno_detalle'),
)
