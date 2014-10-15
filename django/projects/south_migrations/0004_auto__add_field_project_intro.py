# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Project.intro'
        db.add_column('projects_project', 'intro',
                      self.gf('django.db.models.fields.TextField')(max_length=100, default=None, unique=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Project.intro'
        db.delete_column('projects_project', 'intro')


    models = {
        'projects.pclass': {
            'Meta': {'object_name': 'PClass'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pclass_pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'})
        },
        'projects.project': {
            'Meta': {'object_name': 'Project'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'end': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intro': ('django.db.models.fields.TextField', [], {'max_length': '100', 'unique': 'True'}),
            'pclass': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.PClass']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'unique': 'True'}),
            'start': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True'}),
            'title_pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'})
        }
    }

    complete_apps = ['projects']