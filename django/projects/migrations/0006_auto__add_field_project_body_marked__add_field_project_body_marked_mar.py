# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Project.body_marked'
        db.add_column('projects_project', 'body_marked',
                      self.gf('markupfield.fields.MarkupField')(rendered_field=True, default='*body*'),
                      keep_default=False)

        # Adding field 'Project.body_marked_markup_type'
        db.add_column('projects_project', 'body_marked_markup_type',
                      self.gf('django.db.models.fields.CharField')(max_length=30, default='ReST'),
                      keep_default=False)

        # Adding field 'Project._body_marked_rendered'
        db.add_column('projects_project', '_body_marked_rendered',
                      self.gf('django.db.models.fields.TextField')(default='2'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Project.body_marked'
        db.delete_column('projects_project', 'body_marked')

        # Deleting field 'Project.body_marked_markup_type'
        db.delete_column('projects_project', 'body_marked_markup_type')

        # Deleting field 'Project._body_marked_rendered'
        db.delete_column('projects_project', '_body_marked_rendered')


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
            '_body_marked_rendered': ('django.db.models.fields.TextField', [], {}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'body_marked': ('markupfield.fields.MarkupField', [], {'rendered_field': 'True'}),
            'body_marked_markup_type': ('django.db.models.fields.CharField', [], {'max_length': '30', 'default': "'ReST'"}),
            'end': ('django.db.models.fields.DateField', [], {'db_index': 'True', 'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pclass': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.PClass']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'unique': 'True'}),
            'start': ('django.db.models.fields.DateField', [], {'db_index': 'True', 'blank': 'True', 'auto_now_add': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True'}),
            'title_pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['projects']