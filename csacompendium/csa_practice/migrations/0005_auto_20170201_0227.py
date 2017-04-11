# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-31 23:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csa_practice', '0004_auto_20170201_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csatheme',
            name='slug',
            field=models.SlugField(blank=True, max_length=80, unique=True),
        ),
        migrations.AlterField(
            model_name='practicelevel',
            name='slug',
            field=models.SlugField(blank=True, max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='practicetype',
            name='slug',
            field=models.SlugField(blank=True, max_length=120, unique=True),
        ),
    ]
