# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-20 07:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0079_auto_20190420_0701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regularrevalutionmodel',
            name='subject',
        ),
        migrations.AddField(
            model_name='regularrevalutionmodel',
            name='subject1',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='regularrevalutionmodel',
            name='subject2',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='regularrevalutionmodel',
            name='subject3',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='regularrevalutionmodel',
            name='subject4',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='regularrevalutionmodel',
            name='subject5',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='regularrevalutionmodel',
            name='subject6',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
