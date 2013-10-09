# coding=utf-8
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import datetime
from django.test import TestCase
from django.utils import timezone
from models import Usuari
from django.core.urlresolvers import reverse
from django.test import Client


class SimpleTest(TestCase):
    def test_alta_amb_data_futura(self):
        """
        Hauria de tornar FALSE per a una data d'alta d'usuari futura.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        alta_futura = Usuari(data_alta=time)
        self.assertEqual(alta_futura.donat_alta_en_ultim_dia(), False)

	def test_alta_amb_data_davui(self):
		"""
		Hauria de tornar FALSE per a una data d'alta d'usuari propera a l'actual.
		"""
		time = timezone.now() + datetime.timedelta(hours=3)
		alta_futura = Usuari(data_alta=time)
		self.assertEqual(alta_futura.donat_alta_en_ultim_dia(), True)

	def test_alta_amb_data_passada(self):
		"""
		Hauria de tornar FALSE per a una data d'alta d'usuari anterior a l'actual en més de 30 dies.
		"""
		time = timezone.now() - datetime.timedelta(days=30)
		alta_futura = Usuari(data_alta=time)
		self.assertEqual(alta_futura.donat_alta_en_ultim_dia(), False)



def crear_usuari(nom,cognoms,email,carrec,days):
	time = timezone.now() + datetime.timedelta(days=days)
	return Usuari.objects.create(nom=nom,cognoms=cognoms,email=email,carrec=carrec,
                                   data_alta=time)


class QuestionViewTests(TestCase):
	
	def test_vista_index_sense_usuaris(self):
		response = self.client.get(reverse('usuaris:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No s'han creat usuaris.")
		self.assertQuerysetEqual(response.context['llista_usuaris'], [])