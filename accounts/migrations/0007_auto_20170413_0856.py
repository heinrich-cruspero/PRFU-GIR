# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-13 08:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_userprofile_blood_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('contact_no', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='emergency_contacts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Contact'),
        ),
    ]
