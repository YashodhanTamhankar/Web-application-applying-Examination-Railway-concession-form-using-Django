# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-25 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0103_auto_20190425_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilemodel',
            name='branch',
            field=models.CharField(choices=[('information technology', 'information technology'), ('computer engineering', 'computer engineering'), ('production engineering', 'production engineering'), ('mechanical engineering', 'mechanical engineering'), ('chemical engineering', 'chemical engineering'), ('electronics & telecommunication engineering', 'electronics & telecommunication engineering')], max_length=100, null=True),
        ),
    ]
