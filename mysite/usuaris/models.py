# -*- coding: utf-8 -*-
"""
Definició de les classes i els seus mètodes
"""
import datetime
from django.utils import timezone
from django.db import models

#Càrrec que ocupa dins de l'empresa
class Carrec(models.Model):

	nom = models.CharField(max_length=25)
	descr = models.CharField(max_length=100) #Breu descripció de les responsabilitats.
	
	def __unicode__(self):
		return self.nom

class Usuari(models.Model):

    nom = models.CharField(max_length=20)
    cognoms = models.CharField(max_length=40)
    correu = models.CharField(max_length=50)
    carrec = models.ForeignKey(Carrec)
    data_alta = models.DateField()
    

    #Mètode que torna 'true' si l'usuari ha estat donat d'alta en el darrer dia.
    def donat_alta_en_ultim_dia(self):
        now=timezone.now();
        return now - datetime.timedelta(days=1) <= self.data_alta < now

    #Format en què es mostraran els usuaris quan fem un "Usuari.objects.all()".
    def __unicode__(self):  
        return self.nom+" "+self.cognoms

