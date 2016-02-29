# coding=utf-8
# template tags for cueva app
# version 0.1
from random import choice
from django import template
from django.contrib.contenttypes.models import ContentType
from cueva.models import ImagenFondoHome

register = template.Library()


@register.simple_tag
def random_image():
    """Return a random image for the home page."""
    return choice(ImagenFondoHome.objects.all())
