# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 01:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0006_intentos_tiempo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiantes',
            name='Grupo',
        ),
        migrations.RemoveField(
            model_name='intentos',
            name='ID_Problema',
        ),
        migrations.RemoveField(
            model_name='intentos',
            name='Matricula',
        ),
        migrations.DeleteModel(
            name='Estudiantes',
        ),
        migrations.DeleteModel(
            name='Intentos',
        ),
    ]