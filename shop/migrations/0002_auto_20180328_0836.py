# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-28 08:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopingChart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='ShopingCart',
        ),
        migrations.AddField(
            model_name='provider',
            name='name',
            field=models.CharField(db_index=True, default='proveedor', max_length=100),
        ),
        migrations.AddField(
            model_name='shoptag',
            name='name',
            field=models.CharField(db_index=True, default='etiqueta', max_length=100),
        ),
    ]
