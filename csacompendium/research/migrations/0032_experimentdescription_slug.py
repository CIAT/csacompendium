# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-20 09:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0031_auto_20170420_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='experimentdescription',
            name='slug',
            field=models.SlugField(blank=True, max_length=500, unique=True),
        ),
    ]
