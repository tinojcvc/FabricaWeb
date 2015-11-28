
from django.http import HttpResponseRedirect, HttpResponse

def index(request):
    return HttpResponseRedirect('/station/')

def services(request):
    return HttpResponse('prueba')

def whatsapp(request):
    return HttpResponseRedirect('/whatsapp/')
