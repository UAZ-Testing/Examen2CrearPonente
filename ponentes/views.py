from django.shortcuts import render

# Create your views here.
from ponentes.models import Ponente


def mostrar_ponentes(request):
    ponentes = Ponente.objects.all()

    return render(request, 'ponentes.html', {
        'ponentes': ponentes
    })
