# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 20:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0007_auto_20170301_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(related_name='articles', to='feed.Tag', verbose_name='теги'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(db_index=True, max_length=200, unique=True, verbose_name='назва'),
        ),
        migrations.AlterField(
            model_name='new',
            name='title',
            field=models.CharField(db_index=True, max_length=200, unique=True, verbose_name='назва'),
        ),
    ]