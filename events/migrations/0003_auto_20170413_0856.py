# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-13 08:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20170408_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='participants',
            field=models.ManyToManyField(blank=True, null=True, related_name='Participants', to='accounts.UserProfile'),
        ),
    ]
