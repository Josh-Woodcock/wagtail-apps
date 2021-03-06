# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 14:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('ourresearch', '0012_auto_20170322_1405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ourresearcharticle',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='ourresearchgalleryimage',
            name='image',
        ),
        migrations.RemoveField(
            model_name='ourresearchgalleryimage',
            name='page',
        ),
        migrations.RemoveField(
            model_name='ourresearchindex',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='ourresearchsubject',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='OurResearchArticle',
        ),
        migrations.DeleteModel(
            name='OurResearchGalleryImage',
        ),
        migrations.DeleteModel(
            name='OurResearchIndex',
        ),
        migrations.DeleteModel(
            name='OurResearchSubject',
        ),
    ]
