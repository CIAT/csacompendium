# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-31 23:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csa_practice', '0003_auto_20170131_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practicetype',
            name='practice_type',
            field=models.CharField(max_length=120, unique=True, verbose_name='Practice category'),
        ),
    ]
