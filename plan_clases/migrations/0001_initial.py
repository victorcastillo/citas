# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PlanClases'
        db.create_table('plan_clases_planclases', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('materia', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('curso', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('fecha_de_clases', self.gf('django.db.models.fields.DateField')()),
            ('hora_de_clases', self.gf('django.db.models.fields.TimeField')()),
            ('profesor', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('no_de_clase', self.gf('django.db.models.fields.IntegerField')()),
            ('horas_de_clases', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('aprendizaje_esperado_1', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('aprendizaje_esperado_2', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('habilidades_a_desarrollar_1', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('habilidades_a_desarrollar_2', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('habilidades_a_desarrollar_3', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('temas_a_desarrollar_1', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('temas_a_desarrollar_2', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('temas_a_desarrollar_3', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('temas_a_desarrollar_4', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('temas_a_desarrollar_5', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('evidencias_de_aprendizaje_1', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('evidencias_de_aprendizaje_2', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('evidencias_de_aprendizaje_3', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('evidencias_de_aprendizaje_4', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('recursos_de_aprendizaje_1', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('uso_pedagogico_1', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('nivel_1', self.gf('django.db.models.fields.IntegerField')()),
            ('recursos_de_aprendizaje_2', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('uso_pedagogico_2', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('nivel_2', self.gf('django.db.models.fields.IntegerField')()),
            ('recursos_de_aprendizaje_3', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('uso_pedagogico_3', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('nivel_3', self.gf('django.db.models.fields.IntegerField')()),
            ('recursos_de_aprendizaje_4', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('uso_pedagogico_4', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('nivel_4', self.gf('django.db.models.fields.IntegerField')()),
            ('recursos_de_aprendizaje_5', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('uso_pedagogico_5', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('nivel_5', self.gf('django.db.models.fields.IntegerField')()),
            ('observaciones', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('plan_clases', ['PlanClases'])


    def backwards(self, orm):
        # Deleting model 'PlanClases'
        db.delete_table('plan_clases_planclases')


    models = {
        'plan_clases.planclases': {
            'Meta': {'object_name': 'PlanClases'},
            'aprendizaje_esperado_1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'aprendizaje_esperado_2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'curso': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'evidencias_de_aprendizaje_1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'evidencias_de_aprendizaje_2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'evidencias_de_aprendizaje_3': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'evidencias_de_aprendizaje_4': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'fecha_de_clases': ('django.db.models.fields.DateField', [], {}),
            'habilidades_a_desarrollar_1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'habilidades_a_desarrollar_2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'habilidades_a_desarrollar_3': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'hora_de_clases': ('django.db.models.fields.TimeField', [], {}),
            'horas_de_clases': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materia': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nivel_1': ('django.db.models.fields.IntegerField', [], {}),
            'nivel_2': ('django.db.models.fields.IntegerField', [], {}),
            'nivel_3': ('django.db.models.fields.IntegerField', [], {}),
            'nivel_4': ('django.db.models.fields.IntegerField', [], {}),
            'nivel_5': ('django.db.models.fields.IntegerField', [], {}),
            'no_de_clase': ('django.db.models.fields.IntegerField', [], {}),
            'observaciones': ('django.db.models.fields.TextField', [], {}),
            'profesor': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'recursos_de_aprendizaje_1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'recursos_de_aprendizaje_2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'recursos_de_aprendizaje_3': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'recursos_de_aprendizaje_4': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'recursos_de_aprendizaje_5': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'temas_a_desarrollar_1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'temas_a_desarrollar_2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'temas_a_desarrollar_3': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'temas_a_desarrollar_4': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'temas_a_desarrollar_5': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'uso_pedagogico_1': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'uso_pedagogico_2': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'uso_pedagogico_3': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'uso_pedagogico_4': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'uso_pedagogico_5': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['plan_clases']