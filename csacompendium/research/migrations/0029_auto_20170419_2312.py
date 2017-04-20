# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-19 20:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0028_experimentreplicate_researchexperimentreplicate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='researchexperimentreplicate',
            name='experimentreplicate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='research.ExperimentReplicate', verbose_name='Experiment replicates'),
        ),
    ]
