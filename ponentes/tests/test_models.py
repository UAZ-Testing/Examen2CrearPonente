from django.core.exceptions import ValidationError
from django.test import TestCase

from ponentes.models import Ponente


class PonenteModelTest(TestCase):
    def test_save_ponente(self):
        ponente = Ponente()
        ponente.nombre = 'Porfirio'
        ponente.primer_apellido = 'Díaz'
        ponente.segundo_apellido = 'Sánchez'
        ponente.save()

        ponentes = Ponente.objects.all()

        self.assertEqual(ponentes.count(), 1)
