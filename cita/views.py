# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Cita
from datetime import datetime
from django.http import HttpResponse

# @csrf_exempt
@login_required
def cita(request):
	if request.method == "POST":
		if request.POST.get('id_cita', None):
			try:
				nueva_cita = Cita.objects.get(id=request.POST['id_cita'])
				mensaje = "Cita actualizada correctamente con id %s"
			except:
				nueva_cita = Cita()	
				nueva_cita.fecha_alta = datetime.now()
				nueva_cita.url_alta = request.user
				mensaje = "Cita guardada correctamente con id %s"
		else:
			nueva_cita = Cita()
			nueva_cita.fecha_alta = datetime.now()
			nueva_cita.url_alta = request.user
			mensaje = "Cita guardada correctamente con id %s"
		for clave,valor in request.POST.iteritems():
			if valor == "S" or valor == "s":
				valor = True
			elif valor ==  "N" or valor == "n":
				valor = False
			setattr(nueva_cita, clave, valor)
		nueva_cita.save()
		return HttpResponse(mensaje %(str(nueva_cita.id)))
	if request.GET.get('id_cita', None):
		try:
			nueva_cita = Cita.objects.get(id=request.GET['id_cita'])
		except: nueva_cita = None
	return render(request, 'citas/formulario_citas.html', locals())

