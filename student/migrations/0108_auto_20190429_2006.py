# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-29 20:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0107_consessionadmin_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadnoticemodel',
            name='branch',
            field=models.CharField(choices=[('all branch', 'all branch'), ('Information Technology', 'Information Technology'), ('Computer Engineering', 'Computer Engineering'), ('Production Engineering', 'Production Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Chemical Engineering', 'Chemical Engineering'), ('Electronics & Telecommunication Engineering', 'Electronics & Telecommunication Engineering')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='uploadresultmodel',
            name='branch',
            field=models.CharField(choices=[('Information Technology', 'Information Technology'), ('Computer Engineering', 'Computer Engineering'), ('Production Engineering', 'Production Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Chemical Engineering', 'Chemical Engineering'), ('Electronics & Telecommunication Engineering', 'Electronics & Telecommunication Engineering')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='userprofilemodel',
            name='branch',
            field=models.CharField(choices=[('Information Technology', 'Information Technology'), ('Computer Engineering', 'Computer Engineering'), ('Production Engineering', 'Production Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Chemical Engineering', 'Chemical Engineering'), ('Electronics & Telecommunication Engineering', 'Electronics & Telecommunication Engineering')], max_length=100, null=True),
        ),
    ]
