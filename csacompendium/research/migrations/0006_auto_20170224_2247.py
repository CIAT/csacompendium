# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-24 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0005_auto_20170224_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experimentdetails',
            name='exp_detail',
            field=models.TextField(verbose_name='Experiment Details'),
        ),
    ]