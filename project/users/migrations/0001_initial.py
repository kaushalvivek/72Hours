# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 05:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('image', models.ImageField(max_length=255, upload_to=b'')),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('payment_mode', models.CharField(choices=[('COD', 'Cash on delivery'), ('Online', 'Online')], max_length=15)),
                ('quantity', models.IntegerField()),
                ('time', models.DateTimeField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Item')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('number', models.IntegerField()),
                ('email', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='transaction',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User'),
        ),
        migrations.AddField(
            model_name='item',
            name='seller_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User'),
        ),
    ]
