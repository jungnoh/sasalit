# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-29 08:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20170829_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classtime',
            name='class_no',
            field=models.IntegerField(default=1, help_text='분반'),
        ),
        migrations.AlterField(
            model_name='classtime',
            name='code',
            field=models.TextField(default='4ad831ad'),
        ),
    ]