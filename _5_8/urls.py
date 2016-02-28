# coding=utf-8
# URLS para el proyecto _5_8
# Version 0.2
from django.conf import settings
from django.conf.urls import include, url, static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.views.generic import RedirectView
# from .views import ElEstudio, dynamic_css, home_page, site_search
from roubo.views import contacto
from maloof.views import PerfilView
from cueva.views import ElEstudio, home_page, dynamic_css, dynamic_css_1, site_search
from cueva.feeds import SiteFeed
admin.autodiscover()

urlpatterns = [
    url(r'^(index)?(home)?(.html)?/?$', home_page),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^roubo/', include('roubo.urls')),
    url(r'^studley/', include('studley.urls')),
    url(r'el-estudio/?$', ElEstudio.as_view(), name='el-estudio'),
    url(r'styles/5-8-styles.css/?$', dynamic_css, name='css'),
    url(r'styles/5-8-styles-1.css/?$', dynamic_css_1, name='css'),
    url(r'contacto/?$', contacto, name='contacto_sitio'),
    url(r'rss/?$', SiteFeed()),
    url(r'q/?$', site_search, name='busqueda'),
    url(r'accounts/', include('allauth.urls')),
    url(r'cuenta/perfil/?$', PerfilView.as_view(), name='perfil'),
    url(r'accounts/profile/?$', RedirectView.as_view(url='/cuenta/perfil/')),
    # url(r'accounts/profile/?$', RedirectView.as_view(url='/cuenta/perfil/')),
    # url(r'accounts/?$', RedirectView.as_view(url='/cuenta/'))
]

urlpatterns += staticfiles_urlpatterns()

# urlpatterns += [
#    static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
#    ]
urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#

# urlpatterns += [
#     url(r'^media/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
#     ]
#
# urlpatterns += [
#     url(r'^static/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
#     ]