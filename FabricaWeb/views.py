
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse

def index(request):
    return redirect('whatsapp')

def services(request):
    return HttpResponse('prueba')

def whatsapp(request):
    return HttpResponseRedirect('/whatsapp/')
