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
	news_list = News.objects.all().order_by('-pub_date')[:5]
	context = {'news_list':news_list}
	return render_to_response('index.html', context, context_instance=RequestContext(request))
	#return render_to_response('index.html', context, context_instance=RequestContext(request))
	#return render(request, 'index.html', context)

def newslist(request):
	news_list = News.objects.all().order_by('-pub_date')
	context = {'news_list':news_list}
	return render(request, 'news.html', context)

def newsdettaglio(request, post_id):
    news = News.objects.get(pk=post_id)
    context = {'news': news}
    return render_to_response('news_dettaglio.html', context, context_instance=RequestContext(request))

def pagina(request, post_id):
    page = Page.objects.get(pk=post_id)
    context = {'page': page}
    return render_to_response('pagina.html', context, context_instance=RequestContext(request))

def galleria(request):
	immagini_list = Immagini.objects.all()
	context = {'immagini_list':immagini_list}
	return render(request, 'galleria.html', context)

def menulist(request):
	menu_list = Food.objects.all()
	context = {'menu_list':menu_list}
	return render(request, 'lista.html', context)