from django.http import HttpRequest
from django.shortcuts import render

from newformulario.Models.Usuario.forms import FormularioUsuario


class FormularioUsuaarioView(HttpRequest):
    def index(request):
        usuario = FormularioUsuario()
        return render(request, "UsuarioIndex.html", {"form": usuario})

    def procesar_usuario(request):
        usuario = FormularioUsuario()
