# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-19 17:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
