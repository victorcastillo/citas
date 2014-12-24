from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm
from django.shortcuts import render

def login_view(request):
	if not request.user.is_authenticated():
		form = LoginForm()
		if request.method == "POST":
			form = LoginForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				user = authenticate(username=username, password=password)
				if user:
					login(request, user)
					return HttpResponseRedirect('/citas/')
				else:
					return HttpResponse('Nope no puedes')
		return render(request, 'login.html', locals())
	return HttpResponseRedirect('/citas/')