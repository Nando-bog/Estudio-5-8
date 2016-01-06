#coding=utf-8
# Views para la aplicación "Roubo"
#Version 0.1
from datetime import date
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.db.models import Q
from django.forms import ValidationError
from random import choice
from .models import Recurso, Destacado #, DesempenoDeComprension, Curso
from .forms import ContactoForm



class CuadernoListView(ListView):
    model = Recurso
    template_name = 'roubo_cuaderno_landing.html'
    context_object_name = 'entradas'
    
    destacado_blog = Q(recurso__tipo = 'BLG')
    destacado_tutorial = Q(recurso__tipo = 'TUT')
    destacado_documento = Q(recurso__tipo = 'DOC')
    destacado_proyecto = Q(recurso__tipo = 'PRY')
    destacado_video = Q(recurso__tipo = 'VID')
    destacado_galeria = Q(recurso__tipo = 'GLR')
    blog = Q(tipo = 'BLG')
    tutorial = Q(tipo = 'TUT')
    documento = Q(tipo = 'DOC')
    proyecto = Q(tipo = 'PRY')
    video = Q(tipo = 'VID')
    galeria = Q(tipo = 'GLR')
    
    def get_queryset(self, **kwargs):
        if self.kwargs['tipo'] == 'VID':
            q_filter = self.video
            q_filter_destacado = self.destacado_video
        elif self.kwargs['tipo'] == 'GLR':
            q_filter = self.galeria
            q_filter_destacado = self.destacado_galeria
        else:
            q_filter = self.blog | self.tutorial | self.documento | self.proyecto
            q_filter_destacado = self.destacado_proyecto | self.destacado_blog | self.destacado_tutorial | self.destacado_documento
        destacados = Destacado.objects.filter(q_filter_destacado).order_by('-sticky', 'orden')
        if len(destacados) > 0:
            entrada_destacada = destacados[0].recurso.pk
        else:
            entrada_destacada = 0
        entradas = Recurso.objects.filter(q_filter).exclude(pk = entrada_destacada)
        return entradas

    def get_context_data(self, **kwargs):
        context = super(CuadernoListView, self).get_context_data(**kwargs)
        # for destacado in self.destacados:
        #     self.entradas_destacadas.append(destacado.recurso.pk)
        if self.kwargs['tipo'] == 'VID':
            q_filter = self.video
            q_filter_destacado = self.destacado_video
        elif self.kwargs['tipo'] == 'GLR':
            q_filter = self.galeria
            q_filter_destacado = self.destacado_galeria
        else:
            q_filter = self.blog | self.tutorial | self.documento | self.proyecto
            q_filter_destacado = self.destacado_proyecto | self.destacado_blog | self.destacado_tutorial | self.destacado_documento
            
        destacados = Destacado.objects.filter(q_filter_destacado).order_by('-sticky', 'orden')
        if len(destacados) > 0:
            destacados = destacados[0].recurso
        context['destacados'] = destacados
        context['tipo'] = self.kwargs['tipo']
        return context


#Detalle de un recurso.
class RecursoDetailView(DetailView):
    model = Recurso
    template_name = 'roubo_recurso_detalle.html'
    context_object_name = 'recurso'
    slug_url_kwarg= 'nombre_corto'
    slug_field = 'nombre_corto'
    
    # def get_queryset(self, **kwargs):
    #    recurso=Recurso.objects.filter(nombre_corto=self.kwargs['nombre_corto'])
    #     #self.desempenos=self.recurso.desempenodecomprension_set.all()
    #     #if len(self.desempenos)==0:
    #     #    self.desempenos="No hay desempeños asociados con este recurso."
    #   return recurso
    
    def get_context_data(self, **kwargs):
        context = super(RecursoDetailView, self).get_context_data(**kwargs)
        relacionados_tags = context['recurso'].tags.similar_objects()
        context['relacionados_tags'] = relacionados_tags
        return context


def contacto(request):
    """Muestra el formulario de contacto del sitio.
    """
    
    politica=False
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
        #else:
            #raise ValidationError('Debe aceptar la política de tratamiento.')
    else:
        form = ContactoForm(initial={'fecha':date.today()})
    return render(
        request,
        'contacto.html',
        {'form': form,
         'datos': request.POST,
         'politica': politica
        }
        )


##############################  ##############################
# #Detalle de un desempeño
# class DesempenoDeComprensionDetailView(DetailView):
#     template_name='desempeno_detalle.html'
#     context_object_name='desempeno'
#     
#     def get_object(self, **kwargs):
#         self.desempeno=get_object_or_404(DesempenoDeComprension, nombre_corto=self.kwargs['nombre_corto'])
#         self.cursos=self.desempeno.curso_set.all()
#         return self.desempeno
#     
#     def get_context_data(self, **kwargs ):
#          # Call the base implementation first to get a context
#         context = super(DesempenoDeComprensionDetailView, self).get_context_data(**kwargs)
#         context['cursos']=self.cursos
#         return context
#     
# #Detalle de un curso (página de inicio)
# class CursoInicioDetailView(DetailView):
#     template_name="curso_presentacion.html"
#     model=Curso
#     slug_field='codigo'
#     slug_url_kwarg='codigo'
# 
# #Lista general de cursos (landing).
# class CursoListView(ListView):
#     model=Curso
#     context_object_name='cursos'
#     template_name='cursos_index.html'
# 
# #Lista de recursos. Debe tener filtro y caja de búsqueda.
# class RecursosListView(ListView):
#     pass

##Editar recurso
#Agregar recurso

