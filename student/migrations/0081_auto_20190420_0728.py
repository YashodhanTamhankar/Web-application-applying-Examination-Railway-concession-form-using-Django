# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-20 07:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0080_auto_20190420_0717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atktmodel',
            name='admission_no',
        ),
        migrations.RemoveField(
            model_name='examformmodel',
            name='admission_no',
        ),
        migrations.RemoveField(
            model_name='regularrevalutionmodel',
            name='admission_no',
        ),
    ]
