# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-11 12:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0027_auto_20190311_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examform',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.UserProfileModel'),
        ),
    ]
