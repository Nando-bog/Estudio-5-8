#coding=utf-8
# URLS para el proyecto _5_8
# Version 0.2
from django.conf import settings
from django.conf.urls import include, url, static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from .views import ElEstudio, HomePage, dynamic_css, home_page
from roubo.views import contacto
admin.autodiscover()

urlpatterns = [
    url(r'^(index)?(home)?(.html)?/?$',  home_page),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^roubo/', include('roubo.urls')),
    url(r'^studley/', include('studley.urls')),
    url(r'el-estudio/?$',  ElEstudio.as_view(), name='el-estudio'),
    url(r'styles/5-8-styles.css/?$', dynamic_css, name='css'),
    url(r'contacto/?$', contacto, name='contacto_sitio'),
    #url(r'^recursos/', include('cursos.urls')),
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns += [
#     url(r'^media/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
#     ]
# 
# urlpatterns += [
#     url(r'^static/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
#     ]