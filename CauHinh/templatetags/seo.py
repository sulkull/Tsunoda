import re
from django import template
from django.shortcuts import render
from CauHinh.models import CauHinhSeo

register = template.Library()
@register.simple_tag(name='seo')
def get_meta():
    return CauHinhSeo.objects.all()