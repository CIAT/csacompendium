# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-18 12:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('locations', '0004_auto_20160918_1342'),
    ]

    operations = [
        migrations.CreateModel(
            name='Precipitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('precipitation', models.DecimalField(decimal_places=2, max_digits=7)),
                ('precipitation_uom', models.CharField(default='mm', max_length=5, verbose_name='Precipitation UOM')),
                ('precipitation_desc', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('modified_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='locations_precipitation', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-time_created', '-last_update'],
            },
        ),
    ]