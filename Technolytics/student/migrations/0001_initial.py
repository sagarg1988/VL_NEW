# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-02-03 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(blank=True, max_length=30, null=True)),
                ('lastName', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
