#coding=utf-8
# roubo.urls
# URLS para el app "Roubo"
# Version 0.1

from django.conf.urls import patterns, url
from .views import RecursoDetailView, DesempenoDeComprensionDetailView, CursoListView, CursoInicioDetailView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', '_5_8.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'recurso/(?P<tipo>[A-Z]{3})/(?P<nombre_corto>[A-Za-z0-9-_]+)/?$', RecursoDetailView.as_view(), name='recurso_detalle'),
    url(r'leccion/(?P<nombre_corto>[A-Za-z0-9-_]+)/?$', DesempenoDeComprensionDetailView.as_view(), name='desempeno_detalle'),
    url(r'curso/(?P<codigo>[A-Z0-9-]{6,12})/?$', CursoInicioDetailView.as_view(), name='curso_inicio'),
    url(r'', CursoListView.as_view(), name='curso_lista'),
)
