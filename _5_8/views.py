#coding=utf-8
#Views para el proyecto general.

from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.db.models import Q
import watson
from .forms import SiteSearch
from roubo.models import Recurso, Destacado
from studley.models import ClaseHerramienta

# class HomePage(TemplateView):
    # template_name='index-fp.html'

class ElEstudio(TemplateView):
    template_name='quees.html'
    
def home_page(request, *args, **kwargs):
    """Retorna los destacados para la página de inicio.
    """
    search_form = SiteSearch()
    contexto = {}
    destacado_blog = Q(recurso__tipo = 'BLG')
    destacado_tutorial = Q(recurso__tipo = 'TUT')
    destacado_documento = Q(recurso__tipo = 'DOC')
    destacado_proyecto = Q(recurso__tipo = 'PRY')
    destacado_video = Q(recurso__tipo = 'VID')
    destacado_galeria = Q(recurso__tipo = 'GLR')
    q_filter_destacado = destacado_proyecto | destacado_blog | destacado_tutorial | destacado_documento | destacado_video | destacado_galeria
    destacados = Destacado.objects.filter(q_filter_destacado).order_by('-sticky', 'orden', '-recurso__fecha_actualizacion')
    contexto['destacados_roubo'] = destacados
    clases_herramientas = ClaseHerramienta.objects.all().order_by('nombre')
    contexto['herramientas'] = clases_herramientas
    contexto['search_form'] = search_form
    return render(
        request,
        'index-fp.html',
        contexto,
    )
    
def dynamic_css(request):
    return render(
        request,
        '5-8-styles-dynamic.css',
        {'background' : 'background-home-1.jpg'},
        content_type="text/css")

def site_search(request):
    """Site wide search implemented with django-watson
    """
    if request.POST:
        super_search_form = SiteSearch(request.POST)
        if super_search_form.is_valid():
            results = watson.search.search(request.POST['query'])
            #results = ''
            return render(
                request,
                'search_results.html',
                # {'super_search_form': super_search_form,'results': results, 'req': request.POST}
                {'super_search_form': super_search_form,'results': results, 'query': request.POST['query']}
            )
    else:
        super_search_form = SiteSearch()
        results = ''
        return render(
            request,
            'search_results.html',
            {'super_search_form': super_search_form}
        )