# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-11 21:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0003_auto_20170128_2157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experimentduration',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='experimentduration',
            name='user',
        ),
        migrations.RemoveField(
            model_name='research',
            name='experimentduration',
        ),
        migrations.DeleteModel(
            name='ExperimentDuration',
        ),
    ]
