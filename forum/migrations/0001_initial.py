# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 20:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('brief', models.CharField(max_length=500)),
                ('link', models.URLField(blank=True)),
                ('must_host', models.BooleanField()),
                ('affiliation', models.CharField(blank=True, max_length=100)),
                ('description', models.CharField(blank=True, max_length=5000)),
                ('categories', models.ManyToManyField(to='mainsite.Category')),
            ],
        ),
    ]
