# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-23 22:09
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soils', '0014_auto_20170128_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soil',
            name='initial_soc',
            field=models.DecimalField(blank=True, decimal_places=4, default=Decimal('0.0'), max_digits=6, null=True, verbose_name='Initial SOM'),
        ),
        migrations.AlterField(
            model_name='soil',
            name='soil_ph',
            field=models.DecimalField(blank=True, decimal_places=4, default=Decimal('0.0'), max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='soil',
            name='som',
            field=models.DecimalField(blank=True, decimal_places=4, default=Decimal('0.0'), max_digits=6, null=True, verbose_name='Soil Organic Matter-SOM'),
        ),
        migrations.AlterField(
            model_name='soil',
            name='som_uom',
            field=models.CharField(blank=True, default='%', max_length=6, null=True, verbose_name='SOM UOM'),
        ),
    ]
