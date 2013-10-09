# -*- coding: utf-8 -*-


from django.contrib import admin
from usuaris.models import Usuari, Carrec


#D'aquesta manera podem reordenar els camps del model perquè apareguin en el formulari d'una manera diferent.
class UsuariAdmin(admin.ModelAdmin):

	#Ordenar camps del formulari i separar per categories.
	fieldsets=[
		(None,						{'fields': ['data_alta']}),
		("Dades de l'usuari",		{'fields': ['nom','cognoms','correu']}),
		#Amb la següent línia faríem que la categoria estigués oculta i calgués clicar-hi per desplegar-la.
		#("Dades de l'usuari",		{'fields': ['nom','cognoms','correu'],'classes':['collapse']}),
		("Posició dins l'empresa",	{'fields': ['carrec']}),
	]
	#fields=['data_alta','nom','cognoms','correu','carrec']		#Sense separar per categories

admin.site.register(Usuari,UsuariAdmin)

