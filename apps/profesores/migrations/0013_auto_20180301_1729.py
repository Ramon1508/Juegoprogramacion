# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-03-02 00:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profesores', '0012_auto_20180301_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiantes',
            name='num_list',
            field=models.TextField(choices=[('1', 'ONE'), ('2', 'TWO'), ('3', 'Three'), ('4', 'Four')], default=('1', '2', '3', '4')),
        ),
    ]
