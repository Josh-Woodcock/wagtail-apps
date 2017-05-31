# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 09:55
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20170404_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('Carousel', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('title', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), ('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('link', wagtail.wagtailcore.blocks.PageChooserBlock())))),), blank=True, null=True),
        ),
    ]
