# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-13 09:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('affiliations', '0003_affiliation_contacts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='affiliation',
            old_name='contacts',
            new_name='contact',
        ),
    ]
