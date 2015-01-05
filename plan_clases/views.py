# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.http import HttpResponse
from .models import PlanClases

@login_required
def plan_clases(request):
	if request.method == "POST":
		nuevo_plan = PlanClases()
		# if request.POST.get('id_cita', None):
		# 	try:
		# 		nueva_cita = Cita.objects.get(id=request.POST['id_cita'])
		# 		mensaje = "Cita actualizada correctamente con id %s"
		# 	except:
		# 		nueva_cita = Cita()	
		# 		nueva_cita.fecha_alta = datetime.now()
		# 		nueva_cita.url_alta = request.user
		# 		mensaje = "Cita guardada correctamente con id %s"
		# else:
		# 	nueva_cita = Cita()
		# 	nueva_cita.fecha_alta = datetime.now()
		# 	nueva_cita.url_alta = request.user
		# 	mensaje = "Cita guardada correctamente con id %s"
		for clave,valor in request.POST.iteritems():
			# if valor == "S" or valor == "s":
			# 	valor = True
			# elif valor ==  "N" or valor == "n":
			# 	valor = False
			setattr(nuevo_plan, clave, valor)
		nuevo_plan.save()
		return HttpResponse("Plan guardado con id %s" %(str(nuevo_plan.id)))
	# if request.GET.get('id_cita', None):
	# 	try:
	# 		nueva_cita = Cita.objects.get(id=request.GET['id_cita'])
	# 	except: nueva_cita = None
	return render(request, 'plan_clases/formulario_plan_clases.html', locals())

