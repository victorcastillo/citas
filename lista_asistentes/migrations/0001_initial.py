# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ListaAsistentes'
        db.create_table('lista_asistentes_listaasistentes', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha_clase', self.gf('django.db.models.fields.DateTimeField')()),
            ('hora_inicio', self.gf('django.db.models.fields.TimeField')()),
            ('hora_fin', self.gf('django.db.models.fields.TimeField')()),
            ('matricula_1', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('nombre_alumno_1', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('retardo_1', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('actitud_1', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('cal_1', self.gf('django.db.models.fields.IntegerField')()),
            ('matricula_2', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('nombre_alumno_2', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('retardo_2', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('actitud_2', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('cal_2', self.gf('django.db.models.fields.IntegerField')()),
            ('matricula_3', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('nombre_alumno_3', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('retardo_3', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('actitud_3', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('cal_3', self.gf('django.db.models.fields.IntegerField')()),
            ('matricula_4', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('nombre_alumno_4', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('retardo_4', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('actitud_4', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('cal_4', self.gf('django.db.models.fields.IntegerField')()),
            ('matricula_5', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('nombre_alumno_5', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('retardo_5', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('actitud_5', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('cal_5', self.gf('django.db.models.fields.IntegerField')()),
            ('matricula_6', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('nombre_alumno_6', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('retardo_6', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('actitud_6', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('cal_6', self.gf('django.db.models.fields.IntegerField')()),
            ('matricula_7', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('nombre_alumno_7', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('retardo_7', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('actitud_7', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('cal_7', self.gf('django.db.models.fields.IntegerField')()),
            ('matricula_8', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('nombre_alumno_8', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('retardo_8', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('actitud_8', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('cal_8', self.gf('django.db.models.fields.IntegerField')()),
            ('matricula_9', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('nombre_alumno_9', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('retardo_9', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('actitud_9', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('cal_9', self.gf('django.db.models.fields.IntegerField')()),
            ('matricula_10', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('nombre_alumno_10', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('retardo_10', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('actitud_10', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('cal_10', self.gf('django.db.models.fields.IntegerField')()),
            ('in_matricula_1', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('in_nombre_alumno_1', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('in_aviso_1', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('in_causa_1', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('in_matricula_2', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('in_nombre_alumno_2', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('in_aviso_2', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('in_causa_2', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('in_matricula_3', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('in_nombre_alumno_3', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('in_aviso_3', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('in_causa_3', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('in_matricula_4', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('in_nombre_alumno_4', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('in_aviso_4', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('in_causa_4', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('in_matricula_5', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('in_nombre_alumno_5', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('in_aviso_5', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('in_causa_5', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('observaciones', self.gf('django.db.models.fields.TextField')()),
            ('alumnos_que_debieron_asistir', self.gf('django.db.models.fields.IntegerField')()),
            ('alumnos_que_asistieron', self.gf('django.db.models.fields.IntegerField')()),
            ('por_ciento_asistencia', self.gf('django.db.models.fields.IntegerField')()),
            ('nombre_capturista', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('grupo', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('folio', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal('lista_asistentes', ['ListaAsistentes'])


    def backwards(self, orm):
        # Deleting model 'ListaAsistentes'
        db.delete_table('lista_asistentes_listaasistentes')


    models = {
        'lista_asistentes.listaasistentes': {
            'Meta': {'object_name': 'ListaAsistentes'},
            'actitud_1': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'actitud_10': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'actitud_2': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'actitud_3': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'actitud_4': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'actitud_5': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'actitud_6': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'actitud_7': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'actitud_8': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'actitud_9': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'alumnos_que_asistieron': ('django.db.models.fields.IntegerField', [], {}),
            'alumnos_que_debieron_asistir': ('django.db.models.fields.IntegerField', [], {}),
            'cal_1': ('django.db.models.fields.IntegerField', [], {}),
            'cal_10': ('django.db.models.fields.IntegerField', [], {}),
            'cal_2': ('django.db.models.fields.IntegerField', [], {}),
            'cal_3': ('django.db.models.fields.IntegerField', [], {}),
            'cal_4': ('django.db.models.fields.IntegerField', [], {}),
            'cal_5': ('django.db.models.fields.IntegerField', [], {}),
            'cal_6': ('django.db.models.fields.IntegerField', [], {}),
            'cal_7': ('django.db.models.fields.IntegerField', [], {}),
            'cal_8': ('django.db.models.fields.IntegerField', [], {}),
            'cal_9': ('django.db.models.fields.IntegerField', [], {}),
            'fecha_clase': ('django.db.models.fields.DateTimeField', [], {}),
            'folio': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'grupo': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'hora_fin': ('django.db.models.fields.TimeField', [], {}),
            'hora_inicio': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_aviso_1': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'in_aviso_2': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'in_aviso_3': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'in_aviso_4': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'in_aviso_5': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'in_causa_1': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'in_causa_2': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'in_causa_3': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'in_causa_4': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'in_causa_5': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'in_matricula_1': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'in_matricula_2': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'in_matricula_3': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'in_matricula_4': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'in_matricula_5': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'in_nombre_alumno_1': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'in_nombre_alumno_2': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'in_nombre_alumno_3': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'in_nombre_alumno_4': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'in_nombre_alumno_5': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'matricula_1': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'matricula_10': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'matricula_2': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'matricula_3': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'matricula_4': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'matricula_5': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'matricula_6': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'matricula_7': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'matricula_8': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'matricula_9': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'nombre_alumno_1': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nombre_alumno_10': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nombre_alumno_2': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nombre_alumno_3': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nombre_alumno_4': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nombre_alumno_5': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nombre_alumno_6': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nombre_alumno_7': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nombre_alumno_8': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nombre_alumno_9': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nombre_capturista': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'observaciones': ('django.db.models.fields.TextField', [], {}),
            'por_ciento_asistencia': ('django.db.models.fields.IntegerField', [], {}),
            'retardo_1': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'retardo_10': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'retardo_2': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'retardo_3': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'retardo_4': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'retardo_5': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'retardo_6': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'retardo_7': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'retardo_8': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'retardo_9': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['lista_asistentes']