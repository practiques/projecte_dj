# coding=utf-8

"""
Definició de les vistes
"""

from models import Usuari
from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
	tots_usuaris = Usuari.objects.all()
	template = loader.get_template('usuaris/index.html')
	context = RequestContext(request, {
		'tots_usuaris': tots_usuaris,
	})
	return HttpResponse(template.render(context))

def usuari(request, usuari_id):
   	detall_usuari = Usuari.objects.get(pk=usuari_id)
	template = loader.get_template('usuaris/detall_usuari.html')
	context = RequestContext(request, {
		'detall_usuari': detall_usuari,
	})
	return HttpResponse(template.render(context))

def carrec(request, carrec_id):
    response = "Estas veient el càrrec %s."
    return HttpResponse(response % carrec_id)

