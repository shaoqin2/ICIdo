# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_auto_20170219_0347'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='usage',
            field=models.TextField(blank=True, default='', max_length=1000),
        ),
    ]