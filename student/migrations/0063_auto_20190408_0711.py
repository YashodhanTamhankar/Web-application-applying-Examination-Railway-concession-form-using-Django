# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-08 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0062_consessionformmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consessionadmin',
            name='mobile_no',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='examcelladmin',
            name='mobile_no',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
