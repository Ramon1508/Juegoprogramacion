# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 04:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profesores', '0001_initial'),
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='intentos',
            name='ID_Problema',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profesores.Problemas'),
        ),
    ]