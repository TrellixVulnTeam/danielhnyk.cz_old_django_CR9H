# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Category.categ_pic'
        db.add_column('blog_category', 'categ_pic',
                      self.gf('django.db.models.fields.files.ImageField')(default='/static/images/n33-robot-invader.jpg', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Category.categ_pic'
        db.delete_column('blog_category', 'categ_pic')


    models = {
        'blog.blog': {
            'Meta': {'object_name': 'Blog'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.Category']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posted': ('django.db.models.fields.DateField', [], {'blank': 'True', 'db_index': 'True', 'auto_now_add': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'unique': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True'}),
            'title_pic': ('django.db.models.fields.files.ImageField', [], {'default': "'/static/images/n33-robot-invader.jpg'", 'max_length': '100'})
        },
        'blog.category': {
            'Meta': {'object_name': 'Category'},
            'categ_pic': ('django.db.models.fields.files.ImageField', [], {'default': "'/static/images/n33-robot-invader.jpg'", 'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['blog']