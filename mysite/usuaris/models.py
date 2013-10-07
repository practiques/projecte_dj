from django.db import models

# Create your models here.
class Usuari(models.Model):
    nom = models.CharField(max_length=20)
    cognoms = models.CharField(max_length=40)
    data_alta = models.DateField()

class Fitxer(models.Model):
	nom = models.CharField(max_length=30)	
	usuari = models.ForeignKey(Usuari)

