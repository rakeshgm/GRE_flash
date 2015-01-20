# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Word_List'
        db.create_table(u'vocab_word_list', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal(u'vocab', ['Word_List'])

        # Adding model 'Word'
        db.create_table(u'vocab_word', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('word_list', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vocab.Word_List'])),
            ('word', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('meaning', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('example', self.gf('django.db.models.fields.TextField')(max_length=500)),
        ))
        db.send_create_signal(u'vocab', ['Word'])


    def backwards(self, orm):
        # Deleting model 'Word_List'
        db.delete_table(u'vocab_word_list')

        # Deleting model 'Word'
        db.delete_table(u'vocab_word')


    models = {
        u'vocab.word': {
            'Meta': {'object_name': 'Word'},
            'example': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meaning': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'word': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'word_list': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vocab.Word_List']"})
        },
        u'vocab.word_list': {
            'Meta': {'object_name': 'Word_List'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        }
    }

    complete_apps = ['vocab']