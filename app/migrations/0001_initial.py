# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-01 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=250)),
                ('lat', models.CharField(max_length=15)),
                ('lng', models.CharField(max_length=15)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
