# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-26 19:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0045_consessionadmin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examform',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='examrequest', to='student.UserProfileModel'),
        ),
    ]
