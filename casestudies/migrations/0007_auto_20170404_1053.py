# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 09:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casestudies', '0006_auto_20170322_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casestudyindex',
            name='intro',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]