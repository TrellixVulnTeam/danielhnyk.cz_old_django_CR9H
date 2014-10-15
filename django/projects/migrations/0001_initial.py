# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markupfield.fields
import easy_thumbnails.fields
import projects.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=100, db_index=True)),
                ('slug', models.SlugField(max_length=100)),
                ('pclass_pic', easy_thumbnails.fields.ThumbnailerImageField(verbose_name='Foto kategorie', upload_to=projects.models.get_name_file)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(unique=True, max_length=100)),
                ('description', markupfield.fields.MarkupField()),
                ('description_markup_type', models.CharField(editable=False, default='ReST', choices=[('', '--'), ('ReST', 'ReST')], max_length=30)),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('_description_rendered', models.TextField(editable=False)),
                ('start', models.DateField(db_index=True, auto_now_add=True)),
                ('last_mod', models.DateField(auto_now=True)),
                ('body_marked', markupfield.fields.MarkupField()),
                ('body_marked_markup_type', models.CharField(editable=False, default='ReST', choices=[('', '--'), ('ReST', 'ReST')], max_length=30)),
                ('end', models.DateField(db_index=True, auto_now_add=True)),
                ('_body_marked_rendered', models.TextField(editable=False)),
                ('title_pic', easy_thumbnails.fields.ThumbnailerImageField(verbose_name='Titulní foto', null=True, blank=True, upload_to=projects.models.get_name_file)),
                ('pclass', models.ForeignKey(to='projects.PClass')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
