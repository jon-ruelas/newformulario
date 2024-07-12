from email import message
from pyexpat.errors import messages
from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from Models.reclamo.models import Entidadreclamo
from Views.SetupView import listar_autorizacion_correo, listar_entidades, listar_tipo_documento, listar_tipo_servicio


class HomeView():

    def home(self):
        plantilla = get_template('index.html')
        return HttpResponse(plantilla.render())

    def pagina1(self):

        return HttpResponse('Hoal2')

    def pagina2(self, parametro1):
        return HttpResponse("HOLA DESDE PARAMETRO" + str(parametro1))

    def formulario(self):
        plantilla = get_template('formulario.html')
        return HttpResponse(plantilla.render())

    def registroReclamo(request):
        data = {
            'entidad': listar_entidades(),
            'tipo_documento': listar_tipo_documento(),
            'tipo_servicio': listar_tipo_servicio(),
            'autorizacion': listar_autorizacion_correo()


        }

        if request.method == 'POST':
            entidad_id = request.POST["inputestablecimiento"]
            servicio_hecho_reclamo = request.POST["inputtiposervicio"]

            tipo_documento_ususario = request.POST["inputtipodocusuario"]
            numero_documento_ususario = request.POST["inputdocumentousuario"]
            nombres_usuario = request.POST["inputnombreusuario"]
            apellido_paterno_usuario = request.POST[""]
            apellido_materno_usuario = request.POST[""]
            correo_usuario = request.POST["inputcorreousuario"]
            # CREAR CAMPO EN BASE DE DATOS
            telefono_usuario = request.POST["inputtelefonousuario"]
            distrito_usuario = request.POST[""]  # CREAR CAMPO EN BASE DE DATOS
            # CREAR CAMPO EN BASE DE DATOS
            direccion_usuario = request.POST["inputdireccionusuario"]

            tipo_documento_presenta = request.POST["inputtipodocpresenta"]
            numero_documento_presenta = request.POST["inputdocumentopresenta"]
            nombres_presenta = request.POST[""]
            apellido_paterno_presenta = request.POST[""]
            apellido_materno_presenta = request.POST[""]
            correo_presentao = request.POST["inputcorreopresenta"]
            telefono_presenta = request.POST["inputtelefonopresenta"]
            # CREAR CAMPO EN BASE DE DATOS
            distrito_presenta = request.POST[""]
            direccion_presenta = request.POST["inputdireccionpresenta"]

            detalle_reclamo = request.POST["detallereclamo"]

            autorizacion_notificacion_correo = request.POST["inputautoriza"]

            Entidadreclamo(
                entidad_id=entidad_id,
                servicio_hecho_reclamo=servicio_hecho_reclamo,

                tipo_documento_ususario=tipo_documento_ususario,
                numero_documento_ususario=numero_documento_ususario,
                nombres_usuario=nombres_usuario,
                apellido_paterno_usuario=apellido_paterno_usuario,
                apellido_materno_usuario=apellido_materno_usuario,
                correo_usuario=correo_usuario,  # CREAR CAMPO EN BASE DE DATOS
                telefono_usuario=telefono_usuario,  # CREAR CAMPO EN BASE DE DATOS
                distrito_usuario=distrito_usuario,  # CREAR CAMPO EN BASE DE DATOS
                direccion_usuario=direccion_usuario,  # CREAR CAMPO EN BASE DE DATOS

                tipo_documento_presenta=tipo_documento_presenta,
                numero_documento_presenta=numero_documento_presenta,
                nombres_presenta=nombres_presenta,
                apellido_paterno_presenta=apellido_paterno_presenta,
                apellido_materno_presenta=apellido_materno_presenta,
                correo_presentao=correo_presentao,
                telefono_presenta=telefono_presenta,
                distrito_presenta=distrito_presenta,  # CREAR CAMPO EN BASE DE DATOS
                direccion_presenta=direccion_presenta,

                detalle_reclamo=detalle_reclamo,

                autorizacion_notificacion_correo=autorizacion_notificacion_correo
            ).save()

            messages.success(request, 'Se registró correctamente')
            return render(request, 'formulario.html', data)
        else:
            return render(request, 'formulario.html', data)
