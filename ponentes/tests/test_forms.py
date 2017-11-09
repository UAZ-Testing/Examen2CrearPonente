from django.test import TestCase

from ponentes.forms import PonenteForm


class PonenteFormTest(TestCase):
    def test_form_has_input_placeholders_and_css_classes(self):
        form = PonenteForm()
        self.assertIn('class="form-control input-lg"', form.as_p())
        self.assertIn('placeholder="Ingresa el nombre"', form.as_p())
        self.assertIn('placeholder="Ingresa el primer apellido"', form.as_p())
        self.assertIn('placeholder="Ingresa el segundo apellido"', form.as_p())

        # def test_form_validation_for_blank_items(self):
        #     form = ItemForm(data={'text': ''})
        #     self.assertFalse(form.is_valid())
        #     self.assertEqual(
        #         form.errors['text'],
        #         [EMPTY_ITEM_ERROR]
