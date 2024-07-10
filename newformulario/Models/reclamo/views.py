from django.http import HttpRequest
from django.shortcuts import render

from newformulario.Models.reclamo.forms import FormularioReclamo


class FormularioReclamoView(HttpRequest):
    def index(request):
        reclamo = FormularioReclamo()
        return render(request, "formulario.html", {"form": reclamo})

    def procesar_formulario(request):
        reclamo = FormularioReclamo(request.POST)
        if reclamo.is_valid():
            reclamo.save()
            reclamo = FormularioReclamo()

        return render(request, "formulario.html", {"from": reclamo, "mensaje": 'OK'})
