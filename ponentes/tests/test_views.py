from django.utils.html import escape
from django.test import TestCase
from ponentes.forms import PonenteForm, NOMBRE_REQUIRED_ERROR, \
    PRIMER_APELLIDO_REQUIRED_ERROR
from ponentes.models import Ponente


class PonentesPageTest(TestCase):
    def test_uses_ponentes_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'ponentes.html')


class PonentePageTest(TestCase):
    def test_uses_ponentes_template(self):
        response = self.client.get('/new')
        self.assertTemplateUsed(response, 'ponente.html')

    def test_uses_ponente_form(self):
        response = self.client.post('/new')
        self.assertIsInstance(response.context['form'], PonenteForm)

    def test_can_save_a_POST_request(self):
        self.client.post('/new', data={
            'nombre': 'Martín',
            'primer_apellido': 'Morales'
        })

        self.assertEqual(Ponente.objects.count(), 1)

        new_item = Ponente.objects.first()
        self.assertEqual(new_item.nombre, 'Martín')
        self.assertEqual(new_item.primer_apellido, 'Morales')

    def test_redirects_after_POST(self):
        response = self.client.post('/new', data={
            'nombre': 'Martín',
            'primer_apellido': 'Morales'
        })

        self.assertRedirects(response, '/')

    def test_for_invalid_input_renders_ponente_template(self):
        response = self.client.post('/new', data={'nombre': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ponente.html')

    def test_validation_errors_are_shown_on_home_page(self):
        response = self.client.post('/new', data={
            'nombre': '',
            'primer_apellido': ''
        })
        self.assertContains(response, escape(NOMBRE_REQUIRED_ERROR))
        self.assertContains(response, escape(PRIMER_APELLIDO_REQUIRED_ERROR))

    def test_for_invalid_input_passes_form_to_template(self):
        response = self.client.post('/new', data={'nombre': ''})
        self.assertIsInstance(response.context['form'], PonenteForm)

    def test_invalid_ponentes_arent_saved(self):
        self.client.post('/new', data={'nombre': ''})
        self.assertEqual(Ponente.objects.count(), 0)
