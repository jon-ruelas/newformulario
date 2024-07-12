from django.db import connection


def listar_entidades():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    # out_cur = django_cursor.connection.cursor()

    cursor.callproc("listar_entidad")

    lista = []
    for fila in cursor:
        lista.append(fila)

    return lista


def listar_tipo_documento():

    TIPOS_DOCUMENTO = {1: "DNI",
                       2: "CARNE DE EXTRANJERIA",
                       3: "PASAPORTE"}

    dicc_tipo_documento = TIPOS_DOCUMENTO

    return dicc_tipo_documento


def listar_tipo_servicio():
    SERVICIOS = {
        '01': 'CONSULTA EXTERNA',
        '02': 'HOSPITALIZACION',
        '03': 'EMERGENCIA',
        '04': 'CENTRO QUIRURGICO',
        '05': 'CENTRO OBSTÉTRICO',
        '06': 'UCI O UCIN',
        '07': 'FARMACIA',
        '08': 'SERVICIOS MEDICOS DE APOYO',
        '09': 'ATENCION A DOMICILIO CONSULTA AMBULATORIA',
        '10': 'ATENCION A DOMICILIO URGENCIA A EMERGENCIA',
        '11': 'OFICINAS O AREAS ADMINISTRATIVAS DE IAFAS A 1 IPRESS A UGIPRESS ',
        '12': 'INFRAESTRUCTURA',
        '13': 'REFERENCIA Y CONTRAREFERENCIA'
    }

    dicc_tipo_servicio = SERVICIOS

    return dicc_tipo_servicio


def listar_autorizacion_correo():
    AUTORIZACION = {
        0: "Sí autorizo que se me notifique el resultado del reclamo al email consignado",
        1: "No autorizo que se me notifique el resultado del reclamo al email consignado"
    }
    dicc_autorizacion = AUTORIZACION

    return dicc_autorizacion
