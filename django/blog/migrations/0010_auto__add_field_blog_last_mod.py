# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Blog.last_mod'
        db.add_column('blog_blog', 'last_mod',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 7, 17, 0, 0), blank=True, auto_now=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Blog.last_mod'
        db.delete_column('blog_blog', 'last_mod')


    models = {
        'blog.blog': {
            'Meta': {'object_name': 'Blog'},
            '_body_marked_rendered': ('django.db.models.fields.TextField', [], {}),
            'body_marked': ('markupfield.fields.MarkupField', [], {'rendered_field': 'True'}),
            'body_marked_markup_type': ('django.db.models.fields.CharField', [], {'max_length': '30', 'default': "'ReST'"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.Category']"}),
            'files': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_mod': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now': 'True'}),
            'posted': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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