# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 18:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share_images', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='geographimage',
            name='orig_image',
            field=models.ImageField(max_length=800, null=True, upload_to='images/geograph/'),
        ),
    ]
