# coding=utf-8
# Views que integran el home para el proyecto general.
# Version 0.1
# Django/Python Libs.
from random import choice
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType
# 3rd party libs
import watson
# Project libs
from .forms import SiteSearch
from .models import DestacadoHome, ImagenFondoHome
from roubo.models import Recurso, Destacado
from studley.models import ClaseHerramienta


class ElEstudio(TemplateView):
    template_name = 'quees.html'


def home_page(request, *args, **kwargs):
    """Return destacados del home del sitio"""
    search_form = SiteSearch()
    contexto = {}
    # Destacados de roubo
    videos_destacados = []
    cuadernos_destacados = []  # agrupa tipos distintos de roubo... confuso... pero bueno: blogs, tutoriales, proyectos y documentos, segun recurso.tipo
    galerias_destacadas = []
    # Destacados de studley
    herramientas_destacadas = []
    destacados = DestacadoHome.objects.all().order_by('-fecha_creacion')
    for destacado in destacados:
        if ContentType.objects.get_for_model(destacado.contenido_destacado).model == 'recurso':
            if destacado.contenido_destacado.tipo == 'VID':
                videos_destacados.append(destacado.contenido_destacado)
            elif (destacado.contenido_destacado.tipo == 'BLG') | (destacado.contenido_destacado.tipo == 'PRY') | (destacado.contenido_destacado.tipo == 'TUT') | (destacado.contenido_destacado.tipo == 'DOC'):
                cuadernos_destacados.append(destacado.contenido_destacado)
            elif destacado.contenido_destacado.tipo == 'GLR':
                galerias_destacadas.append(destacado.contenido_destacado)
            elif destacado.contenido_destacado.tipo == 'PRY':
                proyectos_destacados.append(destacado.contenido_destacado)
        elif (ContentType.objects.get_for_model(destacado.contenido_destacado).model == 'tipoherramienta') | (ContentType.objects.get_for_model(destacado.contenido_destacado).model == 'herramientabase') | (ContentType.objects.get_for_model(destacado.contenido_destacado).model == 'herramienta') | (ContentType.objects.get_for_model(destacado.contenido_destacado).model == 'coleccion'):
            herramientas_destacadas.append(destacado.contenido_destacado)

    # Destacados por sección
    contexto['videos_destacados'] = videos_destacados[0:1]
    contexto['cuadernos_destacados'] = cuadernos_destacados[0:1]
    contexto['galerias_destacadas'] = galerias_destacadas[0:1]
    contexto['herramientas_destacadas'] = herramientas_destacadas[0:1]
    contexto['search_form'] = search_form

    return render(
        request,
        'index.html',
        contexto,
    )


def dynamic_css(request):
    return render(
        request,
        '5-8-styles-dynamic.css',
        {'background': 'background-home-1.jpg'},
        content_type="text/css",
    )


def dynamic_css_1(request):
    # imagen de fondo
    imagen_fondo = ImagenFondoHome.objects.all()[0]
    return render(
        request,
        '5-8-styles-dynamic-1.css',
        {'background': imagen_fondo.imagen},
        content_type="text/css",
    )


def site_search(request):
    """Site wide search implemented with django-watson
    """
    if request.POST:
        # if request.POST['query'] == '':
        #     results = watson.search.search('')
        #     super_search_form = SiteSearch()
        #     return render(
        #         request,
        #         'search_results.html',
        #         {'super_search_form': super_search_form,'results': results, 'query': request.POST['query']}
        #     )
        super_search_form = SiteSearch(request.POST)
        if super_search_form.is_valid():
            results = watson.search.search(request.POST['query'])
            return render(
                request,
                'search_results.html',
                {'super_search_form': super_search_form, 'results': results, 'query': request.POST['query']}
            )
        else:
            query = 'Búsqueda 5-8'
            results = [{'title': 'No buscó nada. Por favor inténtelo de nuevo.'}]
            return render(
                request,
                'search_results.html',
                {'super_search_form': SiteSearch(), 'results': results, 'query': query}
            )
    else:
        super_search_form = SiteSearch()
        results = ''
        return render(
            request,
            'search_results.html',
            {'super_search_form': super_search_form}
        )


def handler404(request):
    response = render(request, '404.html', {'request': request})
    return response


def handler500(request):
    response = render(request, '500.html', {'request': request})
    return response
