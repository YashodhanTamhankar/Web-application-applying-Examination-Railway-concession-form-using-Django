# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-09-22 18:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0111_auto_20190922_2336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examformmodel',
            name='subject',
        ),
    ]
