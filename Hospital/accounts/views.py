from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf


def home(request):
	return render_to_response('index.html')

def login(request):
	c={}
	c.update(csrf(request))
	return render_to_response('login_here.html',c)

def check_user(request):
	c={}
	c.update(csrf(request))
	username=request.POST.get('username','')
	password=request.POST.get('password','')
	print request.POST.get('username','')
	print request.POST.get('password','')
	user=auth.authenticate(username=username,password=password)

	if user is not None or user.is_active():
		auth.login(request,user)
		return render_to_response('loggedin.html')
	else:
		return render_to_response('invalid.html')
