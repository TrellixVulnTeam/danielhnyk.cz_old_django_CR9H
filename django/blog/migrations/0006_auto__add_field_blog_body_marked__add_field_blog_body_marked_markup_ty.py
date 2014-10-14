# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Blog.body_marked'
        db.add_column('blog_blog', 'body_marked',
                      self.gf('markupfield.fields.MarkupField')(default='*em* and **bold**', rendered_field=True),
                      keep_default=False)

        # Adding field 'Blog.body_marked_markup_type'
        db.add_column('blog_blog', 'body_marked_markup_type',
                      self.gf('django.db.models.fields.CharField')(max_length=30, default='ReST'),
                      keep_default=False)

        # Adding field 'Blog._body_marked_rendered'
        db.add_column('blog_blog', '_body_marked_rendered',
                      self.gf('django.db.models.fields.TextField')(default='<p>odstavec</p>'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Blog.body_marked'
        db.delete_column('blog_blog', 'body_marked')

        # Deleting field 'Blog.body_marked_markup_type'
        db.delete_column('blog_blog', 'body_marked_markup_type')

        # Deleting field 'Blog._body_marked_rendered'
        db.delete_column('blog_blog', '_body_marked_rendered')


    models = {
        'blog.blog': {
            'Meta': {'object_name': 'Blog'},
            '_body_marked_rendered': ('django.db.models.fields.TextField', [], {}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'body_marked': ('markupfield.fields.MarkupField', [], {'rendered_field': 'True'}),
            'body_marked_markup_type': ('django.db.models.fields.CharField', [], {'max_length': '30', 'default': "'ReST'"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.Category']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posted': ('django.db.models.fields.DateField', [], {'blank': 'True', 'db_index': 'True', 'auto_now_add': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'unique': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True'}),
            'title_pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'default': "'/media/pictures/blog/template.jpg'"})
        },
        'blog.category': {
            'Meta': {'object_name': 'Category'},
            'categ_pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'default': "'/media/pictures/blog/template.jpg'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'})
        }
    }

    complete_apps = ['blog']