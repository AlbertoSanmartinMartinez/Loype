# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-04 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20180328_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='shopingchart',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='shoptag',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
