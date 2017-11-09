from django.test import TestCase


class PonentesPageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'ponentes.html')
