"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import datetime
from django.test import TestCase
from django.utils import timezone
from models import Usuari

class SimpleTest(TestCase):
    def test_publicat_ultim_dia_amb_data_futura(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        alta_futura = Usuari(data_alta=time)
        self.assertEqual(alta_futura.publicat_en_el_ultim_dia(), False)
