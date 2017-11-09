from ponentes.models import Ponente
from django import forms

NOMBRE_PLACEHOLDER = 'Ingresa el nombre'
PRIMER_APELLIDO_PLACEHOLDER = 'Ingresa el primer apellido'
SEGUNDO_APELLIDO_PLACEHOLDER = 'Ingresa el segundo apellido'
NOMBRE_REQUIRED_ERROR = 'El nombre es requerido'
PRIMER_APELLIDO_REQUIRED_ERROR = 'El primer apellido es requerido'


class PonenteForm(forms.models.ModelForm):
    use_required_attribute = False

    class Meta:
        model = Ponente
        fields = ('nombre', 'primer_apellido', 'segundo_apellido')

        widgets = {
            'nombre': forms.fields.TextInput(attrs={
                'placeholder': NOMBRE_PLACEHOLDER,
                'class': 'form-control input-lg',
            }),
            'primer_apellido': forms.fields.TextInput(attrs={
                'placeholder': PRIMER_APELLIDO_PLACEHOLDER,
                'class': 'form-control input-lg',
            }),
            'segundo_apellido': forms.fields.TextInput(attrs={
                'placeholder': SEGUNDO_APELLIDO_PLACEHOLDER,
                'class': 'form-control input-lg',
            }),
        }

        error_messages = {
            'nombre': {'required': NOMBRE_REQUIRED_ERROR},
            'primer_apellido': {'required': PRIMER_APELLIDO_REQUIRED_ERROR},
        }
