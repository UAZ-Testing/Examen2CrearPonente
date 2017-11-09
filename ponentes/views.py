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
    if request.method == 'POST':
        form = PonenteForm(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('mostrar_ponentes')
        else:
            return render(request, 'ponente.html', {"form": form})
    else:
        form = PonenteForm()
        return render(request, 'ponente.html', {"form": form})
