# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Cita.direccion_habitacional'
        db.delete_column('cita_cita', 'direccion_habitacional')


    def backwards(self, orm):
        # Adding field 'Cita.direccion_habitacional'
        db.add_column('cita_cita', 'direccion_habitacional',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=60),
                      keep_default=False)


    models = {
        'cita.cita': {
            'Meta': {'object_name': 'Cita'},
            'asesor': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'calle': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'calle_paralela': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'cod_resultado': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'como_llegar': ('django.db.models.fields.TextField', [], {}),
            'contrasena': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'cp': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'dias_horario_oa': ('django.db.models.fields.TextField', [], {}),
            'direccion_a': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'edad': ('django.db.models.fields.IntegerField', [], {}),
            'en_esquina_de': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'entrada_color': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'entre_calle1': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'entre_calle2': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'estacion_parada': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'estudia_actualmente': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fachada_color': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'fecha_act': ('django.db.models.fields.DateTimeField', [], {}),
            'fecha_alta': ('django.db.models.fields.DateTimeField', [], {}),
            'fecha_baja': ('django.db.models.fields.DateTimeField', [], {}),
            'fecha_hora_llamada': ('django.db.models.fields.DateTimeField', [], {}),
            'fecha_hora_visita': ('django.db.models.fields.DateTimeField', [], {}),
            'filtrada_por': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'filtro_fecha_llamada': ('django.db.models.fields.DateTimeField', [], {}),
            'filtro_num_exterior': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'filtro_observaciones': ('django.db.models.fields.TextField', [], {}),
            'filtro_tel_alterno': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_encuesta': ('django.db.models.fields.IntegerField', [], {}),
            'info_extra': ('django.db.models.fields.TextField', [], {}),
            'interes_autorizo': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'municipio': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'nom_depende': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'nombre_autoriza': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'num_camiones': ('django.db.models.fields.IntegerField', [], {}),
            'num_exterior': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'num_interior': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'num_metrobuses': ('django.db.models.fields.IntegerField', [], {}),
            'num_metros': ('django.db.models.fields.IntegerField', [], {}),
            'num_visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'observaciones': ('django.db.models.fields.TextField', [], {}),
            'ocupacion': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'origeninfo': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'otras_actividades': ('django.db.models.fields.TextField', [], {}),
            'parentesco_autoriza': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'programa': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'prospecto': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'que_convencera': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'que_si_no_aprovecha': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'referencia_bajada': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'referencia_correcta': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rvt': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'tel_casa': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'tel_cel': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'tipo_calle': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'tipo_entrada': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'tipo_habitacional': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'ultimo_destino': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'ultimo_grado': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'url_act': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'url_alta': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'url_baja': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'vive_alado': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'vive_cerca_de': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'vive_frente_a': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['cita']