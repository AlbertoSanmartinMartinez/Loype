# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-04 23:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20180604_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopingchart',
            name='products',
            field=models.CharField(default='', max_length=300),
        ),
    ]
