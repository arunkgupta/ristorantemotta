from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import ListView, DetailView
from django.template.loader import render_to_string
from sito.models import *
from django.core.mail import send_mail

# Create your views here.

def HomePage(request):
	return render_to_response('index.html', context_instance=RequestContext(request))
	#return render_to_response('index.html', context, context_instance=RequestContext(request))

