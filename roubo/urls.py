#coding=utf-8
# roubo.urls
# URLS para el app "Roubo"
# Version 0.1

from django.conf.urls import url
from .views import CuadernoListView, RecursoDetailView#, VideoDetailView #, DesempenoDeComprensionDetailView, CursoListView, CursoInicioDetailView

urlpatterns = [
    url(r'(?P<tipo>[A-Z]{3})/?$', CuadernoListView.as_view(), name = 'lista_cuaderno_con_tipo'),
    url(r'(?P<tipo>cuaderno)/?$', CuadernoListView.as_view(), name = 'lista_cuaderno'),
    #url(r'videos/?$', VideosListView.as_view(), name = 'lista_videos'),
    url(r'recurso/(?P<tipo>[A-Z]{3})/(?P<nombre_corto>[A-Za-z0-9-_]+)/?$', RecursoDetailView.as_view(), name='recurso_detalle'),
    #url(r'leccion/(?P<nombre_corto>[A-Za-z0-9-_]+)/?$', DesempenoDeComprensionDetailView.as_view(), name='desempeno_detalle'),
    #url(r'curso/(?P<codigo>[A-Z0-9-]{6,12})/?$', CursoInicioDetailView.as_view(), name='curso_inicio'),
    #url(r'', CursoListView.as_view(), name='curso_lista'),
]