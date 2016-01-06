#coding=utf-8
#Views para el app Studley. Versión 0.1.

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import ClaseHerramienta, TipoHerramienta, HerramientaBase, Herramienta, Coleccion, ColeccionesHerramientas, ColeccionesHerramientasBase


class HerramientaClaseListView(ListView):
    model=ClaseHerramienta
    context_object_name='clases_herramientas'
    template_name='studley_landing.html'
    
#class HerramientaTestView(ListView):
    #model=ClaseHerramienta
    #context_object_name='clases_herramientas'
    #template_name='studley_index.html'


class HerramientaClaseDetailView(DetailView):
    model=ClaseHerramienta
    context_object_name='clase_herramienta'
    template_name='studley_clase.html'
    slug_field='nombre'
    slug_url_kwarg='nombre'
    
    def get_context_data(self, **kwargs):
        #Call the base implementation first to get a context
        context=super(HerramientaClaseDetailView, self).get_context_data(**kwargs)
        clase=ClaseHerramienta.objects.filter(nombre=self.kwargs['nombre'])
        tipos=TipoHerramienta.objects.filter(clase=clase).order_by('nombre')
        
        tipos_herramientas={}
        for tipo in tipos:
            herramientas_tipo=HerramientaBase.objects.filter(tipo=tipo)
            tipos_herramientas[tipo]=herramientas_tipo
        
        herramientas=HerramientaBase.objects.filter(clase=clase, tipo__isnull=True)
        context['tipos']=tipos
        context['tipos_herramientas']=tipos_herramientas
        context['herramientas']=herramientas
        return context


class HerramientaTipoDetailView(DetailView):
    model=TipoHerramienta
    context_object_name='tipo'
    template_name='studley_tipo.html'
    slug_field='nombre_corto'
    slug_url_kwarg='nombre_corto'
    
    def get_context_data(self, **kwargs):
        context=super(HerramientaTipoDetailView, self).get_context_data(**kwargs)
        tipo=TipoHerramienta.objects.filter(nombre_corto=self.kwargs['nombre_corto'])
        herramientas=HerramientaBase.objects.filter(tipo=tipo).order_by('nombre')
        context['herramientas']=herramientas
        return context


class HerramientaBaseDetailView(DetailView):
    model=HerramientaBase
    context_object_name='herramienta'
    template_name='studley_herramienta_base.html'
    slug_field='nombre_corto'
    slug_url_kwarg='nombre_corto'
    
    def get_context_data(self, **kwargs):
        context=super(HerramientaBaseDetailView, self).get_context_data(**kwargs)
        tipo=context['herramienta'].tipo
        mismo_tipo=HerramientaBase.objects.filter(tipo=tipo).exclude(nombre=context['herramienta'].nombre)
        context['mismo_tipo']=mismo_tipo
        misma_base=Herramienta.objects.filter(herramienta_base=context['herramienta'])
        if len(misma_base) == 0:
            misma_base=[{'modelo':'No hay versiones registradas.'}]
        context['misma_base']=misma_base
        return context
    

class HerramientaDetailView(DetailView):
    model=Herramienta
    context_object_name='herramienta'
    template_name='studley_herramienta_version.html'
    slug_field='pk'
    slug_url_kwarg='pk'
    
    def get_context_data(self, **kwargs):
        context=super(HerramientaDetailView, self).get_context_data(**kwargs)
        otras_versiones=Herramienta.objects.filter(herramienta_base=context['herramienta'].herramienta_base).exclude(pk=context['herramienta'].pk)
        context['otras_versiones']=otras_versiones
        return context
    
    
class ColeccionesListView(ListView):
    model = Coleccion
    context_object_name = 'colecciones'
    template_name='studley_colecciones.html'
    slug_field='nombre_corto'
    

class ColeccionDetailView(DetailView):
    model = Coleccion
    context_object_name = 'coleccion'
    template_name = 'studley_coleccion.html'
    slug_field = 'nombre_corto'
    slug_url_kwarg = 'nombre_corto'
    
    def get_context_data(self, **kwargs):
        context = super(ColeccionDetailView, self).get_context_data(**kwargs)
        coleccion = context['coleccion']
        herramientas = coleccion.herramientas_base.all()
        clases = {}
        for herramienta in herramientas:
            if herramienta.clase not in clases:
                clases[herramienta.clase] = {}
            if herramienta not in clases[herramienta.clase]:
                clases[herramienta.clase][herramienta] = []
                recomendaciones = ColeccionesHerramientas.objects.filter(recomendada_para=ColeccionesHerramientasBase.objects.filter(coleccion = coleccion, herramienta_base = herramienta))
                #clases[herramienta.clase][herramienta]+=recomendaciones
                recomendar = []
                for recomendacion in recomendaciones:
                    recomendar.append(recomendacion.herramienta)
                clases[herramienta.clase][herramienta] += recomendar
        context['clases'] = clases
        #context['herramientas']=herramientas
        #context['herramientas_recomendadas']=herramientas_recomendadas
        return context
