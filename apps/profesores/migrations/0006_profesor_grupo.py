# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 04:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profesores', '0005_auto_20171114_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='Grupo',
            field=models.ManyToManyField(to='profesores.Grupos'),
        ),
    ]
