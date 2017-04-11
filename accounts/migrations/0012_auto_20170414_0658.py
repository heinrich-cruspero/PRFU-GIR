# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-14 06:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20170414_0653'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
