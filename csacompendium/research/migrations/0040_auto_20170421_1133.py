# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-21 08:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('research', '0039_researchmeasurementyear_measurementduration'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeasurementSeason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, max_length=120, unique=True)),
                ('measurement_season', models.CharField(choices=[('First Growing Season', 'First Growing Season'), ('Second Growing Season', 'Second Growing Season')], max_length=42, null=True, unique=True)),
                ('modified_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='research_measurementseason', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-time_created', '-last_update'],
                'verbose_name_plural': 'Measurement Seasons',
            },
        ),
        migrations.AddField(
            model_name='researchmeasurementyear',
            name='measurementseason',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='research.MeasurementSeason'),
        ),
    ]
