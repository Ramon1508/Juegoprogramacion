# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 04:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profesores', '0002_grupo_profesor'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrupoxProfesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_Grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profesores.Grupo')),
                ('ID_Prof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profesores.Profesor')),
            ],
        ),
    ]
