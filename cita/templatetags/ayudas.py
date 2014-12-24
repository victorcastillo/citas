from django import template

register = template.Library()

def booleano(value):
	if value ==  None or value == "":
		return ""
	return "S" if value else "N"

register.filter('booleano', booleano)
