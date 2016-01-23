# coding=utf-8
# Formularios para la aplicación "Roubo"
# Version 0.21

from django.forms import ModelForm, DateInput, TextInput, EmailInput, URLInput, Textarea, CheckboxInput, BooleanField, CharField
# from django import forms
from .models import Contacto
# from third-party apps
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget


class ContactoForm(ModelForm):
    """Formulario de contacto del sitio, guardado en el objeto Contacto.
    """
    acepto_tratamiento = BooleanField(
        required=True,
        error_messages={'required': 'Debe aceptar la política de tratamiento.'},
        label='Acepto la política de tratamiento de datos que se encuentra en la parte inferior de esta página.'
    )
    captcha = ReCaptchaField(
        widget=ReCaptchaWidget(explicit=True)
    )

    class Meta:
        model = Contacto
        fields = ['fecha', 'autor', 'email', 'url', 'texto', 'acepto_tratamiento', 'acepto_contacto']
        labels = {
            'fecha': 'Fecha',
            'autor': 'Nombre*',
            'email': 'Correo electrónico*',
            'url': 'Página web o perfil',
            'texto': 'Mensaje*',
            'acepto_contacto': 'Quiero recibir información sobre nuevas publicaciones o servicios de Estudio 5-8.'
        }
        widgets = {
            'fecha': DateInput(attrs={'size': 10, 'readonly': True}),
            'autor': TextInput(attrs={'size': 50, 'required': True}),
            'email': EmailInput(attrs={'size': 50, 'required': True}),
            'url': URLInput(attrs={'size': 50}),
            'texto': Textarea(attrs={'cols': 65, 'rows': 12, 'required': True})
        }

# class ContactoForm(forms.Form):
#     """
#     """
#     autor = forms.CharField(
#         error_messages = {'required': 'Por favor escriba su nombre.'}
#     )
#     email = forms.EmailField(
#         error_messages = {
#         }
#     )
#     url
#     fecha
#     texto
#     acepto_tratamiento
#     acepto_contacto
