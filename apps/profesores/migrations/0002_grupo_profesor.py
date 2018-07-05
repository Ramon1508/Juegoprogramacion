# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 04:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profesores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('Matricula', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('ApellidoPaterno', models.CharField(max_length=50)),
                ('ApellidoMaterno', models.CharField(max_length=50)),
                ('Nombres', models.CharField(max_length=100)),
            ],
        ),
    ]