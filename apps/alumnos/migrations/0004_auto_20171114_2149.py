# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 04:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0003_estudiantes_grupo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intentos',
            name='Matricula',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='alumnos.Estudiantes'),
        ),
    ]
