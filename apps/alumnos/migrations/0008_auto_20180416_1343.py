# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-04-16 19:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('alumnos', '0007_auto_20171126_1829'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('vin', models.TextField(max_length=21, primary_key=True, serialize=False)),
                ('modelo', models.TextField(max_length=20)),
                ('puertas', models.PositiveIntegerField()),
                ('velocidad', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='movimieto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='carro',
            name='marca',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='alumnos.Marca'),
        ),
        migrations.AddField(
            model_name='carro',
            name='movimiento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='alumnos.movimieto'),
        ),
    ]
