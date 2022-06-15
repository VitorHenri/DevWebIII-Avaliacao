from django.shortcuts import render, HttpResponse
from datetime import date
from django.shortcuts import render
from cadastroApi.models import FeriadoModel

def feriado(request):
    hoje = date.today()
    try:
        feriados = FeriadoModel.objects.all().filter(data=hoje)
    except FeriadoModel.DoesNotExist:
        feriados = None

    resp = [f'Feriado {f}' for f in feriados] if feriados else ['NÃO É FERIADO']

    return render(request, 'feriados.html', {'resp': resp})