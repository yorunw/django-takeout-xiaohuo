# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-06 21:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20170906_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='number',
            field=models.CharField(blank=True, max_length=11, verbose_name='电话号码'),
        ),
    ]
