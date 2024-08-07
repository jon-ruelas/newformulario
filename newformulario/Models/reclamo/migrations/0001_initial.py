# Generated by Django 4.1 on 2024-07-10 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entidadreclamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entidad_id', models.CharField(max_length=100)),
                ('servicio_hecho_reclamo', models.CharField(max_length=100)),
                ('tipo_documento_ususario', models.CharField(max_length=50)),
                ('numero_documento_ususario', models.CharField(max_length=50)),
                ('nombres_usuario', models.CharField(max_length=100)),
                ('apellido_paterno_usuario', models.CharField(max_length=100)),
                ('apellido_materno_usuario', models.CharField(max_length=100)),
                ('correo_usuario', models.CharField(max_length=100)),
                ('telefono_usuario', models.CharField(max_length=100)),
                ('distrito_usuario', models.CharField(max_length=100)),
                ('direccion_usuario', models.CharField(max_length=100)),
                ('tipo_documento_presenta', models.CharField(max_length=50)),
                ('numero_documento_presenta', models.CharField(max_length=50)),
                ('nombres_presenta', models.CharField(max_length=100)),
                ('apellido_paterno_presenta', models.CharField(max_length=100)),
                ('apellido_materno_presenta', models.CharField(max_length=100)),
                ('correo_presentao', models.CharField(max_length=100)),
                ('telefono_presenta', models.CharField(max_length=100)),
                ('distrito_presenta', models.CharField(max_length=100)),
                ('direccion_presenta', models.CharField(max_length=100)),
                ('detalle_reclamo', models.CharField(max_length=100)),
                ('autorizacion_notificacion_correo', models.CharField(max_length=100)),
            ],
        ),
    ]
