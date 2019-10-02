# Generated by Django 2.2.5 on 2019-09-25 03:17

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0124_auto_20190925_0815'),
    ]

    operations = [
        migrations.AddField(
            model_name='atktmodel',
            name='IT_FE_1',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Applied Physics – I', 'Applied Physics – I'), ('Applied Mathematics – I', 'Applied Mathematics – I'), ('Applied Chemistry – I\t', 'Applied Chemistry – I'), ('Manufacturing Process', 'Manufacturing Process'), ('Introduction to Computers and Auto CAD', 'Introduction to Computers and Auto CAD')], max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='atktmodel',
            name='IT_FE_2',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Applied Mathematics – II', 'Applied Mathematics – II'), ('Applied Physics – II', 'Applied Physics – II'), ('Applied Chemistry – II\t', 'Applied Chemistry – II'), ('Introduction to Programming', 'Introduction to Programming'), ('Engineering Mechanics', 'Engineering Mechanics'), ('Electrical Science', 'EElectrical Science')], max_length=138, null=True),
        ),
    ]
