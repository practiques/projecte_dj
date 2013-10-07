# Create your views here.
# -*- coding: ISO-8859-1 -*-


from django.http import HttpResponse

def index(request):
    return HttpResponse("Estic al mòdul d'usuaris.")

def detail(request, user_id):
    return HttpResponse("Estas accedint a la info. de l'usuari %s." % user_id)