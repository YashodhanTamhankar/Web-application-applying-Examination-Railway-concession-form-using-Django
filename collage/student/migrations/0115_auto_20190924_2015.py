# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-09-24 14:45
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0114_atktmodel_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atktmodel',
            name='subject',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Information Technology', 'Information Technology'), ('Computer Engineering', 'Computer Engineering'), ('Production Engineering', 'Production Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Chemical Engineering', 'Chemical Engineering'), ('Electronics & Telecommunication Engineering', 'Electronics & Telecommunication Engineering')], max_length=154, null=True),
        ),
    ]