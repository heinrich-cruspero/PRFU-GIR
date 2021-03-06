# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-11 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0004_userprofile_middle_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Affiliation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('classification', models.IntegerField(blank=True, choices=[(1, 'School'), (2, 'Foundation'), (3, 'Company')], null=True)),
                ('members', models.ManyToManyField(related_name='Member', to='accounts.UserProfile')),
            ],
            options={
                'verbose_name': 'Affiliation',
                'verbose_name_plural': 'Affiliations',
            },
        ),
    ]
