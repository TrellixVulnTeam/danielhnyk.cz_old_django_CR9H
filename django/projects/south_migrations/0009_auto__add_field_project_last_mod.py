# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Project.last_mod'
        db.add_column('projects_project', 'last_mod',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 7, 17, 0, 0), auto_now=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Project.last_mod'
        db.delete_column('projects_project', 'last_mod')


    models = {
        'projects.pclass': {
            'Meta': {'object_name': 'PClass'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pclass_pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100'})
        },
        'projects.project': {
            'Meta': {'object_name': 'Project'},
            '_body_marked_rendered': ('django.db.models.fields.TextField', [], {}),
            '_description_rendered': ('django.db.models.fields.TextField', [], {}),
            'body_marked': ('markupfield.fields.MarkupField', [], {'rendered_field': 'True'}),
            'body_marked_markup_type': ('django.db.models.fields.CharField', [], {'max_length': '30', 'default': "'ReST'"}),
            'description': ('markupfield.fields.MarkupField', [], {'rendered_field': 'True'}),
            'description_markup_type': ('django.db.models.fields.CharField', [], {'max_length': '30', 'default': "'ReST'"}),
            'end': ('django.db.models.fields.DateField', [], {'db_index': 'True', 'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_mod': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'pclass': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.PClass']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'unique': 'True'}),
            'start': ('django.db.models.fields.DateField', [], {'db_index': 'True', 'blank': 'True', 'auto_now_add': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True'}),
            'title_pic': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['projects']