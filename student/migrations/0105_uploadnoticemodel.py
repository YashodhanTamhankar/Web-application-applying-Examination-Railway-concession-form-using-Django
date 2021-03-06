# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-28 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0104_auto_20190425_2230'),
    ]

    operations = [
        migrations.CreateModel(
            name='uploadnoticemodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(choices=[('all branch', 'all branch'), ('information technology', 'information technology'), ('computer engineering', 'computer engineering'), ('production engineering', 'production engineering'), ('mechanical engineering', 'mechanical engineering'), ('chemical engineering', 'chemical engineering'), ('electronics & telecommunication engineering', 'electronics & telecommunication engineering')], max_length=200, null=True)),
                ('notice', models.TextField(max_length=500)),
                ('image', models.ImageField(blank=True, upload_to='notice_image')),
            ],
        ),
    ]
