from django.shortcuts import render, redirect

# Create your views here.
from ponentes.forms import PonenteForm
from ponentes.models import Ponente


def mostrar_ponentes(request):
    ponentes = Ponente.objects.all()

    return render(request, 'ponentes.html', {
        'ponentes': ponentes
    })


def insertar_ponente(request):
    form = PonenteForm(data=request.POST)

    if form.is_valid():
        ponente = Ponente.objects.create()
        form.save(ponente)
        return redirect('mostrar_ponentes')
    else:
        return render(request, 'ponentes.html', {"form": form})
