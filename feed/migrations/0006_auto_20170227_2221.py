# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0005_auto_20170227_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(max_length=25, unique=True),
        ),
    ]
