#coding=utf-8
# URLS para el proyecto _5_8
# Version 0.2
from django.conf import settings
from django.conf.urls import patterns, include, url, static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', '_5_8.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^cursos/', include('roubo.urls')),
    url(r'^studley/', include('studley.urls')),
    #url(r'^recursos/', include('cursos.urls')),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )