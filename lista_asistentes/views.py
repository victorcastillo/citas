# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
#from datetime import datetime
from django.http import HttpResponse
from .models import ListaAsistentes

@login_required
def lista_asistentes(request):
	if request.method == "POST":
		lista = ListaAsistentes()
		lista.nombre_capturista = request.user.first_name + " " + request.user.last_name
		for clave,valor in request.POST.iteritems():
			setattr(lista, clave, valor)
		x1 = int((request.POST.get('alumnos_que_asistieron')))
		x2 = int(request.POST.get('alumnos_que_debieron_asistir'))
		lista.por_ciento_asistencia = int((x1*100)/x2)
		lista.save()
		return HttpResponse("Plan guardado con id %s" %(str(lista.id)))
	return render(request, 'lista_asistentes/lista_de_asistentes.html', locals())

