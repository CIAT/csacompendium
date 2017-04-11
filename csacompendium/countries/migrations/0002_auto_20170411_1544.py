# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-11 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='country_code',
            field=models.CharField(help_text='Country abbreviated name', max_length=3, unique=True),
        ),
    ]
