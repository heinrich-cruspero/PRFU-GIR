# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-13 09:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('affiliations', '0004_auto_20170413_0931'),
        ('events', '0003_auto_20170413_0856'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='affiliations.Affiliation'),
        ),
    ]
