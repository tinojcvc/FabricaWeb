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
    list_msg = WhatsappReceived.objects
    return render_to_response('whats_online.html', {'list_msg':list_msg},
                              context_instance=RequestContext(request))

    #return render_to_response('whatsapp.html', {'phones': phones},
     #                         context_instance=RequestContext(request))

def view_message(request, message_id):
    list_content = WhatsappReceived.objects.filter(phone=message_id)
    #phone_number = WhatsappReceived.objects.get(id=message_id)

    return render_to_response('view_message.html', {'list_content': list_content},
                              context_instance=RequestContext(request))