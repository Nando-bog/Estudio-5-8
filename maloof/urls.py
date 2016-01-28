#coding=utf-8
# roubo.urls
# URLS para el app "Roubo"
# Version 0.1

from django.conf.urls import url
from django.views.generic.simple import direct_to_template

from .views import CuadernoListView, RecursoDetailView#, VideoDetailView #, DesempenoDeComprensionDetailView, CursoListView, CursoInicioDetailView

urlpatterns = [
    url(r'(/', direct_to_template, name='perfil'),
]




url(r'^accounts/profile/', direct_to_template, { 'template' : 'profile.html' }),