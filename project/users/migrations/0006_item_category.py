# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20170426_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]