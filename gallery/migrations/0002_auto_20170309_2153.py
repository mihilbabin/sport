# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 19:53
from __future__ import unicode_literals

from django.db import migrations, models
import gallery.models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ('-created',), 'verbose_name': 'альбом', 'verbose_name_plural': 'альбоми'},
        ),
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ('-created',), 'verbose_name': 'фото', 'verbose_name_plural': 'фото'},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ('-created',), 'verbose_name': 'відео', 'verbose_name_plural': 'відео'},
        ),
        migrations.AddField(
            model_name='album',
            name='slug',
            field=models.SlugField(blank=True, max_length=140, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to=gallery.models.get_upload_location, verbose_name='зображення'),
        ),
    ]
