# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-28 22:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0013_auto_20170329_0126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='research',
            name='exp_detail',
        ),
        migrations.AddField(
            model_name='research',
            name='experiment_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
