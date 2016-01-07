"""
WSGI config for _5_8 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""
#Python and Python standard imports
import os
from django.core.wsgi import get_wsgi_application
#Third party imports
#from whitenoise.django import DjangoWhiteNoise
from dj_static import Cling

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "_5_8.settings")

#application = DjangoWhiteNoise(get_wsgi_application())

application = Cling(get_wsgi_application())