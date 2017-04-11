# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-21 13:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soils', '0005_remove_soil_soil_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='soil',
            name='soiltype',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='soils.SoilType'),
            preserve_default=False,
        ),
    ]
