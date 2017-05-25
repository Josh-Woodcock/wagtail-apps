# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-07 11:26
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_auto_20170405_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock())), null=True),
        ),
    ]
