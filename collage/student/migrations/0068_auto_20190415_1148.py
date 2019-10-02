# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-15 11:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0067_regularrevalutionmodel_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atktphotocopymodel',
            old_name='seat_no',
            new_name='roll_no',
        ),
        migrations.RenameField(
            model_name='atktrevalutionmodel',
            old_name='seat_no',
            new_name='roll_no',
        ),
        migrations.RenameField(
            model_name='regularphotocopymodel',
            old_name='seat_no',
            new_name='roll_no',
        ),
        migrations.RemoveField(
            model_name='atktphotocopymodel',
            name='exam_type',
        ),
        migrations.RemoveField(
            model_name='atktphotocopymodel',
            name='semister',
        ),
        migrations.RemoveField(
            model_name='atktrevalutionmodel',
            name='exam_type',
        ),
        migrations.RemoveField(
            model_name='atktrevalutionmodel',
            name='semister',
        ),
        migrations.RemoveField(
            model_name='regularphotocopymodel',
            name='semister',
        ),
        migrations.AddField(
            model_name='atktphotocopymodel',
            name='admission_no',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='atktphotocopymodel',
            name='branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.Branch'),
        ),
        migrations.AddField(
            model_name='atktphotocopymodel',
            name='semester',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.Semester'),
        ),
        migrations.AddField(
            model_name='atktphotocopymodel',
            name='subject',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='atktphotocopymodel',
            name='year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.Year'),
        ),
        migrations.AddField(
            model_name='atktrevalutionmodel',
            name='admission_no',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='atktrevalutionmodel',
            name='branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.Branch'),
        ),
        migrations.AddField(
            model_name='atktrevalutionmodel',
            name='semester',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.Semester'),
        ),
        migrations.AddField(
            model_name='atktrevalutionmodel',
            name='subject',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='atktrevalutionmodel',
            name='year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.Year'),
        ),
        migrations.AddField(
            model_name='regularphotocopymodel',
            name='admission_no',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='regularphotocopymodel',
            name='branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.Branch'),
        ),
        migrations.AddField(
            model_name='regularphotocopymodel',
            name='last_seat_no',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='regularphotocopymodel',
            name='semester',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.Semester'),
        ),
        migrations.AddField(
            model_name='regularphotocopymodel',
            name='subject',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='regularphotocopymodel',
            name='year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.Year'),
        ),
        migrations.AlterField(
            model_name='atktphotocopymodel',
            name='last_seat_no',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='atktrevalutionmodel',
            name='last_seat_no',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='regularrevalutionmodel',
            name='branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.Branch'),
        ),
    ]
