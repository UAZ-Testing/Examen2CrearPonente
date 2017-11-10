import urllib

from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from ponentes.forms import PonenteForm
from ponentes.models import Ponente

INFO_PONENTE_CREADO = 'Ponente creado con éxito'


def mostrar_ponentes(request):
    ponentes = Ponente.objects.all()

    info_message = request.GET.get('info_message', None)

    return render(request, 'ponentes.html', {
        'ponentes': ponentes,
        'info_message': info_message
    })


def insertar_ponente(request):
    if request.method == 'POST':
        form = PonenteForm(data=request.POST)

        if form.is_valid():
            form.save()
            kwargs = {'info_message': INFO_PONENTE_CREADO}

            return redirect(
                reverse('mostrar_ponentes') + '?%s' % (
                    urllib.parse.urlencode(kwargs)))
        else:
            return render(request, 'ponente.html', {"form": form})
    else:
        form = PonenteForm()
        return render(request, 'ponente.html', {"form": form})
