# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-03 22:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20181103_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
