# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Blog.body'
        db.delete_column('blog_blog', 'body')


    def backwards(self, orm):
        # Adding field 'Blog.body'
        db.add_column('blog_blog', 'body',
                      self.gf('django.db.models.fields.TextField')(default=None),
                      keep_default=False)


    models = {
        'blog.blog': {
            'Meta': {'object_name': 'Blog'},
            '_body_marked_rendered': ('django.db.models.fields.TextField', [], {}),
            'body_marked': ('markupfield.fields.MarkupField', [], {'rendered_field': 'True'}),
            'body_marked_markup_type': ('django.db.models.fields.CharField', [], {'default': "'ReST'", 'max_length': '30'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.Category']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posted': ('django.db.models.fields.DateField', [], {'blank': 'True', 'db_index': 'True', 'auto_now_add': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'title_pic': ('django.db.models.fields.files.ImageField', [], {'default': "'/media/pictures/blog/template.jpg'", 'max_length': '100'})
        },
        'blog.category': {
            'Meta': {'object_name': 'Category'},
            'categ_pic': ('django.db.models.fields.files.ImageField', [], {'default': "'/media/pictures/blog/template.jpg'", 'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['blog']