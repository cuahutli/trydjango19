# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-14 18:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=datetime.datetime(2016, 1, 14, 18, 31, 35, 885948, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2016, 1, 14, 18, 32, 1, 974068, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
