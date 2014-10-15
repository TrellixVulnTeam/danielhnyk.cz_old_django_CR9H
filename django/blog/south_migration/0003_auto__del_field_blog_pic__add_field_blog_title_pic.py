# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Blog.pic'
        db.delete_column('blog_blog', 'pic')

        # Adding field 'Blog.title_pic'
        db.add_column('blog_blog', 'title_pic',
                      self.gf('django.db.models.fields.files.ImageField')(null=True, max_length=100, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Blog.pic'
        db.add_column('blog_blog', 'pic',
                      self.gf('django.db.models.fields.files.ImageField')(null=True, max_length=100, blank=True),
                      keep_default=False)

        # Deleting field 'Blog.title_pic'
        db.delete_column('blog_blog', 'title_pic')


    models = {
        'blog.blog': {
            'Meta': {'object_name': 'Blog'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.Category']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posted': ('django.db.models.fields.DateField', [], {'db_index': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'unique': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True'}),
            'title_pic': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'})
        },
        'blog.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['blog']