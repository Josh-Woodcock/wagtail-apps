# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 10:32
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ourresearch', '0006_auto_20170322_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourresearchindex',
            name='subject',
            field=wagtail.wagtailcore.fields.StreamField((('subject_thumb', wagtail.wagtailcore.blocks.StructBlock((('fa_icon', wagtail.wagtailcore.blocks.CharBlock(default='fa-', max_length=255, required=True)), ('caption', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True))))),)),
        ),
    ]
