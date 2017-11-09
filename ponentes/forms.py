from ponentes.models import Ponente
from django import forms


class PonenteForm(forms.models.ModelForm):
    class Meta:
        model = Ponente
        fields = ('nombre', 'primer_apellido', 'segundo_apellido')

        widgets = {
            'nombre': forms.fields.TextInput(attrs={
                'placeholder': 'Ingresa el nombre',
                'class': 'form-control input-lg',
            }),
            'primer_apellido': forms.fields.TextInput(attrs={
                'placeholder': 'Ingresa el primer apellido',
                'class': 'form-control input-lg',
            }),
            'segundo_apellido': forms.fields.TextInput(attrs={
                'placeholder': 'Ingresa el segundo apellido',
                'class': 'form-control input-lg',
            }),
        }

    def save(self):
        return forms.models.ModelForm.save(self)

        # def validate_unique(self):
        #     try:
        #         self.instance.validate_unique()
        #     except ValidationError as e:
        #         e.error_dict = {'text': [DUPLICATE_ITEM_ERROR]}
        #         self._update_errors(e)
