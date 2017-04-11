# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-21 11:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soils', '0002_auto_20160921_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soil',
            name='initial_soc',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='Initial SOM'),
        ),
        migrations.AlterField(
            model_name='soil',
            name='som',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='Soil Organic Matter (SOM)'),
        ),
        migrations.AlterField(
            model_name='soil',
            name='som_uom',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='SOM UOM'),
        ),
        migrations.AlterField(
            model_name='soiltype',
            name='classification',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='soiltype',
            name='soil_type',
            field=models.CharField(max_length=80),
        ),
    ]
