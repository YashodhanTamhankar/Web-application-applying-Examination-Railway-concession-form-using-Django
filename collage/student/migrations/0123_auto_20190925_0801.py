# Generated by Django 2.2.5 on 2019-09-25 02:31

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0122_auto_20190925_0743'),
    ]

    operations = [
        migrations.AddField(
            model_name='atktmodel',
            name='subject',
            field=multiselectfield.db.fields.MultiSelectField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='subject_multiple',
            name='name',
            field=multiselectfield.db.fields.MultiSelectField(max_length=200, null=True),
        ),
    ]
