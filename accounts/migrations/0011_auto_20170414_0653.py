# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-14 06:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20170414_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.CharField(choices=[('Davao City', 'Davao City'), ('Tagum City', 'Tagum City'), ('Panabo City', 'Panabo City')], default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='course',
            field=models.CharField(default='', max_length=30, verbose_name='Section or Degree'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='level',
            field=models.SmallIntegerField(choices=[(1, 'Grade 1'), (2, 'Grade 2'), (3, 'Grade 3'), (4, 'Grade 4'), (5, 'Grade 5'), (6, 'Grade 6'), (7, 'Grade 7 - Junior High School'), (8, 'Grade 8 - Junior High School'), (9, 'Grade 9 - Junior High School'), (10, 'Grade 10 - Senior High School'), (11, 'Grade 11 - Senior High School'), (12, 'Grade 12 - Senior High School'), (13, 'Undergraduate'), (14, 'Graduate'), (15, 'Masteral'), (16, 'Doctorate')], default=1, verbose_name='Grade or Year Level'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='middle_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
