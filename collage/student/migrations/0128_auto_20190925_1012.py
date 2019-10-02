# Generated by Django 2.2.5 on 2019-09-25 04:42

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0127_auto_20190925_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='atktmodel',
            name='IT_FE_3',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Applied Mathematics III', 'Applied Mathematics III'), ('Logic Design', 'Logic Design'), ('Data Structures & Analysis', 'Data Structures & Analysis'), ('Database Management System', 'Database Management System'), ('Principle of Communications 2', 'Principle of Communications 2')], max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='atktmodel',
            name='IT_FE_4',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Applied Mathematics-IV', 'Applied Mathematics-IV'), ('Computer Networks', 'Computer Networks'), ('Operating Systems', 'Operating Systems'), ('Computer Organization and Architecture', 'Computer Organization and Architecture'), ('Automata Theory', 'Automata Theory')], max_length=113, null=True),
        ),
        migrations.AddField(
            model_name='atktmodel',
            name='IT_FE_5',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Microcontroller and Embedded Programming', 'Microcontroller and Embedded Programming'), ('Internet Programming', 'Internet Programming'), ('Advanced Data Management Technology', 'Advanced Data Management Technology'), ('Cryptography & Network Security', 'Cryptography & Network Security'), ('E-Commerce & E-Business', 'E-Commerce & E-Business')], max_length=153, null=True),
        ),
        migrations.AddField(
            model_name='atktmodel',
            name='IT_FE_6',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Software Engineering with Project Management', 'Software Engineering with Project Management'), ('Data Mining and Business Intelligence', 'Data Mining and Business Intelligence'), ('Cloud Computing & Services', 'Cloud Computing & Services'), ('Wireless Networks', 'Wireless Networks'), ('Digital Forensics', 'Digital Forensics')], max_length=145, null=True),
        ),
        migrations.AlterField(
            model_name='atktmodel',
            name='IT_FE_1',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Applied Physics – I', 'Applied Physics – I'), ('Applied Mathematics – I', 'Applied Mathematics – I'), ('Applied Chemistry – I\t', 'Applied Chemistry – I'), ('Engineering Mechanics', 'Engineering Mechanics'), ('Introduction to Computers and Auto CAD', 'Introduction to Computers and Auto CAD'), ('Environmental Studies', 'Environmental Studies')], max_length=149, null=True),
        ),
    ]
