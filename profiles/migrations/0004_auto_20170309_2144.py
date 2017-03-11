# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20170304_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='full_name',
            field=models.CharField(max_length=100, verbose_name="Прізвище,ім'я та по-батькові"),
        ),
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(choices=[('p', 'Учасник'), ('m', 'Член')], default='p', max_length=1),
        ),
    ]
