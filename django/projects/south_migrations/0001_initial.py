# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table('projects_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, unique=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100, unique=True)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('start', self.gf('django.db.models.fields.DateField')(db_index=True, blank=True, auto_now_add=True)),
            ('end', self.gf('django.db.models.fields.DateField')(db_index=True, blank=True, auto_now_add=True)),
            ('pclass', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.PClass'])),
            ('title_pic', self.gf('django.db.models.fields.files.ImageField')(blank=True, null=True, max_length=100)),
        ))
        db.send_create_signal('projects', ['Project'])

        # Adding model 'PClass'
        db.create_table('projects_pclass', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
            ('pclass_pic', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('projects', ['PClass'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table('projects_project')

        # Deleting model 'PClass'
        db.delete_table('projects_pclass')


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
            'body': ('django.db.models.fields.TextField', [], {}),
            'end': ('django.db.models.fields.DateField', [], {'db_index': 'True', 'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pclass': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.PClass']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'unique': 'True'}),
            'start': ('django.db.models.fields.DateField', [], {'db_index': 'True', 'blank': 'True', 'auto_now_add': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True'}),
            'title_pic': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['projects']