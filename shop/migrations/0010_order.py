# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-05 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_shopingchart_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=300)),
                ('created_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
