from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext

from datetime import datetime
from whatsapp.models import WhatsappReceived

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.utils.six import BytesIO


# Create your views here.
def index(request):
    list_msg = WhatsappReceived.objects.filter(is_read=False).order_by('-date_creation')
    return render_to_response('whats_online.html', {'list_msg':list_msg},
                              context_instance=RequestContext(request))

    #return render_to_response('whatsapp.html', {'phones': phones},
     #                         context_instance=RequestContext(request))

def view_message(request, message_id):
    message = WhatsappReceived.objects.get(id=message_id)
    message.update(is_read=True)

    list_content = WhatsappReceived.objects.filter(id=message_id).order_by('-date_creation')
    #phone_number = WhatsappReceived.objects.get(id=message_id)

    return render_to_response('view_message.html', {'list_content': list_content},
                              context_instance=RequestContext(request))

def no_valid(request, message_id):
    message = WhatsappReceived.objects.get(id=message_id)
    message.update(is_valid=False)

    list_msg = WhatsappReceived.objects.filter(is_read=False).order_by('-date_creation')
    return render_to_response('whats_online.html', {'list_msg':list_msg},
                              context_instance=RequestContext(request))

def no_valid(request, message_id):
    message = WhatsappReceived.objects.get(id=message_id)
    message.update(is_valid=True)

    list_msg = WhatsappReceived.objects.filter(is_read=False).order_by('-date_creation')
    return render_to_response('whats_online.html', {'list_msg':list_msg},
                              context_instance=RequestContext(request))

def view_all(request):
    list_msg = WhatsappReceived.objects.order_by('-date_creation')
    return render_to_response('whats_online_all.html', {'list_msg':list_msg},
                              context_instance=RequestContext(request))

def view_read(request):
    list_msg = WhatsappReceived.objects.filter(is_read=True).order_by('-date_creation')
    return render_to_response('whats_online_read.html', {'list_msg':list_msg},
                              context_instance=RequestContext(request))

def view_no_valid(request):
    list_msg = WhatsappReceived.objects.filter(is_valid=False).order_by('-date_creation')
    return render_to_response('whats_online_invalid.html', {'list_msg':list_msg},
                              context_instance=RequestContext(request))
