# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-26 20:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0047_auto_20190326_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examform',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='examrequest', to=settings.AUTH_USER_MODEL),
        ),
    ]
