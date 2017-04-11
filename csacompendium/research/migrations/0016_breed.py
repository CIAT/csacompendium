# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-31 11:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('research', '0015_nitrogenapplied_nitrogen_source'),
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
                ('breed', models.CharField(max_length=200, unique=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contenttypes.ContentType')),
                ('modified_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='research_breed', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-time_created', '-last_update'],
                'verbose_name_plural': 'Breeds',
            },
        ),
    ]
