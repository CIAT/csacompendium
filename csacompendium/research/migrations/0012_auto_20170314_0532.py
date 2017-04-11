# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-14 02:32
from __future__ import unicode_literals

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('research', '0011_auto_20170314_0239'),
    ]

    operations = [
        migrations.CreateModel(
            name='Research',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('object_id', models.PositiveIntegerField()),
                ('experiment_design', models.CharField(choices=[('Control Treatment', 'Control Treatment'), ('Improved Treatment', 'Improved Treatment')], max_length=22)),
                ('mean_outcome', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.0'), max_digits=8, null=True, verbose_name='Mean outcome')),
                ('std_outcome', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.0'), max_digits=8, null=True, verbose_name='Standard outcome')),
                ('outcome_uom', models.CharField(blank=True, default='kg/ha', max_length=200, null=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contenttypes.ContentType')),
                ('experimentdetails', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='research.ExperimentDetails', verbose_name='Experiment Details')),
                ('experimentduration', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='research.ExperimentDuration', verbose_name='Experiment Duration')),
                ('experimentrep', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='research.ExperimentRep', verbose_name='Experiment Replications')),
                ('measurementyear', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='research.MeasurementYear', verbose_name='Measurement Year')),
                ('modified_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='research_research', to=settings.AUTH_USER_MODEL)),
                ('nitrogenapplied', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='research.NitrogenApplied', verbose_name='Nitrogen Applied')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-time_created', '-last_update'],
                'verbose_name_plural': 'Research',
            },
        ),
        migrations.RemoveField(
            model_name='controlresearch',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='controlresearch',
            name='experimentdetails',
        ),
        migrations.RemoveField(
            model_name='controlresearch',
            name='experimentduration',
        ),
        migrations.RemoveField(
            model_name='controlresearch',
            name='experimentrep',
        ),
        migrations.RemoveField(
            model_name='controlresearch',
            name='measurementyear',
        ),
        migrations.RemoveField(
            model_name='controlresearch',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='controlresearch',
            name='nitrogenapplied',
        ),
        migrations.RemoveField(
            model_name='controlresearch',
            name='user',
        ),
        migrations.DeleteModel(
            name='ControlResearch',
        ),
    ]
