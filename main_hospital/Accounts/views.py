from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import TemplateView
# Create your views here.
def home(request):
	name="Welcome to Website";
	version="Beta"
	#t=get_template('home.html');
	#html=t.render(Context({'name':name}));
	return render_to_response('home.html',({'name':name,'version':version}))
