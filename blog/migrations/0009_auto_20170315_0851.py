# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 08:51
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
        ('blog', '0008_auto_20170313_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventindexpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='eventpagegalleryimage',
            name='image',
        ),
        migrations.RemoveField(
            model_name='eventpagegalleryimage',
            name='page',
        ),
        migrations.AlterField(
            model_name='blogpagetag',
            name='content_object',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='blog.BlogPage'),
        ),
        migrations.DeleteModel(
            name='EventIndexPage',
        ),
        migrations.DeleteModel(
            name='EventPage',
        ),
        migrations.DeleteModel(
            name='EventPageGalleryImage',
        ),
    ]