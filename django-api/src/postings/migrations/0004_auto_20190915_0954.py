# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-09-15 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postings', '0003_auto_20190915_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='impressions',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='installs',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='revenue',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='spend',
            field=models.FloatField(default=0.0),
        ),
    ]