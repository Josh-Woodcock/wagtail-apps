# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-18 09:33
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('casestudies', '0007_auto_20170404_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casestudy',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()))),
        ),
    ]
