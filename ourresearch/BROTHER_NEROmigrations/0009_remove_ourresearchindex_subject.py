# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 10:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ourresearch', '0008_auto_20170322_1033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ourresearchindex',
            name='subject',
        ),
    ]