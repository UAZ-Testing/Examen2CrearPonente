from django.test import TestCase

from ponentes.forms import (
    PonenteForm,
    NOMBRE_PLACEHOLDER,
    PRIMER_APELLIDO_PLACEHOLDER,
    SEGUNDO_APELLIDO_PLACEHOLDER,
    NOMBRE_REQUIRED_ERROR,
    PRIMER_APELLIDO_REQUIRED_ERROR
)
from ponentes.models import Ponente


class PonenteFormTest(TestCase):
    def test_form_has_input_placeholders_and_css_classes(self):
        form = PonenteForm(None)
        self.assertIn('class="form-control input-lg"', form.as_p())
        self.assertIn('placeholder="%s"' % (NOMBRE_PLACEHOLDER), form.as_p())
        self.assertIn('placeholder="%s"' % (PRIMER_APELLIDO_PLACEHOLDER),
                      form.as_p())
        self.assertIn('placeholder="%s"' % (SEGUNDO_APELLIDO_PLACEHOLDER),
                      form.as_p())

    def test_form_validation_for_blank_items(self):
        form = PonenteForm(data={
            'nombre': '',
            'primer_apellido': ''
        })

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['nombre'], [NOMBRE_REQUIRED_ERROR])
        self.assertEqual(form.errors['primer_apellido'],
                         [PRIMER_APELLIDO_REQUIRED_ERROR])

    def test_form_save(self):
        form = PonenteForm(data={
            'nombre': 'Porfirio',
            'primer_apellido': 'Díazz'
        })

        new_ponente = form.save()

        self.assertEqual(new_ponente, Ponente.objects.all()[0])
