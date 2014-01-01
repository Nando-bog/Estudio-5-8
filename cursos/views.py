#coding=utf-8
# Views para la aplicaci—n "Cursos"
#Version 0.1

from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Recurso

class RecursoDetailView(DetailView):
    model = Recurso
    context_object_name = 'recurso'
    slug_field='nombre_corto'
    slug_url_kwarg = 'nombre_corto'
    template_name = 'recurso_detalle.html'
    
    def get_query_set(self, **kwargs):
        self.recurso=Recurso.objects.get(self.kwargs['nombre_corto'])
        #self.autor=self.recurso.autor.all()
        return self.recurso
    
    #def get_context_data(self, **kwargs):
    #    context=super(RecursoDetailView, self).get_context_data(**kwargs)
    #    context['autor']=self.autor
    #    return context