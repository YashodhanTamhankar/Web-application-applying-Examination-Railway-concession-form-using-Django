# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-02-14 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0022_auto_20190213_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofilemodel',
            name='imsge',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]
