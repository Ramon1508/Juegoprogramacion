# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-03-02 00:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profesores', '0009_auto_20171128_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiantes',
            name='num_list',
            field=models.CharField(choices=[('1', 'ONE'), ('2', 'TWO'), ('3', 'Three'), ('4', 'Four')], default=('1', '2'), max_length=3),
        ),
    ]
