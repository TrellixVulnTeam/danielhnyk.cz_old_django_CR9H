# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Project.description'
        db.add_column('projects_project', 'description',
                      self.gf('markupfield.fields.MarkupField')(default='*bold*', rendered_field=True),
                      keep_default=False)

        # Adding field 'Project.description_markup_type'
        db.add_column('projects_project', 'description_markup_type',
                      self.gf('django.db.models.fields.CharField')(max_length=30, default='ReST'),
                      keep_default=False)

        # Adding field 'Project._description_rendered'
        db.add_column('projects_project', '_description_rendered',
                      self.gf('django.db.models.fields.TextField')(default='2'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Project.description'
        db.delete_column('projects_project', 'description')

        # Deleting field 'Project.description_markup_type'
        db.delete_column('projects_project', 'description_markup_type')

        # Deleting field 'Project._description_rendered'
        db.delete_column('projects_project', '_description_rendered')


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
            'body': ('django.db.models.fields.TextField', [], {}),
            'body_marked': ('markupfield.fields.MarkupField', [], {'rendered_field': 'True'}),
            'body_marked_markup_type': ('django.db.models.fields.CharField', [], {'max_length': '30', 'default': "'ReST'"}),
            'description': ('markupfield.fields.MarkupField', [], {'rendered_field': 'True'}),
            'description_markup_type': ('django.db.models.fields.CharField', [], {'max_length': '30', 'default': "'ReST'"}),
            'end': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pclass': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.PClass']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'start': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'title_pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['projects']