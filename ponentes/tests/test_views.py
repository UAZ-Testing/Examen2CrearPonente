from django.test import TestCase

from ponentes.forms import PonenteForm


class PonentesPageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'ponentes.html')

    def test_uses_ponente_form(self):
        response = self.client.post('/new')
        self.assertIsInstance(response.context['form'], PonenteForm)
