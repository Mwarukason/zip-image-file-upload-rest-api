# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-19 18:30
from __future__ import unicode_literals

from django.db import migrations, models
import image_upload.models


class Migration(migrations.Migration):

    dependencies = [
        ('image_upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageuploaded',
            name='image',
            field=models.ImageField(upload_to=image_upload.models.format_uploaded_filename, verbose_name='Image Uploaded'),
        ),
    ]
