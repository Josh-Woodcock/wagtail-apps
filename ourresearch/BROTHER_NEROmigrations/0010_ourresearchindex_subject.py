# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 11:07
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ourresearch', '0009_remove_ourresearchindex_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourresearchindex',
            name='subject',
            field=wagtail.wagtailcore.fields.StreamField((('subject_thumb', wagtail.wagtailcore.blocks.StructBlock((('fa_icon', wagtail.wagtailcore.blocks.CharBlock(blank=True, max_length=255, null=True)), ('caption', wagtail.wagtailcore.blocks.CharBlock(blank=True, max_length=255, null=True))))),), default=0),
            preserve_default=False,
        ),
    ]
