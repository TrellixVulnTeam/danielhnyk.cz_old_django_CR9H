# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields
import markupfield.fields
import blog.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('posted', models.DateField(db_index=True, auto_now_add=True)),
                ('last_mod', models.DateField(auto_now=True)),
                ('body_marked', markupfield.fields.MarkupField()),
                ('body_marked_markup_type', models.CharField(editable=False, choices=[('', '--'), ('ReST', 'ReST')], max_length=30, default='ReST')),
                ('publish', models.BooleanField(default=False, verbose_name='Should I publish it?')),
                ('_body_marked_rendered', models.TextField(editable=False)),
                ('files', models.FileField(upload_to=blog.models.get_name_file, blank=True)),
                ('title_pic', easy_thumbnails.fields.ThumbnailerImageField(upload_to=blog.models.get_name_file, default='/media/pictures/blog/template.jpg', verbose_name='Titulní foto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('categ_pic', easy_thumbnails.fields.ThumbnailerImageField(upload_to=blog.models.get_name_file, default='/media/pictures/blog/template.jpg', verbose_name='Foto kategorie')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(to='blog.Category'),
            preserve_default=True,
        ),
    ]
