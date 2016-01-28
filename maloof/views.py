# coding = utf-8
# views para el app maloof, que maneja los perfiles de usuario

from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class PerfilView(TemplateView):
    template_name = 'perfil.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PerfilView, self).dispatch(*args, **kwargs)